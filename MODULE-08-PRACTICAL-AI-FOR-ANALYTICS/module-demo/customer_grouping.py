#!/usr/bin/env python3
"""Topic 8.3 demonstration: what clustering finds in SwiftRoute's Q3 customers.

This topic is literacy only. Nobody builds a model in the lab, and nothing here is
presented as a deliverable. The script exists so the facilitator can show a real clustering
result on the module's own data, in plain language, and then show the two ways it misleads.

Reads swiftroute_q3_cleaned.xlsx, writes customer_groups.xlsx and customer_groups.png.

Three things it demonstrates:

1. Clustering finds groups nobody defined. There is no column called "customer type", and
   the algorithm was never told what to look for.
2. Forgetting to put the columns on the same scale changes the answer completely. Fee runs
   into the thousands and delivery count runs from 1 to 12, so unscaled distance is
   effectively fee alone.
3. The number of groups is your decision, not the data's. The same customers split three
   ways or five ways on request, and both look equally convincing on a chart.

    python customer_grouping.py
"""
import os
import sys

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

HERE = os.path.dirname(os.path.abspath(__file__))
CLEAN = os.path.join(HERE, "swiftroute_q3_cleaned.xlsx")
OUT_XLSX = os.path.join(HERE, "customer_groups.xlsx")
OUT_PNG = os.path.join(HERE, "customer_groups.png")

SEED = 8003
FEATURES = ["deliveries", "mean_fee_naira", "mean_distance_km"]


def customer_table(path):
    d = pd.read_excel(path, sheet_name="deliveries_clean")
    c = (d.groupby("customer_id")
           .agg(deliveries=("delivery_id", "count"),
                mean_fee_naira=("fee_naira", "mean"),
                mean_distance_km=("distance_km", "mean"),
                total_fee_naira=("fee_naira", "sum"))
           .reset_index())
    return c


def cluster(frame, k, scale=True):
    x = frame[FEATURES].values.astype(float)
    if scale:
        x = StandardScaler().fit_transform(x)
    km = KMeans(n_clusters=k, n_init=10, random_state=SEED)
    return km.fit_predict(x)


def describe(frame, labels, title):
    f = frame.copy()
    f["group"] = labels
    summary = (f.groupby("group")
                 .agg(customers=("customer_id", "count"),
                      mean_deliveries=("deliveries", "mean"),
                      mean_fee=("mean_fee_naira", "mean"),
                      mean_km=("mean_distance_km", "mean"),
                      total_revenue=("total_fee_naira", "sum"))
                 .round(1)
                 .sort_values("mean_deliveries", ascending=False))
    print("\n%s" % title)
    print(summary.to_string())
    return f, summary


def main():
    if not os.path.exists(CLEAN):
        print("missing %s. Copy it from topic 01 or run clean_swiftroute_q3.py first." % CLEAN)
        return 1

    c = customer_table(CLEAN)
    print("%d customers, %d deliveries, total revenue N%d"
          % (len(c), int(c.deliveries.sum()), int(c.total_fee_naira.sum())))

    labels3 = cluster(c, 3, scale=True)
    f3, s3 = describe(c, labels3, "THREE GROUPS, columns put on the same scale")

    print("\nIn plain language, what the algorithm separated:")
    # Name each group from its own numbers rather than from its position, so the labels
    # stay honest if the data is regenerated.
    top = s3.mean_deliveries.idxmax()
    rest = [g for g in s3.index if g != top]
    rest.sort(key=lambda g: s3.loc[g, "mean_km"])
    naming = [(top, "frequent customers"),
              (rest[0], "occasional, short hops"),
              (rest[1], "occasional, long hauls")]
    for g, name in naming:
        row = s3.loc[g]
        print("  %-24s %d customers, about %.1f deliveries each at N%d average fee over %.0f km"
              % (name, row.customers, row.mean_deliveries, row.mean_fee, row.mean_km))
    print("  Note what actually separates the second and third groups: not how often they")
    print("  order, which is the same, but how far the delivery goes and therefore what it")
    print("  costs. Nobody labelled these. There is no customer type column in the data.")

    labels_unscaled = cluster(c, 3, scale=False)
    agree = float((pd.crosstab(labels3, labels_unscaled).max(axis=1).sum()) / len(c))
    print("\nSAME DATA, SAME k, COLUMNS LEFT ON THEIR ORIGINAL SCALES")
    describe(c, labels_unscaled, "three groups, unscaled")
    print("  Only %.0f per cent of customers land in a matching group." % (agree * 100))
    print("  Unscaled, fee runs to thousands and delivery count runs to twelve, so the")
    print("  algorithm is effectively grouping on fee alone. Nothing warns you about this.")

    labels5 = cluster(c, 5, scale=True)
    describe(c, labels5, "FIVE GROUPS, same data, same method, k changed on request")
    print("  Equally convincing, and a different answer. k is a decision you make and")
    print("  must be able to defend, not something the data hands you.")

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as x:
        f3.to_excel(x, sheet_name="customers_k3", index=False)
        s3.reset_index().to_excel(x, sheet_name="summary_k3", index=False)
        c.assign(group_unscaled=labels_unscaled, group_k5=labels5).to_excel(
            x, sheet_name="comparisons", index=False)
    print("\nwrote %s" % OUT_XLSX)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        palette = ["#387F7F", "#A8322D", "#64748B", "#B08B2E", "#4B6BA8"]
        fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=160, sharey=True)
        for ax, labs, title in ((axes[0], labels3, "Scaled: groups differ by how often they order"),
                                (axes[1], labels_unscaled, "Unscaled: groups differ by fee alone")):
            for g in sorted(set(labs)):
                sel = labs == g
                ax.scatter(c.deliveries[sel], c.mean_fee_naira[sel], s=14, alpha=0.75,
                           color=palette[g % len(palette)], label="group %d" % g)
            ax.set_xlabel("deliveries in the quarter")
            ax.set_title(title, fontsize=10)
            ax.spines[["top", "right"]].set_visible(False)
        axes[0].set_ylabel("mean fee, naira")
        axes[0].legend(frameon=False, fontsize=8)
        fig.suptitle("Same customers, same algorithm, one preparation step different",
                     fontsize=12)
        fig.tight_layout()
        fig.savefig(OUT_PNG)
        print("wrote %s" % OUT_PNG)
    except ImportError:
        print("matplotlib not available, skipped the chart")
    return 0


if __name__ == "__main__":
    sys.exit(main())
