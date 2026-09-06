# Demo Guide - Power Query
**Module 2, Topic 2.6 | Estimated duration: 28-32 minutes**

---

## What This Demo Teaches

- Import data through Power Query, both from a table already in the workbook and from an external file
- Apply transformation steps in Power Query that mirror the manual cleaning judgement from Topic 2.3
- Reorder steps when they were applied in the wrong sequence, and confirm the result in the preview grid
- Refresh a query when the source file changes, and verify the result before trusting it

---

## Setup - Before the Demo Starts

1. Open the structured, still-raw `RawSales` table (1,025 rows) from Topic 2.1, kept separately from the already-cleaned file used in Topics 2.4-2.5
2. Prepare a second, slightly updated copy of the raw export in advance, with a few extra rows added, for the Part 3 refresh demonstration
3. Have a finished, pre-built copy of the completed query, loaded and refreshed, ready as a fallback

> **Instructor note:** ask trainees directly how long the Topic 2.3 manual cleaning lab took them before starting Part 1. The contrast with what is about to happen in seconds here is the entire motivation for this topic; let it land before touching any buttons.

---

## Demo Steps

### Part 1 - Importing Data: From Table and From File (7 min)

> "This isn't a new set of cleaning rules. It's the same duplicate, format and stray-space checks from 2.3, done once and remembered by Excel forever."

- Click inside the structured `RawSales` table, Data tab, From Table/Range, and let the Power Query Editor open with that data already loaded
- Point out the three zones: the preview grid in the centre, the Applied Steps pane on the right, and the ribbon at the top, and state plainly that nothing here changes the original file until Close & Load is clicked
- If a second file is available, also demonstrate Data tab, Get Data, From File, From Text/CSV, browsing to the updated export, to show the difference between starting from a table already in the workbook and pulling in an external file

> "Starting from a table matters for one specific reason: new rows added later get picked up automatically on refresh. Starting from a plain range doesn't give you that."

### Part 2 - Applying and Reordering Transformation Steps (10 min)

> "Every one of these tools has a direct match to something already built by hand in 2.3. I'm going to name that match out loud as we go."

- Transform tab, Format, Trim, on the Product line column: "this is exactly the TRIM formula from 2.2 and 2.3, just applied to the whole column at once, forever"
- Add a capitalisation step to fix the ALL CAPS entries
- Select every column, Home tab, Remove Duplicates, deliberately taking the whole-row route first. Load it and read the count: **1,006**, exactly as Excel's own dialog produced in Topic 2.3, and for the same reason
- Delete that step. Right-click the Invoice ID column alone, Remove Duplicates, reload, and confirm the count reads exactly **1,000**. Narrate the same judgement from 2.3: the column that defines a duplicate is the decision, and the tool only carries it out
- Now show the honest step-order lesson on the whole-row route, since it is the one where order genuinely bites. Drag the whole-row Remove Duplicates back in and move it above the Trim and capitalisation steps: **1,006**. Drag it below them: **1,004**, because the two casing-mismatched pairs have collapsed into each other. Add the date standardisation above it as well: **1,001**. It never reaches 1,000, whatever the order
- Say what that proves: cleaning first genuinely improves a whole-row rule, 1,006 to 1,004 to 1,001, and still does not get the right answer. Choosing Invoice ID does, first time, in any order

> "Same lesson as Topic 2.3, and notice which half of it is which. Step order is real, and it moved that count twice. But it never once got us to 1,000. Only naming the right column did that. The difference here is that Excel remembers both the column choice and the order forever, instead of us redoing them by hand next month."

### Part 3 - Loading and Refreshing (10 min)

> "This step is what actually makes Power Query worth learning, not the cleaning itself, but what happens when a new file lands."

- Home tab, Close & Load, sending the finished query to a new worksheet as a table, and rename that loaded table `CleanSales` so it matches the name Topics 2.3 to 2.5 already use for the trusted 1,000-row data
- Point out explicitly that this loaded table can feed a PivotTable exactly as covered in Topic 2.4, nothing about pivoting changes because the data came from a query
- Swap in the prepared updated source file, Data tab, Refresh All, and watch the row count update automatically as the same five steps rerun against the new file
- Check the new row count against what is expected, and spot-check two or three values against the updated source file to confirm the transformation steps still applied correctly
- Spot-check one figure that is easy to hold in your head as well as the row count: on the unmodified export, the loaded `CleanSales` table totals ₦32,296,674.90 in Sales, so any refresh that lands on that figure with more rows than 1,000 has gone wrong somewhere the row count alone would not show

> "Watch that. The exact same five steps, Trim, capitalise, deduplicate, in the right order, just ran themselves against a brand new file. That's the entire point of this topic."

**Ask students:** after a refresh produces a row count that doesn't match expectations, what should happen next?

> "Reopen the query and check the Applied Steps in order, the same way we'd investigate a manual cleaning pass that came out wrong. A refresh reruns the steps, it doesn't guarantee the result, it just changes what needs checking, the process instead of every individual value."

---

## Final State of the Workbook

A Power Query, built from the structured `RawSales` table (1,025 rows), with Applied Steps in the order Trim, capitalise, standardise dates, Remove Duplicates **on Invoice ID**, loaded into a new 1,000-row table named `CleanSales` and refreshed once against an updated source file with the new row count verified. On the unmodified export it reproduces the Topic 2.3 figures exactly: 1,000 rows and ₦32,296,674.90 in total Sales. This query, and the table it produces, is what the module's AI-augmented topic checks its own AI-generated cleaning suggestions against next.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Applying steps in an order that produces a subtly wrong result, without checking the final preview carefully | "The preview grid is there for exactly this reason. Check it after every step that could plausibly change the row count, not just at the end." |
| Deleting a step without checking whether a later step depends on it | "Excel will usually throw an error rather than fail silently here, that's a good thing. Read the error, it tells you exactly what broke." |
| Assuming a refresh worked correctly without checking the row count or a few sample values | "This is named directly in the topic's common mistakes. A refresh reruns the steps, it does not guarantee the result, always check." |

---

## Up Next

Topic 2.7, AI-Augmented Excel, is the final topic in the module. Everything covered so far, formulas, cleaning, pivot tables, charts and now Power Query, has been done entirely by hand, and that was deliberate: it's what makes it possible to judge whether an AI assistant's answer is right.
