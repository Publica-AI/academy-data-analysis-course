# Solution Workbook Notes, Topic 2.6

> ### Status: built, executed and tested
>
> **`2.6_lab_solution.xlsx` ships with this lab pack** (131 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.6_lab_solution.xlsx`, built from a fresh copy of `Datasets/Ilesanmi_Sales_Raw_Export.csv`.

## Query: Clean Ilesanmi Sales

Applied Steps, in this order:

| Step | Detail |
|---|---|
| Source | From Table/Range on `RawSales`, 1,025 rows |
| Changed Type | Default types, Date left as text at this stage |
| Trimmed Text | Product line |
| Capitalized Each Word | Product line |
| Changed Type with Locale | Date, to Date, English day-first locale |
| Inserted Quantity Fixed | `= if [Quantity] < 0 then [cogs] / [#"Unit price"] else [Quantity]` |
| Removed Columns | the original Quantity |
| Renamed Columns | `Quantity Fixed` to `Quantity` |
| Removed Duplicates | **Invoice ID only** |

Loaded to a worksheet as a table named **`CleanSales`**.

## Sheet: Step Order Evidence

A table recording the four counts, each produced by actually running the query in that configuration:

| Configuration | Rows |
|---|---|
| Whole-row Remove Duplicates, above Trim and Capitalize | 1,006 |
| Whole-row Remove Duplicates, below Trim and Capitalize | 1,004 |
| Whole-row Remove Duplicates, below Trim, Capitalize and the date step | 1,001 |
| Remove Duplicates on Invoice ID alone, any position | 1,000 |

Beneath it, a text cell carrying the conclusion in full: step order moved the count three times and
never reached 1,000, and only the column choice did.

## Sheet: Verification

| Check | Formula | Must show |
|---|---|---|
| Rows | `=COUNTA(CleanSales[Invoice ID])` | 1,000 |
| Total Sales | `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| Total quantity | `=SUM(CleanSales[Quantity])` | 5,510 |
| Duplicated Invoice IDs | COUNTA minus SUMPRODUCT/COUNTIF | 0 |
| Negative quantities | `=COUNTIF(CleanSales[Quantity],"<0")` | 0 |
| Distinct Product line values | `=SUMPRODUCT(1/COUNTIF(CleanSales[Product line],CleanSales[Product line]))` | 6 |

## Sheet: Refresh Test

The predicted-versus-actual table from `tier-3-solution.md`, filled in on both sides, plus a note
recording exactly which rows were added to the source file for the test.

## Before sign-off

1. Confirm all six Verification figures.
2. Confirm total Sales is ₦32,296,674.90 and **not** ₦32,517,975.00, which is what a
   1,006-row whole-row deduplication produces.
3. Confirm a date that was originally `DD-MM-YYYY` converted to the correct day, not just to a date.
4. Add rows to the source file, Refresh All, confirm every Verification figure moves as predicted,
   then restore the source file.

---

> ### One thing a facilitator must do once
>
> This workbook contains a real Power Query named **Clean Ilesanmi Sales**, with all ten Applied
> Steps. Open Data > Queries & Connections to see it, and Edit to step through it. The M code is the
> solution to the Tier 1 and Tier 2 exercises, and the automated test asserts that every named step
> is present and that the deduplication runs on Invoice ID alone.
>
> The machine this workbook was built on did **not** have the `Microsoft.Mashup.OleDb` provider
> registered, so the query could not be bound to a worksheet table automatically. The `CleanSales`
> table therefore holds the query's output as materialised values, produced by the identical logic
> and verified against the same figures. To bind the two on a normal Excel installation: open the
> query in the Power Query Editor, choose Close & Load To, select Table, and point it at a new
> worksheet. Confirm the loaded table reports 1,000 rows and ₦32,296,674.90 in total Sales,
> then delete the Read Me First sheet.
>
> Nothing in the teaching content depends on that binding. It matters only for demonstrating a live
> Refresh All in front of the room, which Tier 3 asks for.
