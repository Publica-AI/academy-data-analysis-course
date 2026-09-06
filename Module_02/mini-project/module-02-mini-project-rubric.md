# Module 2 Mini Project Rubric: The Ilesanmi Stores Quarterly Report

**Six criteria, three performance levels each. Total 60 marks.**

Every criterion below describes something a reviewer can observe in the submitted files. Where a
criterion names a figure, the reviewer checks that figure rather than judging the impression the
workbook gives. Two reviewers marking the same submission against this rubric should reach the same
total.

Marks: **Developing 0 to 4 | Competent 5 to 7 | Excellent 8 to 10** on each criterion.

---

## Criterion 1: Cleaning accuracy (10 marks)

*Does the cleaned dataset match the verifiable target?*

| Level | Descriptor |
|---|---|
| **Developing** | `CleanSales` holds a row count other than 1,000, or duplicated Invoice IDs, negative quantities or untrimmed Product line values remain in the file. |
| **Competent** | `CleanSales` holds exactly 1,000 rows with 0 duplicated Invoice IDs, 0 negative quantities, 6 distinct Product line values, and a total Sales figure of ₦32,296,674.90. |
| **Excellent** | All of Competent, and the five sign-flipped quantities were corrected from `cogs ÷ Unit price` rather than deleted or left flagged, giving a total quantity of 5,510. |

> Reviewer check: `=COUNTA(CleanSales[Invoice ID])` reads 1,000; `=SUM(CleanSales[Sales])` reads
> ₦32,296,674.90; `=SUM(CleanSales[Quantity])` reads 5,510;
> `=COUNTIF(CleanSales[Quantity],"<0")` reads 0. A row count of 1,006 caps this criterion at
> Developing, whatever else the workbook contains.

---

## Criterion 2: Cleaning record and decision reasoning (10 marks)

*Can a reviewer reconstruct what was done and why, without asking?*

| Level | Descriptor |
|---|---|
| **Developing** | The cleaning log is absent, or lists actions without stating how many rows each fault affected, how it was detected, or why the chosen repair was chosen. |
| **Competent** | The log covers all five faults, and for each one records the fault, the number of rows affected, the detection method, the action taken and a reason for that action. |
| **Excellent** | All of Competent, and the log distinguishes the faults where the true value was recoverable from the file (the five sign-flipped quantities) from the fault where it was not (the blank Ratings), giving a different and correct decision for each with the reasoning stated. |

> Reviewer check: the log names Invoice ID as the column that defined a duplicate, and treats
> negative quantities and blank Ratings differently rather than applying one policy to both.

---

## Criterion 3: Verification evidence (10 marks)

*Is the work demonstrably correct, independently of the analyst's assurance?*

This criterion marks the evidence, not the output. A correct answer with no demonstration scores
lower here than a correct answer with one.

| Level | Descriptor |
|---|---|
| **Developing** | The verification block is absent, or contains typed numbers rather than live formulas, or no figure anywhere in the workbook has been checked by a second method. |
| **Competent** | A verification block of live formulas shows row count, duplicated Invoice IDs, negative quantities, total Sales and each branch total; and at least two pivot figures are checked by a method independent of the pivot, with the check visible in the workbook. |
| **Excellent** | All of Competent, and the block includes at least one reconciliation that must equal zero (branch totals minus the chain total, or pivot minus SUMIF), so that a future error announces itself without anyone re-reading the figures. |

> Reviewer check: delete one row from `CleanSales`. Every figure in the verification block should
> move. Any figure that does not is a typed number and caps this criterion at Developing. Undo
> afterwards.

---

## Criterion 4: Summarisation (10 marks)

*Do the pivot tables answer the questions asked, from the right source?*

| Level | Descriptor |
|---|---|
| **Developing** | Fewer than three pivot tables, or a pivot built from a cell range rather than from `CleanSales`, or totals that do not reconcile to ₦32,296,674.90. |
| **Competent** | Three pivots present, all sourced from `CleanSales`, covering Sales by branch, Sales by product line broken down by branch, and one question of the trainee's own with a stated reason; all totals reconcile to the chain total. |
| **Excellent** | All of Competent, and the self-chosen third question produces a finding the manager did not ask for and could act on, with the reason for choosing it stated in terms of the business rather than the data. |

> Reviewer check: branch totals read ₦10,620,037.05 (Ikeja), ₦10,619,767.20 (Wuse) and
> ₦11,056,870.65 (Trans-Amadi). Each pivot's Table/Range reads `CleanSales`, not a cell range.

---

## Criterion 5: Dashboard (10 marks)

*Does one screen answer the manager's stated question?*

| Level | Descriptor |
|---|---|
| **Developing** | The dashboard requires scrolling, or any chart still carries a default title such as `Chart Title` or `Sum of Sales`, or a slicer is connected to some charts but not all, or a chart type obscures the comparison it is meant to show. |
| **Competent** | One screen with no scrolling; every chart carries a specific title naming the measure and the dimension; chart types suit their questions; at least one slicer is connected to every chart on the sheet and moves all of them. |
| **Excellent** | All of Competent, and the layout puts the answer to the manager's question where the eye lands first, carries data labels wherever a ranking is too close to read from bar length, and includes no chart that does not serve the stated question. |

> Reviewer check: click every slicer button, including multi-select, and confirm every chart moves
> every time. Confirm the Ikeja and Wuse bars are distinguishable, since they sit ₦269.85 apart
> and are visually identical without data labels.

---

## Criterion 6: Interpretation and AI disclosure (10 marks)

*Is the written analysis usable by the manager, and is the AI use accounted for?*

| Level | Descriptor |
|---|---|
| **Developing** | The interpretation is absent, is under 300 or over 500 words, omits one or more of the four required points, or makes claims without the figures behind them. Or: AI was evidently used and no prompt log was submitted. |
| **Competent** | All four required points covered, addressed to the manager rather than the instructor, with a figure supporting every claim. A prompt log is present recording task, prompt, output, verification method and result for each AI interaction. |
| **Excellent** | All of Competent, and the recommendation names a branch and a product line with the figures behind it; the stated limitation identifies the data that would be needed to resolve it; and the verification note states at least one AI output that was rejected, with the check that caught it. |

> Reviewer check: every prompt log entry has a verification method that is an independent route to
> the figure. Entries reading "looked correct", "seemed right" or "checked it" are treated as missing,
> and a log where most entries read that way caps this criterion at Developing.

---

## Grade bands

| Total | Band | What it means |
|---|---|---|
| 48 to 60 | Excellent | Could be sent to a client with light review |
| 35 to 47 | Competent | Meets the module's outcomes; specific areas to strengthen |
| 24 to 34 | Developing | Outcomes partly met; resubmission on named criteria |
| Below 24 | Not yet met | Rework required, starting with Criterion 1 |

## Note for reviewers

If Criterion 1 scores Developing, mark the remaining criteria on what was actually built rather than
adjusting them downwards a second time for the same fault. A trainee who cleaned to 1,006 rows and
then built a genuinely excellent dashboard on that file has demonstrated the dashboard outcome and
not the cleaning one, and the feedback is more useful when it says so precisely.

Where a figure in a submission differs from a figure in this rubric, check whether the trainee
measured the raw 1,025-row export rather than the cleaned file before treating it as an error. The
raw chain total is ₦33,156,782.40 and the raw Ikeja total is ₦11,062,565.85. Both are
arithmetically correct and neither answers the client's question, and the distinction is worth making
explicitly in written feedback rather than simply marking the figure wrong.
