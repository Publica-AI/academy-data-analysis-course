#!/usr/bin/env python3
"""Topic 8.2 solution file: a trend forecast for SwiftRoute's Q4 2026, with its uncertainty.

Runs on swiftroute_q3_cleaned.xlsx, the output of Topic 8.1, and writes
swiftroute_q4_forecast.xlsx plus q4_forecast.png.

The forecast is deliberately a straight line fitted to weekly totals. That is the whole
method: one assumption, made explicit, and the honest reporting of how much it explains.

Three things this file is designed to teach, all of them visible in the output:

1. Partial periods at the ends will wreck a trend if you let them. Q3 2026 starts on a
   Wednesday and ends on a Wednesday, so the first and last calendar weeks hold 190 and 113
   deliveries against a typical 270. Fit on all 14 weeks and the slope comes out slightly
   negative with an R-squared of 0.0008. Drop the two partial weeks and the same data gives
   a positive slope. Nothing changed except which rows you were entitled to use.

2. A trend line is not a promise. On the 12 complete weeks the fit explains about a third
   of the week to week variation, so the range matters more than the point estimate.

3. The naive baseline has to be beaten before the model is worth using. Q3's weekly mean
   projected flat across Q4 is the number to beat.

    python build_forecast.py
"""
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
CLEAN = os.path.join(HERE, "swiftroute_q3_cleaned.xlsx")
OUT_XLSX = os.path.join(HERE, "swiftroute_q4_forecast.xlsx")
OUT_PNG = os.path.join(HERE, "q4_forecast.png")

Q4_WEEKS = 13


def weekly_totals(path):
    df = pd.read_excel(path, sheet_name="deliveries_clean")
    df = df[df["date"].notna()].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["week"] = df["date"].dt.to_period("W-SUN")
    w = (df.groupby("week")
           .agg(deliveries=("delivery_id", "count"), revenue=("fee_naira", "sum"))
           .reset_index())
    w["week_start"] = w["week"].dt.start_time.dt.date
    w["week_end"] = w["week"].dt.end_time.dt.date
    return w


