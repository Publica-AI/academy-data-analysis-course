# Solution Workbook Notes, Topic 2.2

> ### Status: built, executed and tested
>
> **`2.2_lab_solution.xlsx` ships with this lab pack** (246 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.2_lab_solution.xlsx`, continuing from the Topic 2.1 solution workbook.

## Sheet: Raw Export

`RawSales`, 1,025 rows, carrying forward `Subtotal` and `Tax Check` from Topic 2.1 and adding:

| Added column | Formula |
|---|---|
| `Satisfaction` | `=IF([@Rating]>=7,"Satisfied","Needs Follow-up")` |
| `Satisfaction Band` | `=IFS([@Rating]>=8,"Highly Satisfied",[@Rating]>=7,"Satisfied",TRUE,"Needs Follow-up")` |
| `Branch Code` | `=LEFT([@[Invoice ID]],3)` |
| `Trimmed Length` | `=LEN(TRIM([@[Product line]]))` |
| `Raw Length` | `=LEN([@[Product line]])` |
| `Days Since` | `=DATEDIF([@Date],TODAY(),"d")` |

`Days Since` will error on the 51 rows holding a DD-MM-YYYY date as text. That is correct behaviour
and should be left visible in the solution workbook, because it is the clearest possible preview of
why Topic 2.3 exists.

## Sheet: Lookups

| Cell | Contents | Must show |
|---|---|---|
| F1 | `351-62-0822` | |
| G1 | `=XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])` | Wuse |
| G2 | `=VLOOKUP(F1,RawSales[#All],2,FALSE)` | Wuse |
| G3 | `=INDEX(RawSales[Branch],MATCH(F1,RawSales[Invoice ID],0))` | Wuse |
| G4 | `=VLOOKUP(F1,RawSales[#All],2)` | Any value, labelled "approximate match, unreliable, no error raised" |

## Sheet: Summary

Every figure a live formula, and every one labelled **raw, 1,025 rows**.

| Label | Formula | Must show |
|---|---|---|
| Total Sales | `=SUM(RawSales[Sales])` | ₦33,156,782.40 |
| Average rating | `=AVERAGE(RawSales[Rating])` | 6.97 |
| Transactions | `=COUNT(RawSales[Sales])` | 1,025 |
| Rated 7 or above | `=COUNTIF(RawSales[Rating],">=7")` | 508 |
| Ikeja Sales | `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])` | ₦11,062,565.85 |
| Wuse Sales | `=SUMIF(RawSales[Branch],"Wuse",RawSales[Sales])` | ₦10,755,627.75 |
| Trans-Amadi Sales | `=SUMIF(RawSales[Branch],"Trans-Amadi",RawSales[Sales])` | ₦11,338,588.80 |
| Ikeja transactions | `=COUNTIF(RawSales[Branch],"Ikeja")` | 353 |
| Wuse transactions | `=COUNTIF(RawSales[Branch],"Wuse")` | 338 |
| Trans-Amadi transactions | `=COUNTIF(RawSales[Branch],"Trans-Amadi")` | 334 |
| Branch Sales reconcile | `=SUM(...three cells...)-SUM(RawSales[Sales])` | 0 |
| Branch counts reconcile | `=SUM(...three cells...)-COUNTA(RawSales[Invoice ID])` | 0 |
| Wuse Health and beauty, exact | `=COUNTIFS(...,"Health and beauty")` | 48 |
| Wuse Health and beauty, wildcard | `=COUNTIFS(...,"Health and beauty*")` | 53 |
| Wuse Health and beauty Sales, wildcard | `=SUMIFS(...)` | ₦1,998,066.00 |

Beneath the block, a text cell carrying the raw-versus-cleaned warning in full: these figures are
measured on a file containing 25 duplicated invoices, and the two that move most are the rated-7-or-
above count (508 raw, 501 cleaned) and every branch total.

## Before sign-off

Confirm both reconciliation cells read exactly 0, and confirm the exact-versus-wildcard pair shows
48 and 53. If the wildcard row shows 48 as well, the trailing spaces have been cleaned out of the
source file by accident and the workbook is no longer built on the issued dataset.

## Note on the shipped workbook

The `Days Since` column returns `#VALUE!` on the 51 rows holding a `DD-MM-YYYY` text date. That is deliberate and must be left visible: it is the clearest possible preview of why Topic 2.3 exists.
