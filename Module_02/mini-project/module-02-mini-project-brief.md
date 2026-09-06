# Module 2 Mini Project: The Ilesanmi Stores Quarterly Report

**Module 2, Excel for Data Analysis (Weeks 2 to 3) | LMS practice slot | Expected effort: 3 to 5 hours**

---

## 1. Business scenario

Ilesanmi Retail Limited, trading as **Ilesanmi Stores**, runs three supermarkets: Ikeja in Lagos,
Wuse in Abuja and Trans-Amadi in Port Harcourt. The regional manager has asked Origin Analytics, the
Lagos consultancy where you work, for a single workbook she can open at the start of each quarter to
see how the three branches are performing and where to put next quarter's stock budget.

She has sent one file: the point-of-sale export for January to March 2019, exactly as it came out of
the till system. It has not been checked by anyone. Your job is to turn it into something she can
open in a board meeting without you standing next to her.

---

## 2. The dataset

**File:** `Datasets/Ilesanmi_Sales_Raw_Export.xlsx` (or the `.csv` of the same name)
**Rows:** 1,025, before any cleaning
**Column dictionary:** see [`Datasets/README.md`](../Datasets/README.md) for the full definition of
all seventeen columns, the value ranges and the arithmetic relationships between them.

All monetary values are in Naira. No real person, business or transaction is represented in the file.

### The deliberate quirks you should expect

This export was dirtied on purpose, the way a real till export arrives. Every fault below is
genuinely present, and the client has told you the file **should** contain 1,000 completed sales.

| What you will find | How many rows |
|---|---|
| Duplicated Invoice IDs | 25 |
| Product line in ALL CAPS with a trailing space | 102 |
| Dates written `DD-MM-YYYY` instead of `M/D/YYYY` | 51 |
| Blank Rating | 10 in the raw file, 9 surviving deduplication |
| Negative Quantity | 5 |

Two of these carry traps worth naming in advance, because they are the ones that separate a workbook
that looks finished from one that is:

- **Remove Duplicates opens with every column ticked.** Left on that default it removes only 19 rows
  and leaves 1,006, with six duplicated sales still counted. Deciding which column defines a
  duplicate is part of the work, not a setting.
- **Not every impossible value should be flagged.** For each fault you find, work out whether the
  true value can be recovered from the file itself before you decide what to do about it. Two of the
  faults above have different correct answers for exactly this reason, and the marks are in the
  reasoning, not the outcome.

The arithmetic relationships in the column dictionary are your friend here. They hold exactly, to two
decimal places, and they are how you check both the file and yourself.

---

## 3. The tasks

### Task 1: Clean and verify (apply)

Produce a cleaned dataset from the raw export, as a structured table named `CleanSales`.

Alongside it, produce a **cleaning log** recording, for each fault you found: what it was, how many
rows it affected, how you detected it, what you did about it, and why. Where you had a choice, say
what the alternatives were and why you chose as you did.

Then produce a **verification block** of live formulas, not typed numbers, proving the result. It
must show at minimum: the row count, the number of duplicated Invoice IDs remaining, the number of
negative quantities remaining, the total Sales, and each branch's total Sales.

> Your row count should be 1,000. If it is 1,006 or 995, go back to the two traps in section 2 before
> going any further, because everything downstream inherits this number.

### Task 2: Summarise (apply)

Build pivot tables from `CleanSales` answering at least these three questions:

1. Total Sales by branch.
2. Total Sales by product line, broken down by branch.
3. One question of your own choosing that the manager has not asked for but that you think she
   should see. Say in one sentence why you chose it.

Verify at least two figures from your pivots using a method independent of the pivot table, and show
the check.

### Task 3: Build a one-screen dashboard (apply)

Assemble a dashboard on its own sheet that answers, at a glance and with no scrolling:

> **"Which branch is performing best, and what is driving it?"**

