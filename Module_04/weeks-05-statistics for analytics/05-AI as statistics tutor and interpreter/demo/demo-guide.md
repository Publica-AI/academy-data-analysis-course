# Demo Guide - AI as Statistics Tutor and Interpreter
**Module 4, Topic 4.5 | Estimated duration: 22-26 minutes**

---

## What This Demo Teaches

- Writing a role, context, data, and constraints prompt to ask an AI assistant for a statistical interpretation
- Recognising the four common ways an AI-generated interpretation can overstate or misstate a result
- Applying a five-point verification checklist to an AI-drafted interpretation before trusting it
- Rewriting a flawed AI interpretation into an accurate, business-ready version

---

## Setup - Before the Demo Starts

1. Open `Topic-4.5-Aduke-Stores-AI-Verification-Kit.xlsx` and confirm the **Statistical Outputs Reference** and **AI Response - Guided** sheets are both visible.
2. Have a free AI assistant open in a browser tab as an optional live alternative. The pre-built response on the **AI Response - Guided** sheet is the primary version for this demo, not a fallback, so the same planted errors are guaranteed to appear regardless of network access.
3. Trainees should already have completed Topics 4.1 to 4.4 by hand. This demo assumes they know what a correct interpretation looks like, it does not re-teach any of the four skills, it audits them.

> **Instructor note:** Do not tell trainees how many errors are planted in the response before they start reading. Let the five-point checklist do the work of finding all of them, rather than trainees stopping once they've found a round number.

---

## Demo Steps

### Part 1 - Why the Manual Method Came First (4 min)

> "Every topic this week, we calculated everything by hand before touching AI. That was deliberate. Today we finally bring AI in, and you're about to see exactly why the order mattered."

> "An analyst pasted this week's Ikeja results into an AI assistant and asked for a plain-language summary for the branch manager. Read the prompt it used first."

Display the prompt from the **AI Response - Guided** sheet: role, context, the regression and checkout pilot figures, and a 150-word constraint.

> "Role, context, data, constraints. That's a well-built prompt. A good prompt does not guarantee a correct answer, and that's exactly what we're about to check."

### Part 2 - Reading the Response Cold (5 min)

Display the fabricated AI response in full, without commentary yet.

> "Read this the way the analyst first did, quickly, as a whole. Does it sound confident? Does it sound correct?"

**Ask students:** "Before we check anything, who in the room would have sent this straight to a branch manager without changes?"

> "Confident and correct are not the same thing. That gap is the entire reason this topic exists. Let's find out where it fails."

### Part 3 - Running the Five-Point Checklist (12 min)

> "Five questions, every time, no exceptions. Do the numbers match what we calculated? Is any causal language actually justified? Are the data's limits respected? Is significance kept separate from importance? Is anything important missing?"

Work through the response line by line against the **Statistical Outputs Reference** sheet, catching each planted error as a group:

> "'Proves conclusively that increasing marketing spend causes higher sales.' Check question two. Regression shows association, never proof of causation on its own."

> "'R² of 0.61 means the model is correct 61% of the time.' Check question one against the reference sheet. That is not what R-squared measures, it's the share of variation explained, not a hit rate."

> "It predicts sales at 150,000 naira spend with no caveat at all. Check question three. We tested spend up to 69,535 naira. This is extrapolation, presented as fact."

> "'Only a 0.03% chance the pilot had no effect... 99.97% certainty the checkout lane caused the increase.' Check question one again, and question two. This is a classic misreading of what a p-value actually measures, and it smuggles a causal claim in alongside it."

> "Four errors, all different kinds. Two misstated numbers, one unflagged limit, one overstated cause. This is what 'confident and correct are not the same thing' looks like up close."

### Part 4 - Rewriting the Corrected Version (5 min)

> "Finding the errors isn't the job. The job is still getting an accurate summary to the branch manager, so we fix this, we don't bin it."

Rewrite the response live, sentence by sentence, keeping the same plain-language tone and the same 150-word constraint from the original prompt:

> "Spend and sales are strongly associated, R-squared of 0.61 means spend explains about 61% of the variation in sales, this does not prove spend directly causes the increase. This model is reliable within the tested range, 8,584 to 69,535 naira, not beyond it. The checkout lane result, p equals 0.0003, is very unlikely to be due to chance, but this alone does not prove the lane itself was the cause."

> "Same plain language, same length limit, same numbers. The only thing that changed is accuracy. That's the whole skill this topic teaches: not writing from scratch, correcting."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Accepts the AI response as correct because it reads fluently and uses the right technical terms | "Fluent and accurate are different qualities. Run it through the checklist regardless of how polished the language sounds." |
| Finds the causation error but stops there, missing the R-squared and p-value misreadings | "That's one error type out of four possible ones. Go back through all five checklist questions in order, not just the one that jumped out first." |
| Argues the AI's prediction at 150,000 naira must be fine because the arithmetic is correct | "The arithmetic is correct. The question is whether we have any evidence for how the relationship behaves at that spend level. We don't." |
| Wants to skip the checklist and just trust whichever AI tool the class is using | "That is exactly the shortcut this topic exists to prevent. The checklist doesn't change based on which tool produced the answer." |
| Rewrites the entire response from scratch instead of correcting the four flagged sentences | "We're not starting over. What in the original draft was already accurate and worth keeping?" |

---

## Up Next

This closes Week 5. The interpretation worksheet, Module 4's assessment, checks exactly this skill: reading a statistical result correctly and stating plainly what it does and does not prove. Module 5, Python for Data Analysis, begins in Week 6.
