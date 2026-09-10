# Demo Guide - AI-Assisted Exploration and Drafting
**Module 6, Topic 6.5 | Estimated duration: 48-50 minutes**

---

## What This Demo Teaches

- Uploading a clean dataset to an AI tool and interrogating it with structured, context-rich prompts
- Applying the three-step verification loop (trace, reproduce, compare) to any AI-surfaced claim before trusting it
- Marking up an AI-drafted narrative for vague, wrong, or unverifiable claims, using the red-pen method
- Rebuilding a verified narrative from scratch using the Module 6.3 Context, Finding, Implication, Recommendation structure, rather than polishing the AI's draft
- Assembling the two attachments - a prompt log and a verification note - that make an AI-assisted deliverable auditable

---

## Setup - Before the Demo Starts

1. Trainees must have `ajebo_finance_loan_applications_CLEANED.csv` (356 rows) from Module 6.1, and should have the Module 6.2 charts and Module 6.3 narratives on hand for comparison, since this topic's entire verification exercise checks AI claims against those established figures.
2. Trainees need access to one of the programme's free-tier AI assistants (Claude, ChatGPT, or Gemini, per Module 1's toolkit).
3. Have the AI-drafted narrative from Section 4 ready to distribute as a printout or a shared document trainees can annotate directly - this is the centrepiece exercise and needs to be markable, not just readable on a shared screen.

> **Instructor note:** if you plan to demonstrate a live exploratory prompt against an AI assistant in Part 2, have a saved screenshot or transcript of a prior real response ready as a fallback - live AI output is not reproducible on demand, and a network or service issue should not stall the session. The red-pen exercise itself (Part 4) needs no live AI call at all - the flawed narrative is fixed text, provided precisely so the exercise survives without one.

---

## Demo Steps

### Part 1 - Why this matters (5 min)

> "An AI assistant can explore a dataset and draft a narrative significantly faster than a human analyst. It can also state a wrong number with exactly the same confident, fluent tone as a right one. Tone carries zero information about factual correctness. This topic is not about whether to use AI for this work - the programme assumes you will. It's about building the habit of checking every AI-surfaced claim before it reaches a reader, the same discipline Module 6.1 built for cleaning and Module 6.2 built for charts, now applied to narrative text."

> "And the data-safety check comes first, every time, no exceptions. AJEBO's dataset is safe to upload because Module 6.1's design guaranteed no real personal data is present. This is not a one-time check - it's a habit for every new file, especially once a dataset has been merged or extended beyond its original safe version."

---

### Part 2 - Exploratory prompting (6 min)

> "A good exploratory prompt gives the assistant context, the data, a specific task, and an output format - the same structure Module 1 taught for prompt fundamentals, now applied to analysis instead of code."

Read the weak prompt aloud: *"Tell me about this data."*

> "Too open-ended. It produces generic observations with no way to verify any of them."

Read the stronger prompt aloud: *"This is loan application data for a Nigerian microfinance bank, already cleaned. Identify the three most notable patterns in approval rates across branches, and for each one, tell me exactly which columns and calculation you used, so I can verify it myself."*

> "Notice this prompt explicitly asks the assistant to show its working. That's the single most important habit in this topic: never accept a claim you can't trace back to a specific calculation."

---

### Part 3 - The three-step verification loop (5 min)

> "Every AI-surfaced claim gets checked the same way you'd check your own work in Module 6.1: re-run the calculation from the source data. This isn't slower than trusting the output - it's the difference between a claim and a fact."

