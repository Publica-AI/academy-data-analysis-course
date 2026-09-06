# Lab Exercise Pack, Topic 2.1: The Excel Environment, Tables and Referencing

**Module 2 (Weeks 2 to 3) | Total time-box: 75 minutes | Dataset: `Datasets/Ilesanmi_Sales_Raw_Export.xlsx` (1,025 rows)**

By the end of this topic, the trainee can navigate the Excel interface confidently, convert a
range to a structured table, and use relative and absolute references correctly in copied formulas.

## The situation

Ilesanmi Stores has sent Origin Analytics its point-of-sale export for January to March 2019:
1,025 rows across the Ikeja, Wuse and Trans-Amadi branches. Nobody has touched it yet. Before
anyone can answer a question about it, it has to behave like data rather than like text on a grid.

Open `Ilesanmi_Sales_Raw_Export.xlsx` and work in that file throughout. Do not clean anything
in this lab; cleaning is Topic 2.3, and part of the point here is to see what an untouched export
looks like.

---

## Tier 1, Guided (25 minutes)

Follow every step. The expected figures are stated so you can check yourself as you go.

1. Open the workbook and rename the sheet holding the data to `Raw Export`.
2. Press Ctrl+Home, then Ctrl+End. Write down the address Ctrl+End lands on. With a header row and
   1,025 data rows, the last row is **row 1026**.
3. Select the whole Sales column and read the Status bar at the bottom right. Note the Sum, Count
   and Average it shows without you writing a single formula.
4. Click any cell inside the data and press **Ctrl+T**. Read the dialog before confirming, and make
   sure **My table has headers** is ticked.
5. Go to Table Design, Table Name, and rename the table from `Table1` to **`RawSales`**.
6. In a blank cell above the table, say `B1`, type `0.05` and label it `Tax rate` in `A1`.
7. Add a new column at the right of the table, headed `Subtotal`, and enter:
   `=[@[Unit price]]*[@Quantity]`
   Let it fill down on its own. Do not drag it.
8. Add a second new column, headed `Tax Check`, and enter `=[@Subtotal]*B1`. Copy it down and watch
   it go wrong: the reference walks to `B2`, `B3` and so on, and the results collapse to zero.
9. Fix it. Click into the formula, select `B1`, press **F4** once to get `$B$1`, and confirm every
   row now returns a sensible figure.
10. Check your work against the file itself. Below the table, build:
    - `=SUM(RawSales[Subtotal])`
    - `=SUM(RawSales[Tax Check])`
    - `=SUM(RawSales[cogs])`
    - `=SUM(RawSales[Tax 5%])`

### Expected output, Tier 1

| Check | Expected |
|---|---|
| Rows in `RawSales` | 1,025 |
| Last cell (Ctrl+End) | Row 1026 |
| `=SUM(RawSales[Tax Check])` | ₦1,565,351.20 |
| `=SUM(RawSales[Tax 5%])` | ₦1,578,894.40 |
| `=SUM(RawSales[cogs])` | ₦31,577,888.00 |
| `=SUM(RawSales[Subtotal])` | ₦31,307,024.00 |

Check your Tax Check column row by row against the Tax 5% column. On the rows you sample it will
match to the penny, and if it does not, the `$B$1` reference is still wrong somewhere.

**Now look at the totals, because two pairs of them disagree.** Subtotal and cogs are calculated the
same way and are ₦270,864.00 apart. Tax Check and Tax 5% are calculated the same way and are
₦13,543.20 apart. Do not fix either. Write both differences down, notice that ₦13,543.20
is exactly five per cent of ₦270,864.00, and carry that observation into Tier 2.

---

## Tier 2, Semi-guided (25 minutes)

The task and the expected result are given. The steps are not. Hints are at the end of this file.

**Task.** Your Subtotal column and the export's own `cogs` column both claim to be Unit price
multiplied by Quantity, and their totals differ by ₦270,864.00. Your Tax Check column and the
export's own `Tax 5%` column are ₦13,543.20 apart, which is five per cent of the same figure.
Find out how many rows actually disagree, and identify them by Invoice ID.

