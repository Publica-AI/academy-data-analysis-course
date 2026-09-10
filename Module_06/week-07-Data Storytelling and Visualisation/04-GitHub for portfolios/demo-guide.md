# Demo Guide - GitHub for Portfolios
**Module 6, Topic 6.4 | Estimated duration: 48-50 minutes**

---

## What This Demo Teaches

- Setting up a public GitHub repository structured for a data analysis project
- Running a repeatable, programmatic data-safety check before publishing anything
- Publishing a README that follows the strong-analyst structure, generated from real computed numbers rather than typed from memory
- Recognising that a README (or any generated document) rendering without error is not the same as it being correct
- Sharing a portfolio link a stranger could open, understand, and reproduce in ninety seconds

---

## Setup - Before the Demo Starts

1. Trainees must have `ajebo_finance_loan_applications_CLEANED.csv` (356 rows) saved from Module 6.1, plus the Module 6.1-6.3 notebooks and Module 6.3's written narratives ready to reference.
2. Trainees need a GitHub account created in advance - account creation itself should not eat into session time.
3. Open `Topic_6_4_github_portfolios.ipynb` and run the Setup cell (pandas, `re`, `os` - no new installs beyond what 6.1-6.3 already used).

> **Instructor note:** the README this notebook generates embeds two chart images by path (`./images/kano_approval_rate.png` and `./images/income_vs_loan.png`), but neither this notebook nor the Module 6.2 notebook contains a `savefig()` call that actually creates those files - Module 6.2 only calls `plt.show()`. Before running this demo live, export the Kano approval-rate chart and the income-vs-loan scatter from Module 6.2 as PNG files into an `images/` folder yourself, or the rendered README preview in Part 4 will show two broken image links. Flag this to trainees too, since they will hit the same gap doing the practical activity with their own charts.

---

## Demo Steps

### Part 1 - Why this matters (5 min)

> "Nobody hiring an analyst asks to see your code before they see your portfolio link. Many employers check a GitHub repository before they ever read a CV closely, and the average recruiter skim time on a portfolio repository is about ninety seconds. An analysis that lives only on your laptop, however good, does not exist to an employer. Today's job is making this week's work visible, understandable, and credible to someone who has never met you and has ninety seconds to decide whether to keep reading."

---

### Part 2 - GitHub basics and the minimum steps to publish (6 min)

> "Three concepts are enough to complete this topic: a repository, a commit, and a README."

Walk through each definition briefly - repo as a project folder with full history, commit as a saved snapshot with a descriptive message, README as the file GitHub automatically renders on the front page.

> "Commit messages are part of the portfolio too. 'Fixed stuff' reads very differently to an employer than 'clean duplicate applications and standardise branch names, Module 6.1.'"

Walk through the six minimum steps to publish: create a public repo, add the cleaned dataset (after the safety check), add the 6.1-6.3 notebooks, add a README, commit and push, copy the URL.

---

### Part 3 - The data-safety check, live (8 min)

> "This is not optional, and it is not new - it's Module 6.1's data-protection discipline, now applied to a public space. Before uploading anything, we scan it programmatically."

Run the `data_safety_check()` definition cell, which also runs it against the real AJEBO dataset at the bottom.

> "It checks column names against a list of suspicious keywords - name, email, phone, BVN, and so on - and scans every string column for email- and phone-shaped patterns, checked one value at a time, never joined into one long string first, because joining values before matching can create false matches across unrelated rows. AJEBO's data passes clean, which is expected - Module 6.1's dataset design already guaranteed no real personal data."

**Ask students:** "A clean pass here - does that prove there's no personal data in the file?"

> "No. The docstring says it outright: this is a first pass, not a guarantee. Let's prove the checker actually catches something, not just trivially passes on data we already know is safe."

Run the injected-email test cell (`test_df` with a fake `Contact_Email` column).

> "We deliberately added a column with an obvious email address, and the checker flags it immediately. That's the difference between a check that passes because nothing's wrong, and a check that's actually been proven to catch something when it is wrong. Run this exact check on any new dataset before it goes anywhere public - and still look at the columns and a sample of rows yourself afterward."

