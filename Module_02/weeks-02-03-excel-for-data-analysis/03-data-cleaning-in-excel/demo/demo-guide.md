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
3. Have the clean 1,000-row answer key (`Ilesanmi_Sales_Clean_AnswerKey.xlsx`) available as your own private reference, not shown to trainees until the row count check at the end. Its Verification sheet holds every figure this demo lands on as a live formula
4. Have a finished, pre-built copy of the fully cleaned file ready as a fallback

> **Instructor note:** this file's numeric columns (Unit price, Quantity, Sales) do not contain a genuine mixed-data-type fault on inspection. To cover that outcome honestly, seed one deliberate example live rather than claiming the file already has one; see Part 4.

---

## Demo Steps

### Part 1 - Finding and Repairing Duplicates (7 min)

> "No formula, pivot table or chart is trustworthy if the data underneath it is wrong. This is where the file becomes reliable, and duplicates are the first problem, because they're the easiest to miss."

- Apply Conditional Formatting, Highlight Cell Rules, Duplicate Values, on the Invoice ID column first, as a visual check before deleting anything: 25 invoices are flagged
- Open Data tab, Remove Duplicates, and stop on the dialog before clicking OK. It opens with **every column ticked**, which is the default nobody reads
- Run it on that default once. 19 rows come out and the file lands on **1,006**. Six duplicated sales are still sitting in a file that now looks clean
- Undo, reopen the dialog, click Unselect All, tick **Invoice ID alone**, and run it again. 25 rows come out and the file lands on exactly **1,000**
- State the decision out loud, in the order a professional actually makes it: "one Invoice ID is one completed sale, so Invoice ID on its own is what defines a duplicate here", and only then click OK
- Explain the six-row gap: of the 25 duplicated Invoice IDs, 19 are exact copies in every column, which is why the default caught those. The other 6 differ in exactly one field each, three by date format, two by Product line casing, and one (`263-10-3913`) by a blank Rating on one of the two rows, so an every-column rule reads them as different transactions

> "Both of those runs are Excel behaving correctly. Only one of them answers the client's question. The column choice, not the tool, is what decided whether six real duplicate sales stayed in this file."

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
- Walk the three-path decision out loud before touching anything. **Correct** it, if the true value can be recovered or confirmed. **Flag** it, if it cannot. **Remove** it, only once it is confirmed as an error with no recoverable value, and that is the path you have to justify in writing
- Test the first path properly instead of assuming it fails. `cogs` and `Unit price` are both intact on all five rows, and this dataset holds `cogs = Unit price × Quantity` exactly on every row, so `cogs ÷ Unit price` recovers the quantity with no guesswork:

| Invoice ID | Shown Quantity | Unit price | cogs | cogs ÷ Unit price | True Quantity |
|---|---|---|---|---|---|
| 875-31-8302 | -1 | ₦9,338.00 | ₦9,338.00 | 9,338 ÷ 9,338 | 1 |
| 200-40-6154 | -6 | ₦6,591.00 | ₦39,546.00 | 39,546 ÷ 6,591 | 6 |
| 134-75-2619 | -7 | ₦1,932.00 | ₦13,524.00 | 13,524 ÷ 1,932 | 7 |
| 827-26-2100 | -9 | ₦3,384.00 | ₦30,456.00 | 30,456 ÷ 3,384 | 9 |
| 499-27-7781 | -8 | ₦5,321.00 | ₦42,568.00 | 42,568 ÷ 5,321 | 8 |

- Land on **Correct**, not Flag: every one of the five divisions returns a whole number matching the magnitude already in the cell, so this is a sign that was flipped, not a quantity that was lost. Build `=[@cogs]/[@[Unit price]]` in a helper column, check the five results, then paste the values into Quantity
- Note that Sales, Tax 5% and cogs were never wrong on these rows, so no total needs recalculating. Only Quantity changes, taking the chain total quantity to 5,510
- Record the decision, the reason and the method in the cleaning record. "Corrected from cogs divided by Unit price" is a sentence a reviewer can check; "looked wrong, fixed it" is not. Had `cogs` been damaged too, the same record would have read "flagged, true value not recoverable from the file"

> "This is the part people get backwards. Flagging is not the safe default, it is the answer you give when the first path genuinely fails. Here it doesn't fail, the file can prove its own answer, and that is why the cleaned dataset holds 1,000 rows and not 995."

**Ask students:** Remove Duplicates was run twice on the same untouched file, once with every column ticked and once on Invoice ID alone, and gave 1,006 rows and 1,000 rows. Nothing else changed. Why?

> "Only the definition of a duplicate changed. Every column ticked means two rows must agree on all seventeen fields, and six of these repeats disagree on exactly one, so they survive. Invoice ID alone matches how the business defines a sale, so all 25 come out. Trimming first would not have changed either number, because Invoice ID itself carries no formatting fault. Cleaning first still matters, for a different and more honest reason: it is what makes those six disguised copies visible to a human scrolling the sheet, and it is what a whole-row rule would need in order to catch them at all. Fix the casing and spacing and an every-column run drops from 1,006 to 1,004; fix the dates as well and it drops to 1,001. It still never reaches 1,000, because only choosing the right column does that."

### Part 6 - Confirming the Row Count, and Renaming the Table (6 min)

> "Every one of the last five parts is unproven until this step happens."

- Run `=COUNTA()` on the Invoice ID column before starting (1,025) and again now
- Confirm the result reads exactly 1,000
- Record the before-count, the after-count, and the reason for the difference: 25 duplicates removed on Invoice ID, matching exactly what was found in Part 1
- Rename the table from `RawSales` to `CleanSales` (Table Design, Table Name) as the last act of the cleaning pass, and say why: from here on every formula names the table it trusts, so a stale reference to the messy file becomes impossible to write by accident
- Add one honest caveat about the 10 blank Ratings, 9 of which survive deduplication. This demo leaves them alone, and leaving them is a defensible choice, but it moves a headline figure: `=COUNTIF(CleanSales[Rating],">=7")` reads 496 with those 9 left blank and 501 once they are filled in from the client's confirmed values, which is what the answer key does. Say which of the two you are reporting, every time

> "1,000 rows, matching the number stated on the task sheet. That's not a formality, it's the proof that nothing was silently lost or double-counted along the way."

---

## Final State of the Workbook

A cleaned table, 1,000 rows, **renamed from `RawSales` to `CleanSales` via Table Design, Table Name**, so that no formula written from here on can silently point at the messy version. It has standardised Product line casing, true dates throughout, no stray spaces, the seeded mixed-type example repaired, the 5 negative Quantity rows corrected from `cogs ÷ Unit price` with the decision recorded, and a documented before/after row count (1,025 to 1,000, 25 duplicates removed on Invoice ID). Its verification figures are ₦32,296,674.90 total Sales, 5,510 total quantity and 0 duplicated Invoice IDs. This is the trusted file that Topics 2.4 through 2.6 all build on, and `CleanSales` is the name they all refer to.

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