**Expected result.** Exactly **5 rows** disagree. Report their Invoice IDs, and for each one, state
in a single sentence what is wrong with the row. Do not repair anything.

**Deliverable.** A small block below your table listing the five Invoice IDs and the count of
disagreeing rows, plus one sentence naming the fault they share.

---

## Tier 3, Independent (25 minutes)

A business question and a dataset. You choose the method.

> Adaeze needs to tell the client, before any cleaning happens, whether the arithmetic inside this
> export can be trusted. Her question is narrow and answerable: **on how many of the 1,025 rows do
> the file's own three arithmetic relationships hold?**
>
> Those relationships are:
> `cogs = Unit price × Quantity`, `Tax 5% = cogs × 0.05`, and `Sales = cogs + Tax 5%`.

Build the checks, report one number per relationship, and write two sentences on what the pattern
tells you about where the fault was introduced. Reference type is the whole exercise here: every
check must fill down 1,025 rows without you touching it a second time.

**Expected outputs, Tier 3**

| Relationship | Rows where it holds |
|---|---|
| `Sales = cogs + Tax 5%` | 1,025 of 1,025 |
| `Tax 5% = cogs × 0.05` | 1,025 of 1,025 |
| `cogs = Unit price × Quantity` | 1,020 of 1,025 |

The two-sentence conclusion should land on this: the money columns are internally consistent
everywhere, so the fault sits in the Quantity column alone, not in the totals. That is a very
different repair job from a file where the money is wrong, and it is worth knowing before you quote
the client a cleaning estimate.

---

## The core exercise, in two versions

The core exercise for this topic is **Tier 1, steps 6 to 10**: building a calculated column that
mixes relative and absolute references, and proving it against a column already in the file.

### Version A, without AI (assessed)

Complete Tier 1 steps 6 to 10 with no AI assistance of any kind. Use Excel's own help, the demo
notes, or a colleague. This is the version that counts towards assessment, because this is the
version that proves you can do it when the tool is not available.

### Version B, with AI (not assessed, still submitted)

Repeat the same task with an AI assistant, then verify it.

1. Ask an AI assistant to write the Tax Check formula for you. Give it real context: the table name,
   the column names, and the fact that the rate lives in a single cell `B1`.
2. Paste its answer into a fresh column and fill it down.
3. **Verify it** against `=SUM(RawSales[Tax 5%])`, which is ₦1,578,894.40. Not by eye, and not
   on one row.
4. If the two disagree, work out why before changing anything. The most common cause is an answer
   that used `B1` without locking it, which produces a total that is wrong and a formula that looks right.

**Version B deliverable.** Three things: the exact prompt you used, the formula the assistant
returned, and one or two sentences stating how you verified it and what the verification returned.
An answer that says "it looked correct" has not been verified.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 25 minutes |
| Tier 2, Semi-guided | 25 minutes |
| Tier 3, Independent | 25 minutes |
| **Total** | **75 minutes** |

## Submission checklist

- [ ] Workbook contains a structured table named `RawSales` with 1,025 rows
- [ ] `Subtotal` and `Tax Check` columns both present and filled to the last row
- [ ] `=SUM(RawSales[Tax Check])` reads ₦1,565,351.20, and the ₦13,543.20 gap against Tax 5% is noted
- [ ] Tier 2 block lists 5 Invoice IDs and names the shared fault
- [ ] Tier 3 reports 1,025 / 1,025 / 1,020 with a two-sentence conclusion
- [ ] Version B prompt log and verification note included

---

## Hints for Tier 2

<details>
<summary>Hint 1</summary>

You do not need to find the rows by scrolling. Add one more column that compares the two values on
each row and returns TRUE or FALSE, then count the FALSEs with a conditional aggregate. Rounding
both sides to two decimal places before comparing avoids a false alarm from floating point.
</details>

<details>
<summary>Hint 2</summary>

Once you can count them, filter the table on that column to see only the disagreeing rows. Look at
the Quantity value on each one before you look at anything else, and the shared fault will be
obvious immediately.
</details>
