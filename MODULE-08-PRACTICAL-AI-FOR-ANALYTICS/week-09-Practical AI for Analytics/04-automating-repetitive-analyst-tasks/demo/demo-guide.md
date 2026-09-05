# Demo Guide - Automating Repetitive Analyst Tasks
**Module 8, Topic 8.4 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Separating the parts of a recurring task that are genuinely automatable from the parts that are not
- Writing the four rules that decide whether an automation survives next quarter's file
- Turning a manual monthly report into a script that takes the file as an argument
- Proving an automation survives a refresh by testing it against a changed file, not by hoping
- Making a broken refresh fail loudly instead of publishing a confident wrong report
- Using an AI assistant to draft the boring parts while you own the rules

---

## Setup - Before the Demo Starts

1. `swiftroute_q3_raw.xlsx` in this folder
2. `monthly_report.py` and `test_refresh.py` in this folder, as the worked solution and the fallback
3. Run `python test_refresh.py` once before the session. It should print eleven checks and "The report follows the file. It survives a refresh."
4. A free-tier AI assistant open in a browser tab
5. Python with pandas and openpyxl available

> **Instructor note:** set the bar explicitly at the top. This is not a software engineering topic. The standard is "survives a data refresh", not "production pipeline". Trainees who think they are being asked to build infrastructure will disengage.

> **Instructor note:** Part 4 shows a bug that was genuinely in the first version of this script. Deliver it as that, not as a contrived example. Watching a real fault get caught by a test is the point.

---

## Demo Steps

### Part 1 - Which Parts Are Actually Automatable (8 min)

> "Adaeze wants this delivery report every quarter. Before writing anything, split the job into steps and mark each one."

**On the board, list the steps and take a verdict on each from the room.**

| Step | Automatable |
|---|---|
| Open the export and remove duplicate delivery ids | Yes, it is a rule |
| Parse the dates, whatever shape they arrive in | Yes, the five formats are known |
| Standardise route codes before joining | Yes, it is a pattern |
| Total deliveries and revenue by month | Yes |
| Decide whether an unusual month is a data fault or a real event | No |
| Write the sentence that tells Adaeze what to do | No |

> "The line falls in the same place every time. Anything that is a rule, automate. Anything that is a judgement, keep. If you automate a judgement you have not saved time, you have hidden a decision."

---

### Part 2 - The Four Rules (8 min)

> "Four rules, and every one of them exists because somebody's automation broke on the four rules."

1. **The file path is an argument, never a constant.** A path buried in line forty means next quarter someone edits code to run a report, and that person will be you at eleven at night.
2. **Periods come from the data, never hardcoded.** The moment you type `["Jul", "Aug", "Sep"]` your script has an expiry date.
3. **Standardise before you join.** `LAG07` and `LAG-07` are different strings, and a join drops the mismatches without a word.
4. **Assert what you expect.** Row counts, totals, coverage. An automation that cannot fail is an automation that publishes wrong numbers quietly.

---

### Part 3 - Build It, With the Assistant Doing the Typing (10 min)

**Prompt the assistant:**

> "Write a Python function that reads an Excel sheet of deliveries, removes duplicate delivery_id rows keeping the first, parses a date column that may be in any of these five formats, converts a fee column written as ₦45,320 to an integer, and standardises route codes so LAG07 becomes LAG-07. Take the file path as an argument."

**Paste the answer in. Read it aloud before running it.**

> "Read the date handling. Most assistants reach for a general parser here, because it is shorter and it usually works. Usually. On `03-08-2026` it decides for you, and it does not tell you which way it decided. I am replacing that with the five named formats, tried in order."

> "This is the division of labour that actually works. It writes the boring parts fast, and I own every rule that decides what the numbers mean."

**Run it on the Q3 file.**

```
periods found     2026-07 to 2026-09 (3)
rows read         3640
duplicates removed 40
deliveries counted 3598
revenue            N12,191,640
internal checks passed
```

---

### Part 4 - The Bug the Test Caught (10 min)

> "The first version of this script did not print three periods. It printed five, running from July 2026 to February 2027."

**Show why: the reporting window was taken from the minimum and maximum parsed date, and two rows in this file are dated 2027.**

> "Two rows out of three thousand six hundred, and the entire report changed shape. No error, no warning. The code was correct. The window was not."

**Show the fix, and note that it is data derived rather than hardcoded:**

> "A month holding less than one per cent of the dated rows is not a reporting period, it is a data quality signal. It gets excluded from the totals and reported as its own line. That rule works on this file and it will still work on a file with different months in it, which is the whole test."

**Ask students:** "Why not just filter to July, August and September?"

> "Because that is rule two, broken. It would fix this quarter and silently produce an empty report next quarter."

---

### Part 5 - Proving It Survives (8 min)

> "Everything so far is a claim. Here is the proof."

**Run `test_refresh.py` and narrate what it manufactures.**

It builds a plausible next-quarter file from the Q3 workbook, changing everything a real refresh changes: every date moves forward one quarter, a brand new route OYO-04 appears, forty LAG-01 rows arrive as LAG01 without the hyphen, two hundred rows are removed so no total can be reused, and the column order is shuffled because exports do that.

**Then it runs the report against both files and checks eleven things, including these four:**

| Check | Why it matters |
|---|---|
| Periods followed the data, not a constant | Rule 2 |
| New route OYO-04 reached the report | The script does not have a fixed route list |
| No unhyphenated LAG01 survived cleaning | Rule 3, and the join stayed whole |
| Totals were recomputed, not copied | Nothing was carried over from last quarter |

> "Eleven checks, eleven passing. That sentence, and not my confidence, is what makes this safe to hand over."

---

## Final State of the Automation

`monthly_report.py`, which takes any workbook with the same three sheets and writes `report_<first-period>_to_<last-period>.md` and `.xlsx`. `test_refresh.py`, which manufactures a changed file and proves the report follows it. Both run from the command line with no editing.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| The script works on Q3 and produces an empty report on the test file | "A month or a route has been hardcoded somewhere. Search the file for a month name or a route code in quotes." |
| Reported period range runs into 2027 | "The window is being taken from min and max date, and two rows are dated 2027. Derive the window from where the rows actually are." |
| The join loses rows after the refresh | "Route codes were standardised after the join instead of before it. Rule three, in the wrong order." |
| A trainee automates the interpretation as well | "Ask which line of the output a human would be accountable for. That line stays human." |
| The assistant's date parsing is accepted as written | "Ask it what its parser does with 03-08-2026, then ask it to prove the answer against the file." |
| The refresh test fails on the new route check | "The report's markdown lists only the busiest five routes. Check the full route table in the workbook, not the summary." |

---

## Up Next

Topic 8.5 - Limits, Risks and the Verification Checklist. You have automated the parts that are rules. The last topic is about the failure that survives every rule you can write: an answer that is correct, confident and completely wrong.
