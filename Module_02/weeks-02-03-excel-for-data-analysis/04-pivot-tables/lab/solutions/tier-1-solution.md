# Tier 1 Worked Solution, Topic 2.4

Every figure was recomputed from `Datasets/Ilesanmi_Sales_Clean_AnswerKey.xlsx` with pandas.

## Expected pivot

| Branch | Sum of Sales | Count of transactions |
|---|---|---|
| Trans-Amadi | ₦11,056,870.65 | 328 |
| Ikeja | ₦10,620,037.05 | 340 |
| Wuse | ₦10,619,767.20 | 332 |
| **Grand total** | **₦32,296,674.90** | **1,000** |

## The two things worth narrating

**Trans-Amadi leads on Sales with the fewest transactions.** 328 transactions producing more revenue
than Ikeja's 340 means a higher average basket, and that is a real finding a manager can act on. A
trainee who reports only the ranking has read the pivot; a trainee who notices the counts contradict
the ranking has analysed it.

**Ikeja and Wuse are ₦269.85 apart**, on totals above ten million. That gap is far too small to
survive any error in the cleaning pass, which is the practical argument for why Topic 2.3 mattered:
on the raw 1,025-row file the same two branches sit ₦306,938.10 apart and in the same order,
but there is no way to know that without doing the work.

## Step 2, the Sum versus Count default

Excel defaults the Values area to Sum for a field it reads as fully numeric, and to Count when it
finds a blank or a text value. Sales comes in as Sum. **Rating comes in as Count**, because nine
blanks survive deduplication in a trainee's own cleaned file. That default is not a nuisance, it is a
free data quality signal, and it is worth saying so rather than just correcting it.

Changing it: right-click the value, Value Field Settings, Average. Rename the heading, because
`Average of Rating` in a shared report reads as a machine's label rather than a person's.

## Step 8, the verification

```
=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])   ->  ₦11,056,870.65
```

Both routes must read the same figure. The condition on that check is that both read the **same
table**: the identical formula against the raw 1,025-row export returns ₦11,338,588.80, which is
not a mismatch to investigate but an answer to a different question. A trainee who verifies a cleaned
pivot against a raw SUMIF has proved nothing, and this is worth demonstrating live if time allows.

## Common wrong answers

| What the trainee gets | What went wrong |
|---|---|
| Grand total of ₦33,156,782.40 | The pivot was built on the raw export rather than the cleaned table |
| Grand total of ₦32,517,975.00 | Built on a file deduplicated with every column ticked, so 1,006 rows |
| Counts instead of totals | Sales landed in Values as Count, usually because the column contains a text-stored number |
| Pivot that does not grow when rows are added | Built from a cell range rather than from `CleanSales` |
