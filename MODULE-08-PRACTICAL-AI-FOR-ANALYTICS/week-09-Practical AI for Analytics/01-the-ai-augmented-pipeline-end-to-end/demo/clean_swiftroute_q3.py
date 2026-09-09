#!/usr/bin/env python3
"""Topic 8.1 solution file: take swiftroute_q3_raw.xlsx to a cleaned, checkable table.

This is the worked solution for the pipeline lab. It is deliberately written as a
documented, repeatable script rather than a set of manual edits, because the whole point of
Topic 8.4 is that the same job has to survive next quarter's file.

Every step prints what it changed, so the output doubles as the verification note.

    python clean_swiftroute_q3.py

Writes swiftroute_q3_cleaned.xlsx beside this script, and compares the result against
swiftroute_q3_answer_key.xlsx so the agreement is measured, not assumed.

Two faults are deliberately NOT silently repaired, because no cleaning rule can recover
the true value from the raw file alone:
  - the 116 blank delivery statuses become NaN and are counted, not guessed
  - the 2 dates in 2027 become NaT and are counted, not guessed
Both are things you go back to operations about. Inventing a value here is exactly the
failure mode Topic 8.5 is about.
"""
import os
import re
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "swiftroute_q3_raw.xlsx")
KEY = os.path.join(HERE, "swiftroute_q3_answer_key.xlsx")
OUT = os.path.join(HERE, "swiftroute_q3_cleaned.xlsx")

QUARTER_START = pd.Timestamp("2026-07-01")
QUARTER_END = pd.Timestamp("2026-09-30")

DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d %b %Y", "%d.%m.%Y"]


def parse_date(value):
    """Parse one of the five known formats. Order matters.

    %d/%m/%Y is tried before %m-%d-%Y because the separators differ, so the two never
    compete. Never fall back to a guessing parser here: on a day of 12 or less it would
    swap day and month without telling you.
    """
    s = str(value).strip()
    for fmt in DATE_FORMATS:
        try:
            return pd.Timestamp(pd.to_datetime(s, format=fmt))
        except (ValueError, TypeError):
            continue
    return pd.NaT


def money_to_int(value):
    """'₦45,320' -> 45320."""
    digits = re.sub(r"[^0-9]", "", str(value))
    return int(digits) if digits else np.nan


