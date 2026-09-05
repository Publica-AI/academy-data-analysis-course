# Demo Guide - Correlation and Relationships
**Module 4, Topic 4.2 | Estimated duration: 22-26 minutes**

---

## What This Demo Teaches

- Building a scatter plot to see a relationship before trusting any single number about it
- Calculating a correlation coefficient in Excel using CORREL
- Reading the strength and direction of a correlation coefficient in plain business language
- Explaining, with a concrete example, why a strong correlation does not prove causation
- Spotting a likely spurious relationship and naming a plausible hidden factor behind it

---

## Setup - Before the Demo Starts

1. Open `Topic-4.2-Aduke-Stores-Dataset.xlsx` and confirm the **Ikeja Marketing Data** and **Spurious Correlation Data** sheets are both visible.
2. Keep the **Tutor Answer Key** sheet open in a separate window, not projected, it holds every formula and expected value used in this demo.
3. Do not mention the word "temperature" before Part 3, it is the answer to a question trainees are meant to work out for themselves.

> **Instructor note:** The Spurious Correlation Data sheet deliberately does not include a temperature column. If a trainee asks why it is missing, say only "that's worth thinking about" and move on, the missing column is the whole point of Part 3.

---

## Demo Steps

### Part 1 - Building the Scatter and Calculating r (7 min)

> "Aduke Stores ran a 24-day test at Ikeja branch, changing how much they spent on ads each day, then recording that day's sales. The marketing manager wants to know one thing: does spending more actually move sales, or are we just hoping so?"

Select the Marketing Spend and Daily Sales columns on the **Ikeja Marketing Data** sheet, insert a scatter chart.

> "Look at the shape before we calculate anything. The dots trend upward, left to right, with some scatter around that trend. That shape is what a positive relationship looks like on a chart. Now let's put a number on it."

```
=CORREL(C5:C28,D5:D28)   → 0.78
```

> "0.78. That number confirms what the chart already showed us, and gives us something precise to report instead of just 'it looks related'."

### Part 2 - Reading the Strength and Direction (5 min)

> "A number on its own means nothing to a branch manager. We need to translate it."

Write the rough strength guide on the board or a slide: 0.0-0.2 very weak, 0.2-0.4 weak, 0.4-0.7 moderate, 0.7-1.0 strong.

> "0.78 falls in the strong band, and it's positive, so spend and sales move together fairly closely. Compare that to Yaba branch, which ran the identical test."

```
=CORREL(C5:C28,D5:D28)   [on the Yaba Marketing Data sheet]   → 0.27
```

> "0.27 is weak. Same experiment, same branch type, two very different answers. That's exactly why we calculate this for each branch rather than assuming one branch's result applies everywhere."

### Part 3 - Correlation Is Not Causation (8 min)

> "Here's where a lot of real analysts get into trouble. A colleague at the Lagos warehouse has noticed something: on days when generator fuel purchases are high, sachet water purchases are high too. Let's check it properly."

```
=CORREL(C5:C28,D5:D28)   [on the Spurious Correlation Data sheet]   → 0.79
```

**Ask students:** "0.79, a strong positive relationship. Before I tell you what to conclude, what do you think is really going on here? Does buying generator fuel make someone want to buy water?"

> "Notice this dataset has no temperature column. That's deliberate. On hot days, customers buy more sachet water because they're thirsty, and generators run more for fans and air conditioning, because it's hot. Temperature drives both. Neither variable causes the other, they're both responding to a hidden third factor we never measured directly."

### Part 4 - The Verification Habit (4 min)

> "So what do we actually do the next time a strong correlation lands on our desk?"

State the two-question check out loud: "Is there a believable reason X would directly affect Y? Could a third factor explain both?"

> "Run every correlation through those two questions before it goes anywhere near a report. A strong number is a reason to investigate further, never a reason to announce a cause."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Reports Ikeja's r = 0.78 as proof that spend causes sales | "What would it take to actually prove that? A correlation on its own only tells us the two variables move together." |
| Treats Yaba's r = 0.27 as a mistake because it's lower than Ikeja's | "It's not a mistake, it's a real, different result. Different branches can behave differently, that's useful information, not an error to fix." |
| Concludes from the spurious dataset that generator fuel purchases directly cause water sales | "Is there a direct, believable reason one would cause the other? Or is something else driving both at the same time?" |
| Confuses the CORREL argument order, or mixes up which column is which variable | "CORREL doesn't care about order the way SLOPE and INTERCEPT do, but always double-check you selected the two columns you actually meant to compare." |

---

## Up Next

Topic 4.3, Regression Fundamentals, uses this same Ikeja marketing data to go one step further: not just whether spend and sales are related, but how much sales to expect for a specific spend amount.
