# Demo Guide - Hypothesis Testing
**Module 4, Topic 4.4 | Estimated duration: 24-28 minutes**

---

## What This Demo Teaches

- Stating a null hypothesis and an alternative hypothesis for a business comparison
- Calculating a p-value in Excel using T.TEST to compare two groups
- Interpreting a p-value correctly, using the 0.05 significance threshold and precise language
- Recognising that failing to reject the null hypothesis is not the same as proving nothing changed
- Distinguishing statistical significance from business importance, and recommending accordingly

---

## Setup - Before the Demo Starts

1. Open `Topic-4.4-Aduke-Stores-Dataset.xlsx` and confirm the **Ikeja Checkout Pilot**, **Yaba Checkout Pilot**, and **Basket Value Trial** sheets are all visible.
2. Keep the **Tutor Answer Key** sheet open in a separate window, not projected, it holds every formula and expected value used in this demo.
3. Confirm Excel recognises T.TEST (Excel 2010 or later).

> **Instructor note:** Yaba's result in Part 2 is deliberately not significant. Do not treat this as a disappointing or wasted result when you present it, a non-significant p-value is a genuine, useful finding, and the demo depends on trainees seeing that reaction modelled correctly.

---

## Demo Steps

### Part 1 - Stating the Hypotheses and Testing Ikeja (7 min)

> "Ikeja branch trialled a new quick checkout lane. Sales in the 20 days after look higher than the 20 days before. The operations director wants to know: is that a real improvement, or just a good month?"

State the hypotheses out loud before touching Excel.

> "H0, the null hypothesis, our starting assumption: average daily sales are the same before and after the pilot, and any difference we see is random noise. H1, the alternative: they are actually different. We assume H0 until the data gives us a strong enough reason to think otherwise."

On the **Ikeja Checkout Pilot** sheet:

```
=AVERAGE(B6:B25)              → 283,100
=AVERAGE(E6:E25)              → 322,590
=T.TEST(B6:B25,E6:E25,2,3)    → 0.0003
```

> "p equals 0.0003. If the pilot truly did nothing, we'd only expect to see a gap this large by pure chance about 0.03% of the time. That's far below the usual 0.05 threshold, so we call this statistically significant."

### Part 2 - Testing Yaba, and Learning to Report a Non-Significant Result (7 min)

> "Yaba branch ran the identical pilot on the same dates. Let's find out if it worked there too."

```
=AVERAGE(B6:B25)              → 284,110
=AVERAGE(E6:E25)              → 280,490
=T.TEST(B6:B25,E6:E25,2,3)    → 0.80
```

> "p equals 0.80. Far above 0.05. Notice the mean actually went down slightly, and this test tells us that small drop is well within normal day-to-day variation."

**Ask students:** "How should we word this finding to the Yaba branch manager? Try it in one sentence before I give you the answer."

> "The precise phrase is: we do not have enough evidence that the pilot changed sales at Yaba. Not: the pilot proved sales did not change. Those sound similar and mean very different things. Absence of evidence is not evidence of absence."

### Part 3 - When a Significant Result Still Isn't Enough (10 min)

> "One more test, company-wide this time. Head office trialled a new digital price display and sampled 500 transactions before and 500 after."

```
=AVERAGE(B6:B505)              → 2,484.09
=AVERAGE(E6:E505)              → 2,518.46
=T.TEST(B6:B505,E6:E505,2,3)   → 0.026
```

> "p equals 0.026. Below 0.05. Statistically significant. A colleague sees this number and drafts a recommendation to roll the display out to every branch immediately. Before we sign off on that, let's look at what actually changed."

Calculate the difference in means: 2,518.46 minus 2,484.09.

> "34 naira. On a roughly 2,500 naira basket, that's about 1.4%. With 500 transactions in each group, even a small, genuine difference like this one is easy to detect as statistically significant. That's not a flaw in the test, it's exactly what large samples are good at. But it means p equals 0.026 tells us the difference is probably real, it tells us nothing about whether a 34 naira lift is worth the cost of installing new displays at every remaining branch."

> "The recommendation isn't yes or no yet. It's: compare the total projected revenue from that 34 naira lift, chain-wide, against the full rollout cost, before anyone commits budget."

### Part 4 - The Two Things Every Test Result Needs (4 min)

> "Three tests, three lessons. Say them back to me."

Confirm as a group: significance tells us if a difference is likely real, not whether it's large enough to matter; a non-significant result is information, not failure; every test result needs both a p-value and a sense of the actual size of the effect before it goes into a recommendation.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| States Yaba's non-significant result as "the pilot proved nothing changed" | "Proved is too strong. We simply don't have enough evidence of a change here. What would 'proved nothing changed' actually require?" |
| Mixes up which column is Before and which is After in the T.TEST formula | "Check which column header says Before and which says After before you read the p-value, not after." |
| Treats the Basket Value Trial's significant p-value as automatic grounds for a full rollout | "What was the actual size of the difference in naira? Does that number, on its own, tell you the rollout is worth it?" |
| Assumes a larger sample size makes a result less trustworthy because it's "easier" to get significance | "A large sample doesn't make the test unreliable, it makes it more sensitive. That's exactly why small, real effects show up as significant, and exactly why we need to look at effect size separately." |

---

## Up Next

Topic 4.5, AI as Statistics Tutor and Interpreter, is where AI enters this module for the first time. Every skill from Topics 4.1 to 4.4 becomes a checklist for catching an AI assistant when it overstates what a result like these actually proves.
