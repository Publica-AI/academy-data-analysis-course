# Solution Workbook Notes, Topic 2.3

> ### Status: built, executed and tested
>
> **`2.3_lab_solution.xlsx` ships with this lab pack** (233 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.3_lab_solution.xlsx`. This is the workbook Topics 2.4 to 2.7 all build on, so it matters more
than any other solution file in the module.

## Sheet: Raw Export (untouched)

A verbatim copy of the 1,025-row export, kept so the before-and-after comparison can be re-run and
so a reviewer can confirm the cleaning rather than take it on trust.

## Sheet: Clean Data

A structured table named **`CleanSales`**, 1,000 rows, with:

- Duplicates removed on **Invoice ID only**
- Product line repaired with `=PROPER(TRIM(...))` and pasted as values, six distinct values remaining
- The 51 `DD-MM-YYYY` dates re-parsed with Text to Columns, Date: DMY, so `=COUNT()` on the column reads 1,000
- The five sign-flipped quantities corrected from `cogs ÷ Unit price` and pasted as values
- The nine surviving blank Ratings **left blank**, deliberately

## Sheet: Cleaning Log

The five-row table from `tier-2-solution.md`, with columns: Fault, Rows affected, How detected,
Action taken, Why. Plus a note stating that the blank Ratings were left in place and that
`=COUNTIF(CleanSales[Rating],">=7")` therefore reads 496 in this workbook, against 501 in the
instructor answer key where those nine values are filled.

## Sheet: Verification

Every cell a live formula. No typed numbers anywhere.

| Check | Must show |
|---|---|
| `=COUNTA(CleanSales[Invoice ID])` | 1,000 |
| Duplicated Invoice IDs (COUNTA minus SUMPRODUCT/COUNTIF) | 0 |
| `=COUNTBLANK(CleanSales[Rating])` | 9 |
| `=COUNTIF(CleanSales[Quantity],"<0")` | 0 |
| `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` | ₦10,620,037.05 |
| `=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])` | ₦10,619,767.20 |
| `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])` | ₦11,056,870.65 |
| `=SUM(CleanSales[Quantity])` | 5,510 |
| `=COUNTIF(CleanSales[Rating],">=7")` | 496, labelled "blanks left in place" |
| Branch totals minus chain total | 0 |

## Sheet: Colleague Note

The Tier 3 model answer, under 200 words, plus the `1,006 / 1,004 / 1,001 / 1,000` comparison table
showing what step order does and does not achieve.

## Before sign-off

1. Confirm every Verification figure matches the table above.
2. Delete one row from `CleanSales` and confirm **every** Verification figure moves. Undo.
3. Confirm the Date column returns 1,000 to `=COUNT()`, and spot-check one row that was originally
   `DD-MM-YYYY` to make sure it converted to the right day rather than the right-looking day.
4. Confirm `Raw Export` still holds 1,025 rows and has not been cleaned by accident.

## Note on the shipped workbook

Both tables ship in one file: `RawSales` at 1,025 rows on the untouched sheet, and `CleanSales` at 1,000 rows on the cleaned sheet, so the before-and-after comparison can be re-run without a second workbook.
