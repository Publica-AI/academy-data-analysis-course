# Demo Guide - Data Cleaning in Excel
**Module 2, Topic 2.3 | Estimated duration: 33-37 minutes**

---

## What This Demo Teaches

- Identify and repair duplicates in a messy dataset
- Identify and repair inconsistent formats in a messy dataset
- Identify and repair stray spaces in a messy dataset
- Identify and repair mixed data types in a messy dataset
- Identify and repair impossible values in a messy dataset
- Confirm the cleaned file matches a stated expected row count

---

## Setup - Before the Demo Starts

1. Open a fresh copy of `RawSales` (the 1,025-row file from Topics 2.1-2.2, formulas intact)
2. Keep an untouched backup copy of the raw file closed and set aside, per the module's own rule that Remove Duplicates is not reversible by Undo alone once a file is saved and closed
3. Have the clean 1,000-row answer key available as your own private reference, not shown to trainees until the row count check at the end
4. Have a finished, pre-built copy of the fully cleaned file ready as a fallback

> **Instructor note:** this file's numeric columns (Unit price, Quantity, Sales) do not contain a genuine mixed-data-type fault on inspection. To cover that outcome honestly, seed one deliberate example live rather than claiming the file already has one; see Part 4.

---

## Demo Steps

### Part 1 - Finding and Repairing Duplicates (7 min)

> "No formula, pivot table or chart is trustworthy if the data underneath it is wrong. This is where the file becomes reliable, and duplicates are the first problem, because they're the easiest to miss."

- Apply Conditional Formatting, Highlight Cell Rules, Duplicate Values, on the Invoice ID column first, as a visual check before deleting anything
- State the decision out loud: "same Invoice ID counts as a true duplicate here, that's the column combination we're using to define one"
- Run Data tab, Remove Duplicates, on Invoice ID: 25 rows come out
- Point out that not all 25 look identical, 19 are exact full-row repeats, but 6 are the same transaction disguised by a formatting difference, such as a DD-MM-YYYY date against the same transaction's M/D/YYYY row, or a Product line entered in a different case

> "That second group is the one people miss when they clean too fast. A duplicate can be hiding behind a formatting difference, not just an exact copy."

### Part 2 - Repairing Inconsistent Formats (6 min)

> "Same meaning, different shape, and Excel treats every shape as a different value."

- Show the ALL CAPS Product line entries (102 rows in the raw file) next to a normally cased entry, and point out these are genuinely three different values to Excel, not a display quirk
- Fix with `=PROPER([@[Product line]])`, then paste values back over the original column to lock in the fix
- Show a text-stored date's left alignment against a true date's right alignment as the fast diagnostic tell, then use Text to Columns to re-parse the 51 DD-MM-YYYY rows into true dates

> "Fixing one cell by hand doesn't fix the column. Every one of these repairs needs to apply to the whole column, or the problem just resurfaces two rows later."

### Part 3 - Stray Spaces (5 min)

> "This one's a callback to 2.2, not new material."

- Show two Product line cells that look identical on screen, run `=LEN()` on both, and let the differing character counts reveal the invisible trailing space
- Fix with `=TRIM()`, the same function trainees already used in the previous topic, now applied as part of a full cleaning pass rather than a standalone formula exercise

### Part 4 - Mixed Data Types (5 min)

> "This file's numeric columns happen to be clean on this point, so I'm going to break one on purpose so we can practise spotting and fixing it."

- Type a number into a normally numeric Sales cell with a leading apostrophe, forcing it to store as text; point out the resulting green triangle warning
- Run `=ISNUMBER()` on the cell to confirm it returns FALSE
- Repair it with `=VALUE()`, then paste the result back as a value; alternatively, demonstrate Paste Special, Multiply, against an empty cell containing 1
- Close the loop: re-run `=SUM()` on the column and confirm the total is back to what it should be

> "I want to be upfront that I planted that one. It's a genuine, common problem in real exported files, it just doesn't happen to appear in this particular dataset, so seeding one example is the honest way to cover it."

### Part 5 - Impossible Values (6 min)

> "Now the judgement call problem. Not everything unusual is wrong, but everything unusual needs a decision, not a guess."

- Sort the Quantity column ascending and surface the 5 negative values (-1, -6, -7, -8, -9)
- Run the three-path decision live on one of them: can it be confirmed and corrected against another source? If not, flag it with a status column rather than deleting it outright; only remove once confirmed as an error with no recoverable value
- Record the decision and the reason, out loud, as part of the cleaning record

**Ask students:** why would running duplicate detection before trimming the 102 Product line rows have missed some of the 6 disguised duplicates?

> "Because a trailing space or a caps difference is enough for Excel to treat two identical transactions as different rows. Clean the smaller, quieter problems first, or you under-count what you find later. That's why this topic teaches a fixed order: stray spaces, then formats, then mixed types, then duplicates, then impossible values."

### Part 6 - Confirming the Row Count (6 min)

> "Every one of the last five parts is unproven until this step happens."

- Run `=COUNTA()` on the Invoice ID column before starting (1,025) and again now
- Confirm the result reads exactly 1,000
- Record the before-count, the after-count, and the reason for the difference: 25 duplicates removed, matching exactly what was found in Part 1

> "1,000 rows, matching the number stated on the task sheet. That's not a formality, it's the proof that nothing was silently lost or double-counted along the way."

---

## Final State of the Workbook

A cleaned `RawSales` table, 1,000 rows, with standardised Product line casing, true dates throughout, no stray spaces, the seeded mixed-type example repaired, the 5 negative Quantity rows flagged with a recorded decision, and a documented before/after row count (1,025 to 1,000, 25 duplicates removed). This is the trusted file that Topics 2.4 through 2.6 all build on.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Deleting an impossible value immediately instead of checking whether it could be confirmed and corrected | "Cleaning isn't the same as deleting anything unusual. Flag it if you can't confirm it, don't guess and remove." |
| Running Remove Duplicates without first deciding which columns define a true duplicate | "Two rows can share a name and not be duplicates. Decide the column combination out loud before running the tool, not after." |
| Skipping the row count check under time pressure | "This is the step most people skip when they're rushing, and it's the one that catches every other mistake in this list. Never skip it." |

---

## Up Next

Topic 2.4, Pivot Tables, depends entirely on the accuracy built here: a pivot table only summarises correctly if the data underneath it is correct.
