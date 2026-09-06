# Tier 2 Worked Solution, Topic 2.3

## The cleaning log

A full-credit log covers all five faults with all five fields. This is the model answer.

| Fault | Rows affected | How detected | Action taken | Why |
|---|---|---|---|---|
| Duplicated Invoice IDs | 25 | Conditional Formatting, Duplicate Values, on Invoice ID | Remove Duplicates on **Invoice ID only**, taking 1,025 rows to 1,000 | One Invoice ID is one completed sale. Excel's default of every column ticked removes only the 19 exact copies and leaves 1,006 rows, with six duplicated sales still counted |
| Product line in ALL CAPS with a trailing space | 102 | `LEN` before and after `TRIM` on two entries that look identical | `=PROPER(TRIM(...))`, pasted back as values | Six categories were being stored as more than six distinct values, which breaks any grouping, lookup or exact-match criterion applied to the column |
| Dates stored as `DD-MM-YYYY` text | 51 | Left alignment against the right-aligned true dates; `DATEDIF` errors on those rows | Text to Columns, Date: **DMY** | A text date is not a date. It cannot be sorted, filtered by period or used in a date calculation, and it made three of the duplicated invoices look like different transactions |
| Sign-flipped Quantity | 5 | Sorted Quantity ascending | **Corrected** from `=[@cogs]/[@[Unit price]]`, then pasted as values | The true value is recoverable from the file itself, because `cogs` and `Unit price` are intact and `cogs = Unit price × Quantity` holds on every row. All five divisions return whole numbers. Flagging would have been the answer only if that check had failed; deleting would have left 995 rows |
| Blank Rating | 10 in the raw file, 9 after deduplication | `=COUNTBLANK` on the Rating column | **Left blank**, and recorded | The true value is not recoverable from the file, and inventing one would be fabrication. This is the fault where flagging is the correct answer, and the contrast with the row above is the point |

## The verification block

Every cell a live formula over `CleanSales`. Nothing typed by hand.

| Check | Formula | Expected |
|---|---|---|
| Rows | `=COUNTA(CleanSales[Invoice ID])` | 1,000 |
| Duplicated Invoice IDs | `=COUNTA(CleanSales[Invoice ID])-SUMPRODUCT(1/COUNTIF(CleanSales[Invoice ID],CleanSales[Invoice ID]))` | 0 |
| Blank Ratings | `=COUNTBLANK(CleanSales[Rating])` | 9 |
| Negative quantities | `=COUNTIF(CleanSales[Quantity],"<0")` | 0 |
| Total Sales | `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| Ikeja | `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` | ₦10,620,037.05 |
| Wuse | `=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])` | ₦10,619,767.20 |
| Trans-Amadi | `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])` | ₦11,056,870.65 |
| Total quantity | `=SUM(CleanSales[Quantity])` | 5,510 |
| Branch totals reconcile | three SUMIFs added, minus `=SUM(CleanSales[Sales])` | 0 |

## The blank Rating consequence, and why it is in this lab

Leaving the nine blanks in place is correct, and it changes a headline figure:

| Formula | With 9 blanks left in place | With the 9 filled from confirmed values |
|---|---|---|
| `=COUNTIF(CleanSales[Rating],">=7")` | **496** | **501** |
| `=AVERAGE(CleanSales[Rating])` | 6.97 over 991 rows | 6.97 over 1,000 rows |

Both were verified by execution. `Ilesanmi_Sales_Clean_AnswerKey.xlsx` holds the filled version and
therefore reports 501, which is why every downstream topic in this module quotes 501.

A trainee's file will report **496**, and that is not an error. What is marked here is whether the
log states which of the two is being reported and why. A figure that moves depending on a defensible
judgement call must travel with the judgement call attached.

## Marking notes

- All five faults present with all five fields: full credit.
- The blank Rating row is the one that separates a good log from a complete one. A log that treats
  blanks and sign flips the same way has missed the distinction the whole topic turns on.
- Any figure in the verification block that is typed rather than calculated fails the block, however
  correct the number is. Test by deleting a row: everything should move.
