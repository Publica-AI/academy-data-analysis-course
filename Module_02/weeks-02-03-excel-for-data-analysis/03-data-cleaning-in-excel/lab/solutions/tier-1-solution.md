# Tier 1 Worked Solution, Topic 2.3

Every figure was recomputed from `Datasets/Ilesanmi_Sales_Raw_Export.csv` and cross-checked against
the Verification sheet of `Ilesanmi_Sales_Clean_AnswerKey.xlsx`.

## Part A, duplicates

| Run | Columns ticked | Rows removed | Rows remaining |
|---|---|---|---|
| First | Every column (Excel's default) | 19 | 1,006 |
| Second | Invoice ID only | 25 | 1,000 |

**Why they differ.** 25 Invoice IDs appear twice. 19 of those pairs are identical in all seventeen
columns, so an every-column rule catches them. The remaining 6 differ in exactly one field each:

| Invoice ID | Field that differs |
|---|---|
| 137-63-5492 | Date |
| 291-55-6563 | Date |
| 700-81-1757 | Date |
| 569-71-4390 | Product line |
| 189-52-0236 | Product line |
| 263-10-3913 | Rating (blank on one of the two rows) |

**What is not the explanation.** Step order. Trimming and re-casing before deduplicating does not
change either count, because Invoice ID itself carries no formatting fault. Deduplicating on Invoice
ID returns exactly 1,000 rows whether the file was cleaned first or not. Cleaning first matters for a
different reason: it is what makes the six disguised copies visible to a human, and what a whole-row
rule would need in order to catch any of them. Even then it does not get there: clean the casing and
spacing and an every-column run drops from 1,006 to 1,004, add the date repair and it drops to 1,001,
and only choosing Invoice ID reaches 1,000. All four counts were verified by execution.

## Part B, spaces and casing

102 rows hold the Product line in ALL CAPS with a trailing space. `=PROPER(TRIM([@[Product line]]))`
repairs both in one pass, then Paste Special, Values over the original column. After the repair the
column holds exactly six distinct values: Electronic Accessories, Fashion Accessories, Food And
Beverages, Health And Beauty, Home And Lifestyle, Sports And Travel.

PROPER capitalises every word, so "Food and beverages" becomes "Food And Beverages". That is a
cosmetic difference from the answer key's casing and does not affect any total, because Excel's
criteria matching is not case sensitive. Accept either. A trainee who notices and fixes it with a
more precise formula has done better than the brief asked for.

## Part C, dates

51 rows hold the date as `DD-MM-YYYY` text. Text to Columns with the data format set to **Date: DMY**
re-parses them. Setting it to MDY instead is the trap: `15-03-2019` errors, because there is no
fifteenth month, but `05-03-2019` silently converts to 3 May instead of 5 March. Check a
known day-first value after the conversion, not just the row count.

After the repair `=COUNT()` on the Date column reads 1,000, because COUNT counts numbers and true
dates are numbers, while text dates are not.

## Part D, impossible values

| Invoice ID | Shown Quantity | Unit price | cogs | cogs ÷ Unit price | True Quantity |
|---|---|---|---|---|---|
| 875-31-8302 | -1 | ₦9,338.00 | ₦9,338.00 | 9,338 ÷ 9,338 | 1 |
| 200-40-6154 | -6 | ₦6,591.00 | ₦39,546.00 | 39,546 ÷ 6,591 | 6 |
| 134-75-2619 | -7 | ₦1,932.00 | ₦13,524.00 | 13,524 ÷ 1,932 | 7 |
| 827-26-2100 | -9 | ₦3,384.00 | ₦30,456.00 | 30,456 ÷ 3,384 | 9 |
| 499-27-7781 | -8 | ₦5,321.00 | ₦42,568.00 | 42,568 ÷ 5,321 | 8 |

**Correct, do not flag.** Flagging is the right answer when the true value cannot be recovered, and
here it can: this dataset holds `cogs = Unit price × Quantity` exactly on every row, `cogs` and
`Unit price` are both intact on all five, and every division returns a whole number matching the
magnitude already shown. Deleting instead is what produces a 995-row file.

Sales, Tax 5% and cogs were never wrong on these rows, so no money total changes. Only the quantity
total moves, from a raw 5,605 to a cleaned 5,510.

## Final state

Table renamed to `CleanSales`, 1,000 rows, `=SUM(CleanSales[Sales])` reading ₦32,296,674.90 and
`=SUM(CleanSales[Quantity])` reading 5,510.
