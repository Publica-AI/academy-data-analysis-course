# Solution Workbook Notes, Topic 2.1

The solution for this topic is a workbook. This file describes exactly what the finished workbook
contains and every figure it must show, so that a reviewer can mark against it and a facilitator can
build it.

> ### Status: built, executed and tested
>
> **`2.1_lab_solution.xlsx` ships with this lab pack** (179 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.1_lab_solution.xlsx`, built from `Datasets/Ilesanmi_Sales_Raw_Export.xlsx`.

## Sheet: Raw Export

A structured table named `RawSales`, 1,025 data rows, 17 original columns plus these added columns:

| Added column | Formula | Purpose |
|---|---|---|
| `Subtotal` | `=[@[Unit price]]*[@Quantity]` | Relative references, Tier 1 |
| `Tax Check` | `=[@Subtotal]*$B$1` | Absolute reference, Tier 1 |
| `Arithmetic Check` | `=ROUND([@Subtotal],2)=ROUND([@cogs],2)` | Tier 2 |
| `Check tax` | `=ROUND([@cogs]*0.05,2)=ROUND([@[Tax 5%]],2)` | Tier 3 |
| `Check sales` | `=ROUND([@cogs]+[@[Tax 5%]],2)=ROUND([@Sales],2)` | Tier 3 |

Cells `A1` and `B1`, above the table: the label `Tax rate` and the value `0.05`.

## Sheet: Checks

Every figure below must be a live formula reading the table, not a typed number.

| Cell label | Formula | Must show |
|---|---|---|
| Rows | `=COUNTA(RawSales[Invoice ID])` | 1,025 |
| Sum of Subtotal | `=SUM(RawSales[Subtotal])` | ₦31,307,024.00 |
| Sum of cogs | `=SUM(RawSales[cogs])` | ₦31,577,888.00 |
| Difference | `=SUM(RawSales[cogs])-SUM(RawSales[Subtotal])` | ₦270,864.00 |
| Sum of Tax Check | `=SUM(RawSales[Tax Check])` | ₦1,565,351.20 |
| Sum of Tax 5% | `=SUM(RawSales[Tax 5%])` | ₦1,578,894.40 |
| Tax Check gap | `=SUM(RawSales[Tax 5%])-SUM(RawSales[Tax Check])` | ₦13,543.20, which is 5% of the Subtotal gap |
| Sum of Sales | `=SUM(RawSales[Sales])` | ₦33,156,782.40 |
| Rows failing the cogs check | `=COUNTIF(RawSales[Arithmetic Check],FALSE)` | 5 |
| Rows passing the cogs check | `=COUNTIF(RawSales[Arithmetic Check],TRUE)` | 1,020 |
| Rows passing the tax check | `=COUNTIF(RawSales[Check tax],TRUE)` | 1,025 |
| Rows passing the sales check | `=COUNTIF(RawSales[Check sales],TRUE)` | 1,025 |

## Sheet: Findings

A five-row block listing the disagreeing Invoice IDs with their Branch, Unit price, Quantity and
cogs: 875-31-8302, 200-40-6154, 134-75-2619, 827-26-2100 and 499-27-7781. Beneath it, the
one-sentence statement of the shared fault and the two-sentence Tier 3 conclusion.

## Before sign-off

Open the workbook, confirm every figure in the Checks sheet matches the table above, and confirm
that deleting the value in `B1` sends the Tax Check total to zero. That last test is what proves the
absolute reference is real rather than a hard-coded number.

Do not "correct" the Tax Check total to ₦1,578,894.40. It is supposed to differ from Tax 5%,
by ₦13,543.20, because Tax Check is built on Subtotal and Subtotal is negative on the five
sign-flipped rows. This was confirmed by building and recalculating the workbook.

## Note on the shipped workbook

The table header sits on **row 3**, leaving `A1` and `B1` free for the tax rate label and value. The workbook ships one deliberate mismatch: `Sum of Tax Check` reads ₦1,565,351.20 against ₦1,578,894.40 for Tax 5%. That is correct and is the Tier 2 hook, not a fault to repair.
