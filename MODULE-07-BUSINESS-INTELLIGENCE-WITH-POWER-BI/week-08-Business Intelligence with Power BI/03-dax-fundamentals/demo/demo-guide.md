# Demo Guide - DAX Fundamentals
**Module 7, Topic 7.3 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Writing an aggregation measure with COUNTROWS and SUM, and naming it rather than dragging a raw field into a visual
- Writing a ratio measure with DIVIDE, and explaining why the slash operator is unsafe
- Using CALCULATE to change the filter context a measure evaluates against
- Writing a time-intelligence measure with CALCULATE and DATEADD, resting on a marked date table
- Verifying a measure by predicting an expected value, running it at the total level, then reconciling against Table view

---

## Setup - Before the Demo Starts

1. `7.3_solution.pbix` open, built on top of the completed Topic 7.2 star schema
2. A `_Measures` table already created (Home, Enter data, one blank column, hidden) to hold every measure written in this demo
3. Trainees have their own completed relationships from Topic 7.2 and their dates table marked

> **Instructor note:** write every measure live, character by character, rather than pasting. The point of this demo is the reasoning behind each function choice, not the finished text.

> **Instructor note:** `7.3_solution.pbix` is the finished state, so its `_Measures` table already holds the measures written below. Before the session, either delete them so you can write them live, or keep a second copy of the file for the live build and use this one as the fallback. Do not open it in front of the room and then start typing a measure that is already there.

### Getting to a clean starting point, if not already done

The measures themselves are written live during this demo, in Part 1 onwards below, so there is nothing to pre-build beyond having a working, empty model.

