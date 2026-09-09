# swiftroute_q3_raw.xlsx, fault injection log

Verified against the actual generated files with `verify_swiftroute_q3.py`, 32 checks, all
passing. Run it to reproduce every count below, including the affected delivery ids. The same discipline applies going forward: never assert a figure from this
document without recomputing it from the file.

- Generated: 2026-08-29T06:56:55.149653Z (seed 80261, reproducible)
- Company: SwiftRoute Logistics, last-mile delivery, Lagos, Ogun and Oyo. Continuity
  character: operations manager Adaeze Nwosu.
- Quarter covered: Q3 2026 (1 Jul to 30 Sep 2026)
- Unique deliveries: 3,600
- Total rows in the `deliveries` sheet after duplicate injection: 3,640

## Files

- `swiftroute_q3_raw.xlsx`, the dirty file trainees receive. Sheets: `deliveries`,
  `fuel_cost`, `customer_complaints`.
- `swiftroute_q3_answer_key.xlsx`, clean ground truth, the same delivery_id set (3,600
  unique rows, no duplicates), correct types throughout. Sheets: `deliveries_clean`,
  `fuel_cost`, `customer_complaints`. The latter two are identical in both files, because
  they were never fault injected.
- `verify_swiftroute_q3.py`, the script that checks every claim in this document against
  the actual workbooks. Re-run it after any regeneration.

## Injected faults

### 1. Mixed date formats

All 3,640 rows in `deliveries.date` are text, each rendered in one of five formats chosen
at random per row: `YYYY-MM-DD` (713 rows), `DD/MM/YYYY` (770), `MM-DD-YYYY` (706),
`D Mon YYYY` (699) and `DD.MM.YYYY` (752). All five are confirmed present.

`MM-DD-YYYY` and `DD/MM/YYYY` are the pair that matters. A day of 12 or less parses
silently under either reading, so a careless conversion swaps day and month on those rows
without raising a single error.

### 2. Naira amounts stored as text

All 3,640 rows in `deliveries.fee_naira` are text carrying the naira sign and thousands
commas, for example `₦45,320`, instead of a plain numeric column.

### 3. Rider names, trailing whitespace and inconsistent casing

628 rows have `rider_name` altered, upper, lower or title cased and padded with one to
three trailing spaces, some with leading spaces too. The canonical spelling is preserved in
the answer key under the same `delivery_id`.

### 4. Route code inconsistency, LAG-07 against LAG07

Route LAG-07 covers 288 rows in the sheet, split evenly: 144 keep the hyphenated `LAG-07`
and 144 use `LAG07`. The `fuel_cost` sheet uses only the canonical hyphenated form, so
`route_code` must be standardised in `deliveries` before that join is clean. This is
deliberate, not an oversight.

### 5. Blank delivery statuses

116 rows carry an empty string in `delivery_status`. The true status is preserved in the
answer key. The four real statuses are Delivered (2,541), In Transit (364), Returned (355)
and Failed (340).

Those 116 rows span only 115 distinct delivery_ids, because `SR-Q3-000941` is both blank
and one of the 40 duplicates in fault 7. Remove duplicates first and 115 blanks remain, so
a cleaned table has 3,485 rows with a known status. Trainees who clean in a different order
and report 116 have not made an error in the count, they have made one in the sequence, and
that is a useful thing to catch in the lab.

### 6. Six impossible values

Four negative durations and two dates in 2027, outside the Q3 2026 window.

| delivery_id | field | raw value | true value |
|---|---|---|---|
| SR-Q3-000972 | duration_min | -122 | 122 |
| SR-Q3-001746 | duration_min | -65 | 65 |
| SR-Q3-002289 | duration_min | -35 | 35 |
| SR-Q3-002303 | duration_min | -99 | 99 |
| SR-Q3-000794 | date | 2027-02-03 | 2026-08-02 |
| SR-Q3-001458 | date | 14.01.2027 | 2026-09-22 |

### 7. Forty duplicate delivery IDs

Exactly 40 delivery_ids each appear twice in `deliveries`. The second occurrence is a
verbatim duplicate, including whatever fault state the source row already had, appended at
the end of the sheet.

## Sheets not fault injected

- `fuel_cost`: 42 rows at route by month grain, 14 routes across 3 months, canonical
  hyphenated route codes. Clean by design, because the join against the messy
  `deliveries.route_code` is itself the exercise.
- `customer_complaints`: 175 rows, each referencing a `delivery_id` that exists in
  `deliveries`. Clean by design. A duplicated delivery_id causes a complaint to fan out to
  two rows on join, which is a realistic and intended side effect, not a separate injected
  fault.

## A known property of the data, not a fault: the routes do not cover their fuel

Recomputed from the files: quarterly delivery revenue is ₦12,196,290 across all 3,600 rows,
or ₦12,191,640 once the two rows with unrecoverable dates are set aside, against a fuel bill
of ₦23,352,881. Fuel costs about 1.9 times what the deliveries earn either way. Every one of the 14 routes
is loss making on that comparison, from LAG-06 at minus ₦38,505 to LAG-01 at minus
₦1,378,026. The mean fee is ₦3,388 for a mean distance of 22.98 km, while fuel works out at
₦3,522 to ₦8,645 per delivery depending on route.

The two sheets are each internally consistent. Fuel at 3.38 km per litre and around ₦955 a
litre is realistic for a Nigerian van fleet in 2026. The gap comes from comparing a fleet
level fuel bill against a 3,600 row delivery extract, which is roughly three deliveries per
route per day.

**Do not build a profitability exercise on this pairing** unless you first decide, and
state, what the delivery extract is a sample of. What the pairing is genuinely good for is
cost per kilometre, cost per litre trends across the three months, and the standardise
before you join lesson in fault 4.

It is also the sharpest verification exercise in the module. Ask an AI assistant for margin
by route and it will return 14 confident negative numbers, correctly calculated, without
once asking whether a business that loses money on every single route for a whole quarter
is plausible. Topic 8.5 uses exactly this.

## Hard rules honoured

- No week numbers anywhere in the sheets, checked programmatically.
- No real personal data. Rider names, business identifiers and delivery ids are generated,
  so the file is safe to upload to an AI tool.
- Every figure in this document was recomputed from the written workbooks, not carried over
  from generation-time bookkeeping.
