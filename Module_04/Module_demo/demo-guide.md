
# Module Demo Guide - Statistics for Analytics (Week 5)
**Module 4 | Estimated duration: 65 minutes**

---

## The Story

Aduke Stores is a Lagos-based retail chain with branches across the city. Ngozi, a newly hired data analyst on the Insights team, has been asked by the Regional Operations Director for a month-end report on the Ikeja branch, needed for tomorrow's budget meeting. The report must answer four questions in plain language: how consistent is daily footfall, does marketing spend actually move sales, what should tomorrow's spend be, and did the new checkout lane pilot genuinely work.

**What this demo builds:**

A complete Month-End Analyst Report for Ikeja branch that ties together every topic from Week 5:
- A descriptive-statistics profile of daily footfall, including how one outlier day distorts the picture (Topic 4.1)
- A correlation coefficient measuring how strongly marketing spend and sales move together (Topic 4.2)
- A regression model that predicts tomorrow's sales from a proposed spend amount, and exposes the danger of predicting beyond it (Topic 4.3)
- A hypothesis test confirming whether the checkout lane pilot produced a real, statistically significant sales increase (Topic 4.4)
- An AI-drafted summary of all four findings, audited and corrected before it goes anywhere near the Director (Topic 4.5)

---

## Prerequisites

