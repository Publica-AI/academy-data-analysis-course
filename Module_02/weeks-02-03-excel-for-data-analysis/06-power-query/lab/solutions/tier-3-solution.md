# Tier 3 Worked Solution, Topic 2.6

## Baseline, before anything is added

On the unmodified export the finished query must reproduce Topic 2.3 exactly. All verified by
execution:

| Check | Expected |
|---|---|
| Rows | 1,000 |
| Total Sales | ₦32,296,674.90 |
| Total quantity | 5,510 |
| Duplicated Invoice IDs | 0 |
| Negative quantities | 0 |
| Distinct Product line values | 6 |

## The predicted-versus-actual table

This is the assessed artefact, and the prediction column must be filled in **before** the refresh.

| Check | Predicted | Actual | Match |
|---|---|---|---|
| Rows | 1,000 + rows added | | |
| Total Sales | ₦32,296,674.90 + Sales added | | |
| Total quantity | 5,510 + quantity added | | |
| Duplicated Invoice IDs | 0 | | |
| Negative quantities | 0 | | |
| Distinct Product line values | 6 | | |

A trainee who adds five clean rows should predict 1,005 and get 1,005. A trainee who adds a row
carrying a deliberately duplicated Invoice ID, or a negative quantity, and predicts correctly that
the query will absorb it, has understood what the query is for. Credit that strongly.

## The verification block

```
=COUNTA(CleanSales[Invoice ID])
=SUM(CleanSales[Sales])
=SUM(CleanSales[Quantity])
=COUNTA(CleanSales[Invoice ID])-SUMPRODUCT(1/COUNTIF(CleanSales[Invoice ID],CleanSales[Invoice ID]))
=COUNTIF(CleanSales[Quantity],"<0")
```

The fourth is the one worth keeping permanently. It returns 0 on a correctly deduplicated table and
the number of excess rows otherwise, so it catches a broken Remove Duplicates step on a file nobody
has looked at.

## The two sentences on an unexpected 1,010

A full-credit answer says something equivalent to:

> I would not touch the loaded table. I would reopen the query and step through Applied Steps one at
> a time, watching the row count in the preview after each, because a count that is five higher than
> expected means one specific step stopped doing its job on this month's data, and the step list will
> show me which one within a minute. Deleting five rows from the loaded table would give me the right
> count this month and guarantee the same fault comes back next month with the row count now hiding it.

## Common wrong answers

| What the trainee does | What went wrong |
|---|---|
| Fills the prediction column after refreshing | The exercise is the prediction, not the arithmetic |
| Checks only the row count | A query can reach the right count having kept the wrong rows; a value check has to sit beside it |
| Reports the refresh worked with no figures | The claim this topic exists to stop: a refresh reruns the steps, it does not guarantee the result |