Requirements: every chart carries a specific title stating what it shows, axes are labelled where
they carry meaning, chart types suit the questions they answer, and at least one slicer is connected
to every chart on the sheet.

Include no chart that does not help answer the question above. What you leave off is marked as
carefully as what you put on.

### Task 4: Interpret and recommend (analyse)

Write a short interpretation, 300 to 500 words, addressed to the regional manager rather than to your
instructor. It must cover:

1. **Which branch is performing best**, with the figure, and what is driving it.
2. **One recommendation about stock**, naming a branch and a product line, with the figures that
   support it.
3. **One thing your analysis cannot tell her**, and what data would be needed to answer it.
4. **One caveat about the data itself**, drawn from your cleaning log, stated plainly enough for a
   non-analyst to act on.

Point 3 is not a hedge and point 4 is not an apology. An analyst who states the limits of their own
work is more useful than one who does not, and both are marked.

---

## 4. The deliverable

Two files, submitted together:

| File | Format | Contents |
|---|---|---|
| `<yourname>_module2_project.xlsx` | Excel workbook | Sheets for: the untouched raw import, the cleaned `CleanSales` table, the cleaning log, the verification block, the pivot tables, and the dashboard |
| `<yourname>_module2_interpretation.pdf` | PDF, 1 to 2 pages | The 300 to 500 word interpretation from Task 4, plus your AI prompt log (see section 6) |

The workbook must open without external links and without broken references. Sheets must be named so
that a reader who did not build it can find things.

---

## 5. The rubric

You are marked against [`module-02-mini-project-rubric.md`](module-02-mini-project-rubric.md). Read
it before you start, not after you finish. It has six criteria, and one of them marks your
verification evidence rather than your output, which means a correct answer you cannot demonstrate is
worth less than a correct answer you can.

---

## 6. AI usage rule for this project

**AI assistance is permitted, and it is part of the submission.**

You may use any AI assistant for any part of this project. In exchange, two things are required.

**A prompt log.** For every AI interaction that affected your submission, record:

| Field | What goes in it |
|---|---|
| Task | What you were trying to do |
| Prompt | The exact text you sent |
| Output | The formula, figure or advice that came back |
| Verification method | The independent method you used to check it |
| Result | What that method returned, and whether it matched |

**A verification note.** One short paragraph at the end of the log stating which AI-produced results
you accepted, which you rejected and why, and what you would have got wrong if you had not checked.

An entry whose verification method reads "looked correct", "seemed right" or "checked it" counts as a
missing entry. Verification means an independent route to the same number: a second prompt to the
same assistant is not a second method.

Submissions with no prompt log are assumed to have used no AI. If AI use is later evident in a
submission that declared none, that is a matter of academic honesty rather than of marks.

---

## 7. Sizing and pacing

This is built for **3 to 5 hours** in the LMS practice slot. A suggested split:

| Task | Suggested time |
|---|---|
| Task 1, clean and verify | 90 minutes |
| Task 2, summarise | 60 minutes |
| Task 3, dashboard | 60 minutes |
| Task 4, interpretation | 45 minutes |
| Prompt log and tidying up | 15 minutes |

If Task 1 is taking more than two hours, stop and check your row count against the traps in section
2. Nearly every overrun on this project comes from cleaning that has gone quietly wrong and is being
patched by hand rather than corrected at the source.

---

## 8. Before you submit

- [ ] `CleanSales` holds exactly 1,000 rows
- [ ] The verification block is entirely live formulas, with no typed numbers
- [ ] The three branch totals add to the chain total, with a difference of exactly 0
- [ ] The cleaning log covers all five faults, with a reason for each decision
- [ ] Every figure that depends on a judgement call is labelled with the judgement
- [ ] The dashboard fits on one screen with no scrolling
- [ ] Every slicer is connected to every chart, tested button by button
- [ ] No chart still carries the title `Chart Title` or `Sum of Sales`
- [ ] The interpretation is addressed to the manager and covers all four required points
- [ ] The prompt log has a real verification method against every entry
