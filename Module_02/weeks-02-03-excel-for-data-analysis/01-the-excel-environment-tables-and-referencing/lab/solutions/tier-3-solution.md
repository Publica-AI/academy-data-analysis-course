# Tier 3 Worked Solution, Topic 2.1

## The question

On how many of the 1,025 rows do the export's three internal arithmetic relationships hold?

## One correct method

Three comparison columns, each filled down the table, then three conditional counts:

```
Check cogs    =ROUND([@[Unit price]]*[@Quantity],2)=ROUND([@cogs],2)
Check tax     =ROUND([@cogs]*0.05,2)=ROUND([@[Tax 5%]],2)
Check sales   =ROUND([@cogs]+[@[Tax 5%]],2)=ROUND([@Sales],2)

=COUNTIF(RawSales[Check cogs],TRUE)
=COUNTIF(RawSales[Check tax],TRUE)
=COUNTIF(RawSales[Check sales],TRUE)
```

Using `0.05` typed into the formula is acceptable here. Referencing `$B$1` from Tier 1 is better,
and is the answer a trainee should be nudged towards, because it means the whole check can be
re-pointed at a different tax rate by editing one cell.

## Expected answer

| Relationship | Rows where it holds | Rows where it fails |
|---|---|---|
| `Sales = cogs + Tax 5%` | 1,025 | 0 |
| `Tax 5% = cogs × 0.05` | 1,025 | 0 |
| `cogs = Unit price × Quantity` | 1,020 | 5 |

Verified with pandas against `Ilesanmi_Sales_Raw_Export.csv`: only the five sign-flipped rows break
the third relationship, and nothing breaks the first two.

## The two-sentence conclusion

A full-credit answer says something equivalent to:

> Every money column in this export is internally consistent on all 1,025 rows: the tax is exactly
> five per cent of cogs, and Sales is exactly cogs plus tax, with no exceptions. The only
> relationship that breaks is the one involving Quantity, and it breaks on five rows, so the fault
> was introduced into the Quantity column alone and none of the financial totals is affected by it.

## Why this matters, and what to say when marking

This is the finding that makes Topic 2.3's repair decision possible. Because `cogs` is provably
intact on every row, the true quantity on those five rows can be recovered exactly as
`cogs ÷ Unit price`, and the file can be corrected rather than merely flagged. A trainee who reaches
the 1,020 figure here has already done the analysis that justifies that decision, two topics early.

Credit a trainee who notices something stronger and says so: because `Sales` never depends on
`Quantity` in this file, the branch and product line totals reported anywhere in this module are
unaffected by the sign flips. Only the total quantity moves, from a raw 5,605 to a cleaned 5,510.

## Common wrong answers

| What the trainee reports | What went wrong |
|---|---|
| 1,020 / 1,020 / 1,020 | One check was written and copied twice without changing the columns |
| A number below 1,000 on the tax or sales check | Compared without rounding, so floating point noise registered as failures |
| 1,025 / 1,025 / 1,025 | The cogs check references `cogs` on both sides, so it is comparing a column with itself |
