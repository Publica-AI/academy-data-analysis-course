# Demo Guide - Data Modelling and Relationships
**Module 7, Topic 7.2 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Watching a flat, single-table design produce a plausible but completely wrong count (41,280 riders instead of 68)
- Explaining why the flat table's grain, one row per delivery, means every question it can answer is a question about deliveries, not riders
- Classifying tables as fact or dimension using the "filter or group by it, versus sum or count it" rule of thumb
- Drawing correct one-to-many relationships in Model view, and reading the cardinality Power BI infers
- Diagnosing a relationship that builds without error but produces blanks, caused by a trailing space
- Explaining why cross-filter direction should default to Single, not Both

---

## Setup - Before the Demo Starts

1. `7.2_demo_flat.pbix` open and ready - the deliberately wrong file, all five SwiftRoute tables pre-merged into one flat table via Power Query before import
2. `7.2_demo_star.pbix` open in a second window - the correctly modelled version, used from Part 3 onwards
3. `routes_raw.csv` available for the second half of the demo, carrying the planted trailing-space fault on one RouteID
4. Trainees have completed Topic 7.1 and have their own cleaned five files ready

> **Instructor note:** do not preview the 41,280 result before Part 1. The whole demo depends on trainees not seeing the wrong number coming - if it is spoiled in advance, the explanatory weight of Part 2 falls flat.

> **Instructor note:** the shipped `7.2_demo_star.pbix` is the finished model, with all four relationships already drawn and dates already marked. Part 3 below asks you to drag those relationships in live, so before the session either delete the four lines in Model view, or open `7.1_fallback_loaded.pbix` instead and delete the three relationships Power BI auto-detected there. Keep the finished star file open in the second window as your fallback.

### Building `7.2_demo_star.pbix`, if not already done

Start from `7.1_fallback_loaded.pbix` (all five files loaded and cleaned).

1. Click the **Model view** icon, far left edge. Right-click and delete any relationship lines Power BI guessed automatically - draw them yourself so the demo's "watch me drag this" moment is genuine.
2. Click the `dates` table, **Table tools** tab, **Mark as date table**, choose `DateKey`, **OK**.
3. Draw the four relationships by dragging the key field from each dimension onto the matching field in `swiftroute_deliveries`: `riders.RiderID`, `routes.RouteID`, `customers_business.CustomerID`, `dates.DateKey`.
4. Double-click each line and confirm: cardinality **One to many** with the "one" on the dimension, cross-filter direction **Single**, **Make this relationship active** ticked. You should end with four solid lines, no dotted ones.
5. **File → Save as → `7.2_demo_star.pbix`.**

### Building `7.2_demo_flat.pbix`, if not already done

This file must be genuinely wrong, so build it as a **separate new file**, not a copy of the star model.

1. **File → New. Home → Get data → Text/CSV** → `swiftroute_deliveries.csv` → **Transform data**.
2. In Power Query: **Home → New Source → Text/CSV** → `riders.csv` → OK. Repeat for `routes.csv`. Three queries now sit in the left-hand list.
3. Click `swiftroute_deliveries` to select it. **Home → Merge Queries** (the plain option, not "Merge Queries as New").
4. Two table previews appear, stacked. The top is `swiftroute_deliveries` already. In the dropdown above the bottom preview, choose `riders`.
5. **This is the step that catches people.** In the top preview, click once on the `RiderID` column header - it highlights green. In the bottom preview, click once on `RiderID` there too - green as well. Both must be green or OK stays greyed out.
6. Set **Join Kind** to **Left Outer (all from first, matching from second)**. Click **OK**.
7. Scroll to the far right of the table. A new `riders` column appears, every cell reading the word `Table` - correct, each cell holds the matched record, not yet unpacked. Click the small **⇄** icon in that column's header to expand it.
8. Untick **Select All Columns**, tick only `RiderName` and `Hub`, untick **Use original column name as prefix**, click **OK**.
9. Repeat steps 3 to 8 for `routes`, matching on `RouteID`, expanding only `RouteName`.
10. **Home → Close & Apply.**
11. In Report view, add a **Card** visual, tick `RiderName`, then click the small arrow next to it in the Fields well and set it to **Count** (not Count Distinct). It should read **41,280**.
12. Add a bar chart of deliveries by `RiderName` so the visual looks like a plausible real report.
13. **File → Save as → `7.2_demo_flat.pbix`.**

---

## Demo Steps

### Part 1 - Watch the Flat Table Break (8 min)

