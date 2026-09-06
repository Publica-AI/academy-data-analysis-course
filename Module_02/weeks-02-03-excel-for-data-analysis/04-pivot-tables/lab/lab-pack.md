# Lab Exercise Pack, Topic 2.4: Pivot Tables

**Module 2 (Weeks 2 to 3) | Total time-box: 80 minutes | Dataset: your cleaned `CleanSales` table (1,000 rows) from Topic 2.3**

By the end of this topic, the trainee can build pivot tables that summarise data by multiple
dimensions, apply filters and slicers, and verify pivot totals against source data.

> **A note on which file you are using.** From here on, every figure is a **cleaned-file** figure,
> measured on the 1,000-row `CleanSales` table you produced in Topic 2.3. If a total in this lab does
> not match, check the table name in Table Design before you check anything else. The same formulas
> against the raw 1,025-row export return different and equally valid numbers, and mistaking one for
> the other is the most common way work in this module goes wrong.

## The situation

Adaeze has a trustworthy 1,000-row file. The regional manager now wants answers, and wants to be
able to ask new questions without phoning her each time. A pivot table is the cheapest way to give
one file the ability to answer many questions.

---

## Tier 1, Guided (30 minutes)

1. Click any cell inside `CleanSales`, then Insert, PivotTable, and place it on a **new worksheet**.
   Confirm the Table/Range box reads `CleanSales`, not a cell range like `$A$1:$Q$1001`.
2. Drag **Branch** into Rows and **Sales** into Values. Confirm it defaulted to **Sum**, not Count.
3. Sort the result largest to smallest.
4. Drag **Product line** into Columns to build a cross-tab: branches down the side, product lines
   across the top.
5. Drag **Rating** into Values as a second measure. It will default to **Count**, which is Excel
   telling you it found blanks in that field. Right-click it, Value Field Settings, change to
   **Average**, and rename the heading to something a reader would recognise.
6. Drag **Branch** into the Filters area and set it to Trans-Amadi only. Say out loud what has and
   has not changed: the display has, the data has not. Clear the filter again.
7. PivotTable Analyze, Insert Slicer, choose **Branch**. Click through the three buttons, then hold
   Ctrl to select two at once.
8. Verify one total independently. On a separate sheet, build
   `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])` and confirm it matches the pivot.

### Expected output, Tier 1

| Branch | Total Sales | Transactions |
|---|---|---|
| Trans-Amadi | ₦11,056,870.65 | 328 |
| Ikeja | ₦10,620,037.05 | 340 |
| Wuse | ₦10,619,767.20 | 332 |
| **Grand total** | **₦32,296,674.90** | **1,000** |

Two things in that table are worth stopping on. **Trans-Amadi leads on Sales while handling the
fewest transactions**, which is a finding rather than a rounding artefact. And **Ikeja and Wuse are
₦269.85 apart**, which is close enough that nobody could have guessed the order by eye.

| Other Tier 1 check | Expected |
|---|---|
| Pivot Trans-Amadi total = the manual SUMIF | Both ₦11,056,870.65 |
| Rating field default before you change it | Count, not Sum |
| Cross-tab grand total | ₦32,296,674.90 |

---

## Tier 2, Semi-guided (25 minutes)

**Task.** The manager wants to know whether Member customers are worth more than Normal customers,
and whether the answer is the same at all three branches. Build one pivot table that answers both
halves at once, then verify one cell of it independently.

**Expected result.**

| Branch | Member | Normal |
|---|---|---|
| Ikeja | ₦6,289,577.70 | ₦4,330,459.35 |
| Trans-Amadi | ₦6,697,481.70 | ₦4,359,388.95 |
| Wuse | ₦5,982,417.00 | ₦4,637,350.20 |

Your six cells must add to ₦32,296,674.90. Verify at least one of them with a formula built
independently of the pivot, and state which cell you checked and what your formula returned.

**Deliverable.** The pivot table, the independent check, and two sentences answering the manager's
actual question, including the part where the answer is **not** the same at all three branches.

---

## Tier 3, Independent (25 minutes)

> The manager is planning stock for the next quarter and asks: **"which product line should each
> branch be stocking more of?"**

Answer it from `CleanSales`. You choose the layout, the fields and the summary function. The only
requirements are that your answer names one product line per branch, that you can defend the measure
you chose, and that you verify at least one figure independently of the pivot.

**Expected outputs, Tier 3**

Measured by total Sales, the leading product line at each branch is:

| Branch | Leading product line | Its Sales |
|---|---|---|
| Ikeja | Home and lifestyle | ₦2,241,719.55 |
| Wuse | Sports and travel | ₦1,998,819.90 |
| Trans-Amadi | Food and beverages | ₦2,376,685.50 |

All three differ, which is the interesting part of the answer and the part the manager cannot get
from a chain-wide total.

Credit strongly any submission that questions the measure rather than just applying it. Sales is one
defensible choice; total quantity is another, and it answers a stock question arguably better, since
shelves hold units rather than naira. A trainee who reports both and says which one they would send
to the manager, and why, has done the job properly.

---

## The core exercise, in two versions

The core exercise for this topic is **building a multi-dimension pivot and verifying a total against
the source**.

### Version A, without AI (assessed)

Complete Tier 1 with no AI assistance, including step 8. The verification step is the assessed part.
A pivot table that has not been checked against anything is not a finished piece of work.

### Version B, with AI (not assessed, still submitted)

1. Describe your cleaned table to an AI assistant, naming the columns, and ask it how to find the
   total Sales for each branch broken down by customer type.
2. Ask it a second question it cannot answer safely: **what is the Trans-Amadi total?** It cannot see
   your file, so whatever number comes back is either refused, hedged, or invented.
3. Record which of those three happened. If a figure came back, compare it against
   ₦11,056,870.65 and note how far out it was.
4. Then give it the real numbers from your pivot and ask it to interpret them. Judge that answer on
   whether the interpretation follows from the figures you supplied, not on how confident it sounds.

**Version B deliverable.** The prompts used, what came back at each step, the figure it produced for
step 2 with a note on how you checked it, and one sentence on which of the three tasks an assistant
was genuinely useful for.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 30 minutes |
| Tier 2, Semi-guided | 25 minutes |
| Tier 3, Independent | 25 minutes |
| **Total** | **80 minutes** |

## Submission checklist

- [ ] Pivot built from `CleanSales`, not from a cell range
- [ ] Branch by Sales sorted, Trans-Amadi leading at ₦11,056,870.65
- [ ] Grand total reads ₦32,296,674.90
- [ ] Rating changed from Count to Average with a renamed heading
- [ ] Working Branch slicer
- [ ] Independent SUMIF check documented, matching the pivot
- [ ] Tier 2 six-cell table reconciling to the grand total
- [ ] Tier 3 names one product line per branch with a defended measure
- [ ] Version B prompt log and verification note included

---

## Hints for Tier 2

<details>
<summary>Hint 1</summary>

You need two dimensions and one measure. One dimension goes down, one goes across, and the measure
goes in the middle. You have already built exactly this shape in Tier 1 with Branch and Product line,
so this is the same structure with one field swapped.
</details>

<details>
<summary>Hint 2</summary>

To verify one cell independently you need a condition on two columns at once, which `SUMIF` cannot
do. The plural version takes the sum range first and then as many range-and-criterion pairs as you
need. Check the argument order in the tooltip rather than assuming it matches `SUMIF`.
</details>
