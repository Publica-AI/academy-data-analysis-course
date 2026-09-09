# Demo Guide - Forecasting with AI Support
**Module 8, Topic 8.2 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Building a trend forecast by hand first, so its single assumption is visible
- Spotting the partial period at each end of a series before it destroys the trend
- Reading R-squared as a statement about how much the line is entitled to claim
- Turning a point estimate into a defensible range using the fit's own errors
- Beating the naive baseline, or admitting the model is not worth using
- Using an AI assistant to stress-test a forecast rather than to produce one

---

## Setup - Before the Demo Starts

1. `swiftroute_q3_cleaned.xlsx` in this folder, carried forward from Topic 8.1
2. `build_forecast.py` in this folder as the fallback and the worked solution
3. `q4_forecast.png` and `swiftroute_q4_forecast.xlsx` pre-built, in case the live run stalls
4. A free-tier AI assistant open in a browser tab
5. A whiteboard or blank slide for the two forecasts, drawn side by side

> **Instructor note:** signal in the first minute that no machine learning happens today. This is arithmetic plus judgement. Topic 8.3 handles the vocabulary, and nobody builds a model in either.

> **Instructor note:** the partial-week finding in Part 2 is the spine of this session. Do not preview it. Let the room watch the slope flip sign.

---

## Demo Steps

### Part 1 - One Assumption, Made Explicit (8 min)

> "Adaeze needs a number for next quarter's capacity planning. I am going to give her one, and the entire method is a straight line. That sounds too simple until you say the assumption out loud: whatever has been happening for the last twelve weeks keeps happening for the next thirteen. Every forecast has an assumption. Most of them hide it."

**Group the cleaned deliveries by calendar week and show the fourteen weekly totals.**

| Week starting | Deliveries |
|---|---|
| 29 Jun | 190 |
| 6 Jul | 271 |
| 13 Jul | 264 |
| ... | ... |
| 21 Sep | 298 |
| 28 Sep | 113 |

> "Fourteen weeks. Look at the first and the last."

---

### Part 2 - The Partial Weeks, and What They Do (10 min)

**Ask students:** "Before I fit anything, is this business growing or shrinking?"

*(Take a show of hands. Most rooms say growing, because the middle of the series rises.)*

**Fit the line on all fourteen weeks and show the result.**

> "Slope minus nought point three four seven deliveries per week. Shrinking. R-squared nought point zero zero zero eight, which means the line explains essentially nothing. On this evidence I would tell Adaeze her business is flat to declining."

Pause.

> "That answer is wrong, and nothing in the arithmetic is wrong. Q3 starts on a Wednesday and ends on a Wednesday. The first calendar week holds three days and the last holds three days. A hundred and ninety and a hundred and thirteen against a typical two hundred and seventy. Those two weeks are not low, they are short."

**Drop the two partial weeks. Refit on the twelve complete ones.**

| | All 14 weeks | 12 complete weeks |
|---|---|---|
| Slope | -0.347 per week | +2.948 per week |
| R-squared | 0.0008 | 0.3262 |

> "Same file, same method, opposite conclusion. The only thing that changed is which rows I was entitled to use. This is the single most common way a forecast goes wrong, and it never announces itself."

---

### Part 3 - What the Line Is Entitled to Claim (8 min)

> "Positive slope, about three more deliveries each week. Before anyone gets excited, read the R-squared: nought point three three. The trend explains about a third of the week to week movement. Two thirds is noise I cannot account for."

**Show the residuals: standard deviation 16.0 deliveries, mean absolute percentage error 3.96 per cent.**

> "So the honest sentence is not 'we forecast four thousand and forty-nine deliveries'. It is 'we expect somewhere between three thousand eight hundred and forty and four thousand two hundred and fifty-seven, and our best single guess is around four thousand'."

**Project thirteen weeks forward and read the numbers.**

| Q4 2026 forecast | Deliveries | Revenue |
|---|---|---|
| Point estimate | 4,049 | ₦13,386,188 |
| Low, minus one residual sd | 3,840 | ₦12,736,564 |
| High, plus one residual sd | 4,257 | ₦14,035,812 |
| Naive baseline, Q3 weekly mean held flat | 3,570 | ₦12,074,790 |

> "The naive baseline matters. If my clever line cannot beat 'next quarter looks like this quarter', I should ship the baseline and save everyone the meeting. Here it does differ, by about four hundred and eighty deliveries, and that difference is worth planning around."

---

### Part 4 - Stress-Testing with the Assistant (10 min)

> "Now the assistant, and notice what I am using it for. Not to produce the forecast. To attack it."

**Give it the numbers, not the file:**

> "I have 12 complete weeks of delivery counts from one quarter. A linear trend gives a slope of +2.95 deliveries per week with an R-squared of 0.33 and residual standard deviation of 16. I have projected 13 weeks forward to 4,049 deliveries. Argue against this forecast. What would make it wrong?"

**Read what comes back and sort it live into two piles, out loud: things it can know, and things it cannot.**

Things it can reasonably raise: one quarter is thin history, a linear trend cannot see seasonality, R-squared of 0.33 does not support a precise point estimate, thirteen weeks is a long extrapolation from twelve.

Things it cannot know and may assert anyway: December volumes, Nigerian fuel price movements, whether SwiftRoute is opening routes.

**Ask students:** "It just told us Q4 will spike because of the festive season. Is that a finding?"

> "It is a hypothesis, and a plausible one. It is not in our data, because our data stops in September. Write it down as a question for Adaeze, not as a line in the forecast. The moment you cannot point at the row that supports a claim, it stops being analysis."

---

### Part 5 - Saying It Out Loud (5 min)

**Deliver the forecast the way it should be delivered, in three sentences.**

> "We expect between three thousand eight hundred and four thousand two hundred and fifty deliveries next quarter, most likely around four thousand. That is based on twelve complete weeks, and the trend explains about a third of the week to week variation, so plan against the range rather than the single figure. It also assumes nothing changes about the routes or the season, and one of those assumptions is probably worth a conversation."

> "Nobody in that sentence was misled, and nobody had to be told a number I could not defend."

---

## Final State of the Analysis

`swiftroute_q4_forecast.xlsx`, four sheets: `weekly_actuals` (all 14 weeks), `complete_weeks` (the 12 used), `q4_forecast` (13 weeks with a low and high band) and `summary` (every coefficient, including the slope and R-squared you get if the partial weeks are left in). `q4_forecast.png` is the chart.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| A trainee reports a negative slope | "Check whether the first and last calendar weeks are in the fit. They are partial, and they will drag the line down at both ends." |
| A trainee quotes 4,049 as the forecast with no range | "Ask them what R-squared they got. A third of the variation explained does not support a single number to four significant figures." |
| Weekly totals do not match the guide | "Check the week boundary. This analysis uses weeks ending Sunday. A different convention shifts every total." |
| A trainee includes the assistant's festive-season claim in the forecast | "Ask which row of the data supports it. There is no December in this file. It is a question for the business, not a finding." |
| R-squared is treated as a pass or fail mark | "It is not a grade. It is a statement about how much the line is entitled to claim, and 0.33 is a perfectly usable answer if you report the range with it." |
| A trainee says the forecast is useless because R-squared is low | "Compare it against the naive baseline. If it beats holding this quarter flat, it is earning its place." |

---

## Up Next

Topic 8.3 - Machine Learning Concepts for Literacy. You have just made a prediction with a straight line. The next topic is about the vocabulary people use when a straight line is not enough, and about knowing exactly where an analyst's job ends.
