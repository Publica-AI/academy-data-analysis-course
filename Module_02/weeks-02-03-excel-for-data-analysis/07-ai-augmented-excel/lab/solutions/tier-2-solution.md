# Tier 2 Worked Solution, Topic 2.7

## The verified figures

| Product line | Sales |
|---|---|
| Food and beverages | ₦5,614,484.40 |
| Sports and travel | ₦5,512,282.65 |
| Electronic accessories | ₦5,433,753.15 |
| Fashion accessories | ₦5,430,589.50 |
| Home and lifestyle | ₦5,386,191.30 |
| Health and beauty | ₦4,919,373.90 |
| **Total** | **₦32,296,674.90** |

All recomputed with pandas from `Ilesanmi_Sales_Clean_AnswerKey.xlsx`. The total equals
`=SUM(CleanSales[Sales])`, which is the reconciliation the exercise turns on.

## The three-column deliverable

| Product line | AI figure | My figure | Match |
|---|---|---|---|
| Food and beverages | | ₦5,614,484.40 | |
| Sports and travel | | ₦5,512,282.65 | |
| Electronic accessories | | ₦5,433,753.15 | |
| Fashion accessories | | ₦5,430,589.50 | |
| Home and lifestyle | | ₦5,386,191.30 | |
| Health and beauty | | ₦4,919,373.90 | |
| **Sum of the six** | | **₦32,296,674.90** | |

## Why the reconciliation row is the whole exercise

Six plausible figures are easy to produce and hard to check one at a time. Six figures that must add
to a total you already know are checkable in a single subtraction. An assistant working from a
partial paste, or estimating, will very often produce six individually reasonable numbers that do not
sum to ₦32,296,674.90, and that single failure exposes all six at once.

This is worth stating as a general habit rather than a trick for this lab: **when you ask for a
breakdown, you get a free check, because the parts have to add to the whole.**

## The sentence being marked

A full-credit answer names the concrete consequence, for example:

> If I had accepted the assistant's breakdown without checking, I would have told the client that
> Health and beauty is their weakest line at a figure I never verified, and the recommendation to
> reduce its stock would have gone out on the strength of a number that did not reconcile to a total
> sitting in the same workbook.

## Marking notes

- All six rows filled in on both sides, including where the assistant declined.
- The reconciliation row calculated rather than assumed.
- A trainee whose assistant produced correct figures still has to show the check. Getting a right
  answer from an assistant is luck; demonstrating that it was right is the skill.
