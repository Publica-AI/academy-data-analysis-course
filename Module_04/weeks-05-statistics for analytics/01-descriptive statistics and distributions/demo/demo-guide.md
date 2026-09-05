# Demo Guide - Descriptive Statistics and Distributions
**Module 4, Topic 4.1 | Estimated duration: 20-24 minutes**

---

## What This Demo Teaches

- Calculating the mean, median, mode, range and standard deviation of a dataset in Excel
- Reading the gap between the mean and the median as a signal, not noise
- Locating and reasoning about an outlier before deciding what to do with it
- Recalculating summary statistics with an outlier excluded, and comparing the two results
- Turning a set of statistics into a single, plain-language recommendation a manager could act on

---

## Setup - Before the Demo Starts

1. Open `Topic-4.1-Aduke-Stores-Dataset.xlsx` and confirm the **Ikeja Data** sheet is visible (30 days of daily customer counts, 1-30 November 2025).
2. Keep the **Tutor Answer Key** sheet open in a separate window, not projected, it holds every formula and expected value used in this demo.
3. Confirm Excel recognises `MODE.SNGL` and `STDEV.S` (Excel 2010 or later).

> **Instructor note:** Row 32 (28 November) is highlighted in the workbook, a Black Friday promo day. Do not explain why it is highlighted before Part 3, the demo is built to let trainees notice the mean and median disagree first, then discover the cause themselves.

---

## Demo Steps

### Part 1 - The Mean and the Median (6 min)

> "Aduke Stores' Ikeja branch manager wants one number: how many customers should I plan for on a normal day? Let's calculate it properly."

On the **Ikeja Data** sheet, in an empty cell:

```
=AVERAGE(D5:D34)   → 112.87
=MEDIAN(D5:D34)     → 96
```

> "112.87 and 96. Those two numbers should be close together if the data is evenly spread, and they are not. That gap is worth investigating before we report either one."

### Part 2 - Mode, Range and Standard Deviation (6 min)

> "Before we chase the gap, let's finish the basic toolkit. Three more numbers, three more angles on the same data."

```
=MODE.SNGL(D5:D34)          → 82
=MAX(D5:D34)-MIN(D5:D34)    → 345
=STDEV.S(D5:D34)            → 61.71
```

> "A range of 345 customers is enormous for a single branch. A standard deviation of 61.71 means a typical day sits about 62 customers away from the mean, that's a lot of scatter for a 30-day window. Both numbers are pointing at the same thing the mean-median gap already hinted at: something in this data is not behaving normally."

**Ask students:** "Looking at these five numbers together, what would you guess is going on in this dataset, before I show you the answer?"

> "Most of you will say some kind of unusual day, an outlier. That's exactly right, and that's Part 3."

### Part 3 - Finding and Handling the Outlier (7 min)

> "Scroll to row 32, 28 November. Highlighted for a reason."

Point to row 32: 420 customers, versus a typical day in the 75-150 range.

> "28 November was a Black Friday promo. One day, 420 customers, sitting inside a dataset where every other day is under 150. That single day is dragging our mean upward and inflating our range and standard deviation. Let's see exactly how much, by recalculating everything without it."

```
=AVERAGE(D5:D31,D33:D34)   → 102.28
=MEDIAN(D5:D31,D33:D34)     → 94
=MAX(D5:D31,D33:D34)-MIN(D5:D31,D33:D34)   → 74
=STDEV.S(D5:D31,D33:D34)    → 21.42
```

> "Look at that shift. Mean and median now sit close together, 102 and 94. The range drops from 345 to 74. The standard deviation drops from 61.71 to 21.42. Removing one day changed almost every number we calculated. That is exactly why an analyst never reports a summary statistic without first checking for a day like this one."

### Part 4 - The Business Recommendation (4 min)

> "We now have two versions of the truth. Which one goes in the report to the branch manager?"

> "Neither one on its own. The honest answer is: for everyday staffing, plan around 94 to 102 customers, using the excluding-outlier figures, because that's what a normal day actually looks like. The promo day gets reported separately, on its own terms, as a planned event with its own staffing plan. We never delete the outlier from the dataset and we never hide it from the report, we explain it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Reports the mean (112.87) as the staffing number without noticing the median disagrees | "What does the median say? If those two numbers don't agree, that disagreement is itself information, not something to ignore." |
| Excludes the outlier row incorrectly, for example `=AVERAGE(D5:D34)` with row 32 manually overtyped to blank | "Don't edit the data. Use two ranges in the same formula, `D5:D31` and `D33:D34`, so the original 30-day dataset stays intact for anyone else who opens this file." |
| Suggests deleting the promo day from the dataset entirely | "That would make the dataset lie by omission. The promo day happened, it just doesn't belong in the 'normal day' calculation. Keep it, report it separately." |
| Confuses `MODE.SNGL` with `MEDIAN` when asked which value appears most often | "Mode answers a different question, which single number repeats the most, not which number sits in the middle. Check the definition against what the formula actually returns." |

---

## Up Next

Topic 4.2, Correlation and Relationships, asks a new question about this same branch's data: does marketing spend actually move sales, or does it just look that way?
