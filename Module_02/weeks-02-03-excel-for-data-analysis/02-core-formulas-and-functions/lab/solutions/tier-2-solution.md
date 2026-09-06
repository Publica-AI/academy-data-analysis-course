# Tier 2 Worked Solution, Topic 2.2

## Method

Six conditional aggregates plus two reconciling totals:

```
=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])
=SUMIF(RawSales[Branch],"Wuse",RawSales[Sales])
=SUMIF(RawSales[Branch],"Trans-Amadi",RawSales[Sales])
=COUNTIF(RawSales[Branch],"Ikeja")
=COUNTIF(RawSales[Branch],"Wuse")
=COUNTIF(RawSales[Branch],"Trans-Amadi")

=SUM(RawSales[Sales])            -> must equal the three SUMIFs added together
=COUNTA(RawSales[Invoice ID])    -> must equal the three COUNTIFs added together
```

Referencing a cell holding the branch name, rather than typing `"Ikeja"` into the formula, is the
better answer and should be credited. It means the block can be re-pointed at a new branch by
editing one cell, and it removes the risk of a typo inside quotation marks that Excel will never
flag.

## Expected answer

| Branch | Total Sales (raw) | Transactions |
|---|---|---|
| Ikeja | ₦11,062,565.85 | 353 |
| Wuse | ₦10,755,627.75 | 338 |
| Trans-Amadi | ₦11,338,588.80 | 334 |
| **All three** | **₦33,156,782.40** | **1,025** |

Both reconciliations hold: 11,062,565.85 + 10,755,627.75 + 11,338,588.80 = 33,156,782.40, and
353 + 338 + 334 = 1,025. All six figures were recomputed with pandas from the raw export.

## The sentence about why reconciliation matters

A full-credit answer says something equivalent to:

> If the three branch totals do not add back to the file total, then either a row belongs to a
> branch I have not named, or one of my conditions is matching rows it should not, and in both cases
> I would be reporting a number that is quietly incomplete rather than one that is visibly wrong.

That is the habit the whole module is built on: a figure you cannot reconcile against something else
is a figure you have not checked.

## Common wrong answers

| What the trainee gets | What went wrong |
|---|---|
| Branch totals that do not sum to the chain total | A branch name misspelled inside the quotation marks; SUMIF returns 0 silently rather than erroring |
| Transaction counts summing to 1,000 | The cleaned answer key was used instead of the raw export |
| Correct totals, no reconciliation line | The arithmetic is right and the exercise's actual point was missed |
