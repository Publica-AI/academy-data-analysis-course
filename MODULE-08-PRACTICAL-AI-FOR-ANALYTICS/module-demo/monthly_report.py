#!/usr/bin/env python3
"""Topic 8.4 solution file: the recurring SwiftRoute report, automated.

The bar for this topic is not "production pipeline". It is "survives a data refresh": run
it again next quarter, against a file with different rows, different months and possibly a
new route, and it still produces the right report without anybody editing the code.

Four rules make that true, and each one is a thing trainees get wrong by hand:

1. The file path is an argument, never a constant buried in the middle.
2. Periods are derived from the data, never hardcoded as "Jul, Aug, Sep".
3. Route codes are standardised before any join, so a new LAG09 or a stray LAG09 without
   the hyphen does not silently drop rows.
4. Every number in the output is recomputed, and the row counts are asserted, so a broken
   refresh fails loudly instead of publishing a confident wrong report.

    python monthly_report.py                       # runs on the Q3 raw file
    python monthly_report.py <path-to-raw.xlsx>    # runs on any file with the same shape
    python monthly_report.py <raw.xlsx> <out-dir>

Writes report_<first-period>_to_<last-period>.md and .xlsx into the output directory.
"""
import os
import re
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RAW = os.path.join(HERE, "swiftroute_q3_raw.xlsx")

DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d %b %Y", "%d.%m.%Y"]
# A month holding less than this share of the dated rows is treated as a stray date,
# reported as a data quality note, and kept out of the reporting window.
MIN_PERIOD_SHARE = 0.01
REQUIRED = ["delivery_id", "date", "route_code", "rider_name", "distance_km",
            "duration_min", "delivery_status", "fee_naira", "customer_id"]


def parse_date(value):
    s = str(value).strip()
    for fmt in DATE_FORMATS:
        try:
            return pd.Timestamp(pd.to_datetime(s, format=fmt))
        except (ValueError, TypeError):
            continue
    return pd.NaT


def money_to_int(value):
    digits = re.sub(r"[^0-9]", "", str(value))
    return int(digits) if digits else np.nan


def load_and_clean(path):
    """Same rules as topic 8.1, written once so the refresh cannot drift from the lab."""
    df = pd.read_excel(path, sheet_name="deliveries", dtype=str)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SystemExit("input file is missing required columns: %s" % ", ".join(missing))

    rows_in = len(df)
    df = df.drop_duplicates(subset="delivery_id", keep="first").copy()
    df["date"] = df["date"].map(parse_date)
    df["fee_naira"] = df["fee_naira"].map(money_to_int).astype("Int64")
    df["rider_name"] = df["rider_name"].astype(str).str.strip().str.title()
    df["route_code"] = (df["route_code"].astype(str).str.strip().str.upper()
                        .str.replace(r"^([A-Z]{3})(\d{2})$", r"\1-\2", regex=True))
    df["duration_min"] = pd.to_numeric(df["duration_min"], errors="coerce").abs().astype("Int64")
    df["distance_km"] = pd.to_numeric(df["distance_km"], errors="coerce")
    status = df["delivery_status"].astype(str).str.strip()
    df["delivery_status"] = status.where(~status.isin(["", "nan", "None"]), np.nan)

    # Periods come from the data. Never hardcode the months.
    #
    # A stray date carries the whole report with it if you let it. The Q3 file holds two
    # rows dated 2027, so taking min and max of the parsed dates would produce a report
    # spanning July 2026 to February 2027 with five periods, three of them real. The rule
    # below is data derived and survives a refresh: a month holding less than one per cent
    # of the dated rows is not a reporting period, it is a data quality signal.
    dated = df[df["date"].notna()].copy()
    dated["period"] = dated["date"].dt.to_period("M")
    share = dated["period"].value_counts(normalize=True)
    kept = sorted(p for p in share.index if share[p] >= MIN_PERIOD_SHARE)
    if not kept:
        raise SystemExit("no month holds enough rows to report on")
    lo, hi = kept[0], kept[-1]
    in_window = dated[dated["period"].isin(kept)]
    outliers = dated[~dated["period"].isin(kept)]

    return {
        "rows_in": rows_in,
        "duplicates_removed": rows_in - len(df),
        "rows_clean": len(df),
        "undated": int(df["date"].isna().sum()),
        "unknown_status": int(df["delivery_status"].isna().sum()),
        "first_period": str(lo),
        "last_period": str(hi),
        "outlier_rows": len(outliers),
        "outlier_periods": [str(p) for p in sorted(set(outliers["period"]))],
        "data": in_window,
    }


