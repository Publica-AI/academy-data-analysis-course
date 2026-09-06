# Tier 3 Worked Solution, Topic 2.4

## The question

Which product line should each branch stock more of?

## Expected answer, measured by Sales

Product line in Rows, Branch in Columns, Sales in Values. Full matrix, all recomputed with pandas:

| Product line | Ikeja | Trans-Amadi | Wuse |
|---|---|---|---|
| Electronic accessories | ₦1,831,711.35 | ₦1,896,897.45 | ₦1,705,144.35 |
| Fashion accessories | ₦1,633,250.85 | ₦2,156,007.00 | ₦1,641,331.65 |
| Food and beverages | ₦1,716,310.05 | ₦2,376,685.50 | ₦1,521,488.85 |
| Health and beauty | ₦1,259,775.30 | ₦1,661,532.60 | ₦1,998,066.00 |
| Home and lifestyle | ₦2,241,719.55 | ₦1,389,555.30 | ₦1,754,916.45 |
| Sports and travel | ₦1,937,269.95 | ₦1,576,192.80 | ₦1,998,819.90 |

| Branch | Leading product line | Its Sales |
|---|---|---|
| Ikeja | Home and lifestyle | ₦2,241,719.55 |
| Wuse | Sports and travel | ₦1,998,819.90 |
| Trans-Amadi | Food and beverages | ₦2,376,685.50 |

Three different answers at three branches. That is the finding, and it is invisible in the chain-wide
product line ranking, where Food and beverages leads overall on ₦5,614,484.40.

## The part that separates a good answer from a complete one

**The measure is a choice, not a given.** Sales answers "which line earns most here". A stock
question is arguably about units, since shelf space holds units rather than naira, and total Quantity
is an equally defensible measure. So is transaction count, if the concern is footfall rather than
volume.

A trainee who picks one measure, applies it correctly and says why is at full credit. A trainee who
reports two measures, notes where they disagree and states which one they would send to the manager
has exceeded the brief and should be told so.

Note also what the question does not ask: nothing here says the leading line is the one to stock
more of. A line that already leads may be well served, while a line that under-performs at one branch
and leads at another may be the real opportunity. Health and beauty is the clearest example: it is
last at Ikeja on ₦1,259,775.30 and first at Wuse on ₦1,998,066.00. Any submission that
raises this is thinking like an analyst rather than a report generator.

## The independent check

At least one figure verified outside the pivot, for example:

```
=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Trans-Amadi",CleanSales[Product line],"Food and beverages")
  ->  ₦2,376,685.50
```

## Common wrong answers

| What the trainee reports | What went wrong |
|---|---|
| One product line for the whole chain | Answered the chain question, not the per-branch question that was asked |
| Food and beverages for all three branches | Read the grand total row rather than the per-branch columns |
| Correct matrix, no recommendation | Produced the table and stopped short of the analysis the manager asked for |