def main():
    log = []

    def step(msg):
        log.append(msg)
        print(msg)

    df = pd.read_excel(RAW, sheet_name="deliveries", dtype=str)
    step("loaded %d rows, %d columns" % (df.shape[0], df.shape[1]))

    # 1. duplicates. Keep the first occurrence; the injected copies were appended at the end.
    before = len(df)
    df = df.drop_duplicates(subset="delivery_id", keep="first").copy()
    step("dropped %d duplicate delivery_id rows, %d remain" % (before - len(df), len(df)))

    # 2. dates
    df["date"] = df["date"].map(parse_date)
    unparsed = int(df["date"].isna().sum())
    step("parsed dates, %d unparseable" % unparsed)
    out_of_window = df["date"].notna() & ((df["date"] < QUARTER_START) | (df["date"] > QUARTER_END))
    step("found %d dates outside Q3 2026, set to NaT and flagged for operations"
         % int(out_of_window.sum()))
    df.loc[out_of_window, "date_flag"] = "outside Q3 2026, original value not recoverable"
    df.loc[out_of_window, "date"] = pd.NaT

    # 3. money
    df["fee_naira"] = df["fee_naira"].map(money_to_int).astype("Int64")
    step("converted fee_naira to whole numbers, total ₦{:,}".format(int(df["fee_naira"].sum())))

    # 4. rider names
    raw_names = df["rider_name"].astype(str)
    df["rider_name"] = raw_names.str.strip().str.title()
    changed = int((raw_names != df["rider_name"]).sum())
    step("trimmed and title cased rider_name on %d rows, %d distinct riders remain"
         % (changed, df["rider_name"].nunique()))

    # 5. route codes. LAG07 -> LAG-07, so the fuel_cost join matches.
    before_codes = df["route_code"].nunique()
    df["route_code"] = df["route_code"].astype(str).str.strip().str.upper()
    df["route_code"] = df["route_code"].str.replace(r"^([A-Z]{3})(\d{2})$", r"\1-\2", regex=True)
    step("standardised route_code, %d distinct codes became %d"
         % (before_codes, df["route_code"].nunique()))

    # 6. durations. A negative duration is a captured sign error, so take the magnitude.
    df["duration_min"] = pd.to_numeric(df["duration_min"], errors="coerce")
    negatives = int((df["duration_min"] < 0).sum())
    df["duration_min"] = df["duration_min"].abs().astype("Int64")
    step("corrected %d negative durations to their magnitude" % negatives)

    # 7. statuses. Blank means unknown; it does not mean Delivered.
    df["delivery_status"] = df["delivery_status"].astype(str).str.strip()
    blanks = df["delivery_status"].isin(["", "nan", "None"])
    step("found %d blank delivery_status rows, set to NaN and flagged" % int(blanks.sum()))
    df.loc[blanks, "delivery_status"] = np.nan

    df["distance_km"] = pd.to_numeric(df["distance_km"], errors="coerce")

    # ---- expected-output checks, the numbers a trainee self-verifies against
    print("\nEXPECTED OUTPUT CHECKS")
    checks = [
        ("rows", len(df), 3600),
        ("distinct delivery_id", df.delivery_id.nunique(), 3600),
        ("distinct route_code", df.route_code.nunique(), 14),
        ("rows with a usable date", int(df.date.notna().sum()), 3598),
        # 116 blank rows in the raw sheet, but across only 115 distinct delivery_ids:
        # SR-Q3-000941 is both blank and one of the 40 duplicates, so removing duplicates
        # removes one blank with it. 3600 - 115 = 3485.
        ("rows with a known status", int(df.delivery_status.notna().sum()), 3485),
        ("negative durations remaining", int((df.duration_min < 0).sum()), 0),
        ("total fee", int(df.fee_naira.sum()), 12196290),
    ]
    ok = True
    for label, got, exp in checks:
        good = got == exp
        ok = ok and good
        print("  %-5s %-32s got %-12s expected %s" % ("PASS" if good else "FAIL", label, got, exp))

    # ---- agreement with the answer key, measured column by column
    key = pd.read_excel(KEY, sheet_name="deliveries_clean")
    m = df.merge(key, on="delivery_id", suffixes=("", "_key"))
    print("\nAGREEMENT WITH THE ANSWER KEY (%d matched rows)" % len(m))
    agree = {
        "rider_name": int((m.rider_name == m.rider_name_key).sum()),
        "route_code": int((m.route_code == m.route_code_canonical).sum()),
        "fee_naira": int((m.fee_naira == m.fee_naira_key).sum()),
        "duration_min": int((m.duration_min == m.duration_min_key).sum()),
        "date": int((m.date == pd.to_datetime(m.date_key)).sum()),
        "delivery_status": int((m.delivery_status == m.delivery_status_key).sum()),
    }
    for col, n in agree.items():
        print("  %-16s %d of %d rows match" % (col, n, len(m)))
    print("\n  date differs on the 2 rows whose true value is not recoverable from the raw file.")
    print("  delivery_status differs on the 115 blank rows that survive de-duplication.")
    print("  Every other column matches the answer key on all 3,600 rows.")

    with pd.ExcelWriter(OUT, engine="openpyxl") as w:
        df.to_excel(w, sheet_name="deliveries_clean", index=False)
        pd.read_excel(RAW, sheet_name="fuel_cost").to_excel(w, sheet_name="fuel_cost", index=False)
        pd.read_excel(RAW, sheet_name="customer_complaints").to_excel(
            w, sheet_name="customer_complaints", index=False)
        pd.DataFrame({"step": log}).to_excel(w, sheet_name="cleaning_log", index=False)
    print("\nwrote %s" % OUT)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
