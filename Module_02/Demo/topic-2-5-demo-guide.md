# Demo Guide - Charts and Dashboard Reporting
**Module 2, Topic 2.5 | Estimated duration: 28-32 minutes**

---

## What This Demo Teaches

- Choose the correct chart type for a stated question, before building anything
- Build clearly labelled charts, with a specific title, sensible axis labels, and only the data labels or legend that add information
- Assemble charts into a one-screen dashboard that answers a manager's question, with a connected slicer
- Test a finished dashboard against a stated question to confirm it actually works

---

## Setup - Before the Demo Starts

1. Carry forward the verified PivotTable sheet from Topic 2.4 (Branch by Sales, Branch by Product line cross-tab, working slicer)
2. Write down the manager's stated question for this session before building anything: "Which branch is performing best, and what is driving it?"
3. Have a finished, pre-built copy of the completed dashboard ready as a fallback

> **Instructor note:** the module's real Payment method figures (Ewallet 345, Cash 344, Credit card 311) are close enough in size that they are a genuinely useful example of when a pie chart is the wrong instinct, use them deliberately in Part 1.

---

## Demo Steps

### Part 1 - Why Chart Type Matters, and Choosing the Right One (8 min)

> "A chart's job is to make one comparison obvious at a glance. The wrong chart doesn't just look worse, it can hide the answer or suggest the wrong one."

- Show the three Payment method counts (Ewallet 345, Cash 344, Credit card 311) as a nine-slice-style cluttered pie chart mock-up first, then as a clean sorted bar chart, and ask which one answers "which payment method is most common?" faster
- Walk through the three chart families against real questions: "which branch sold the most?" (bar), "how did sales trend across a period?" (line), "what share of total sales did each branch contribute?" (pie, used sparingly)
- State the rule plainly: "a stated question rarely names the chart type, it describes what needs to be seen, read the question first"

**Ask students:** why would a line chart be the wrong choice for comparing the three branches?

> "Because Branch has no natural order. A line implies a trend across a sequence, and there isn't one here, that's exactly the kind of chart choice that can quietly mislead someone."

### Part 2 - Building and Labelling a Chart from the Pivot Table (8 min)

> "Now we build straight from the pivot table verified last topic, not from scratch."

- Click inside the Branch-by-Sales pivot table, Insert tab, PivotChart, choose a horizontal bar chart, sorted largest to smallest, confirming Giza leads
- Add a second chart, this time from the Branch-by-Product-line data: a bar chart of total Sales by Product line, and point out Food and beverages leads at 56,144.84, closely followed by Sports and travel at 55,122.83, close enough that a bar chart is the right call, not a pie chart
- Replace the default "Chart Title" on both with a specific title stating what each chart shows, add axis labels, and remove the legend from the single-series chart since it adds no information
- Delete default gridlines and apply one highlight colour to the leading bar on each chart

> "Compare that to the default chart Excel gave us five minutes ago. Nobody has to ask what either of these shows now."

### Part 3 - Assembling the Dashboard (8 min)

> "Two good charts sitting on two different sheets are not a dashboard yet. A dashboard is one screen, no scrolling, that answers the question."

- Create a new sheet dedicated entirely to the dashboard, separate from the raw data and pivot sheets
- Hide gridlines (View tab, untick Gridlines) for a clean, report-like appearance
- Move both charts onto this sheet, align their edges to a grid, and place the most important chart, Sales by Branch, in the top-left, where the eye lands first
- Add the Branch slicer from Topic 2.4 to the top of the dashboard sheet, then use Report Connections to link it to both charts

> "Watch what happens when I click Giza." [click the slicer] "Both charts just responded together. That's the difference between a page of charts and an actual report."

### Part 4 - Testing the Dashboard Against the Manager's Question (6 min)

> "Everything built so far is unproven until this last step."

- Read the written question aloud again: "Which branch is performing best, and what is driving it?"
- Try to answer it using only what's visible on the dashboard, no clicking into source data, and time how long it takes
- Repeat with a second related question, given cold, that trainees have not seen prepared for: "which product line should Giza stock more of?"
- If either answer takes more than a few seconds to find, rearrange the dashboard rather than add another chart

> "A slow answer here isn't a failure, it's useful feedback. It tells you the layout needs work, not that you need a fourth chart."

---

## Final State of the Workbook

A dedicated dashboard sheet, gridlines hidden, containing two clearly labelled, sorted bar charts (Sales by Branch, Sales by Product line), a Branch slicer connected via Report Connections to both charts, and a documented test against the stated manager's question. This dashboard, and the pivot tables behind it, carry forward into Topic 2.6, where the source data import and cleaning get automated.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Choosing a pie chart because it looks more finished, on data where the slices are close in size | "This is exactly the instinct this topic pushes back on. If a manager can't tell the slices apart at a glance, the chart has failed, however polished it looks." |
| Leaving a chart's default title in place | "This is named directly in the common mistakes for this topic. A generic title means someone has to ask what they're looking at, which defeats the purpose of a chart." |
| Forgetting to connect the slicer to every chart on the dashboard | "This is the subtle one, it usually isn't caught until someone clicks the one chart that was missed. Test every slicer button before calling a dashboard finished." |

---

## Up Next

Topic 2.6, Power Query, automates the import and cleaning steps behind everything built here, so the next fresh export takes one click instead of a full manual pass.
