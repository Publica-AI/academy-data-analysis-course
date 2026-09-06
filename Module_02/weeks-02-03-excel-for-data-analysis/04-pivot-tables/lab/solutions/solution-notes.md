# Solution Workbook Notes, Topic 2.4

> ### Status: built, executed and tested
>
> **`2.4_lab_solution.xlsx` ships with this lab pack** (185 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.4_lab_solution.xlsx`, built on the cleaned `CleanSales` table from the Topic 2.3 solution.

## Sheet: Clean Data

`CleanSales`, 1,000 rows, exactly as it left Topic 2.3. Untouched by this topic.

## Sheet: Pivots

Four pivot tables, all sourced from `CleanSales`:

1. **Branch by Sales**, Sum, sorted descending. Trans-Amadi ₦11,056,870.65, Ikeja
   ₦10,620,037.05, Wuse ₦10,619,767.20, grand total ₦32,296,674.90.
2. **Branch by Product line cross-tab**, Sum of Sales, with the full matrix from
   `tier-3-solution.md` and a grand total of ₦32,296,674.90.
3. **Branch by Customer type cross-tab**, Sum of Sales. Member column total
   ₦18,969,476.40, Normal ₦13,327,198.50.
4. **Branch by Average of Rating**, with the heading renamed from `Average of Rating`. Note in a
   comment that this field arrives as Count by default because of the nine blank Ratings.

One **Branch slicer**, connected to all four pivots via Report Connections.

## Sheet: Verification

Every figure a live formula, built independently of the pivots.

| Check | Formula | Must show |
|---|---|---|
| Trans-Amadi Sales | `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])` | ₦11,056,870.65 |
| Ikeja Sales | `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` | ₦10,620,037.05 |
| Wuse Sales | `=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])` | ₦10,619,767.20 |
| Chain total | `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| Ikeja Member | `=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Ikeja",CleanSales[Customer type],"Member")` | ₦6,289,577.70 |
| Trans-Amadi Food and beverages | `=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Trans-Amadi",CleanSales[Product line],"Food and beverages")` | ₦2,376,685.50 |
| Ikeja minus Wuse | difference of two cells above | ₦269.85 |
| Pivot minus SUMIF | the pivot cell minus the SUMIF cell | 0 |

The last row is the one that matters. It must be a live subtraction, so that a stale filter left on
the pivot makes it move away from zero immediately.

## Sheet: Findings

The Tier 2 two-sentence answer, the Tier 3 per-branch recommendation with its measure named, and a
short note on the Health and beauty contrast between Ikeja and Wuse.

## Before sign-off

1. Confirm the `Pivot minus SUMIF` cell reads 0.
2. Apply a Product line filter to pivot 1, confirm the same cell moves away from zero, and clear it.
3. Confirm every pivot's Table/Range reads `CleanSales` rather than a cell range.
4. Add a row to `CleanSales`, refresh all pivots, confirm every grand total moves, then undo.

## Note on the shipped workbook

`PT_Branch` carries **Product line in the Filters area** so the stale-filter demonstration works: setting it to Food and beverages drives the `Pivot minus SUMIF` cell away from zero, and clearing it brings the cell back to zero. That behaviour is part of the automated test.
