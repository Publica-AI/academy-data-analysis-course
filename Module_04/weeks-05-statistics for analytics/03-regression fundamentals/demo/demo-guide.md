# Demo Guide - Regression Fundamentals
**Module 4, Topic 4.3 | Estimated duration: 24-28 minutes**

---

## What This Demo Teaches

- Fitting a regression line in Excel using SLOPE and INTERCEPT
- Writing out and using a prediction formula built from those two values
- Interpreting R-squared as the share of the outcome the model actually explains
- Recognising extrapolation, using a model to predict beyond the range of data it was built from
- Recognising when a high R-squared still hides a poor fit, because the true relationship curves rather than follows a straight line

---

## Setup - Before the Demo Starts

1. Open `Topic-4.3-Aduke-Stores-Dataset.xlsx` and confirm the **Ikeja Marketing Data** and **Staffing vs Sales Data** sheets are both visible.
2. Keep the **Tutor Answer Key** sheet open in a separate window, not projected, it holds every formula and expected value used in this demo.
3. Trainees should already have this same Ikeja dataset's scatter chart and CORREL result from the Topic 4.2 demo, this demo builds directly on top of it rather than starting from a blank sheet.

> **Instructor note:** The Staffing vs Sales dataset was built so R-squared looks strong (0.85) while the underlying relationship actually curves. Do not reveal this before Part 3, trainees should be genuinely surprised when the scatter plot shows a shape a straight line does not fit well.

---

## Demo Steps

### Part 1 - Fitting the Line (7 min)

> "Topic 4.2 told us spend and sales at Ikeja branch are strongly related, r equals 0.78. Today the branch manager wants more than a relationship, they want a number: if we spend 40,000 naira tomorrow, what sales should we plan for?"

On the **Ikeja Marketing Data** sheet:

```
=SLOPE(D5:D28,C5:C28)       → 3.47
=INTERCEPT(D5:D28,C5:C28)   → 171,491
```

> "Slope tells us how much sales change for every extra naira of spend, about 3.47 naira in sales for each naira spent. Intercept is the baseline, roughly what the model expects on a day with no ad spend at all. Together, they build a formula: sales equals intercept plus slope times spend."

### Part 2 - Predicting, and Knowing Where to Stop (8 min)

```
=RSQ(D5:D28,C5:C28)   → 0.61
```

> "R-squared of 0.61 means about 61% of the day-to-day swings in sales are explained by spend. The other 39% comes from everything else, footfall, stock, day of the week. Now let's answer the manager's actual question."

Calculate the prediction at 40,000 naira spend using the slope and intercept cells.

> "Roughly 310,000 naira. That's a reasonable estimate, because 40,000 sits comfortably inside the range we actually tested, 8,584 to 69,535 naira."

**Ask students:** "What happens if the manager instead asks us to predict sales at 150,000 naira of spend? Should we just plug that number into the same formula?"

Calculate it live: slope times 150,000 plus intercept, approximately 692,637.

> "The formula happily gives us a number. That doesn't make it trustworthy. We never tested spend anywhere near 150,000, so this is a guess wearing a calculation's clothes. We do not report this figure to the manager as reliable."

### Part 3 - When a High R-squared Still Hides a Poor Fit (10 min)

> "Different dataset now. A trial branch tested staffing levels from 2 to 12 people per shift against daily sales. Let's fit the same kind of model."

```
=SLOPE(D5:D28,C5:C28)   [Staffing vs Sales sheet]   → 18,930
=INTERCEPT(D5:D28,C5:C28)                             → 239,033
=RSQ(D5:D28,C5:C28)                                   → 0.85
```

> "0.85. That's a strong R-squared, stronger than Ikeja's marketing model. A quick glance says this model is even more trustworthy. Let's check that before we believe it."

Build a scatter plot of Staff on Shift against Daily Sales.

> "Look at the shape. Sales rise steeply from 2 staff up to around 8, then flatten out. That is not a straight line, it's a curve, most likely because the shop floor and tills reach capacity and extra staff stop adding as much value."

Compare the model's predicted sales at 2 staff and at 12 staff against the actual data points on the chart.

> "At both ends, the straight line over-predicts what the real data shows. A high R-squared told us the model fits well overall, it did not tell us the model fits well everywhere, and it definitely did not tell us the relationship is actually a straight line."

### Part 4 - The Two Questions Before Reporting Any Regression (3 min)

> "So before either of these models leaves this room in a report, two questions."

State them out loud: "Is the number I'm predicting inside the range we actually tested? Does a scatter plot of the data actually look like a straight line?"

> "Skip either question and you risk handing someone a confident-looking number with no real evidence behind it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Enters SLOPE or INTERCEPT arguments in the wrong order, sales and spend swapped | "These two functions want your outcome, sales, listed first, then what you're predicting from, spend. Check the concept session's worked example if the numbers look inverted." |
| Reports the 150,000 naira prediction without flagging it as extrapolation | "Where does our actual tested data stop? Is 150,000 inside that range, or past the edge of it?" |
| Sees R-squared of 0.85 on the staffing data and declares the model reliable without checking the scatter plot | "A high R-squared is a reason to look closer, not a reason to stop looking. What does the actual shape of the data tell you?" |
| Assumes a curved relationship means regression cannot be used at all | "Regression still works here, it's just that a straight line isn't the right shape for this particular relationship. The lesson is about matching the model to the data, not abandoning the tool." |

---

## Up Next

Topic 4.4, Hypothesis Testing, moves from predicting a number to a sharper question: when Ikeja's checkout lane pilot shows higher sales afterward, is that a real change, or could it easily have happened by chance?
