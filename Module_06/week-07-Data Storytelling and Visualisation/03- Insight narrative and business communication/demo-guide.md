# Demo Guide - Insight Narrative and Business Communication
**Module 6, Topic 6.3 | Estimated duration: 50-55 minutes**

---

## What This Demo Teaches

- Structuring analytical findings into the four-part Context, Finding, Implication, Recommendation framework
- Writing insight statements that pass the "so what" test, rather than restating a chart in words
- Using a lightweight insight-quality checker as a first pass, while recognising what it cannot judge for you
- Adapting the same underlying finding for a technical audience and a non-technical audience without changing the facts

---

## Setup - Before the Demo Starts

1. Trainees must have `ajebo_finance_loan_applications_CLEANED.csv` (356 rows) saved from Module 6.1 - this topic writes about the findings, it does not reclean or rechart the data.
2. Trainees should have Module 6.2 open or fresh in mind - this demo reuses the exact findings established there: Kano's approval rate, the income-loan correlation, the self-employed vs salaried loan gap, and the graduate approval gap.
3. Open `Topic_6_3_insight_narrative.ipynb` and run the Setup cell (pandas, numpy, matplotlib, seaborn, plus the same house colours as Module 6.2). No new libraries to install - `re` is used later for the insight checker and is part of the Python standard library.

> **Instructor note:** the slide deck has a leftover placeholder on the Key Takeaways slide ("Up Next: Arithmetic & Operators") that does not belong to this topic - it is inconsistent with the deck's own closing slide, the notebook, and the reference markdown, all three of which correctly say Module 6.4, GitHub for Portfolios. Skip past it without comment if it comes up on screen, and use "Module 6.4 - GitHub for Portfolios" when you bridge to the next session.

---

## Demo Steps

### Part 1 - Why narrative matters (5 min)

> "Modules 6.1 and 6.2 gave you a clean dataset and honest charts. AJEBO's credit committee does not want a bar chart dropped into a board pack with no accompanying text - they want to know what decision the chart supports. A chart answers what happened. It never answers why does this matter, or what should we do about it."

Walk through the finding-versus-insight table on the slide: same Kano approval-rate fact, stated once as a bare observation ("Kano's approval rate is 50%") and once with its business implication attached.

> "A finding gets a nod and nothing else. An insight gives the reader something to act on, or a specific question to investigate. Turning a finding into an insight is the whole of today's topic."

---

### Part 2 - Computing the real numbers behind four findings (8 min)

> "Before we write a single insight sentence, we compute the actual numbers behind it - nothing in this session gets asserted without a calculation to back it up, and that traceability is itself the discipline we're teaching."

Run the branch-stats cell (approval rate and n per branch, sorted) and the Kano 95% confidence-interval cell.

> "Kano's rate is the lowest of the six branches, but look at that sample size - only 32 applications - which is exactly why we compute a confidence interval before we say anything definitive about it."

Run the second cell: income-loan correlation, the self-employed versus salaried loan and income gap, and the graduate versus non-graduate approval gap.

> "Every number in the before-and-after table on the next slide - r=0.72, the 22% loan gap, the 16-point approval gap - came straight out of this cell. Compare the weak version of each finding against the sharp version: the sharp one always names a number and an implication, never just a better-phrased restatement."

---

### Part 3 - A lightweight insight-quality checker (7 min)

> "This is a first-pass tool, not a replacement for your own judgement - a simple function that flags common 'so what'-test failures: vague hedge words, no number present, and no implication or action language."

Run the `check_insight()` definition cell, then test it on the vague sentence ("The data shows some interesting patterns in loan amounts") and the sharp income-loan sentence.

> "Notice it flags the vague sentence on three separate counts, and passes the sharp one cleanly."

**Ask students:** "Now watch what happens when I run it on this one - 'Kano is underperforming and should be investigated.' What do you think it will say?"

Run the check on that sentence and let the class see the result.

> "Look closely - it only flagged the missing number. It did not flag 'should be investigated' as vague, because 'should' happens to sit in its implication-word list. But this is exactly the weak recommendation we're about to warn against - no owner, no method, no way to know when it's resolved. This is the checker's real limitation, demonstrated live: it can catch an absent number or an absent implication word, but it cannot judge whether an implication is actually specific. The tool narrows what to look for. It does not replace looking."

