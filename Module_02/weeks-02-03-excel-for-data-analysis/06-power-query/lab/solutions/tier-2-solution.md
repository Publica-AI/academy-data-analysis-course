# Tier 2 Worked Solution, Topic 2.6

## The task

Add a query step repairing the five sign-flipped quantities.

## One correct method

Add Column, Custom Column, with a conditional so the repair only touches rows that need it:

```
= if [Quantity] < 0 then [cogs] / [#"Unit price"] else [Quantity]
```

Name it `Quantity Fixed`, set its type to Whole Number, then remove the original Quantity column and
rename this one to `Quantity`. A Conditional Column built through the dialog is equally acceptable
and produces the same M code.

## Expected result

| Check | Before the step | After the step |
|---|---|---|
| `=COUNTIF(CleanSales[Quantity],"<0")` | 5 | **0** |
| `=SUM(CleanSales[Quantity])` | 5,605 | **5,510** |
| `=SUM(CleanSales[Sales])` | ₦32,296,674.90 | **₦32,296,674.90**, unchanged |

Sales must not move. In this dataset Sales is cogs plus tax and never depends on Quantity, so a
repair that changes any money total has changed something it should not have.

## Why the conditional matters, and the sentence being marked

An unconditional `[cogs] / [#"Unit price"]` gives the right answer on all 1,000 rows of **this**
file, because the relationship holds everywhere. It is still the weaker step, and the one-sentence
justification is where that shows.

A full-credit sentence says something equivalent to:

> The step only recalculates rows where Quantity is negative, so on next month's file it repairs the
> same fault if it recurs and leaves every correct row exactly as the source recorded it, which means
> a change in the underlying data can never be silently overwritten by my cleaning step.

The weaker version, "it divides cogs by unit price for every row", invites a real failure: if a
future export ever carries a genuine discount, a corrected price or a rounding difference that breaks
the cogs relationship, an unconditional step would quietly overwrite the true quantity with a derived
one, and no row count or total would flag it.

## Marking notes

- Negative quantities at 0 and the total at 5,510: the mechanical requirement.
- Sales unchanged at ₦32,296,674.90: the check that proves nothing else was disturbed.
- The conditional, and the sentence explaining it: the part that separates a trainee repeating Topic
  2.3 from one thinking about a process that runs unattended next month.
