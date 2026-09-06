# Tier 3 Worked Solution, Topic 2.3

## The scenario

A colleague's cleaned file has 1,006 rows. Write them a note under 200 words.

## Model answer (183 words)

> Your file still contains six duplicated sales. It has 1,006 rows and the client's export should
> reduce to 1,000.
>
> The cause is the Remove Duplicates dialog. It opens with every column ticked, and on that default
> two rows have to agree on all seventeen fields before Excel treats them as duplicates. Only 19 of
> the 25 duplicated invoices are exact copies throughout, so those 19 came out and six did not.
>
> The six that survived differ in exactly one field each: three have the same date written
> `DD-MM-YYYY` on one row and `M/D/YYYY` on the other, two have the Product line in different casing,
> and one, invoice `263-10-3913`, has a blank Rating on one of its two rows.
>
> You can confirm this on your own file in one formula.
> `=COUNTA([Invoice ID])-SUMPRODUCT(1/COUNTIF([Invoice ID],[Invoice ID]))` returns 6 on yours and 0
> on a correctly cleaned one.
>
> The fix is to start again from an untouched copy of the raw export and run Remove Duplicates with
> **Invoice ID alone** ticked. That removes all 25 and lands on 1,000.

## What must be present for full credit

| Element | Why it matters |
|---|---|
| The file has six too many rows, not too few | Names the actual harm: six sales counted twice |
| The cause is the every-column default | The point of the exercise |
| 19 exact copies out of 25 | The arithmetic that makes the cause checkable |
| The six differ in one field each, named | Shows the diagnosis was done, not guessed |
| Re-run on Invoice ID alone | The fix |
| Start from a fresh raw copy, not the 1,006-row file | Remove Duplicates is destructive and the six survivors are now indistinguishable from clean rows without the original |
| A check the colleague can run themselves | Turns the note from an assertion into something verifiable |

## Credit strongly

A note that also says what is **not** the cause. The instinctive explanation, that they should have
trimmed and re-cased before deduplicating, is wrong on this dataset and it is worth saying so:
Invoice ID carries no formatting fault, so deduplicating on it returns 1,000 rows in any order.
Cleaning first improves a whole-row rule without ever rescuing it, taking an every-column run from
1,006 to 1,004 after the casing repair and to 1,001 after the dates as well. All three figures were
verified by execution.

## Common wrong answers

| What the trainee writes | What went wrong |
|---|---|
| "You cleaned in the wrong order, trim first then deduplicate" | The plausible explanation, and false on this file. This is the misconception the exercise exists to catch |
| "Your file is missing 6 rows" | The direction is inverted. 1,006 is too many, not too few |
| "Just delete 6 rows to get to 1,000" | Fixes the count and not the data, and there is no way to tell which six without going back to the original |
| A correct diagnosis over 400 words | The brief is a note to a colleague. Length is part of the exercise |