---

### Part 4 - Generating a real README from real data (10 min)

> "Rather than just describing what a strong README looks like, let's build one from the actual verified numbers in this dataset - the same discipline Module 6.3 used for narratives, applied to a README this time."

Run the `readme_stats` cell (branch stats, Kano's rate and n, the next-lowest branch, the income-loan correlation).

> "Every number in here - Kano's rate, its gap to the next-lowest branch, the correlation - comes straight from a pandas calculation, not from memory."

Run the README-generation cell (the f-string building the full markdown document from `readme_stats`), then the rendering cell that displays it as GitHub would show it.

> "This is what a stranger sees the moment they open the repository - a stated business problem, a data-safety confirmation, a numbered method linking to each notebook, and key findings with their supporting charts embedded directly, not just linked, so nothing needs a click to be visible."

---

### Part 5 - "It ran" is not the same as "it's right" (8 min)

> "Look closely at the business-problem paragraph in what we just rendered. It names Kano directly - typed by hand - while the rest of the README, the approval rate, the gap, the sample size, is pulled dynamically from `readme_stats`."

**Ask students:** "If next quarter's data showed Port Harcourt as the new lowest-performing branch instead of Kano, and we reran this cell, what would happen to this document?"

> "Every number in the Key Findings section would update correctly. The business-problem paragraph would still say Kano, silently wrong, because it was typed by hand instead of pulled from the same data. A README that renders without a Python error is not the same as a README that's actually correct - you have to re-read generated text after the underlying data changes, not just trust that it ran."

Run the fix cell (`lowest_branch_name` pulled from `branch_stats.index[0]`, used to correct the hardcoded reference).

> "Now the whole document updates consistently if the underlying data changes - the exact discipline from Module 6.3's traceable narratives, applied here to a generated document instead of a written one."

---

### Part 6 - What not to upload, and the weak-vs-strong rule (6 min)

> "Three things, and none of them are new: no real personal data ever, no API keys or credentials left in notebook outputs or code cells from testing, and no employer or client data without explicit written permission."

Read the weak README example aloud ("# Project. Some analysis of loan data. See notebook.ipynb for code.") and contrast it with the README just built in Part 4.

> "The weak version has no business problem, no findings, no visuals - an employer scrolls past it in under five seconds. Write the README as if the reader will never open the notebook. If it can't stand completely on its own, it isn't finished."

---

### Part 7 - Setting up the practical activity (5 min)

> "You'll run the data-safety check against your own Module 6.1 file, extend the `readme_stats` dictionary with one more finding from Module 6.3 - the education approval gap or the self-employed loan-size gap - and regenerate your README to include it as a third key finding."

Walk through the five practical-activity steps: run the safety check, extend and regenerate the README, proofread it exactly as demonstrated in Part 5, create the real repository and commit, then swap portfolio links with a partner for review against the checklist.

> "Proofreading is not optional, and Part 5 just showed you why - render it, read it end to end, and fix anything left over before you consider it final."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trainee treats a clean data-safety check result as a guarantee of no personal data | "The docstring says it directly - this is a first pass, not a guarantee. Always pair it with your own manual look at the columns and a sample of rows." |
| Trainee assumes the README is correct because it rendered without an error | "Part 5 showed exactly this - the document ran fine and still had a wrong, hardcoded branch name sitting next to correct, dynamically-generated figures. Read it end to end after every regeneration." |
| Trainee links to a chart image instead of embedding it | "A linked image needs a click to view. An embedded image, using the `![alt text](path)` markdown syntax, displays directly on the page - that's the whole point of a README a stranger skims in ninety seconds." |
| Trainee writes a README that is mostly links with no summary | "That forces the reader to do all the work the README should have done for them. State the business problem and the findings in words, then link to the notebook for anyone who wants the detail." |

---

## Up Next

Module 6.5 - AI-Assisted Exploration and Drafting: the portfolio is now public and documented, and the next session returns to the same AJEBO analysis one more time, this time with an AI assistant doing first-draft exploration and narrative writing while the trainee does the verification.
