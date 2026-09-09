#!/usr/bin/env python3
"""Check every claim in SWIFTROUTE_Q3_FAULT_LOG.md against the actual workbooks.

Run it after any regeneration of the dataset, and before shipping anything that quotes a
figure from it. Exits 0 when every check passes, 1 otherwise.

    python verify_swiftroute_q3.py

Requires: pandas, openpyxl.
"""
import collections
import json
import os
import re
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "swiftroute_q3_raw.xlsx")
KEY = os.path.join(HERE, "swiftroute_q3_answer_key.xlsx")

DATE_PATTERNS = {
    "YYYY-MM-DD": r"^\d{4}-\d{2}-\d{2}$",
    "DD/MM/YYYY": r"^\d{2}/\d{2}/\d{4}$",
    "MM-DD-YYYY": r"^\d{2}-\d{2}-\d{4}$",
    "D Mon YYYY": r"^\d{1,2} [A-Za-z]{3} \d{4}$",
    "DD.MM.YYYY": r"^\d{2}\.\d{2}\.\d{4}$",
}

IMPOSSIBLE = {
    "SR-Q3-002289": ("duration_min", "-35"),
    "SR-Q3-002303": ("duration_min", "-99"),
    "SR-Q3-000972": ("duration_min", "-122"),
    "SR-Q3-001746": ("duration_min", "-65"),
    "SR-Q3-001458": ("date", "14.01.2027"),
    "SR-Q3-000794": ("date", "2027-02-03"),
}

results = []


def check(label, got, expected):
    ok = got == expected
    results.append((ok, label, got, expected))
    print("%-5s %-52s got %-28s expected %s"
          % ("PASS" if ok else "FAIL", label, repr(got), repr(expected)))
    return ok


def main():
    for path in (RAW, KEY):
        if not os.path.exists(path):
            print("FAIL  missing file: %s" % path)
            return 1

    raw = pd.read_excel(RAW, sheet_name="deliveries", dtype=str)
    key = pd.read_excel(KEY, sheet_name="deliveries_clean")
    fuel = pd.read_excel(RAW, sheet_name="fuel_cost")
    comp = pd.read_excel(RAW, sheet_name="customer_complaints")

    # ---- shape
    check("deliveries row count", len(raw), 3640)
    check("unique delivery_ids", raw.delivery_id.nunique(), 3600)
    check("answer key row count", len(key), 3600)
    check("answer key has no duplicate ids", key.delivery_id.nunique(), 3600)
    check("same id set in raw and key", set(raw.delivery_id) == set(key.delivery_id), True)

    # ---- fault 1, mixed date formats
    counts = {name: sum(bool(re.match(pat, str(v))) for v in raw.date)
              for name, pat in DATE_PATTERNS.items()}
    check("every date matches one of five formats", sum(counts.values()), 3640)
    check("all five date formats present", all(c > 0 for c in counts.values()), True)

    # ---- fault 2, naira amounts as text
    check("fee_naira rows carrying the naira sign",
          sum(str(v).startswith("₦") for v in raw.fee_naira), 3640)

    # ---- fault 3, rider name whitespace and casing
    canonical = set(key.rider_name)
    altered = sum(1 for v in raw.rider_name
                  if str(v) != str(v).strip() or str(v).strip() not in canonical)
    check("rider_name rows altered", altered, 628)
    check("every altered rider name trims to a canonical name",
          all(str(v).strip() in canonical or str(v).strip().title() in canonical
              for v in raw.rider_name), True)

    # ---- fault 4, route code inconsistency
    rc = collections.Counter(raw.route_code)
    check("LAG-07 hyphenated rows", rc.get("LAG-07"), 144)
    check("LAG07 unhyphenated rows", rc.get("LAG07"), 144)
    check("LAG-07 rows in total", rc.get("LAG-07", 0) + rc.get("LAG07", 0), 288)
    check("fuel_cost uses only canonical route codes",
          any(c == "LAG07" for c in fuel.route_code), False)

    # ---- fault 5, blank statuses
    check("blank delivery_status rows",
          sum(1 for v in raw.delivery_status if pd.isna(v) or str(v).strip() == ""), 116)

    # ---- fault 6, impossible values
    for did, (field, value) in IMPOSSIBLE.items():
        row = raw[raw.delivery_id == did]
        got = str(row[field].iloc[0]) if len(row) else "<missing>"
        check("impossible value %s.%s" % (did, field), got, value)
    negatives = pd.to_numeric(raw.duration_min, errors="coerce")
    check("negative durations in total", int((negatives < 0).sum()), 4)
    check("dates falling in 2027", sum("2027" in str(v) for v in raw.date), 2)

    # ---- fault 7, duplicates
    dups = [k for k, v in collections.Counter(raw.delivery_id).items() if v > 1]
    check("duplicated delivery_ids", len(dups), 40)
    check("no id appears more than twice",
          max(collections.Counter(raw.delivery_id).values()), 2)

    # ---- untouched sheets
    check("fuel_cost rows", len(fuel), 42)
    check("fuel_cost routes", fuel.route_code.nunique(), 14)
    check("fuel_cost months", fuel.month.nunique(), 3)
    check("complaint rows", len(comp), 175)
    check("every complaint points at a real delivery",
          bool(comp.delivery_id.isin(set(raw.delivery_id)).all()), True)

    # ---- hard rules
    all_cols = list(raw.columns) + list(fuel.columns) + list(comp.columns)
    check("no week numbers in any sheet",
          [c for c in all_cols if "week" in c.lower()], [])
    for col in ("rider_name",):
        check("%s carries generated names only, no real contact data" % col,
              bool(raw[col].astype(str).str.contains(r"@|\+234|https?://").any()), False)

    failed = [r for r in results if not r[0]]
    print("\n%d checks, %d passed, %d failed" % (len(results), len(results) - len(failed), len(failed)))
    if failed:
        print("\nFAILED CHECKS:")
        for _, label, got, exp in failed:
            print("  %s: got %r, expected %r" % (label, got, exp))
        return 1
    print("All fault log claims verified against the workbooks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