1. If `7.2_demo_star.pbix` does not exist yet, build it first (see the 7.2 demo guide's Setup section for the full steps).
2. **File → Save as → `7.3_solution.pbix`**, so the star model file is left untouched.
3. **Home → Enter data.** Name the new table `_Measures`, leave its one column blank, click **Load**. In the Fields pane, right-click `_Measures` → `Column1` → **Hide in report view**. This is the home every measure in this demo gets written into.

---

## Demo Steps

### Part 1 - Aggregation: COUNTROWS and SUM (7 min)

**Right-click `_Measures`, New measure.**

```dax
Total Deliveries = COUNTROWS ( swiftroute_deliveries )
```

> "That is the whole of it. It looks trivial, and it nearly is, because the value is not in the arithmetic. The value is in giving the calculation a name. Every measure downstream in this demo refers to this one by name, which you cannot do with a dragged field."

```dax
Total Revenue = SUM ( swiftroute_deliveries[DeliveryFee] )
```

**Drop both onto Card visuals. Confirm: Total Deliveries reads 41,280. Total Revenue reads ₦247,680,000.**

> "Both verified against the source file before this demo, and both should match exactly what you see now."

---

### Part 2 - Ratio: DIVIDE, Never the Slash (8 min)

```dax
On-Time Deliveries =
CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "On time" )

On-Time Rate = DIVIDE ( [On-Time Deliveries], [Total Deliveries] )
```

**Drop On-Time Rate onto a Card. Confirm it reads 82.0%.**

> "Why DIVIDE and not a plain slash? Picture a rider who joined last week with zero deliveries so far. Filter down to just them and the denominator is zero. With a slash you get an error or Infinity, on Adaeze's screen, not yours. DIVIDE checks the denominator first and returns blank instead, which is the honest outcome."

**Ask students:** "What would a card showing On-Time Rate for a brand-new rider with no deliveries actually display, using DIVIDE?"

> "Blank. Not zero, not an error. Blank, because DIVIDE recognised nothing could be divided."

---

### Part 3 - What CALCULATE Is Actually Doing (7 min)

**Point back at the On-Time Deliveries measure already on screen.**

> "You have already used CALCULATE, and I skipped past it. Read this one aloud in English with me: work out my delivery count, but first, on top of whatever the visual already filtered, also require the status to be On time. If you cannot read a measure aloud like that, you cannot verify it, and you should not ship it."

Have two trainees read a measure aloud in plain English before continuing.

---

### Part 4 - Time Comparison: CALCULATE and DATEADD (8 min)

```dax
Deliveries Previous Month =
CALCULATE ( [Total Deliveries], DATEADD ( dates[DateKey], -1, MONTH ) )

Month on Month Change =
DIVIDE ( [Total Deliveries] - [Deliveries Previous Month], [Deliveries Previous Month] )
```

**Build a table visual: dates[MonthName] on rows, Total Deliveries and Deliveries Previous Month as values.**

> "January reads two thousand, four hundred and seventy-three. Deliveries Previous Month for January returns blank, because there is no December 2024 in this model. That is correct, not a bug - please do not try to fix it. And this only works at all because dates is marked as a date table, which is what Topic 7.2 was setting up."

---

### Part 5 - Verify, Do Not Trust (10 min)

> "Four steps, every time. Predict, run at the total level, reconcile against Table view, then break it deliberately."

**Predict aloud:** "On-Time Rate should land near eighty-two percent, because the SLA is ninety and Adaeze is worried about it."

**Run it. Confirm 82.0%.**

**Switch to Table view. Filter swiftroute_deliveries to Status = On time. Read the row count.**

> "Thirty-three thousand, eight hundred and fifty. That is the reconciliation - a number from a completely different surface, agreeing with the measure."

**Filter the report to a single low-volume rider and check On-Time Rate does not error.**

> "This is where divide-by-zero and blank handling show up, and it is much better to find that here than on Adaeze's screen."

---

## Final State of the Measures

```dax
Total Deliveries = COUNTROWS ( swiftroute_deliveries )
Total Revenue = SUM ( swiftroute_deliveries[DeliveryFee] )
On-Time Deliveries = CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "On time" )
On-Time Rate = DIVIDE ( [On-Time Deliveries], [Total Deliveries] )
Deliveries Previous Month = CALCULATE ( [Total Deliveries], DATEADD ( dates[DateKey], -1, MONTH ) )
Month on Month Change = DIVIDE ( [Total Deliveries] - [Deliveries Previous Month], [Deliveries Previous Month] )
```

Verified values at the total level: Total Deliveries 41,280. Total Revenue ₦247,680,000. On-Time Rate 82.0%. On-Time Deliveries 33,850. January deliveries 2,473. February deliveries 2,329. March deliveries 2,960.

**What the shipped `7.3_solution.pbix` actually contains.** The file carries nine measures in `_Measures`, checked by reading the model directly: the five above plus `Late Deliveries`, `Late Rate`, `Revenue Previous Month` and `Last Refreshed`. The last four are written during Topic 7.4 and are already present here so that topic's start model is ready. `Month on Month Change` is written live in Part 4 above and is not saved in the file, so add it yourself if you want the file to match this list exactly. Late Deliveries reads 7,430 and Late Rate 18.0%, which is the reconciliation worth showing: On-Time Rate and Late Rate must sum to 100%.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| On-Time Rate returns blank at the total level | "That means Status has no rows matching exactly 'On time'. Check for a typo or unexpected casing in the CALCULATE filter condition." |
| Deliveries Previous Month returns blank for every month, not just January | "That usually means the dates table is not marked as a date table. Check Table tools, Mark as date table." |
| Month on Month Change shows an error instead of blank for January | "Check that the slash operator was not used by accident in this measure - it should be DIVIDE throughout." |
| Total Revenue does not match ₦247,680,000 | "Check DeliveryFee's data type from Topic 7.1 - it must be Fixed decimal number, not Decimal number, or rounding will drift the total." |

---

## Up Next

Topic 7.4 - KPI Dashboards and Publishing. You now have correct, verified numbers. What comes next is a design problem, not a DAX problem: deciding which of them Adaeze actually needs to see first.
