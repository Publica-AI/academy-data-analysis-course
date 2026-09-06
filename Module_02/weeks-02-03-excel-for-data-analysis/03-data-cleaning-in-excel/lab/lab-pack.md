# Lab Exercise Pack, Topic 2.3: Data Cleaning in Excel

**Module 2 (Weeks 2 to 3) | Total time-box: 105 minutes | Dataset: `Datasets/Ilesanmi_Sales_Raw_Export.xlsx` (1,025 rows)**

By the end of this topic, the trainee can identify and repair duplicates, inconsistent formats,
stray spaces, mixed data types and impossible values in a messy dataset, and confirm the cleaned
file matches a stated expected row count.

## The situation

This is the lab the whole module rests on. Every figure produced in Topics 2.4 to 2.7 is produced on
the file you finish here, so an error made in this session survives to the end of the module.

**Before you touch anything, save an untouched copy of the raw export somewhere separate.** Remove
Duplicates is not reversible by Undo once a file has been saved and closed, and you will want to
compare against the original more than once.

Ilesanmi Stores states that the export should contain **1,000 completed sales**. It contains 1,025
rows. Your job is to find out why, fix it defensibly, and be able to prove what you did.

---

## Tier 1, Guided (40 minutes)

### Part A, duplicates and the dialog nobody reads (12 minutes)

1. Apply Conditional Formatting, Highlight Cell Rules, Duplicate Values to the Invoice ID column.
   **25 invoices** are flagged. Do not delete anything yet.
2. Open Data, Remove Duplicates. Look at the dialog: every column is ticked. Click OK on that
   default and read the message Excel gives you. **19 rows are removed and 1,006 remain.**
3. **Undo.** Reopen the dialog, click Unselect All, tick **Invoice ID only**, and run it again.
   **25 rows are removed and 1,000 remain.**
4. Write down both results. The tool did not change between those two runs and neither did the file.
   Only the definition of a duplicate changed.

### Part B, stray spaces and casing (10 minutes)

5. On the 1,000-row file, find a Product line entry in ALL CAPS. Run `=LEN()` on it and on a
   normally cased entry of the same category. The counts differ.
6. In a helper column, build `=PROPER(TRIM([@[Product line]]))`. TRIM strips the trailing space,
   PROPER normalises the casing.
7. Copy the helper column, then Paste Special, Values, over the original Product line column. Delete
   the helper. Confirm the Product line column now holds exactly **six** distinct values.

### Part C, dates (8 minutes)

8. Sort by Date. The text-stored dates left-align while true dates right-align, which is the fastest
   diagnostic in Excel and needs no formula.
9. Select the Date column and use Data, Text to Columns, Next, Next, and set the column data format
   to **Date: DMY**. Finish. The left-aligned rows become true dates.
10. Confirm with `=COUNT(Date column)`, which counts numbers only. It should now read 1,000.

### Part D, impossible values (10 minutes)

11. Sort Quantity ascending. Five negative values surface: -1, -6, -7, -8 and -9.
12. Before deciding anything, check whether the true value is recoverable. In a helper column on
    those five rows, build `=[@cogs]/[@[Unit price]]`.
13. All five return whole numbers matching the magnitude already in the cell. That is a flipped
    sign, not a lost quantity, so **correct** the rows rather than flagging or deleting them.
14. Paste the recovered values into Quantity. Record the decision and its reason in a cleaning log.

### Expected output, Tier 1

| Check | Expected |
|---|---|
| Duplicates flagged on Invoice ID | 25 |
| Rows after Remove Duplicates, every column ticked | 1,006 |
| Rows after Remove Duplicates, Invoice ID only | 1,000 |
| Distinct Product line values after repair | 6 |
| `=COUNT()` on the Date column after Text to Columns | 1,000 |
| Negative quantities before repair | 5 |
| Negative quantities after repair | 0 |
| `=SUM(Quantity)` after repair | 5,510 |
| `=SUM(Sales)` on the finished file | ₦32,296,674.90 |

Rename the finished table from `RawSales` to **`CleanSales`** before you finish. Every later topic
refers to it by that name.

---

## Tier 2, Semi-guided (30 minutes)

**Task.** Build a **cleaning log** on a separate sheet that would let a reviewer who has never seen
this file reconstruct exactly what you did and check it. It must record, for every one of the five
faults: what the fault was, how many rows it affected, how you detected it, what you did about it,
and why.

Then prove the log is honest by adding a verification block of live formulas whose results a
reviewer can read without trusting a word of your prose.

**Expected result.** Your verification block reads:

| Check | Expected |
|---|---|
| Rows | 1,000 |
| Duplicated Invoice IDs remaining | 0 |
| Blank Ratings | 9 |
| Negative quantities | 0 |
| Total Sales | ₦32,296,674.90 |
| Ikeja | ₦10,620,037.05 |
| Wuse | ₦10,619,767.20 |
| Trans-Amadi | ₦11,056,870.65 |
| Total quantity | 5,510 |