Walk through the three steps: Trace it (ask which columns and calculation produced the claim, if not already stated), Reproduce it (run the calculation yourself, independently, tool doesn't matter), Compare (if it matches, verified; if not, the claim is wrong until proven otherwise).

> "Never split the difference or assume you made the error when your number disagrees with the AI's. The AI is not the source of truth here - the data is."

---

### Part 4 - The red-pen exercise, live (17 min)

> "This is the centrepiece technique for this topic. Here's a narrative an AI assistant might plausibly draft from the AJEBO dataset."

Distribute or display the full AI-drafted narrative (the four paragraphs: growth claim, Kano branch performance, income-loan relationship, overall summary).

**Ask students:** "Before I show you anything, mark up every sentence you think is vague, wrong, or unverifiable. Aim for at least six distinct issues. Take five minutes on your own first."

Give trainees genuine working time, then walk through the answer key one problem at a time:

> "One: 'strong growth... grown significantly' - wrong. Module 6.2 established the real trend: volume has softened, not grown, roughly 23% down from its early-2025 average. This is the confidently-stated, plausible-sounding, completely incorrect claim this whole topic exists to catch."

> "Two: 'Kano branch has the lowest approval rate at approximately 35%' - wrong number. The verified figure from Module 6.2 is 50%, not 35%. Always re-run the calculation - never accept a rounded or approximate figure without checking it against the source."

> "Three: 'this is likely because Kano serves a riskier customer base' - an unverifiable claim presented as fact. Nothing in the dataset establishes why Kano's rate is lower. Module 6.3's insight for this same finding correctly stopped at naming the uncertainty - genuine risk difference or inconsistent criteria application - instead of picking an explanation."

> "Four: no sample-size caveat anywhere near the Kano claim - missing context. Kano's n=32 and its wide confidence interval, roughly 33 to 67%, is the single most important fact about this finding, and it's completely absent."

> "Five: 'self-employed applicants... because they have more unpredictable income needs' - overclaimed causation and an invented mechanism. The data shows self-employed applicants request larger loans on average, verified at NGN 3.82 million versus NGN 3.13 million. It says nothing about why, and 'unpredictable income needs' was invented, not observed."

> "Six: 'a strong relationship... which makes sense intuitively' - vague. No number is given at all - the verified figure is r=0.72. 'Makes sense intuitively' adds a feeling, not evidence, and wouldn't survive the Module 6.3 'so what' test."

> "Seven: 'overall, AJEBO's loan book appears healthy... no major causes for concern' - an unsupported summary judgement that directly contradicts the Kano finding two paragraphs earlier. The AI's own draft doesn't agree with itself."

> "That's seven distinct issues in four short paragraphs. If you found six, you found the target. If you found fewer, go back through - a confident tone is not a reason to skip a paragraph."

---

### Part 5 - Rebuilding the narrative, not polishing it (8 min)

> "This is not a polish pass on the AI's text. It's a total rebuild from verified facts."

Walk through the rebuilt structure for the Kano finding using the Module 6.3 framework: Context (verified overall loan trends), Finding (Kano's approval rate at 50%, n=32), Implication (the wide confidence interval means genuine caution is needed before concluding anything), Recommendation (audit rejection-reason consistency against a comparable branch before any policy change).

> "None of this rebuild borrows a single sentence from the flawed draft - it's built the same way Module 6.3 built the original Kano narrative, straight from the verified numbers."

---

### Part 6 - What "verified" looks like in the deliverable (5 min)

> "Every AI-assisted deliverable in this programme needs two attachments alongside the final narrative, not just the narrative itself."

Explain the prompt log (the actual prompts used, in order - graded evidence of AI-fluency ladder Level 3 for Weeks 7-8, and something that carries forward into the Module 9 capstone prompt log) and the verification note (a one-line note per retained claim on exactly how it was checked - for example, "re-ran groupby in pandas, matches AI's figure" or "AI's figure was wrong, corrected from 35% to 50%, source: Module 6.2 notebook").

> "The verification note has to say how a claim was checked, not just that it was. 'Verified' with nothing behind it is exactly the kind of confident-but-empty statement this whole topic is built to catch."

---

### Part 7 - Practical activity and Module 6 recap (5 min)

Walk through the five practical-activity steps: confirm data safety, prompt the AI using the stronger-prompt pattern for three new patterns not already covered in 6.2-6.3, trace and reproduce each one independently, red-pen mark up the AI's draft, and submit all four deliverables - the prompt log, the marked-up draft, the verification note, and the final corrected narrative.

> "Step back for a second and look at what this week actually built. The same AJEBO dataset, cleaned and documented in 6.1, charted honestly in 6.2, turned into a narrative that survives scrutiny in 6.3, published as a public, reproducible portfolio piece in 6.4, and now produced again with AI assistance under full verification discipline in 6.5. Same data, same findings, five different professional skills."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trainee treats the AI's confident tone in the red-pen exercise as a reason to trust the claim | "Tone carries zero information about factual correctness - the AI states wrong numbers exactly as fluently as right ones. That's the entire premise of this exercise." |
| Trainee verifies the first claim in a narrative and assumes the rest are equally solid | "Check every claim that will appear in the final deliverable, not a sample of them. The red-pen exercise found seven separate issues in four short paragraphs - solid-sounding claims and wrong ones sit right next to each other." |
| Trainee skips the red-pen markup and goes straight to a cleaned-up rewrite | "The markup is submitted for a reason - it's the evidence that verification actually happened, not just a polish pass. No markup, no proof of the work." |
| Trainee lets the AI draft's paragraph structure and ordering carry over into the final narrative | "An AI draft is a source of candidate claims, not a template. Module 6.3's Context, Finding, Implication, Recommendation structure still governs the final version - that's why Part 5 was a total rebuild, not an edit." |

---

## Up Next

Module 7 - Business Intelligence with Power BI: Week 8 moves this analysis into a live dashboard product and launches the capstone project.