def fit(y):
    x = np.arange(len(y), dtype=float)
    slope, intercept = np.polyfit(x, y, 1)
    fitted = intercept + slope * x
    resid = y - fitted
    ss_res = float((resid ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": 1 - ss_res / ss_tot,
        "resid_sd": float(resid.std(ddof=2)),
        "mape": float(np.mean(np.abs(resid / y)) * 100),
        "fitted": fitted,
    }


def forecast(model, n_history, n_ahead):
    x = np.arange(n_history, n_history + n_ahead, dtype=float)
    point = model["intercept"] + model["slope"] * x
    sd = model["resid_sd"]
    return point, point - sd, point + sd


def main():
    if not os.path.exists(CLEAN):
        print("missing %s. Run clean_swiftroute_q3.py in topic 01 first." % CLEAN)
        return 1

    w = weekly_totals(CLEAN)
    print("%d calendar weeks in the cleaned data" % len(w))
    print(w[["week_start", "week_end", "deliveries", "revenue"]].to_string(index=False))

    # ---- lesson 1: what the partial weeks do to the slope
    all_fit = fit(w["deliveries"].values.astype(float))
    print("\nfitted on all %d weeks, partial ends included:" % len(w))
    print("  slope %+.3f deliveries per week, R-squared %.4f" % (all_fit["slope"], all_fit["r2"]))

    complete = w.iloc[1:-1].reset_index(drop=True)
    y = complete["deliveries"].values.astype(float)
    m = fit(y)
    print("\nfitted on the %d complete weeks only:" % len(complete))
    print("  slope %+.3f deliveries per week, R-squared %.4f" % (m["slope"], m["r2"]))
    print("  residual standard deviation %.1f deliveries, MAPE %.2f%%" % (m["resid_sd"], m["mape"]))

    point, lo, hi = forecast(m, len(complete), Q4_WEEKS)
    naive = y.mean() * Q4_WEEKS

    yr = complete["revenue"].values.astype(float)
    mr = fit(yr)
    rpoint, rlo, rhi = forecast(mr, len(complete), Q4_WEEKS)

    print("\nQ4 2026 FORECAST, 13 weeks")
    print("  deliveries, point estimate      %,d".replace(",", "") % round(point.sum()))
    print("  deliveries, range at +/- 1 sd   %d to %d" % (round(lo.sum()), round(hi.sum())))
    print("  naive baseline, Q3 mean flat    %d" % round(naive))
    print("  revenue, point estimate         N%d" % round(rpoint.sum()))
    print("  revenue, range at +/- 1 sd      N%d to N%d" % (round(rlo.sum()), round(rhi.sum())))

    print("\nWHAT TO SAY TO THE BUSINESS")
    print("  Between %d and %d deliveries next quarter, most likely around %d."
          % (round(lo.sum()), round(hi.sum()), round(point.sum())))
    print("  The trend explains about %d per cent of the week to week variation, so plan"
          % round(m["r2"] * 100))
    print("  against the range, not the single number. One quarter of history is thin.")

    weeks_out = pd.DataFrame({
        "q4_week": np.arange(1, Q4_WEEKS + 1),
        "forecast_deliveries": point.round(1),
        "low_1sd": lo.round(1),
        "high_1sd": hi.round(1),
        "forecast_revenue_naira": rpoint.round(0),
        "revenue_low_1sd": rlo.round(0),
        "revenue_high_1sd": rhi.round(0),
    })
    summary = pd.DataFrame({
        "metric": ["complete weeks used", "slope (deliveries per week)", "intercept",
                   "r_squared", "residual_sd", "mape_percent",
                   "q4_forecast_deliveries", "q4_low_1sd", "q4_high_1sd",
                   "q4_naive_baseline", "q4_forecast_revenue_naira",
                   "slope_if_partial_weeks_included", "r2_if_partial_weeks_included"],
        "value": [len(complete), round(m["slope"], 3), round(m["intercept"], 2),
                  round(m["r2"], 4), round(m["resid_sd"], 2), round(m["mape"], 2),
                  round(point.sum()), round(lo.sum()), round(hi.sum()),
                  round(naive), round(rpoint.sum()),
                  round(all_fit["slope"], 3), round(all_fit["r2"], 4)],
    })

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as x:
        w.drop(columns=["week"]).to_excel(x, sheet_name="weekly_actuals", index=False)
        complete.drop(columns=["week"]).to_excel(x, sheet_name="complete_weeks", index=False)
        weeks_out.to_excel(x, sheet_name="q4_forecast", index=False)
        summary.to_excel(x, sheet_name="summary", index=False)
    print("\nwrote %s" % OUT_XLSX)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(11, 5.5), dpi=160)
        hx = np.arange(1, len(complete) + 1)
        fx = np.arange(len(complete) + 1, len(complete) + 1 + Q4_WEEKS)
        ax.plot(hx, y, "o-", color="#387F7F", lw=2, label="Q3 actual, complete weeks")
        ax.plot(hx, m["fitted"], "--", color="#0A1A23", lw=1.2, label="fitted trend")
        ax.plot(fx, point, "o--", color="#A8322D", lw=2, label="Q4 forecast")
        ax.fill_between(fx, lo, hi, color="#A8322D", alpha=0.15,
                        label="range, plus or minus one residual sd")
        ax.axhline(y.mean(), color="#64748B", lw=1, ls=":", label="Q3 weekly mean")
        ax.set_xlabel("week")
        ax.set_ylabel("deliveries")
        ax.set_title("SwiftRoute weekly deliveries: Q3 2026 actual and Q4 forecast\n"
                     "trend explains %d per cent of week to week variation" % round(m["r2"] * 100))
        ax.legend(frameon=False, fontsize=9)
        ax.spines[["top", "right"]].set_visible(False)
        fig.tight_layout()
        fig.savefig(OUT_PNG)
        print("wrote %s" % OUT_PNG)
    except ImportError:
        print("matplotlib not available, skipped the chart")
    return 0


if __name__ == "__main__":
    sys.exit(main())