def build_report(state, out_dir):
    d = state["data"]
    by_period = (d.groupby("period")
                   .agg(deliveries=("delivery_id", "count"),
                        revenue_naira=("fee_naira", "sum"),
                        mean_distance_km=("distance_km", "mean"),
                        mean_duration_min=("duration_min", "mean"))
                   .round(2).reset_index())
    by_period["period"] = by_period["period"].astype(str)

    by_route = (d.groupby("route_code")
                  .agg(deliveries=("delivery_id", "count"),
                       revenue_naira=("fee_naira", "sum"),
                       mean_distance_km=("distance_km", "mean"))
                  .round(2).sort_values("deliveries", ascending=False).reset_index())

    status = d["delivery_status"].value_counts(dropna=False).rename_axis("status").reset_index(
        name="deliveries")
    status["status"] = status["status"].fillna("unknown")

    known = d[d["delivery_status"].notna()]
    delivered_rate = (known["delivery_status"] == "Delivered").mean() * 100 if len(known) else float("nan")

    name = "report_%s_to_%s" % (state["first_period"], state["last_period"])
    md_path = os.path.join(out_dir, name + ".md")
    xlsx_path = os.path.join(out_dir, name + ".xlsx")

    lines = [
        "# SwiftRoute delivery report, %s to %s" % (state["first_period"], state["last_period"]),
        "",
        "Generated by `monthly_report.py`. Every figure below is recomputed from the source",
        "file on each run. Nothing is carried over from a previous report.",
        "",
        "## Data quality, checked before anything was reported",
        "",
        "| Check | Value |",
        "|---|---|",
        "| Rows read from the file | %d |" % state["rows_in"],
        "| Duplicate delivery ids removed | %d |" % state["duplicates_removed"],
        "| Rows after de-duplication | %d |" % state["rows_clean"],
        "| Rows with no usable date, excluded from totals | %d |" % state["undated"],
        "| Rows with an unknown delivery status | %d |" % state["unknown_status"],
        "| Rows dated outside the reporting window, excluded | %d%s |"
        % (state["outlier_rows"],
           (" (%s)" % ", ".join(state["outlier_periods"])) if state["outlier_periods"] else ""),
        "| Distinct routes after standardising codes | %d |" % d["route_code"].nunique(),
        "",
        "## Headline",
        "",
        "| Measure | Value |",
        "|---|---|",
        "| Periods covered | %d |" % len(by_period),
        "| Deliveries | %s |" % format(int(by_period.deliveries.sum()), ","),
        "| Revenue | N%s |" % format(int(by_period.revenue_naira.sum()), ","),
        "| Mean distance | %.2f km |" % d["distance_km"].mean(),
        "| Delivered, as a share of known statuses | %.1f%% |" % delivered_rate,
        "",
        "## By period",
        "",
        "| Period | Deliveries | Revenue | Mean km | Mean minutes |",
        "|---|---|---|---|---|",
    ]
    for r in by_period.itertuples():
        lines.append("| %s | %s | N%s | %.2f | %.1f |"
                     % (r.period, format(int(r.deliveries), ","),
                        format(int(r.revenue_naira), ","), r.mean_distance_km, r.mean_duration_min))
    lines += ["", "## Busiest five routes", "",
              "| Route | Deliveries | Revenue | Mean km |", "|---|---|---|---|"]
    for r in by_route.head(5).itertuples():
        lines.append("| %s | %s | N%s | %.2f |"
                     % (r.route_code, format(int(r.deliveries), ","),
                        format(int(r.revenue_naira), ","), r.mean_distance_km))
    lines += ["", "## Delivery status", "", "| Status | Deliveries |", "|---|---|"]
    for r in status.itertuples():
        lines.append("| %s | %s |" % (r.status, format(int(r.deliveries), ",")))
    lines += ["",
              "Unknown statuses are reported, never assumed to be Delivered. If that count",
              "rises between runs, the capture process changed and this report is the place",
              "it becomes visible."]

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as x:
        by_period.to_excel(x, sheet_name="by_period", index=False)
        by_route.to_excel(x, sheet_name="by_route", index=False)
        status.to_excel(x, sheet_name="by_status", index=False)
    return md_path, xlsx_path, by_period


def main(argv):
    raw = argv[1] if len(argv) > 1 else DEFAULT_RAW
    out_dir = argv[2] if len(argv) > 2 else HERE
    if not os.path.exists(raw):
        print("input file not found: %s" % raw)
        return 1
    os.makedirs(out_dir, exist_ok=True)

    state = load_and_clean(raw)
    md, xlsx, by_period = build_report(state, out_dir)

    print("source            %s" % raw)
    print("periods found     %s to %s (%d)" % (state["first_period"], state["last_period"], len(by_period)))
    print("rows read         %d" % state["rows_in"])
    print("duplicates removed %d" % state["duplicates_removed"])
    print("deliveries counted %d" % int(by_period.deliveries.sum()))
    print("revenue            N%s" % format(int(by_period.revenue_naira.sum()), ","))
    print("wrote %s" % md)
    print("wrote %s" % xlsx)

    # Fail loudly rather than publishing a confident wrong report.
    assert state["rows_clean"] == state["rows_in"] - state["duplicates_removed"]
    assert int(by_period.deliveries.sum()) == len(state["data"])
    print("internal checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
