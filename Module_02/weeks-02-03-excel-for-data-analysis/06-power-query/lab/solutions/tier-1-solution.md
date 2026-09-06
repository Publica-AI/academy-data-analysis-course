# Tier 1 Worked Solution, Topic 2.6

All four row counts were verified by execution against `Ilesanmi_Sales_Raw_Export.csv`.

## The Applied Steps, in order

```
Source
Changed Type
Trimmed Text            (Product line)
Capitalized Each Word   (Product line)
Changed Type with Locale (Date, English day-first)
Removed Duplicates      (Invoice ID only)
```

## Step 8, the comparison that is the point of this lab

| Whole-row Remove Duplicates placed | Rows remaining |
|---|---|
| Above Trim and Capitalize | 1,006 |
| Below Trim and Capitalize | 1,004 |
| Below Trim, Capitalize and the date step | 1,001 |
| **Remove Duplicates on Invoice ID alone, any position** | **1,000** |

**How to read this.** Step order genuinely matters and it moved the count three times. Cleaning the
casing first collapses the two casing-mismatched pairs, taking 1,006 to 1,004. Repairing the dates as
well collapses the three date-mismatched pairs, taking it to 1,001. What survives at 1,001 is the
single pair that differs by a blank Rating, and no amount of reordering removes it.

**And yet it never reaches 1,000.** Only choosing Invoice ID does that, first time, in any order.
Both halves of that are worth saying explicitly, because the intuitive lesson, "clean first and the
duplicates sort themselves out", is half right and produces a wrong file.

## Step 5, the date trap

Use **Change Type With Locale**, not plain Change Type. Plain Change Type parses against the machine's
locale, and on a month-first machine `15-03-2019` errors, because there is no fifteenth month, while
`05-03-2019` silently becomes 3 May instead of 5 March. The errors are the safe failure; the silent
conversions are the dangerous one. Check a known day-first row after converting, not just the error
count.

## Expected final figures

| Check | Expected |
|---|---|
| `=COUNTA(CleanSales[Invoice ID])` | 1,000 |
| `=SUM(CleanSales[Sales])` | ₦32,296,674.90 |
| `=SUM(CleanSales[Quantity])` | 5,605 at this stage, because the sign flips are Tier 2's job |
| Distinct Product line values | 6 |

Note the quantity figure. At the end of Tier 1 the query has fixed four of the five faults, so the
quantity total is still the raw 5,605. It reaches 5,510 only after the Tier 2 step. A trainee who
reports 5,510 at the end of Tier 1 has either done Tier 2 early or is reading their Topic 2.3 file
rather than the query output.

## Common wrong answers

| What the trainee gets | What went wrong |
|---|---|
| 1,006 rows in the final query | Remove Duplicates left across every column |
| Dates all showing as errors | Plain Change Type on a month-first locale |
| Dates parsed with no errors but the wrong days | Change Type accepted month-first for every row where the day was 12 or under, which is the failure that does not announce itself |
| 1,000 rows but the wrong total Sales | Rows were filtered out rather than deduplicated, usually by a stray Remove Rows step |
