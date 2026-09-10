# Demo Guide - Visualisation Principles and Chart Choice
**Module 6, Topic 6.2 | Estimated duration: 55-60 minutes**

---

## What This Demo Teaches

- Choosing a chart type by starting from the analytical question, not the column
- Applying the QUESTION -> DATA TYPE -> COMPARISON -> CHART framework to a real business question
- Recognising when a pie chart, line chart, histogram, scatter plot, bar chart or table is the right (or wrong) tool for a stated comparison
- Applying labelling and formatting standards (titles that state a finding, zero-baseline axes, restrained colour) that make a chart self-explanatory
- Spotting and correcting misleading visualisation practices: truncated axes, 3D distortion, distorted proportions, and rates reported without sample size
- Choosing a table over a chart when the request is for precise, quotable figures

---

## Setup - Before the Demo Starts

1. Trainees must have `ajebo_finance_loan_applications_CLEANED.csv` (356 rows) saved from Module 6.1 - this demo does not re-clean anything, it charts the already-cleaned file.
2. Python environment with pandas, numpy, matplotlib, and seaborn installed and importable.
3. Open `Topic_6_2_visualisation_principles.ipynb` and run the Setup cell before trainees arrive - this defines the house colour style used in every "AFTER" chart for the rest of the session: `GOOD` (primary teal), `ACCENT` (mint, reserved for the one thing to highlight), `MUTED` (grey-teal for everything else), and `BAD_RAINBOW` (used deliberately, only in "BEFORE" charts, to demonstrate what excessive colour looks like).

> **Instructor note:** the dataset's most recent month is partial (it ends 2026-08-06, six days into August). When you reach the trend-over-time chart in Part 4, the notebook deliberately drops that final partial month before plotting the trend - flag out loud that this is a legitimate cleaning decision, not the cherry-picking you'll warn against later in the same demo. If a trainee asks "isn't dropping data cherry-picking?", this is exactly the moment to draw that distinction live.

---

## Demo Steps

### Part 1 - Why visualisation matters, and starting with the question (6 min)

> "AJEBO's operations lead asks one question: which branch should we be worried about? Here's the answer as a table first."

Run the groupby summary cell (Applications, Avg Income, Avg Loan, Approval Rate by branch).

> "Time yourselves - how many seconds did it take to find the branch with the lowest approval rate? Now watch the same question answered as a sorted horizontal bar chart."

Run the sorted bar chart cell (Kano flagged in accent colour, rest in muted grey-teal).

> "Neither format is wrong on its own - they solve different problems, and we'll come back to exactly when a table wins later in this session. The mistake is picking one out of habit rather than choosing based on the question. And notice the habit that got us to a good chart in the first place: I didn't start by saying 'let me chart Monthly_Income_NGN' - a column, not a question. I started with 'which branch should we be worried about?' - a real question, which told me exactly what to compare."

---

### Part 2 - The chart-selection framework (5 min)

> "Every chart in today's session gets built the same way - four steps, always in this order: Question, Data type, Comparison, Chart."

Walk through the framework on the whiteboard or slide using the Kano example:
- Question: should we change Kano's lending criteria?
- Data type: Branch_Region (categorical) x Approval rate (numeric)
- Comparison: comparison across a small number of categories
- Chart: sorted horizontal bar chart

> "Work through this table left to right, every single time, before opening a notebook. It's the difference between the bar chart you just saw and the pie chart we're about to build by mistake in Part 3."

---

### Part 3 - Comparison: the pie chart trap (7 min)

> "Question: does average loan amount differ between Salaried and Self-Employed applicants? Here's a first attempt."

Run the pie chart cell (average loan by employment type, two slices).

> "Look closely at those percentages - 48% and 52%, or whatever you get. What do they actually tell you about loan amounts in Naira? Nothing. They're each average's share of the sum of both averages - a number with no business meaning at all. A pie chart shows parts of one whole, and two independent averages aren't parts of a whole."

Run the rebuild cell (bar chart, accent colour on the larger value, NGN labels on each bar).

> "Same data, now showing what the committee actually needs to know: self-employed applicants request larger loans on average, and here's the real NGN figure for each group. If your question is 'how do these two numbers compare', reach for a bar chart, every time."

---

### Part 4 - Trends over time (7 min)

> "Question: how has application volume changed over the period we have data for? Here's a first attempt - one line per branch, six branches."

Run the six-line, rainbow-coloured, legend-outside-the-plot cell.

**Ask students:** "What is the one thing this chart wants you to walk away knowing?"

> "There isn't one. Six overlapping, similarly-coloured lines, monthly counts so small some branches have one to three applications a month - every line is mostly noise. A line chart earns its place when the shape of change over time is the finding, and six noisy lines don't add up to six findings."

Run the rebuild cell - single overall trend line, partial final month dropped.

> "One clear line: monthly applications have softened since mid-2025, not grown. If you genuinely need branch-level detail, the fix is small multiples - one mini-chart per branch on the same scale - not cramming six lines into one plot."

---

### Part 5 - Distribution (6 min)

> "Question: what does the shape of applicant income look like - is it skewed, are there extreme values? Here's a first attempt."

Run the bar-by-row-order cell (one bar per applicant, x-axis is file order).

> "The x-axis here is just row order in the file - a meaningless category with 356 near-invisible bars. This chart can't answer 'is the distribution skewed' at all."

Run the histogram cell (30 bins, median line marked in accent colour).

> "This is the correct tool for shape: income is right-skewed, most applicants cluster below three million Naira. And when you need to compare that shape across groups rather than look at one group alone, reach for a box plot instead."

