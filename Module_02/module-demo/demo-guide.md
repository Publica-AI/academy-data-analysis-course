# Module Demo Guide - Excel for Data Analysis (Module 2) (Weeks 2 to 3)
**Module 2 | Estimated duration: 70 minutes**

---

## The Story

Adaeze is a junior data analyst at Origin Analytics, a Lagos-based data consultancy. Her firm has just been contracted by Ilesanmi Stores, a three-branch supermarket chain (Ikeja, Wuse and Trans-Amadi) to turn their raw point-of-sale export into a reporting workbook the regional manager can trust ahead of next week's review. The file has arrived exactly as it left the client's system: 1,025 rows, untrimmed, unformatted and unverified.

**What this demo builds:**

- A structured, referenceable sales table with a verified tax calculation (Topic 2.1)
- Formulas that flag customer satisfaction, look up a specific invoice and total sales by branch (Topic 2.2)
- A cleaned, row-count-verified dataset the rest of the workbook can be trusted to sit on (Topic 2.3)
- A multi-dimension pivot table with a working slicer, verified against the source data (Topic 2.4)
- A one-screen dashboard, built from that pivot table, that answers the regional manager's actual question (Topic 2.5)
- A Power Query that reproduces the Topic 2.3 cleaning automatically and refreshes when a new export arrives (Topic 2.6)
- The same three tasks repeated with an AI assistant, and verified against the manual results already built (Topic 2.7)

---

## Prerequisites

1. Excel (any version with PivotTables and Power Query; note where XLOOKUP is unavailable, see instructor note below)
2. The module's raw dataset, `Ilesanmi_Sales_Raw_Export.csv` (1,025 rows), loaded into a fresh workbook
3. A finished fallback workbook, built and tested in advance, covering every stage from Part 1 through Part 7, in case any live step fails
4. Access to a free AI chatbot in a browser tab for Part 7, and Copilot in Excel available for the instructor's machine only

> **Instructor note:** if the training room's Excel does not have XLOOKUP, use INDEX-MATCH instead in Part 2 and say so explicitly, this is a genuine real-world constraint the module already teaches trainees to expect.

---

## Dataset / Project Setup (before the demo starts)

- Load `Ilesanmi_Sales_Raw_Export.csv` into a new workbook before trainees arrive, on a sheet named "Raw Export"
- Confirm it opens at exactly 1,025 rows (=COUNTA on the Invoice ID column, minus the header) before starting
- Have the clean 1,000-row answer key (`Ilesanmi_Sales_Clean_AnswerKey.xlsx`) open in a separate, hidden workbook as your own answer reference, not shown to trainees until Part 3
- Prepare a second, slightly updated copy of the source file for the Part 6 refresh demonstration (a few added rows is enough)

---

## Demo Steps

### Part 1 - The Excel Environment, Tables and Referencing (8 min)

> "Before Adaeze touches a single formula, she needs this raw export behaving like data Excel understands, not just text on a grid. That starts with a table."

- Open the raw export, select any cell inside the data, press Ctrl+T, confirm "My table has headers" is ticked, and rename the table `RawSales`
- Add a calculated column, `Tax Check`, using `=[@[Unit price]]*[@Quantity]*$B$1`, where B1 holds a fixed 5% rate typed once
- Copy the formula down the table and let it auto-fill on its own
- Compare `Tax Check` against the dataset's existing `Tax 5%` column for a handful of rows, they should match

> "That match matters more than it looks. It proves the absolute reference to B1 held steady down every row, while the row-by-row references to Unit price and Quantity shifted correctly. Get that backwards, and every tax figure in this file would be wrong before Adaeze even gets to cleaning it."

### Part 2 - Core Formulas and Functions (10 min)

> "With the table built, Adaeze can start answering real questions about this export, starting with something the regional manager will ask immediately: which customers are unhappy?"

- Build `=IF([@Rating]>=7,"Satisfied","Needs Follow-up")` in a new column, referencing the real Rating column
- Build a small lookup section: type an Invoice ID into a blank cell, then use `=XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])` to pull back its Branch (or `=INDEX-MATCH` if XLOOKUP is unavailable in the room)
- Build `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])` and read the result off the raw table: ₦11,062,565.85
- Repeat for Wuse (₦10,755,627.75) and Trans-Amadi (₦11,338,588.80), a chain total of ₦33,156,782.40, and ask trainees which branch is currently ahead
- Write all four figures on the board and label them "raw, 1,025 rows", because they are about to change

