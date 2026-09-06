# Demo Guide - Core Formulas and Functions
**Module 2, Topic 2.2 | Estimated duration: 33-37 minutes**

---

## What This Demo Teaches

- Build solutions using logical functions (IF, IFS)
- Build solutions using lookup functions (VLOOKUP, XLOOKUP, INDEX-MATCH), and know when to reach for which
- Build solutions using text functions (TRIM, LEFT, TEXTSPLIT)
- Build solutions using date and aggregate functions (TODAY, DATEDIF, SUM, AVERAGE, COUNT, COUNTIF, SUMIF)
- Choose the appropriate function family for a stated problem, before writing any formula

---

## Setup - Before the Demo Starts

1. Carry forward the `RawSales` table built in Topic 2.1, with its Subtotal and Tax Check columns already in place
2. Confirm the Rating column is visible and the real values (4 to 10, with 501 of the 1,000 clean rows rated 7 or above) are ready to reference
3. Have a finished, pre-built copy of the workbook with every formula in this guide already working, as a fallback

> **Instructor note:** if the training room's Excel does not include XLOOKUP or TEXTSPLIT, say so plainly during Parts 2 and 3 and demonstrate INDEX-MATCH as the reliable fallback; both functions genuinely are missing from some real workplace installations, this is not a hypothetical caveat.

---

## Demo Steps

### Part 1 - Logical Functions: IF and IFS (6 min)

> "First question: am I making a decision here? If yes, that's a logical function, and the simplest one is IF."

- Build `=IF([@Rating]>=7,"Satisfied","Needs Follow-up")` against the real Rating column
- Add a third band live to force the point: rewrite it as a nested IF and let the formula visibly get harder to read
- Rebuild the same rule as `=IFS([@Rating]>=8,"Highly Satisfied",[@Rating]>=7,"Satisfied",TRUE,"Needs Follow-up")`

> "Feel the difference there. IFS didn't just add a feature, it made the formula something the next person can actually read."

### Part 2 - Lookup Functions: VLOOKUP, XLOOKUP, INDEX-MATCH (10 min)

> "Same job, three tools. I want you to feel why we have three, not just be told."

- Using a lookup cell containing a real Invoice ID (`351-62-0822`), build `=VLOOKUP(F1,RawSales[#All],2,FALSE)` to pull back its Branch (Wuse); leave FALSE out once first to show the wrong approximate-match result, then add it back
- Rebuild the same lookup with `=XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])`, noting it defaults to an exact match with no FALSE argument needed
- Build the same result a third way with `=INDEX(RawSales[Branch],MATCH(F1,RawSales[Invoice ID],0))`, first showing the MATCH position number alone in a helper column, then wrapping it in INDEX and deleting the helper

> "All three just returned Wuse. The difference isn't the answer, it's which one still works in five years, on an older machine, or when someone inserts a column."

### Part 3 - Text Functions: TRIM, LEFT, TEXTSPLIT (6 min)

> "This is a direct callback to the lookups we just built. A stray space is one of the most common reasons one of those breaks even when the value looks correct."

- Show two Product line values that look identical on screen, run `=LEN()` on both, and let the differing character counts reveal a hidden trailing space
- Fix it with `=TRIM([@[Product line]])`
- Build `=LEFT([@[Invoice ID]],3)` to pull the first three characters of a real Invoice ID (for example, 750 from 750-67-8428)
- Build `=TEXTSPLIT([@[Invoice ID]],"-")` on the same column and let the room watch it spill automatically into three neighbouring cells

> "Nobody copied that formula three times. It spilled on its own. That's new behaviour if you haven't met it before, and it's worth pausing on."

### Part 4 - Date and Aggregate Functions (6 min)

> "Now we summarise across rows instead of working row by row."

- Build `=TODAY()` in a blank cell and note it updates automatically
- Build `=DATEDIF([@Date],TODAY(),"d")` against the real Date column to get days since each transaction
- Build the plain aggregates first: `=SUM(RawSales[Sales])` (₦33,156,782.40), `=AVERAGE(RawSales[Rating])` (6.97) and `=COUNT(RawSales[Sales])` (1,025)
- Introduce the conditional versions as "the same idea, but only counting rows that match a rule": `=COUNTIF(RawSales[Rating],">=7")` returns 508, and `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])` returns ₦11,062,565.85
- Say the reason for those two figures out loud: `RawSales` is still the 1,025-row export. The same `=COUNTIF(RawSales[Rating],">=7")` returns 508 here and 501 on the cleaned table in Topic 2.3, and only the 501 is reportable. The gap is not a rounding difference: 12 of the 25 duplicated rows were rated 7 or above and come out, and 5 of the 9 restored blank Ratings turn out to be 7 or above and go in, so 508 minus 12 plus 5 is 501

### Part 5 - Choosing the Right Function: Worked Example (7 min)

> "Last piece: reading a plain-English problem and picking the family before typing anything."

- State the problem out loud: "Flag anyone whose Product line entry has extra spaces, then find each row's satisfaction band, then confirm how many rows fall in each band"
- Step 1: `=TRIM([@[Product line]])<>[@[Product line]]` to flag formatting issues (text function)
- Step 2: the IFS satisfaction formula from Part 1 (logical function)
- Step 3: `=COUNTIF()` on the satisfaction column, checked against this file's own total row count of 1,025 (aggregate function), since the bands have to account for every row in `RawSales`

**Ask students:** which function family would you reach for if the question was "how many Health and beauty transactions happened in the Wuse branch?"

> "Aggregate, specifically a conditional one, but notice it needs two conditions at once. That's a preview of COUNTIFS and SUMIFS, which sit just past what this topic covers, worth knowing they exist."

---

## Final State of the Workbook

`RawSales` table with Subtotal and Tax Check (from 2.1) plus: a Satisfaction Band column (IFS), a Branch-lookup demonstration cell (VLOOKUP/XLOOKUP/INDEX-MATCH), a trimmed Product line check column, an Invoice ID prefix and split columns (LEFT/TEXTSPLIT), a Days Since Transaction column (DATEDIF), and verified SUM/AVERAGE/COUNT/COUNTIF/SUMIF summary cells. This is still the raw 1,025-row file, so its summary cells read ₦33,156,782.40 total Sales, 508 transactions rated 7 or above and ₦11,062,565.85 for Ikeja. Cleaning happens next, and every one of those three figures moves.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Forgetting FALSE in VLOOKUP and getting a silently wrong approximate match | "This is named directly in the topic's common mistakes. No error message, just a wrong answer, which is exactly why we always check against something known." |
| Nesting three or four IF statements instead of switching to IFS | "Technically it'll work, but ask yourself if you could read this in six months. That readability cost is the whole reason IFS exists." |
| Using SUM or COUNT when the question actually needed a conditional version | "Reread the question. If it names a condition, Branch equals Ikeja, Rating above 7, you need the IF-suffixed version." |

---

## Up Next

Topic 2.3, Data Cleaning in Excel, leans directly on the TRIM habit just practised, since the file being cleaned next is the same one just built formulas on, still messy, still 1,025 rows.