Run the box plot cell (Monthly_Income_NGN by Employment_Type).

> "If the question contains the words spread, typical, skewed, or outliers, that's your cue - histogram for one group, box plot for comparing groups. Never a bar chart of individual records."

---

### Part 6 - Relationship (6 min)

> "Question: does requesting a larger loan track with having a higher income? First attempt."

Run the oversized-opaque-marker scatter cell.

> "The markers are so large and so solid that dense areas merge into a blob - you can't tell if there are five applicants or fifty stacked in that corner. And there's no axis units at all."

Run the rebuild cell (smaller markers, alpha transparency, split and coloured by employment type, axis units labelled).

> "Now you can see through the density: higher income tracks with larger loan requests, across both employment types. Any time you have more than about thirty points on a scatter plot, transparency and marker size aren't decoration - they're the difference between hiding the finding and showing it."

---

### Part 7 - Composition and ranking (7 min)

> "Two quick ones back to back, because they share the same lesson from opposite directions."

Run the exploded, drop-shadowed four-slice pie cell (approved loan purposes).

> "Exploded slices and a drop shadow don't add information here - they add visual weight that makes the two closest slices even harder to compare, and area and angle judgement is already the weakest thing human vision does well."

Run the sorted bar rebuild.

> "Pie charts are legitimate for composition, but only with few categories, big gaps between them, and zero decoration. When in doubt, a sorted bar is the safer default."

Run the alphabetically-sorted, rainbow-coloured ranking cell (applications by branch).

> "For a ranking question, order is the answer. Alphabetical order buries exactly what the question asked for."

Run the sorted, single-accent rebuild.

> "Sort by value, one colour for everything, a second colour reserved only for the single most important bar - here, Lagos, which alone accounts for nearly a third of all applications."

---

### Part 8 - Three ways a chart can quietly lie (10 min)

> "These aren't exotic tricks. Every one is a default setting or a single extra argument away from the good charts you've already seen today."

**Truncated axes.** Run the side-by-side approval rate comparison (y-axis 65-80 vs y-axis 0-100).

> "Same two numbers, 75.0% and 71.6% for Salaried versus Self-Employed. The truncated version on the left makes a 3.4 point real difference look about ten times more dramatic than it is. Start numeric axes at zero unless you have a specific, disclosed reason not to."

**Distorted proportions.** Run the radius-vs-area circle comparison (Lagos 109 applications vs Kano 32).

> "The true ratio is 3.4 times. Scale the circle's radius linearly with the value, and your eye reads it as roughly ten times bigger, because the eye perceives area, not radius - and area scales with the square of the radius. Scale by area instead, and the perceived difference matches the real one."

**Misleading aggregation.** Run the confidence-interval error-bar chart (approval rate by branch, with sample size labelled).

> "Kano's 50% approval rate looks like a solid, alarming finding on its own. It's calculated from only 32 applications, and its confidence interval runs roughly 33% to 67% - far wider than any other branch's. The honest conclusion is 'Kano's rate might genuinely be low, but we don't have enough applications yet to be as confident as the headline number implies' - not 'Kano is broken.' Show the sample size next to any rate or average."

---

### Part 9 - When a table beats a chart, and the checklist (6 min)

> "Last question of the day: the credit committee wants the exact applications count, average income, average loan, and approval rate for all six branches, to quote in a memo."

Run the bar-chart-of-mixed-scales cell (Applications and Approval_Rate invisible next to Avg_Income and Avg_Loan).

> "Applications and the approval rate are invisible slivers next to income and loan figures in the hundreds of thousands. And even if the scales matched, no chart lets you read off '3,248,274' with any precision at all."

Run the styled table cell (sorted by approval rate, formatted figures, background gradient on the approval rate column).

> "When the actual requirement is precise lookup for quoting, a well-formatted table beats any chart. This is one of the few 'which chart' questions where the right answer is no chart at all."

Close by walking the group through the Visualisation Checklist from the slide deck out loud, one line at a time, against the very last chart you built:

> "Does the title state a finding? Does the numeric axis start at zero, or is the exception disclosed? Are both axes labelled with units? Are categories sorted by value where the question is about ranking? Does colour encode something real? Are sample sizes shown wherever a rate could be misread as certain? If a table would answer the question faster, have you used a table? Run every chart you build in the lab through this same list before you submit it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trainee reads the pie chart percentages in Part 3 as the two loan amounts themselves | "Those percentages are each average's share of the sum of both averages - not the averages. A pie chart only ever answers 'what share of one whole is this', and two independent averages aren't parts of a whole." |
| Trainee assumes the histogram in Part 5 is "just a bar chart with more bars" | "A bar chart compares named categories. A histogram bins a single numeric variable to show its spread. Row order or an ID is not a category - that's the whole reason the first attempt in Part 5 failed." |
| Trainee defaults to a rainbow palette because "it looks more finished" | "Colour should encode something real. One colour for the data, a second accent colour reserved for the single most important value - anything more and the eye starts hunting for meaning that isn't there." |
| Trainee doesn't notice the truncated axis in Part 8 because the axis is labelled with numbers | "The eye judges the visual gap between bars, not the printed axis numbers. A labelled-but-truncated axis still exaggerates the gap to anyone reading at a glance - that's exactly why it counts as misleading even when it's technically accurate." |

---

## Up Next

Module 6.3 - Insight Narrative and Business Communication: every chart built today answers a "what" (Kano's rate is lower, income is right-skewed); 6.3 turns a correct, honest chart into a recommendation someone can act on.
