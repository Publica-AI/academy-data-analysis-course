# Demo Guide - Pivot Tables
**Module 2, Topic 2.4 | Estimated duration: 28-32 minutes**

---

## What This Demo Teaches

- Build pivot tables that summarise data by a single dimension
- Build pivot tables that summarise data by multiple dimensions, including cross-tabs
- Apply filters and slicers to a pivot table, and connect one slicer to more than one pivot table
- Verify pivot totals against source data before trusting or sharing them

---

## Setup - Before the Demo Starts

1. Open the cleaned 1,000-row file from Topic 2.3, with its verified row count intact and its table renamed to `CleanSales`
2. Confirm the file is still a structured table, not a plain range, so the PivotTable is built from the table rather than a fixed range
3. Confirm the name in Table Design reads `CleanSales`, not `RawSales`. Every figure in this topic is a cleaned-file figure, and a pivot built on the 1,025-row table will not match any of them
4. Have a finished, pre-built copy of the workbook with the finished cross-tab, slicer and verified totals already in place, as a fallback

> **Instructor note:** build the second, connected pivot table live in Part 3 only if time allows; it is a genuine "wow" moment worth the extra few minutes, but the topic's outcomes are fully covered without it if the session is running short.

---

## Demo Steps

### Part 1 - Building a Multi-Dimension Pivot Table (10 min)

> "A raw table answers no question by itself, it just holds the facts. A pivot table lets us ask it a new question in seconds."

- Click any cell inside the cleaned table, Insert tab, PivotTable, place it on a new worksheet
- Drag Branch into Rows and Sales into Values, narrating the decision: "I want one line per branch, so Branch goes in Rows; I want a number for each branch, so Sales goes in Values"
- Confirm it defaulted to Sum, not Count, and sort the result largest to smallest, showing Trans-Amadi leading at ₦11,056,870.65
- Drag Product line into Columns to build a cross-tab, narrating: "now I want to see this broken down further, so the second dimension goes across, not down"

> "Same source table, two completely different views, and neither one touched the original data."

### Part 2 - Changing the Summary Calculation and Applying Filters (8 min)

> "Sum is a default, not a rule. Watch what happens when Excel guesses wrong."

- Drag Rating into Values and let it default to Count instead of Sum; point out this usually means Excel has detected a non-numeric or blank value somewhere in that field
- Right-click the value, Value Field Settings, change it to Average, and rename the resulting column heading
- Drag Branch into the Filters area, set the dropdown to Trans-Amadi only, and narrate explicitly: "the source data has not changed, only what this pivot table currently shows has"
- Clear the filter live from the dropdown and let the full table return instantly

### Part 3 - Slicers and Connecting Multiple Pivot Tables (7 min)

> "A filter dropdown works, but a slicer is something you can see and click, which matters the moment this becomes a dashboard."

- PivotTable Analyze tab, Insert Slicer, choose Branch, and click through Ikeja, Wuse and Trans-Amadi, holding Ctrl to select two at once
- If time allows: build a second small pivot table from the same source (Product line by Sales), right-click the existing slicer, Report Connections, and tick both pivot tables
- Click a slicer button and let the room watch both pivot tables respond at once

> "One click, two views updated together. That's the exact mechanism that makes a one-screen dashboard behave like a single report, which is exactly where this goes next topic."

### Part 4 - Verifying Pivot Totals Against Source Data (6 min)

> "Every number so far has looked correct. That's not the same as being verified. This last step is what makes a pivot table safe to hand to someone else."

- Pick the Trans-Amadi total from Part 1 and recreate it independently, on the same cleaned table the pivot was built from: `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])`
- Confirm both figures read ₦11,056,870.65
- Name the condition on that check out loud: a pivot and a SUMIF only prove each other when they read the same table. The same SUMIF against the raw 1,025-row export returns ₦11,338,588.80, which is not a mismatch to investigate, it is a different question
- Deliberately introduce a mismatch: leave a stale Branch filter active on the pivot table, then run the same SUMIF check and let the numbers disagree
- Diagnose it live: "a mismatch like this almost always means a filter is still active, a field was dropped in the wrong area, or the source data changed since the pivot was built", then clear the filter and reconfirm the match

**Ask students:** if a pivot table and a manual SUMIF disagree, which one should be trusted by default, and why?

> "Neither automatically, that's the point. Investigate the mismatch first: check for an active filter, check the field placement, and only trust the number once you know why they disagreed."

---

## Final State of the Workbook

A PivotTable sheet containing: a Branch-by-Sales summary (Sum, sorted, Trans-Amadi leading at ₦11,056,870.65), a Branch-by-Product-line cross-tab, a Rating summary corrected to Average, a working Branch slicer, and a documented verification showing the Trans-Amadi total matching a manual SUMIF. This pivot table is what Topic 2.5's charts and dashboard are built directly from.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Building the PivotTable from a plain range instead of the structured table | "This is named directly in this topic's common mistakes. Build from the table, or new rows will never be picked up automatically." |
| Sharing a pivot table with a filter still quietly applied | "The pivot table looks complete, but it isn't, and the viewer has no way to know data is missing. Always check the Filters area before sharing anything." |
| Assuming a pivot table updates the moment the source data changes | "It doesn't, not automatically. Right-click, Refresh, every time the source changes, that habit needs to become automatic too." |

---

## Up Next

Topic 2.5, Charts and Dashboard Reporting, turns the pivot table just built and verified here directly into visuals, a chart is only as trustworthy as the pivot table feeding it.