1. Excel (or Google Sheets) with the demo workbook `Module-04-Demo-Dataset.xlsx` downloaded locally.
2. A free AI assistant (Claude, ChatGPT, or Gemini) open in a browser tab for Part 5, or the pre-built fallback response ready if live access is unreliable.
3. Trainees already comfortable with the Excel functions taught across Topics 4.1 to 4.4: `AVERAGE`, `MEDIAN`, `MODE.SNGL`, `STDEV.S`, `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, `T.TEST`.

> **Instructor note:** This demo reuses the exact Ikeja branch data already used across the Topic 4.1-4.4 labs, consolidated into one workbook so trainees follow one continuous story instead of jumping between four separate topic files. If live AI access is unreliable in the room, use the pre-built fallback response in Part 5 rather than losing demo time troubleshooting a connection, this mirrors the same fallback discipline used in the Topic 4.5 lab pack.

---

## Dataset / Project Setup (before the demo starts)

1. Open `Module-04-Demo-Dataset.xlsx` and confirm five sheets are visible: **Dataset Provenance**, **Ikeja Daily Customers**, **Ikeja Marketing vs Sales**, **Ikeja Checkout Pilot**, and a blank **Month-End Report** tab.
2. Do not open or preview the Part 5 AI sample response before the session, it should land as a genuine live moment for trainees, not a rehearsed reveal.
3. Have the Month-End Report tab visible on a second window or split screen throughout, so trainees watch it fill in as each Part completes.

---

## Demo Steps

### Part 1 - Descriptive Statistics and Distributions (Topic 4.1) (12 min)

> "Ngozi's first job is figuring out what a normal day actually looks like at Ikeja branch, before she can say whether anything in this report is worth flagging."

On the **Ikeja Daily Customers** sheet (30 days of data, rows 4 to 33):

```
=AVERAGE(C4:C33)          → 112.87
=MEDIAN(C4:C33)            → 96
=MODE.SNGL(C4:C33)         → 82
=MAX(C4:C33)-MIN(C4:C33)   → 345
=STDEV.S(C4:C33)           → 61.71
```

> "The mean, 113, and the median, 96, don't agree. That gap is a signal, not noise. Look at row 31."

Scroll to row 31 (28 November, the highlighted Black Friday promo day).

Recalculate excluding that single row:

```
=AVERAGE(C4:C30,C32:C33)   → 102.28
=MEDIAN(C4:C30,C32:C33)    → 94
```

> "Once we set the promo day aside, mean and median land close together, around 94 to 102. That's Ngozi's real number for the report, not 113."

**Write into Month-End Report, Section 1:** "Typical daily footfall: approximately 94 to 102 customers on an ordinary day. One Black Friday promo day (28 November, 420 customers) is excluded from this baseline and reported separately."

---

### Part 2 - Correlation and Relationships (Topic 4.2) (10 min)

> "Second question: is Aduke Stores' marketing spend actually connected to sales, or has Ngozi just been assuming that?"

On the **Ikeja Marketing vs Sales** sheet (24 days, rows 4 to 27):

```
=CORREL(C4:C27,D4:D27)   → 0.783
```

> "0.78 is a strong positive relationship. Not proof, a relationship. Spend and sales move together fairly closely across these 24 days."

Insert a scatter chart of columns C and D before trusting the number, to visually confirm the relationship looks roughly linear with no single point dominating it.

**Write into Month-End Report, Section 2:** "Marketing spend and sales show a strong positive correlation (r = 0.78). Higher-spend days tend to be higher-sales days, though other factors are still at play."

---

### Part 3 - Regression Fundamentals (Topic 4.3) (12 min)

> "A correlation tells Ngozi that spend and sales move together. The Operations Director wants more than that: if we spend 40,000 naira tomorrow, what sales should we plan for?"

Still on **Ikeja Marketing vs Sales**, in cells F2 to F4:

```
F2: =SLOPE(D4:D27,C4:C27)       → 3.4743
F3: =INTERCEPT(D4:D27,C4:C27)   → 171,491.13
F4: =RSQ(D4:D27,C4:C27)         → 0.6133
```

Predicted sales at 40,000 naira spend, in F6:

```
F6: =(F2*40000)+F3   → approximately 310,463
```

> "Watch this next part closely, it's the mistake that gets analysts in trouble. What if the Director asks for a prediction at 150,000 naira spend instead?"

```
F7: =(F2*150000)+F3   → approximately 692,637
```

> "That number is fiction. This model was only ever tested on spend between 8,584 and 69,535 naira. 150,000 is extrapolation, and Ngozi needs to say so in the report, not just hand over a confident-looking figure."

**Write into Month-End Report, Section 3:** "At a proposed spend of 40,000 naira tomorrow, predicted sales are approximately 310,463 naira (R-squared = 0.61, meaning about 61% of day-to-day sales variation is explained by spend). This model should not be used to justify spend levels much above 70,000 naira, that would be well outside the range actually tested."

---

### Part 4 - Hypothesis Testing (Topic 4.4) (14 min)

> "Now the big one for the budget meeting: did the checkout lane pilot really work, or did Ikeja just have a good month?"

State the hypotheses out loud before touching Excel: "H0, the null hypothesis, average daily sales are the same before and after the pilot. H1, the alternative, they're different."

On the **Ikeja Checkout Pilot** sheet (Before in columns A-B, After in columns D-E, rows 5 to 24):

```
=AVERAGE(B5:B24)              → 283,100   (Before)
=AVERAGE(E5:E24)              → 322,590   (After)
=T.TEST(B5:B24,E5:E24,2,3)    → 0.00033
```

> "p equals 0.0003. That's far below the usual 0.05 threshold. Combined with a real 14% jump in the mean, this is strong evidence the pilot worked, not just a lucky month."

**Write into Month-End Report, Section 4:** "The checkout lane pilot produced a statistically significant increase in daily sales (before approximately 283,100 naira, after approximately 322,590 naira, p approximately 0.0003). This is a reasonable basis to recommend testing the pilot at further branches."

---

### Part 5 - AI as Statistics Tutor and Interpreter (Topic 4.5) (17 min)

> "Ngozi has four solid findings and a deadline. She asks an AI assistant to draft the write-up for the Director, so she can spend her time checking it rather than typing it from scratch."

**If live AI access is available**, prompt an AI assistant live with a role, context, data, and constraints prompt, for example:

"You are a data analyst assistant helping a Regional Operations Director understand a month-end result. Explain the following findings in plain, non-technical language, under 150 words: [paste the four Month-End Report sections written so far]."

**If live access is unavailable**, open the pre-built fallback response instead, the same "AI Response - Guided" example used in the Topic 4.5 lab, which contains four planted errors: overstated causation, a misdefined R-squared, an unflagged 150,000-naira extrapolation, and a misread p-value.

> "Read this back against what Ngozi actually calculated in Parts 1 to 4. Where does the AI's draft go further than the data actually supports?"

Walk through the five-point verification checklist live, as a group:
1. Do the numbers match what we calculated?
2. Is any causal language ("proves," "causes") actually justified?
3. Are the data's limits respected, no unflagged extrapolation?
4. Is statistical significance kept separate from business importance?
5. Is anything important missing, not just wrong?

Rewrite the flawed response into a corrected paragraph live, using the same corrected model answer from the Topic 4.5 Tutor Answer Key as the target.

**Write into Month-End Report, Section 5:** the corrected, verified paragraph, combining all four findings into one accurate, business-ready summary.

> "That's the finished report. Every number in it was calculated by Ngozi first, and wherever AI helped draft the language, she checked it against her own numbers before a single sentence went to the Director."

---

## Demo Wrap-Up

Summarise the finished Month-End Report and map each section back to the topic that taught it:

| Feature / capability | Topic it came from | What it shows |
|---|---|---|
| Typical footfall baseline (94-102 customers/day, outlier excluded) | Topic 4.1 | Mean versus median, and how one outlier can distort a simple average |
| Correlation coefficient (r = 0.78) between spend and sales | Topic 4.2 | Whether two variables move together, and how strongly, without claiming proof |
| Regression prediction for 40,000-naira spend (approximately 310,463 naira in sales) | Topic 4.3 | A working predictive model, and the extrapolation trap exposed at 150,000-naira spend |
| Hypothesis test on the checkout lane pilot (p approximately 0.0003) | Topic 4.4 | Whether an observed improvement is real or could plausibly be chance |
| AI-drafted, then corrected, summary paragraph | Topic 4.5 | Using AI as a first draft, never as the final, unverified word in a real report |

> "This is a real analyst deliverable. If Ngozi sends this Month-End Report to the Regional Operations Director, every claim in it can be defended, because she calculated it herself, and wherever AI helped draft the language, she checked it first."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| `AVERAGE` or `MEDIAN` formulas return an unexpected value | "Check your range starts at row 4, not row 3, row 3 is the header. Including the header text in a numeric formula throws the result off." |
| `SLOPE`, `INTERCEPT`, or `RSQ` give a result that looks inverted or wrong | "These three functions take known_y before known_x, sales before spend. Reversing the order is the single most common mistake with this formula family." |
| `T.TEST` returns a value that looks too large or too small | "Confirm the last two arguments are 2 and 3, tails then type. Leaving type at 1 (paired) instead of 3 (two-sample, unequal variance) changes the result." |
| A trainee wants to skip straight to Part 5 and let AI do the whole report | "That's exactly the shortcut this topic exists to prevent. Without your own numbers from Parts 1 to 4, you have nothing to check the AI's draft against." |
| Live AI output differs from the fallback sample response | "Expected, different tools and different runs will phrase things differently. The five-point verification checklist applies the same way regardless of the exact wording you get." |
| A trainee copies the AI's flawed language straight into the report without editing | "Good, that's the failure mode this exercise is built to catch. Walk the checklist again on this exact sentence before it goes any further." |
