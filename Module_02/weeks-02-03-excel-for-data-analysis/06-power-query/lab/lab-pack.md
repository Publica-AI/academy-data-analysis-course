# Lab Exercise Pack, Topic 2.6: Power Query

**Module 2 (Weeks 2 to 3) | Total time-box: 85 minutes | Datasets: `Datasets/Ilesanmi_Sales_Raw_Export.csv` (1,025 rows) and your cleaned `CleanSales` table from Topic 2.3**

By the end of this topic, the trainee can import data through Power Query, apply and reorder
transformation steps, and refresh a query when the source file changes.

## The situation

Ilesanmi Stores will send a new export every month. Topic 2.3 took you the better part of an hour by
hand. This lab does the same job once, in a form Excel remembers, so next month's file takes one
click.

Start from a **fresh copy of the raw export**, not from your cleaned file. The whole point is to
rebuild the cleaning pass as a repeatable process, and you cannot do that on data that has already
been cleaned.

Before you start, write down the four figures your query has to reproduce. They are the Topic 2.3
answers, and they are how you will know the query worked:

| Target | Value |
|---|---|
| Rows | 1,000 |
| Total Sales | ₦32,296,674.90 |
| Total quantity | 5,510 |
| Duplicated Invoice IDs | 0 |

---

## Tier 1, Guided (35 minutes)

1. Load the raw export into a workbook and make it a table named `RawSales`. Confirm 1,025 rows.
2. Click inside it, Data, From Table/Range. The Power Query Editor opens. Find the three zones: the
   preview grid, the **Applied Steps** pane on the right, and the ribbon.
3. **Trim.** Select Product line, Transform, Format, Trim.
4. **Capitalise.** With Product line still selected, Transform, Format, Capitalize Each Word.
5. **Dates.** Select the Date column and set its type using **Using Locale**, choosing Date and an
   English locale that reads day first, so the 51 `DD-MM-YYYY` rows parse correctly. Check a known
   day-first row afterwards rather than only checking for errors.
6. **Deduplicate, the wrong way first.** Select every column, Home, Remove Rows, Remove Duplicates.
   Close & Load and read the row count: **1,006**.
7. Go back into the query and delete that step. Now select **Invoice ID alone**, right-click, Remove
   Duplicates. Reload: **1,000**.
8. **Now test whether order matters.** Put a whole-row Remove Duplicates back in and drag it up and
   down the Applied Steps pane, reloading each time:

   | Whole-row Remove Duplicates placed | Rows |
   |---|---|
   | Above Trim and Capitalize | 1,006 |
   | Below Trim and Capitalize | 1,004 |
   | Below Trim, Capitalize and the date step | 1,001 |

   Then delete it again and confirm that Invoice ID alone gives **1,000** wherever it sits.
9. Close & Load to a new worksheet and **rename the loaded table `CleanSales`**.
10. Verify against the four targets you wrote down at the start.

### Expected output, Tier 1

