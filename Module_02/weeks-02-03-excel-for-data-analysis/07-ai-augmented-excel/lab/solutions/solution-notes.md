# Solution Workbook Notes, Topic 2.7

> ### Status: built, executed and tested
>
> **`2.7_lab_solution.xlsx` ships with this lab pack** (128 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.7_lab_solution.xlsx`, the final state of the module's running workbook, continuing from Topic 2.6.

## Sheet: Known Totals

Written before any AI tool is opened. Every cell a live formula over `CleanSales`.

| Label | Formula | Must show |
|---|---|---|
| Rows | `=COUNTA(CleanSales[Invoice ID])` | 1,000 |
| Total Sales | `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| Ikeja | `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` | ₦10,620,037.05 |
| Wuse | `=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])` | ₦10,619,767.20 |
| Trans-Amadi | `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])` | ₦11,056,870.65 |
| Total quantity | `=SUM(CleanSales[Quantity])` | 5,510 |
| Rated 7 or above | `=COUNTIF(CleanSales[Rating],">=7")` | 496, labelled "nine blank Ratings left in place" |

## Sheet: AI Comparison

| Column | Contents |
|---|---|
| Task | What was asked for |
| Prompt | The exact prompt text |
| AI output | The exact formula or figure returned |
| My method | The independent check used |
| My result | What that check returned |
| Match | Yes or no |

Minimum entries: the vague ratings prompt, the specific ratings prompt, the nested formula
explanation with its tested prediction, the VLOOKUP debug, the Ikeja total, and all six product line
figures.

## Sheet: Product Line Check

The six product lines with the AI figure and the workbook figure side by side, and a reconciliation
cell computing the sum of the six minus `=SUM(CleanSales[Sales])`, which must read 0.

## Sheet: Verification Checklist

The eight-item checklist from `tier-3-solution.md`, with a column recording the result of applying
each item to this workbook, including at least one honest failure or unanswerable item.

## Before sign-off

1. Confirm the reconciliation cell on Product Line Check reads 0.
2. Confirm the Rated 7 or above cell reads 496 **and** carries its label. A bare 496, or a bare 501,
   is the exact fault the checklist's item 6 exists to catch, and the solution workbook must not
   commit it.
3. Confirm every entry in the AI Comparison sheet has both a method and a result. Any row where the
   method column reads "checked" or "looked right" fails the sheet.
4. Confirm the workbook still opens cleanly with no external links to an AI tool or a chat export.

## Note on the shipped workbook

The `Rated 7 or above` cell reads **496** and carries its label. A bare 496, or a bare 501, is exactly the fault the checklist's item 6 exists to catch, so the solution workbook must not commit it.
