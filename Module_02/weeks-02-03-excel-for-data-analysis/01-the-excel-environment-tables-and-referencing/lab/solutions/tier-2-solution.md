# Tier 2 Worked Solution, Topic 2.1

## The task

Subtotal and `cogs` differ by ₦270,864.00 in total. Find how many rows disagree, and name them.

## Method

Add one comparison column to `RawSales`:

```
Arithmetic Check   =ROUND([@Subtotal],2)=ROUND([@cogs],2)
```

Then count the failures:

```
=COUNTIF(RawSales[Arithmetic Check],FALSE)
```

Rounding both sides first matters. Excel stores these as floating point numbers, and comparing two
computed values directly can report a difference of a fraction of a kobo as a mismatch. Rounding to
two decimal places, which is the precision the money is actually held to, removes that noise.

Filter the table on `Arithmetic Check = FALSE` to read the five rows off directly.

## Expected answer

**5 rows disagree**, out of 1,025.

| Invoice ID | Branch | Unit price | Quantity | cogs | Subtotal (Unit price × Quantity) |
|---|---|---|---|---|---|
| 875-31-8302 | Wuse | ₦9,338.00 | -1 | ₦9,338.00 | -₦9,338.00 |
| 200-40-6154 | Wuse | ₦6,591.00 | -6 | ₦39,546.00 | -₦39,546.00 |
| 134-75-2619 | Ikeja | ₦1,932.00 | -7 | ₦13,524.00 | -₦13,524.00 |
| 827-26-2100 | Ikeja | ₦3,384.00 | -9 | ₦30,456.00 | -₦30,456.00 |
| 499-27-7781 | Wuse | ₦5,321.00 | -8 | ₦42,568.00 | -₦42,568.00 |

**The shared fault, in one sentence:** every one of the five has a negative Quantity, so the
Subtotal comes out as the negative of the correct figure while `cogs` stayed positive and correct.

The total difference checks out: the five subtotals are each double their true magnitude away from
`cogs`, and 2 × (9,338 + 39,546 + 13,524 + 30,456 + 42,568) = ₦270,864.00, which is exactly
the gap found in Tier 1.

## Marking notes

- The count of 5 is the primary answer. A trainee who reports 5 but misidentifies which rows has
  built the check correctly and read the filter carelessly.
- A trainee who reports a number in the hundreds has almost certainly compared without rounding.
- A trainee who repairs the rows here has gone beyond the brief. Say so kindly, and point out that
  the decision about how to repair them is a topic in its own right, with three defensible options,
  which is Topic 2.3.
