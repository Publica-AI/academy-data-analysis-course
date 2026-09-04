# Demo Guide - The Excel Environment, Tables and Referencing
**Module 2, Topic 2.1 | Estimated duration: 28-32 minutes**

---

## What This Demo Teaches

- Navigate the Excel interface confidently: Ribbon, Formula Bar, Name Box, Sheet tabs, Status bar
- Convert a raw range of data into a structured table using Ctrl+T
- Use relative references for formulas that should shift down a column
- Use absolute references, locked with $, for formulas that should always point to the same cell
- Use F4 to switch between reference types without typing dollar signs manually

---

## Setup - Before the Demo Starts

1. Open the raw supermarket sales export (`supermarket_sales_dirty.csv`, 1,025 rows) in a fresh workbook, as a plain range, not yet a table
2. Confirm the file opens with the header row intact and no table formatting applied yet, so Ctrl+T has a genuine effect to demonstrate
3. Have a finished, pre-built copy of the table with both reference-type columns already added, ready as a fallback if any live step fails

> **Instructor note:** use the full 1,025-row file for the Ctrl+End and Ctrl+Arrow demonstrations specifically. A 10-row sample will not produce a convincing jump; this needs to feel dramatic.

---

## Demo Steps

### Part 1 - Navigating the Interface (5 min)

> "Before we touch a single formula, I want everyone comfortable just sitting inside this file. This isn't about memorising menus, it's about not freezing the first time you open someone else's workbook."

- Point to the Ribbon, Formula Bar, Name Box, worksheet grid, sheet tabs and Status bar in turn, clicking into a cell so the Formula Bar and Name Box visibly update together
- Select a column of numbers (Sales) and let the Status bar's instant sum, count and average appear at the bottom right
- Demonstrate Ctrl+Home, then Ctrl+End on the 1,025-row file, then Ctrl+Arrow down a column

> "That jump to the very last row, in one keystroke, on a file this size, is the entire point. Anyone who has scrolled a 1,000-row sheet by hand knows exactly how much time that shortcut saves."

### Part 2 - Building a Structured Table (8 min)

> "Right now this is just cells with data in them. Excel doesn't know it's one connected dataset. That's what we fix next."

- Click any cell inside the raw data, press Ctrl+T, and pause deliberately on the "My table has headers" checkbox before confirming
- Rename the table from Table1 to `RawSales` via Table Design, Table Name
- Type a new row directly beneath the last row of the table and let the room watch the table border auto-expand and formatting apply on its own, without narrating it first

> "Nobody told Excel to do that. That's the entire benefit of a structured table over a plain range: it knows its own boundaries."

### Part 3 - Relative References (6 min)

> "Every formula from here is really just an address book. The interesting part is what happens when we copy one."

- Build `=[@[Unit price]]*[@Quantity]` as a Subtotal column, referencing the real Unit price and Quantity columns
- Fill it down using the table's auto-fill behaviour and click into a few different rows so trainees see the reference shift in the Formula Bar themselves
- Name this explicitly: "no dollar signs, this is the default, and it's exactly what you've probably already done without knowing the term for it"

### Part 4 - Absolute References and F4 (10 min)

> "Now I want to break something on purpose, because seeing this fail is the fastest way to understand why the fix matters."

- Type a fixed 5% rate into cell B1, label it "Tax rate"
- Build `=Subtotal*B1` in the first row and copy it down without locking the reference; let trainees see the result go wrong or blank as B1 shifts to B2, B3, empty cells
- Fix it live: select B1 in the formula, press F4 once to get `$B$1`, and copy down again to show every row now correctly referencing the same fixed cell
- Compare the corrected column against the dataset's real `Tax 5%` column for a handful of rows; they should match

> "That match is the whole lesson. Wrong reference type doesn't throw an error most of the time, it just quietly gives you the wrong number. The only way to catch that is to check it against something you already know is correct."

**Ask students:** what would happen if we used F4 three times instead of once on that B1 reference?

> "You'd land on A$1, a mixed reference, locking the row but not the column. Worth knowing it exists, but this topic only needs you comfortable with F4 getting you to a fully locked $B$1 and back."

---

## Final State of the Workbook

`RawSales` table (1,025 rows) with two new columns: Subtotal (relative reference, `=[@[Unit price]]*[@Quantity]`) and a verified Tax Check column (`=Subtotal*$B$1`, matching the dataset's real Tax 5% column). This table carries forward into Topic 2.2 as the file trainees build their formulas on.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Rushing past the "My table has headers" checkbox and getting Column1, Column2 headers instead of real ones | "This is the single most common Ctrl+T mistake. Undo, redo it, and actually read the dialog box before confirming." |
| Forgetting the $ before copying the tax formula down, so later rows go blank or error | "This is exactly the mistake Topic 2.1 warns about by name. Select the reference in the Formula Bar and press F4, don't retype it." |
| Over-locking with $ on the Unit price or Quantity reference, so the Subtotal formula stops shifting down the rows at all | "Only lock what genuinely shouldn't move. If a value is meant to change every row, it needs to stay relative." |

---

## Up Next

Topic 2.2, Core Formulas and Functions, builds directly on the table and reference habits practised here, every formula from this point is typed once and copied down using exactly what was just demonstrated.