| Check | Expected |
|---|---|
| Source rows | 1,025 |
| After whole-row Remove Duplicates, no cleaning first | 1,006 |
| After whole-row Remove Duplicates, casing cleaned first | 1,004 |
| After whole-row Remove Duplicates, casing and dates cleaned first | 1,001 |
| After Remove Duplicates on Invoice ID | 1,000, in any order |
| `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| `=SUM(CleanSales[Quantity])` | 5,510 |

**Read that table carefully, because it contains two different lessons.** Step order is real and it
moved the count three times. It never once reached 1,000. Only choosing the right column did that.

---

## Tier 2, Semi-guided (25 minutes)

**Task.** Your query reproduces four of the five Topic 2.3 repairs. It does not yet handle the fifth:
the five rows with a sign-flipped Quantity. Add a step that repairs them, without touching the four
correct rows for every other transaction.

**Expected result.** After your step, `=COUNTIF(CleanSales[Quantity],"<0")` reads **0** and
`=SUM(CleanSales[Quantity])` reads **5,510**. Total Sales must be unchanged at
₦32,296,674.90, because Sales never depended on Quantity in this file.

**Deliverable.** The working query, plus one sentence explaining why your step is safe to run every
month on a file you have not seen yet.

---

## Tier 3, Independent (25 minutes)

> A new export arrives from Ilesanmi Stores. It is the same shape, with more rows and the same five
> categories of fault.

Simulate this: take the raw export, add a handful of rows to the bottom of the source file, save it,
and click Data, Refresh All.

Then do the part that actually matters. **Do not assume the refresh worked.** Write and run a
verification block, and report:

1. The new row count, and whether it is what you predicted before refreshing.
2. Whether total Sales moved by exactly the amount you added.
3. Whether any of the five fault types survived the refresh, and how you checked each one.

**Expected outputs, Tier 3**

Before adding anything, on the unmodified export the query must reproduce exactly:

| Check | Expected |
|---|---|
| Rows | 1,000 |
| Total Sales | ₦32,296,674.90 |
| Total quantity | 5,510 |
| Duplicated Invoice IDs | 0 |
| Negative quantities | 0 |
| Distinct Product line values | 6 |

After your additions, every figure should move by exactly what you added and nothing else. Report
your predicted figures **before** you refresh and your actual figures after, in two columns side by
side. A prediction written after the fact is not a prediction, and the habit of stating the expected
answer before running anything is the single most useful thing in this topic.

Write two sentences on what you would do if the row count had come back at 1,010 when you expected
1,005.

---

## The core exercise, in two versions

The core exercise for this topic is **building a repeatable cleaning query and verifying its output**.

### Version A, without AI (assessed)

Complete Tier 1 with no AI assistance, including step 8. The comparison in step 8 is the assessed
part, because it is what separates a trainee who can operate Power Query from one who understands
what it did.

### Version B, with AI (not assessed, still submitted)

1. Describe the five faults to an AI assistant and ask for a Power Query plan: which transformations,
   in which order, and how to verify the result.
2. Check its answer against one specific thing before anything else: **does it name which column
   defines a duplicate?** A plan that says "use Remove Duplicates" without naming Invoice ID produces
   1,006 rows on this file and reads perfectly sensibly while doing it.
3. Ask it to explain what `Table.Distinct` does in the M code its steps generated, then check that
   explanation against what your query actually produced.
4. **Verify by execution.** Build its plan on a copy and check the row count and total Sales against
   1,000 and ₦32,296,674.90.

**Version B deliverable.** The prompt, the plan, an explicit yes or no on whether it named the
deduplication column, the row count its plan actually produced when you ran it, and one sentence on
what you would have got wrong if you had followed it without checking.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 35 minutes |
| Tier 2, Semi-guided | 25 minutes |
| Tier 3, Independent | 25 minutes |
| **Total** | **85 minutes** |

## Submission checklist

- [ ] Query built from a fresh copy of the raw export, not from an already-cleaned file
- [ ] Applied Steps include Trim, Capitalize Each Word, a locale-aware date step and Remove Duplicates
- [ ] All four row counts recorded: 1,006, 1,004, 1,001 and 1,000
- [ ] Remove Duplicates runs on **Invoice ID alone** in the final query
- [ ] Loaded table renamed `CleanSales`
- [ ] Tier 2 quantity repair step present, with negative quantities at 0 and the total at 5,510
- [ ] Tier 3 predicted-versus-actual table, filled in before and after the refresh
- [ ] Version B prompt log with an explicit yes or no on the deduplication column

---

## Hints for Tier 2

<details>
<summary>Hint 1</summary>

You already worked out the repair by hand in Topic 2.3: `cogs ÷ Unit price` recovers the true
quantity, because that relationship holds on every row of this dataset. Power Query has a Custom
Column that can do arithmetic across two columns, under Add Column.
</details>

<details>
<summary>Hint 2</summary>

Applying the division to every row would work here, but think about whether you want it to. A step
that recomputes all 1,000 quantities behaves differently next month from one that only repairs rows
where the quantity is negative. Conditional Column, or a custom column with an `if` test on the
Quantity value, keeps the repair narrow and makes your one-sentence justification much easier to
write.
</details>
