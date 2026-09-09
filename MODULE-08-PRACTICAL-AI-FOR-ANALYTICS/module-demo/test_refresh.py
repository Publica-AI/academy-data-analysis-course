#!/usr/bin/env python3
"""Topic 8.4 proof: the automation survives a data refresh.

An automation that only works on this quarter's exact file is not automated. This script
manufactures a plausible next-quarter file from the Q3 raw workbook, changing everything a
real refresh changes, then runs monthly_report.py against both files and checks that the
report follows the data rather than a hardcoded assumption.

What the manufactured file changes:
  - every date moves forward one quarter, so the reporting periods are different
  - a brand new route, OYO-04, appears, which did not exist in Q3
  - some LAG-01 rows arrive as LAG01 without the hyphen, a fault the cleaner must absorb
  - 200 rows are removed, so no total can be reused from last quarter
  - the column order is shuffled, because exports do that

    python test_refresh.py

Exits 0 when every check passes.
"""
import os
import shutil
import subprocess
import sys
import tempfile

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "swiftroute_q3_raw.xlsx")
REPORT = os.path.join(HERE, "monthly_report.py")

checks = []


def check(label, got, expected=None, predicate=None):
    ok = predicate(got) if predicate else (got == expected)
    checks.append(ok)
    print("%-5s %-46s %s" % ("PASS" if ok else "FAIL", label, got))
    return ok


def make_next_quarter(src, dst):
    d = pd.read_excel(src, sheet_name="deliveries", dtype=str)
    fuel = pd.read_excel(src, sheet_name="fuel_cost")
    comp = pd.read_excel(src, sheet_name="customer_complaints")

    parsed = pd.to_datetime(d["date"], format="mixed", dayfirst=True, errors="coerce")
    shifted = parsed + pd.DateOffset(months=3)
    d["date"] = shifted.dt.strftime("%Y-%m-%d").fillna("2027-01-15")

    d = d.iloc[:-200].copy()
    d.loc[d.index[:60], "route_code"] = "OYO-04"
    lag01 = d.index[d["route_code"] == "LAG-01"][:40]
    d.loc[lag01, "route_code"] = "LAG01"
    d = d[list(reversed(d.columns))]

    with pd.ExcelWriter(dst, engine="openpyxl") as x:
        d.to_excel(x, sheet_name="deliveries", index=False)
        fuel.to_excel(x, sheet_name="fuel_cost", index=False)
        comp.to_excel(x, sheet_name="customer_complaints", index=False)
    return len(d)


def run(raw, out_dir):
    r = subprocess.run([sys.executable, REPORT, raw, out_dir],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout)
        print(r.stderr)
    return r


def main():
    tmp = tempfile.mkdtemp(prefix="swiftroute_refresh_")
    try:
        print("ROUND 1: the original quarter\n")
        r1 = run(RAW, tmp)
        check("original run exits cleanly", r1.returncode, 0)
        check("original report names Q3 periods",
              "2026-07 to 2026-09" in r1.stdout, True)
        q3_files = sorted(f for f in os.listdir(tmp) if f.endswith(".md"))
        check("original wrote one report", len(q3_files), 1)

        nxt = os.path.join(tmp, "swiftroute_q4_raw.xlsx")
        rows = make_next_quarter(RAW, nxt)
        print("\nmanufactured a next-quarter file with %d rows, a new route, "
              "unhyphenated codes and shuffled columns\n" % rows)

        print("ROUND 2: the refreshed quarter\n")
        r2 = run(nxt, tmp)
        check("refreshed run exits cleanly", r2.returncode, 0)
        check("periods followed the data, not a constant",
              "2026-10 to 2026-12" in r2.stdout, True)
        check("internal checks still passed", "internal checks passed" in r2.stdout, True)

        md = [f for f in os.listdir(tmp) if f.endswith(".md")]
        check("a separate report was written for the new quarter", len(md), 2)

        newest = os.path.join(tmp, "report_2026-10_to_2026-12.md")
        text = open(newest, encoding="utf-8").read()
        # The markdown lists only the busiest five routes, so check the full route table
        # in the workbook rather than the summary.
        routes = pd.read_excel(os.path.join(tmp, "report_2026-10_to_2026-12.xlsx"),
                               sheet_name="by_route")
        codes = set(routes.route_code)
        check("new route OYO-04 reached the report", "OYO-04" in codes, True)
        check("no unhyphenated LAG01 survived cleaning", "LAG01" in codes, False)
        check("LAG-01 rows were folded back into the hyphenated code",
              "LAG-01" in codes, True)
        check("totals were recomputed, not copied",
              "3,600" not in text.split("## By period")[0], True)

        print("\n%d checks, %d passed" % (len(checks), sum(checks)))
        if all(checks):
            print("The report follows the file. It survives a refresh.")
            return 0
        print("At least one check failed: the automation does not yet survive a refresh.")
        return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
