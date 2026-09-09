#!/usr/bin/env python3
"""Topic 8.5 demonstration: correct arithmetic, wrong question.

This is the live example for failure mode 4. It does exactly what an AI assistant does when
you ask it for margin by route: joins the two sheets correctly, subtracts fuel from revenue,
and reports the answer with total confidence.

Every number it prints is right. The conclusion is still nonsense, and no step in the
calculation could have told you that. Only question 5 of the verification checklist does.

    python margin_trap.py
"""
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "swiftroute_q3_raw.xlsx")
CLEAN = os.path.join(HERE, "swiftroute_q3_cleaned.xlsx")


def main():
    source = CLEAN if os.path.exists(CLEAN) else None
    if source is None:
        print("missing swiftroute_q3_cleaned.xlsx, run topic 8.1's cleaner first")
        return 1

    d = pd.read_excel(source, sheet_name="deliveries_clean")
    fuel = pd.read_excel(RAW, sheet_name="fuel_cost")

    d = d[d["date"].notna()].copy()
    d["date"] = pd.to_datetime(d["date"])
    d["month"] = d["date"].dt.strftime("%b-%Y")

    rev = (d.groupby(["route_code", "month"])
             .agg(deliveries=("delivery_id", "count"), revenue=("fee_naira", "sum"))
             .reset_index())
    m = rev.merge(fuel, on=["route_code", "month"], how="inner")
    if len(m) != len(fuel):
        print("join dropped rows: %d of %d fuel rows matched" % (len(m), len(fuel)))

    m["margin"] = m["revenue"] - m["total_fuel_cost_naira"]
    by_route = (m.groupby("route_code")
                  .agg(deliveries=("deliveries", "sum"),
                       revenue=("revenue", "sum"),
                       fuel=("total_fuel_cost_naira", "sum"))
                  .assign(margin=lambda t: t.revenue - t.fuel)
                  .sort_values("margin"))

    print("MARGIN BY ROUTE, Q3 2026")
    print("(this is the answer, and it is arithmetically correct)\n")
    print(by_route.round(0).to_string())

    total_rev = by_route.revenue.sum()
    total_fuel = by_route.fuel.sum()
    print("\ntotal revenue  N{:,.0f}".format(total_rev))
    print("total fuel     N{:,.0f}".format(total_fuel))
    print("total margin   N{:,.0f}".format(total_rev - total_fuel))
    print("fuel is {:.2f} times revenue".format(total_fuel / total_rev))
    print("routes with a positive margin: %d of %d"
          % (int((by_route.margin > 0).sum()), len(by_route)))

    print("\nNOW ASK QUESTION 5")
    print("  Would someone who knows this business accept that SwiftRoute lost money on")
    print("  every single route for an entire quarter, and nobody mentioned it?")
    print("  Both sheets are internally sound. Fuel at {:.2f} km per litre and about"
          .format(d.distance_km.sum() / fuel.litres_consumed.sum()))
    print("  N{:.0f} a litre is realistic. The mean fee is N{:.0f} for a mean {:.1f} km run."
          .format(fuel.price_per_litre_naira.mean(), d.fee_naira.mean(), d.distance_km.mean()))
    print("  What is not sound is the comparison: a fleet level fuel bill set against a")
    print("  3,600 row delivery extract that averages about three deliveries per route per")
    print("  day. The two are not at the same grain, and nothing in the calculation says so.")
    print("\n  The finding to report is not 'every route is loss making'. It is 'these two")
    print("  sheets cannot be compared until someone tells us what the delivery extract is")
    print("  a sample of'. That sentence is the deliverable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