**The blank Ratings line is the interesting one.** There are 10 in the raw file and 9 survive
deduplication. This lab leaves them blank, which is a defensible decision, and it has a consequence
you must record: `=COUNTIF(CleanSales[Rating],">=7")` reads **496** with the blanks left in place,
not 501. State in your log which figure you are reporting and why.

**Deliverable.** The cleaning log sheet and the verification block, both in the workbook.

---

## Tier 3, Independent (35 minutes)

> A colleague at Origin Analytics sends you their cleaned version of the same export. It has
> **1,006 rows**. They are confident it is correct, because they used Excel's Remove Duplicates and
> the tool reported that it had removed duplicates successfully.
>
> Write them a short note, no more than 200 words, explaining what has gone wrong, how you know, and
> what they should do about it.

You choose how to demonstrate it. A worked comparison, a screenshot of the dialog, a formula that
exposes the six survivors, or all three.

**Expected outputs, Tier 3**

Your note must contain, in some form:

- Their file is missing nothing and contains six too many rows: six duplicated sales are still in it.
- The cause is the Remove Duplicates dialog's default of every column ticked, which requires two
  rows to agree on all seventeen fields.
- Only 19 of the 25 duplicated invoices are exact copies in every column. The other six differ in
  exactly one field: three by date format, two by Product line casing, and one, `263-10-3913`, by a
  blank Rating on one of the two rows.
- The fix is to re-run Remove Duplicates on **Invoice ID alone**, on a fresh copy of the raw export
  rather than on their 1,006-row file.
- A check they can run themselves:
  `=COUNTA([Invoice ID])-SUMPRODUCT(1/COUNTIF([Invoice ID],[Invoice ID]))` returns **6** on their
  file and **0** on a correctly cleaned one.

Credit strongly any note that also says what is **not** the cause: trimming and re-casing first
would not have fixed it, because Invoice ID itself carries no formatting fault, so deduplicating on
Invoice ID returns 1,000 rows whether the file was cleaned first or not.

---

## The core exercise, in two versions

The core exercise for this topic is **the full cleaning pass, from 1,025 rows to a verified 1,000**.

### Version A, without AI (assessed)

Complete Tier 1 by hand, with no AI assistance. This is the assessed version. You must be able to
reach 1,000 verified rows using only Excel and your own judgement, because the judgement calls in
this lab, particularly the one in Part D, are exactly the ones an assistant will get wrong on your
behalf.

### Version B, with AI (not assessed, still submitted)

1. Describe this file's faults to an AI assistant in plain English and ask for a cleaning plan: what
   to do, in what order, and how to check it.
2. Compare its plan against what you actually did. Pay attention to one thing above all: **does it
   tell you which column defines a duplicate?** A plan that says "use Remove Duplicates" without
   naming Invoice ID produces 1,006 rows and reads perfectly reasonably while doing it.
3. Ask it specifically what to do about five rows with negative quantities where cogs and Unit price
   are intact. Record whether it recommends correcting, flagging or deleting, and whether it spots
   that `cogs ÷ Unit price` recovers the value.
4. **Verify by execution.** Run whatever it suggests on a copy, and check the row count and the total
   Sales against ₦32,296,674.90.

**Version B deliverable.** The prompt, the plan returned, a short table of where the plan agreed with
your manual pass and where it differed, the row count its plan actually produced when you ran it, and
one sentence on which of its suggestions you would not have caught if you had not already done the
work by hand.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 40 minutes |
| Tier 2, Semi-guided | 30 minutes |
| Tier 3, Independent | 35 minutes |
| **Total** | **105 minutes** |

## Submission checklist

- [ ] An untouched copy of the raw export saved separately before any cleaning
- [ ] Both Remove Duplicates results recorded: 1,006 and 1,000
- [ ] Product line holds exactly 6 distinct values
- [ ] Date column returns 1,000 to `=COUNT()`
- [ ] Five negative quantities corrected from `cogs ÷ Unit price`, not deleted
- [ ] Table renamed to `CleanSales`
- [ ] Verification block present, with all nine checks live and matching
- [ ] Cleaning log records what, how many, how detected, what was done, and why
- [ ] Tier 3 note written, under 200 words, naming the 1,006 cause and the fix
- [ ] Version B prompt log, comparison table, and verification note included

---

## Hints for Tier 2

<details>
<summary>Hint 1</summary>

For the duplicated-invoice check, you need a formula that counts distinct values without a helper
column. `=COUNTA(range)-SUMPRODUCT(1/COUNTIF(range,range))` gives the number of rows in excess of the
distinct count, so it returns 0 on a correctly deduplicated file. It is worth building once and
keeping.
</details>

<details>
<summary>Hint 2</summary>

A verification block earns its keep only if nothing in it is typed by hand. Test yours by deleting a
row from the table on purpose: every figure should move at once, and if any of them does not, that
one is a hard-coded number wearing a formula's job title. Undo afterwards.
</details>
