# Demo Guide - AI-Augmented Excel
**Module 2, Topic 2.7 | Estimated duration: 33-37 minutes**

---

## What This Demo Teaches

- Use an AI assistant to generate formulas and Power Query logic from a plain-English description
- Use an AI assistant to explain an unfamiliar formula or set of query steps
- Use an AI assistant to debug a broken formula
- Verify every AI-generated result against a known total before trusting or sharing it
- Describe what Copilot in Excel adds when an employer provides it

---

## Setup - Before the Demo Starts

1. Carry forward the cleaned 1,000-row `CleanSales` table and the verified formulas built across Topics 2.2-2.6
2. Open a free AI chatbot in a browser tab, ready to use
3. Confirm Copilot in Excel is available on the instructor's machine only, per the module's teaching notes; trainees are not expected to have hands-on access
4. Have a finished, pre-built copy of the workbook with every verification step in this guide already completed, as a fallback

> **Instructor note:** this is the final topic in the module for a deliberate reason. Open by naming that sequencing directly: AI is genuinely useful here only because trainees can already build a formula, a pivot table and a query by hand, and can therefore tell whether an AI's answer is right.

---

## Demo Steps

### Part 1 - Writing a Good Prompt and Generating a Formula (8 min)

> "An AI assistant in a separate browser tab cannot see this workbook. It only knows what we type or paste in. That single fact explains almost every bad result trainees will get from this if they rush the prompt."

- Type a deliberately vague prompt first: "write me a formula for ratings", and show the vague or generic result that comes back
- Rewrite it properly, naming the actual column and its location: "write an Excel IF formula that returns Satisfied if the Rating in column J is 7 or above, and Needs Follow-up otherwise", and compare the two results side by side
- Paste the generated formula into the worksheet and run it against the real Rating column
- Compare it directly against the manually built IF formula from Topic 2.2 on the same column, confirming they agree

> "That comparison is only possible because we already know the correct answer from Topic 2.2. That's the whole design of this topic: reuse a task already solved by hand, so a wrong AI answer is obvious immediately, not just plausible."

### Part 2 - Explaining an Unfamiliar Formula (6 min)

> "This is a genuine day-one-on-the-job scenario: opening a colleague's file with no documentation and needing to understand it fast."

- Build, or paste in, a nested formula combining INDEX-MATCH and IF across the real Product line, Customer type and Unit price columns
- Paste it into the AI chat and ask what it does and why
- Ask a plain-English explanation first, then ask what would happen if a specific input changed, for example if Customer type changed from Member to Normal
- Test the AI's prediction live by actually changing that input and checking the result

> "Asking for an explanation is only half the exercise. Testing its prediction against what the sheet actually does is the half that catches a wrong explanation."

### Part 3 - Debugging a Broken Formula (6 min)

> "Same discipline as Topic 2.2's common mistakes, just handed to an AI to diagnose first."

- Build a VLOOKUP meant to return Unit price for a given Product line, deliberately leaving out FALSE as the last argument, and let it return a wrong approximate-match result rather than an obvious error
- Paste the broken formula, a description of the intended result, and the wrong output into the AI chat, and ask what's wrong
- Read the AI's suggested fix, which should point to the missing FALSE argument
- Apply the fix and test it on the actual data before trusting it, confirming the corrected result now matches the expected Unit price

> "Notice the AI recognised something already named as a common mistake back in Topic 2.2. It didn't discover anything new, it just confirmed and sped up a diagnosis that could have been made manually."

### Part 4 - Verifying AI Output Against Known Totals: Worked Example (8 min)

> "Everything before this step was speed. This step is the one that decides whether any of it can be trusted."

- State the scenario aloud: "Total Sales for the Ikeja branch only, from the cleaned `CleanSales` table"
- Prompt the AI, naming the Branch and Sales columns and the condition explicitly, and note the figure it returns
- Build the manual check independently: `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])`, which should return ₦10,620,037.05
- If a trainee's figure comes back as ₦11,062,565.85 instead, do not treat it as an AI failure. That is the same formula run against the raw 1,025-row export, and it is the single most common way this check goes wrong: the formula was right and the table was not
- If the two figures agree, confirm the AI result is trustworthy for this task; if a mismatch was engineered on purpose, for example by leaving the AI's prompt ambiguous about Branch spelling, investigate it live: wrong range, wrong branch spelling, or wrong column, and correct it

> "If an AI-generated result and a manually calculated known total disagree, the manual calculation is trusted, and the AI result gets investigated, never the other way round."

**Ask students:** what "known total" would you check an AI-generated summary of Product line sales against, before trusting it?

> "The same SUMIF pattern, or the pivot table total already verified in Topic 2.4. The specific check changes, the habit of checking something already known doesn't."

### Part 5 - AI for Power Query Logic, and the Copilot Demonstration (7 min)

> "Same approach, just applied to transformation steps instead of a single formula."

- Describe a transformation in plain English to the AI: "remove rows where Invoice ID is duplicated, and standardise Product line to normal capitalisation", and ask which Power Query tools to use, and in what order
- Compare its suggestion against the Topic 2.6 lesson, and check specifically whether it names **which column defines a duplicate**. An answer that says "Remove Duplicates" without naming Invoice ID will produce 1,006 rows on this file, not 1,000, and will look perfectly reasonable while doing it
- Run the suggested steps and check the row count reads exactly 1,000 before trusting any of it
- Instructor only: open Copilot in Excel, select the Sales column, and ask it the same Ikeja branch total question from Part 4, showing the same figure arriving without any copy-pasting between windows
- Name the difference explicitly: Copilot can see the selected data directly inside the workbook; a free chatbot cannot see anything that isn't typed or pasted in; the verification discipline needed is identical either way

> "Same workflow, different window. That's deliberate framing, not an understatement. Convenience is the only real difference here, and convenience is not the same as trustworthiness."

---

## Final State of the Workbook

The cleaned dataset from Topics 2.3-2.6, with an AI-generated and verified Satisfaction formula, an AI-explained nested INDEX-MATCH-IF formula with a tested prediction, a debugged VLOOKUP with its fix applied and confirmed, and a documented Ikeja branch total (₦10,620,037.05) matching between an AI-generated formula and a manual `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])`. This is the final state of the module's running workbook.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Pasting an AI-generated formula straight into the real file without testing it first | "This is named directly in this topic's common mistakes. Test it against the same dataset before it goes anywhere near a shared file." |
| Writing a vague prompt and accepting whatever comes back | "Compare it to the vague-versus-specific prompt from Part 1. Name the actual columns and the expected result, every time." |
| Trusting a confident-sounding AI explanation without checking it produces the correct result | "Confident tone is not a signal of accuracy. A wrong answer sounds exactly like a right one. That's the entire reason Part 4 exists." |

---

## Up Next

Module 2 closes with the **Block 1 mini-assessment**, which covers Modules 1 and 2 together rather than this module alone, per the programme's Module and Topic Breakdown. Tell trainees that plainly at the end of this session: the verification habit practised here, and the AI-use rules from Module 1, are assessed as one thing, because in the job they are one thing.

> **Instructor note:** the programme team should confirm the mini-assessment's date and format (online quiz, practical, or both) before this session runs, so the closing line can name them.
