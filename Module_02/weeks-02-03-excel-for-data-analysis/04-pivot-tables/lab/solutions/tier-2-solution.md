# Tier 2 Worked Solution, Topic 2.4

## Method

Branch in Rows, Customer type in Columns, Sales in Values summarised by Sum. Same shape as the Tier 1
cross-tab with Product line swapped for Customer type.

## Expected result

| Branch | Member | Normal | Row total |
|---|---|---|---|
| Ikeja | ₦6,289,577.70 | ₦4,330,459.35 | ₦10,620,037.05 |
| Trans-Amadi | ₦6,697,481.70 | ₦4,359,388.95 | ₦11,056,870.65 |
| Wuse | ₦5,982,417.00 | ₦4,637,350.20 | ₦10,619,767.20 |
| **Total** | **₦18,969,476.40** | **₦13,327,198.50** | **₦32,296,674.90** |

All figures recomputed with pandas. Member transactions number 565 and Normal 435 across the file.

## The independent check

Two conditions at once, so `SUMIFS` rather than `SUMIF`, and note the sum range comes **first**:

```
=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Ikeja",CleanSales[Customer type],"Member")
  ->  ₦6,289,577.70
```

Any one of the six cells is acceptable. What is marked is that the check was built independently of
the pivot and that the trainee states which cell they checked and what came back.

## The two sentences

A full-credit answer says something equivalent to:

> Member customers are worth more than Normal customers at every branch, ₦18,969,476.40
> against ₦13,327,198.50 across the chain, so the membership programme is associated with
> higher revenue everywhere. The size of the gap is not the same at all three, though: Member
> revenue at Trans-Amadi is more than half as large again as Normal revenue, while at Wuse the two
> are much closer, so whatever Wuse is doing differently with its membership is worth asking about.

The second half is the part that earns the credit. The first half is visible from a chain-wide total
and needed no cross-tab.

## Marking notes

- Six correct cells reconciling to ₦32,296,674.90: the mechanical part, full marks.
- An independent check that is actually independent: a trainee who reads a second pivot cell has not
  verified anything, because both figures come from the same object.
- An answer that stops at "Members are worth more" has answered half the question that was asked.
