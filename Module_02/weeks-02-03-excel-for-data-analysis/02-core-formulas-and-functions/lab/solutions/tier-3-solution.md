# Tier 3 Worked Solution, Topic 2.2

## The question

How many Health and beauty transactions did Wuse handle, and what did they come to? Raw file.

## One correct method

The question names two conditions, so the plural functions are needed:

```
=COUNTIFS(RawSales[Branch],"Wuse",RawSales[Product line],"Health and beauty*")
=SUMIFS(RawSales[Sales],RawSales[Branch],"Wuse",RawSales[Product line],"Health and beauty*")
```

Note the argument order changes between the two families. `SUMIF` puts the sum range last;
`SUMIFS` puts it **first**. Getting this backwards is the most common error in this exercise, and
Excel will often return a plausible number rather than an error, which makes it worth naming
explicitly during the debrief.

## Why the wildcard is needed here

102 rows in this export hold the Product line in ALL CAPS **with a trailing space**. Excel's criteria
matching is not case sensitive, so `"Health and beauty"` matches `HEALTH AND BEAUTY` without help.
The trailing space is the problem: `"Health and beauty"` will not match `"HEALTH AND BEAUTY "`.

| Criterion used | Transactions matched | Total Sales |
|---|---|---|
| `"Health and beauty"` (exact) | 48 | ₦1,676,615.85 |
| `"Health and beauty*"` (wildcard) | 53 | ₦1,998,066.00 |

**53 and ₦1,998,066.00 is the expected answer**, because the 5 rows with a trailing space are
genuine Health and beauty transactions and belong in the count. A trainee who reports 48 has written
a correct formula against a broken file and should be shown the difference rather than simply marked
down, because finding that gap is the real lesson.

Both pairs of figures were recomputed from `Ilesanmi_Sales_Raw_Export.csv` with pandas.

## The two sentences to the manager

A full-credit answer says something equivalent to:

> Wuse handled 53 Health and beauty transactions worth ₦1,998,066.00, measured on the export as
> received. That file still holds 25 duplicated invoices, so any figure taken from it is provisional
> until it is cleaned, even though these two happen to survive cleaning unchanged, because none of
> the duplicated invoices is a Wuse Health and beauty row. The Product line condition is the least
> reliable part of this answer: 102 rows in the file hold that value with inconsistent casing and a
> trailing space, and a formula written the obvious way silently misses 5 of these transactions.

## Marking notes

- Reaching 53 by any defensible route is full credit, including finding it with a filter and the
  Status bar rather than with COUNTIFS.
- Reporting 48 with the caveat that the trailing spaces are suppressing the count is close to full
  credit; the analysis is right and only the reported figure is short.
- Reporting 48 with no caveat is the failure mode this exercise is designed to expose.
- Noting that these two figures are unchanged by cleaning, because no duplicated invoice is a Wuse
  Health and beauty row, is beyond the brief and worth calling out in the debrief.
- Any trainee who cleans the Product line column to get the answer has jumped ahead to Topic 2.3.
  Credit the instinct, and note that the decision about how to clean it is the next topic's work.