> "SwiftRoute employs sixty-eight riders. I have the HR list in front of me. Watch what happens when I count them a different way."

**In `7.2_demo_flat.pbix`, add a Card visual. Drag RiderName in. Set it to Count.**

> "That is forty-one thousand, two hundred and eighty. We have sixty-eight riders."

Pause for three seconds. Say nothing.

> "No error. No warning. No red. The file loaded perfectly, the visual built perfectly, and the answer is nonsense."

---

### Part 2 - Explain the Grain Change (8 min)

**Switch to Table view on the flat table. Filter to RiderID = R-014 and show the repeated rows.**

> "Fatima Abubakar, rider R-014, appears many times in this table. Not because the data is corrupt, because she made many deliveries. In the real table she appears six hundred and seventeen times."

**Ask students:** "If counting her name column counts six hundred and seventeen rows, what are we actually counting?"

> "Deliveries that happen to have her name written next to them. The rider stopped being a rider and became an attribute of a delivery. Remember the word from Topic 7.1: grain. The grain of this table is one row per delivery, so every question it can answer is a question about deliveries."

---

### Part 3 - Fact and Dimension, Then the Star (10 min)

**Switch to `7.2_demo_star.pbix`, Model view. Point at the five disconnected tables.**

> "Two kinds of table. A fact table records events, one row per thing that happened, long and narrow. A dimension table describes things, one row per thing that exists, short and wide. Deliveries is the fact table here. Riders, routes, customers, dates are the four dimensions."

**Drag RiderID from riders onto RiderID in swiftroute_deliveries. A line appears.**

> "Power BI has just made a decision on my behalf. Read the dialogue - it should say one to many, with the one on riders. If it ever says many to many, stop: that means your dimension has duplicate keys."

**Repeat for RouteID, CustomerID, and DateKey. Mark dates as the date table (Table tools, Mark as date table, DateKey).**

**Ask students:** "Before I filter to Apapa, predict: does the filter travel from riders into deliveries, or the other way round?"

> "From the one side to the many side. From the outside of the star into the centre. Watch." Click Apapa on a hub slicer and show only Apapa riders' deliveries surviving.

---

### Part 4 - Diagnose a Relationship That Silently Fails (8 min)

**Load `routes_raw.csv` in place of the clean routes table. Attempt to build the RouteID relationship.**

> "This relationship either refuses to build, or it builds and produces blanks. Nothing turns red, which is exactly the trap."

**In Power Query, inspect the RouteID column on routes_raw. Point out the trailing space on LAG-07.**

> "To you, reading this on screen, LAG-07 and LAG-07 with a trailing space look identical. To Power BI they are two different strings. The fix is upstream, in Power Query: Transform, Format, Trim. Not in the model, and never by editing the source file by hand."

**Apply the trim, rebuild the relationship, confirm it now reads one to many with no blanks.**

---

### Part 5 - Cross-Filter Direction (5 min)

**Right-click the riders-to-deliveries relationship, open its properties.**

> "Cross-filter direction: Single. There is an option called Both, and it looks helpful. It lets filters travel back up out of the fact table into a different dimension, which sounds useful right up until a completely different chart, in a completely different part of your report, goes quietly wrong for reasons nobody can trace. Leave this on Single unless you have a specific, understood reason not to."

---

## Final State of the Model

| Check | Expected value |
|---|---|
| Relationships | Four, all one to many, single direction, dimension on the "one" side |
| Dotted lines in Model view | None |
| Card counting RiderName | 68 |
| Card counting RouteName | 24 |
| dates table | Marked as the date table |

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Rider count still shows a large delivery-grain number after switching to the star file | "Check which visual you are looking at - you may still have the flat-table file's card open in a second window. Confirm you are working in the star schema file." |
| Routes relationship refuses to build even after trimming | "Trim must be applied to both tables' key columns, not just one. Check RouteID is trimmed in both routes and swiftroute_deliveries." |
| Relationship shows many to many unexpectedly | "This means the dimension table has duplicate keys. Go to Table view on the dimension and look for the same ID appearing on more than one row." |
| A slicer click on Hub does not change the rider table at all | "The relationship's cross-filter direction may be set incorrectly, or the relationship may be inactive (a dotted line in Model view). Check both." |

---

## Up Next

Topic 7.3 - DAX Fundamentals. The model now knows how the tables relate. What it cannot yet do is calculate anything beyond a row count, and that is what the next topic teaches.
