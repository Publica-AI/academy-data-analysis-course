# Tier 1 Worked Solution, Topic 2.2

Every figure was recomputed from `Datasets/Ilesanmi_Sales_Raw_Export.csv` with pandas.

## Formulas

```
Satisfaction        =IF([@Rating]>=7,"Satisfied","Needs Follow-up")
Satisfaction Band   =IFS([@Rating]>=8,"Highly Satisfied",[@Rating]>=7,"Satisfied",TRUE,"Needs Follow-up")
Branch Code         =LEFT([@[Invoice ID]],3)

F1: 351-62-0822
G1: =XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])          -> Wuse
G2: =VLOOKUP(F1,RawSales[#All],2,FALSE)                          -> Wuse
G3: =INDEX(RawSales[Branch],MATCH(F1,RawSales[Invoice ID],0))    -> Wuse
```

The `TRUE` in the final IFS pair is the catch-all. Without it, any rating below 7 returns `#N/A`
rather than "Needs Follow-up", which is the most common IFS mistake and worth demonstrating.

## Expected figures

| Check | Expected | Verified by |
|---|---|---|
| XLOOKUP on `351-62-0822` | Wuse | The row reads Wuse, Abuja, Fashion accessories, ₦1,448.00, quantity 4, Sales ₦6,081.60 |
| `=LEFT("750-67-8428",3)` | 750 | String slice |
| `=SUM(RawSales[Sales])` | ₦33,156,782.40 | `raw['Sales'].sum()` |
| `=AVERAGE(RawSales[Rating])` | 6.97 | `raw['Rating'].mean()` is 6.9695, displayed to two places |
| `=COUNT(RawSales[Sales])` | 1,025 | `len(raw)` |
| `=COUNTIF(RawSales[Rating],">=7")` | 508 | `(raw['Rating'] >= 7).sum()` |
| `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])` | ₦11,062,565.85 | `raw.groupby('Branch')['Sales'].sum()['Ikeja']` |

## The VLOOKUP demonstration in step 4

Removing `FALSE` switches VLOOKUP to an approximate match. On an unsorted text column that returns
whatever the search algorithm lands on, with **no error message**. That silence is the teaching
point: an exact-match failure announces itself with `#N/A`, and an approximate-match failure does
not announce itself at all.

Note that `AVERAGE` here reads 6.97 while ignoring the 10 blank Ratings, because AVERAGE skips
blanks rather than treating them as zero. A trainee who expects blanks to drag the average down has
made a reasonable and wrong assumption, and it is worth naming.

## The 508 versus 501 point

This is the single most important thing in the topic. The same `=COUNTIF(RawSales[Rating],">=7")`
returns **508** on this 1,025-row file and **501** on the cleaned 1,000-row file in Topic 2.3, and
the gap is not rounding. Twelve of the 25 duplicated rows are rated 7 or above and come out during
deduplication; five of the nine restored blank Ratings turn out to be 7 or above and go in. So
508 minus 12 plus 5 equals 501. Only 501 is reportable to the client, because the raw file counts 25
sales twice.

Mark down any Tier 1 submission that reports 508 without labelling it as a raw figure. The number is
right; presenting it as the answer to the client's question is the error.