---

### Part 4 - Building the four-part narrative live (8 min)

> "Context, Finding, Implication, Recommendation. Let's build all four for Kano, assembling each part directly from the numbers we already computed in Part 2 - not from memory."

Run the narrative-assembly cell (an f-string pulling `kano.approval_rate`, `ibadan.approval_rate`, `gap_points`, `kano.n`, and the confidence interval directly into the four sections).

> "Every figure in that printed narrative - the 50%, the 73%, the 23-point gap, n=32, the 33 to 67% interval - came from a pandas calculation two cells above, not an approximate recollection. That's the entire point of this exercise. And look at the recommendation specifically: 'pull a manual sample of Kano's rejected applications and compare against Ibadan, then revisit once the sample reaches 60 to 80 applications' is specific and falsifiable. 'Investigate further' is not a recommendation at all - it has no owner, no method, and no way to know it worked."

---

### Part 5 - Before-and-after critique: weak vs sharp (5 min)

> "Same method Module 6.2 used on charts, now applied to writing."

Read the two weak-versus-sharp pairs aloud from the notebook: the "interesting patterns in loan amounts" pair, and the "Kano is underperforming" pair (the same weak sentence the checker just let slip through in Part 3).

> "A sharp insight names a number, a comparison, a mechanism or reason, and a next step. A weak one could be true of almost any dataset and still say nothing - which is exactly why it survives a casual read."

---

### Part 6 - Adapting for two audiences (7 min)

Run the cell that reprints the verified correlation figure once.

> "Same underlying number, r=0.72, feeding two completely different pieces of writing."

Read the technical-audience version aloud (Pearson correlation, single-variable proxy, noisier at the high-income tail), then the non-technical version (applicants who earn more tend to ask for bigger loans - a solid first check for unusually large requests).

> "What changed is vocabulary and emphasis - the statistic became a plain-language pattern, and the implication shifted from a modelling suggestion to an operational check. What did not change is the underlying finding itself - neither version overstates or understates what r=0.72 actually shows. Sending the technical write-up to the credit committee, or the plain-language version to a data science lead who needs the actual statistic, undermines trust in both directions."

---

### Part 7 - Setting up the practical activity (5 min)

> "You'll choose two of five findings and write a full narrative plus a non-technical paragraph for each. Four of the five already have their numbers verified from Part 2. The fifth - the decline in monthly application volume - you verify yourselves, so let's do that one together now as a model."

Run the volume-decline verification cell (first-half versus second-half monthly average, partial final month excluded, as in Module 6.2).

> "Notice this cell drops the same partial final month Module 6.2 dropped, for the same reason. Whichever two findings you pick, verify the number with your own calculation before you write a single sentence about it - don't write from memory or from what you think the Module 6.2 chart showed."

Close by reminding trainees to run their own draft sentences through `check_insight()` before submitting, but to read each pass result with the same scepticism the class just applied to the Kano example in Part 3.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trainee treats a `check_insight()` "PASSES" result as proof the sentence is finished | "The checker only catches an absent number or an absent implication word - it cannot tell whether the implication is actually specific. We saw it pass 'should be investigated' for exactly this reason. Read your own sentence again after it passes." |
| Trainee restates the chart instead of writing an insight ("Kano's bar is shorter than the others") | "That's a caption, not a narrative. State the number and its comparison, then move straight to the implication - what does the gap mean for a decision?" |
| Trainee writes "being self-employed causes larger loan requests" | "The data shows a relationship, not a mechanism. Say 'is associated with' or 'tends to' unless you have evidence beyond a correlation." |
| Trainee writes the same version of a narrative for both the technical and non-technical deliverable | "The underlying facts don't change, but the vocabulary and emphasis must. Sending the technical write-up to the credit committee, or the plain-language version to an analyst who needs the real statistic, undermines trust either way." |

---

## Up Next

Module 6.4 - GitHub for Portfolios: a sharp insight narrative is only useful if someone else can find it, so the next session turns this week's cleaned data, honest charts, and written narratives into a documented project a future employer can actually open.