> "Every one of those totals is on the still-messy file, 1,025 rows, duplicates and all. They are arithmetically correct and commercially useless. Adaeze knows the number isn't final yet, which is exactly why the next topic exists."

### Part 3 - Data Cleaning in Excel (10 min)

> "The formulas from Part 2 are only as trustworthy as the data underneath them. Right now, they aren't, because this file has five separate problems hiding in it."

- Highlight duplicates with Conditional Formatting on Invoice ID first, so the room sees 25 duplicated invoices before anything is deleted
- Open Remove Duplicates and stop on the dialog: it opens with every column ticked. Run it that way once and the file lands on 1,006 rows, because only the 19 rows that are exact copies in every column matched. Six duplicated sales are still in there
- Undo, reopen the dialog, tick Invoice ID alone, and run it again: 25 rows come out and the file lands on exactly 1,000. The column choice, not the step order, is what moved the row count
- Fix the 102 rows where Product line is in ALL CAPS with a trailing space, using TRIM followed by PROPER, in that order
- Standardise the 51 remaining DD-MM-YYYY dates using Text to Columns
- Sort Quantity ascending to surface the 5 impossible negative values (-1, -6, -7, -8, -9), then show that `cogs` and `Unit price` survived intact on all five rows, so `cogs ÷ Unit price` recovers the true quantity exactly: 9,338 ÷ 9,338 = 1, 39,546 ÷ 6,591 = 6, 13,524 ÷ 1,932 = 7, 30,456 ÷ 3,384 = 9, 42,568 ÷ 5,321 = 8. Correct them, and record the correction and its reason
- Finish with `=COUNTA` on the Invoice ID column: confirm it now reads exactly 1,000

> "1,000 rows, matching what the client told us to expect. That number is what makes everything built from here, the pivot table, the dashboard, trustworthy enough to put in front of a manager."

**Ask students:** Remove Duplicates was run twice on the same file and gave two different row counts. What changed?

> "The columns ticked in the dialog, nothing else. Every column ticked means two rows have to agree on all seventeen fields to count as duplicates, and six of these repeats disagree on exactly one: three on date format, two on Product line casing, one on a blank Rating. Invoice ID alone is the rule that matches how this business defines a sale, so it catches all 25. Cleaning first still matters, but for a different reason: it is what makes those six disguised copies visible to a human reading the sheet, and what any whole-row rule would need before it could catch them."

> **Instructor note:** this dataset's numeric columns (Unit price, Quantity, Sales) do not contain a genuine mixed-data-type fault. To cover that stated outcome, seed one deliberate example live, type a number into a normally numeric cell with a leading apostrophe so it stores as text, then repair it with `=VALUE()`, exactly as Topic 2.3 teaches. Say plainly that this one is instructor-added, not native to the file.

### Part 4 - Pivot Tables (10 min)

> "This cleaned 1,000-row table can now answer more than one question, without Adaeze writing a single new formula for each one."

- Insert a PivotTable from the cleaned table into a new sheet
- Drag Branch into Rows and Sales into Values, confirm it summarises by Sum, not Count
- Drag Product line into Columns to build a cross-tab, Branch down the side, Product line across the top
- Add a Branch slicer and click through Ikeja, Wuse and Trans-Amadi to show the report responding live
- Verify one total: right-click the Trans-Amadi total and confirm it reads ₦11,056,870.65
- Rebuild the matching SUMIF on the same cleaned table the pivot sits on, not on the raw table from Part 2: `=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])`, which also returns ₦11,056,870.65
- Say plainly why the Part 2 figure for Trans-Amadi was ₦11,338,588.80 and this one is ₦11,056,870.65: they are answers to two different questions, one on 1,025 rows and one on 1,000. A pivot on the cleaned file can only be checked against a SUMIF on the cleaned file

> "Same number, two different routes to get there, on the same 1,000 rows. That match is what makes this pivot table safe to hand over. Checking it against the raw figure from Part 2 would have proved nothing at all."

### Part 5 - Charts and Dashboard Reporting (12 min)

> "The regional manager's actual question is simple: which branch is winning, and on what. A pivot table answers that if you already know how to read it. A dashboard answers it in five seconds."

- From the pivot table, insert a PivotChart: a sorted horizontal bar chart of Sales by Branch, largest at the top, confirming Trans-Amadi leads
- Build a second chart: total Sales by Product line, and point out Food and beverages leads at ₦5,614,484.40, closely followed by Sports and travel at ₦5,512,282.65, close enough that a bar chart, not a pie chart, is the right call
- Add a pie chart of Payment method share (Ewallet 345, Cash 344, Credit card 311) to show the three methods are used almost equally
- Move all three charts, plus the Branch slicer, onto a single dedicated dashboard sheet, gridlines hidden, aligned to a grid
- Connect the slicer to all three charts using Report Connections, then click through it live

> "Watch what happens when I click Trans-Amadi." [click the slicer] "Every chart on this screen just answered the same question from a different angle, without touching a single formula."

### Part 6 - Power Query (10 min)

> "Adaeze is going to get a fresh export from this client every month. She is not doing Part 3 by hand five times."

- From the raw table, Data tab, From Table/Range, to open the Power Query Editor
- Add the same cleaning steps from Part 3 as query steps: Trim on Product line, a capitalisation fix, a date standardisation step, and Remove Duplicates
- Repeat the Part 3 trap in query form: run Remove Duplicates across every column and load it, giving 1,006 rows. Change that one step to Invoice ID alone, reload, and land on exactly 1,000
- Show that step order moves the whole-row count without ever fixing it: a whole-row Remove Duplicates above the Trim and capitalisation steps gives 1,006, below them 1,004, and below the date step as well 1,001. Invoice ID alone gives 1,000 wherever it sits
- Close & Load into a new table named `CleanSales`, then swap in the prepared updated source file and click Refresh All, watching the row count update automatically

> "Two lessons in one pane. Order matters, and you just watched it move a number three times. The column choice matters more, and it was the only thing that ever reached 1,000. Excel now remembers both, forever. Next month's file goes through the exact same steps with one click."

### Part 7 - AI-Augmented Excel (10 min)

> "Everything so far, Adaeze built and checked by hand. That is exactly what makes the next fifteen minutes useful instead of risky."

- In a free AI chatbot, prompt: "Write an Excel IF formula that returns Satisfied if the Rating in column J is 7 or above, and Needs Follow-up otherwise." Paste the result next to the manual version from Part 2, confirm they agree
- Prompt the AI to explain a nested INDEX-MATCH-inside-IF formula built from Product line, Customer type and Unit price, and check the explanation is actually correct
- Ask the AI for the total Sales for the Ikeja branch on the cleaned file, then verify it against `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])`, which returns ₦10,620,037.05; if the AI's prompt was vague about branch spelling, deliberately show a mismatch and correct it live
- Instructor only: open Copilot in Excel, select the Sales column, and ask it the same Ikeja branch question, showing the same answer arriving without any copy-pasting

> "Notice that last step used the exact same verification habit as everything before it. Copilot is a faster window, not a different kind of trust."

---

## Demo Wrap-Up

The finished workbook now gives the regional manager a self-service report built from a single trusted source file.

| Feature / capability | Topic it came from | What it shows |
|---|---|---|
| Structured table with a verified tax formula | 2.1 | The raw export behaves like real data, and the tax figures check out |
| Satisfaction flag, invoice lookup, branch totals | 2.2 | Individual questions answered instantly from the table |
| 1,000-row cleaned, row-count-verified dataset | 2.3 | Everything downstream can be trusted |
| Cross-tab pivot table with a working slicer | 2.4 | Sales sliced by Branch and Product line on demand |
| One-screen dashboard | 2.5 | The manager's question answered at a glance, no scrolling |
| Refreshable Power Query | 2.6 | Next month's export cleans itself in one click |
| AI-verified formulas and Copilot demonstration | 2.7 | The same answers, reached faster, still checked by hand |

> "Adaeze didn't just clean a spreadsheet today. She built a report the client can reopen every month, drop in a new export, and trust without re-checking her work from scratch. That is the job."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| Forgetting the `$` in the Part 1 tax formula, so it breaks partway down the table | "This is the exact mistake Topic 2.1 warns about, a reference that should have stayed fixed moved instead. Press F4 on the cell reference and it locks correctly." |
| Building the Part 4 pivot table from a plain range instead of the structured table, so it does not include new rows automatically | "This is one of Topic 2.4's named common mistakes. Always build from the table, not the range, so nothing needs rebuilding later." |
| Refreshing the Part 6 query and assuming the new row count is correct without checking it | "Topic 2.6 is explicit about this: a refresh reruns the steps, it doesn't guarantee the result. Always check the row count and a spot value, the same habit from Topic 2.3, just applied to an automated process." |
