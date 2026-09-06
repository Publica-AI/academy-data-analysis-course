# Lab Exercise Pack, Topic 2.7: AI-Augmented Excel

**Module 2 (Weeks 2 to 3) | Total time-box: 90 minutes | Dataset: your cleaned `CleanSales` table (1,000 rows) and everything you built in Topics 2.1 to 2.6**

By the end of this topic, the trainee can use an AI assistant to generate, explain and debug formulas
and Power Query logic, verify the results against known totals, and describe what Copilot in Excel
adds when an employer provides it.

## The situation

Everything in this module so far has been built by hand. That is what makes this lab possible: you
already know the right answers, so you can tell whether an assistant's answer is right. This lab
would be worthless as the first topic in the module and it is useful as the last one.

**Your known totals.** Write these at the top of a sheet before you open any AI tool. Every exercise
below is checked against them.

| Known total | Value |
|---|---|
| Rows | 1,000 |
| Total Sales | ₦32,296,674.90 |
| Ikeja Sales | ₦10,620,037.05 |
| Wuse Sales | ₦10,619,767.20 |
| Trans-Amadi Sales | ₦11,056,870.65 |
| Total quantity | 5,510 |
| Rated 7 or above | 496 with the nine blank Ratings left in place, 501 if they are filled |

**A note on that last row.** It has two defensible values and you must know which one your file
holds. This is exactly the kind of figure an assistant will state confidently without knowing which
file you mean.

---

## Tier 1, Guided (30 minutes)

1. **A deliberately bad prompt.** Ask a free AI chatbot: `write me a formula for ratings`. Keep what
   comes back. Do not fix it yet.
2. **A good prompt.** Ask again, naming the real thing: the table is called `CleanSales`, the column
   is called `Rating`, values run 4 to 10, and you want Satisfied at 7 or above and Needs Follow-up
   below. Compare the two answers side by side.
3. Paste the good answer into your workbook and run it. Compare it against the IF formula you built
   by hand in Topic 2.2 on the same column. They should agree on every row.
4. **Explanation.** Paste a nested formula combining INDEX, MATCH and IF into the chat and ask what
   it does in plain English. Then ask what would happen if Customer type changed from Member to
   Normal, and **test that prediction** by actually changing the input.
5. **Debugging.** Build a VLOOKUP that omits `FALSE`, so it returns a wrong value with no error.
   Paste the formula, the intended result and the wrong output into the chat and ask what is wrong.
   Apply the fix and test it on real data before trusting it.
6. **Verification.** Ask the assistant for the total Sales for the Ikeja branch. Then build
   `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` and compare.

### Expected output, Tier 1

| Check | Expected |
|---|---|
| The vague prompt's answer | Generic, with invented column letters or no column at all |
| The specific prompt's answer | An IF or IFS formula naming Rating, agreeing with your Topic 2.2 column |
| `=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])` | ₦10,620,037.05 |
| The AI's Ikeja figure | Either refused, hedged, or **wrong**, because it cannot see your file |

**If the assistant returns ₦11,062,565.85**, stop and look at it properly. That is the correct
Ikeja total for the **raw 1,025-row export**. An answer that is exactly right for a different file is
the most convincing kind of wrong answer you will meet, and it is the reason this whole topic exists.

---

## Tier 2, Semi-guided (30 minutes)

**Task.** Use an AI assistant to produce a summary of Sales by Product line for the cleaned file,
then verify every figure it gives you before accepting a single one.

**Expected result.** The verified figures, which your own pivot table from Topic 2.4 already holds:

| Product line | Sales |
|---|---|
| Food and beverages | ₦5,614,484.40 |
| Sports and travel | ₦5,512,282.65 |
| Electronic accessories | ₦5,433,753.15 |
| Fashion accessories | ₦5,430,589.50 |
| Home and lifestyle | ₦5,386,191.30 |
| Health and beauty | ₦4,919,373.90 |

These must add to ₦32,296,674.90. That reconciliation is the check that catches an assistant
which has produced six plausible numbers rather than six correct ones.

**Deliverable.** A three-column table: the figure the assistant gave, the figure your own workbook
gives, and whether they match. Plus one sentence naming what you would have reported to the client if
you had accepted the assistant's numbers without checking.

---

## Tier 3, Independent (30 minutes)

> You are handed a workbook by a colleague who used an AI assistant heavily and has now left the
> project. You have their file and their prompt log. You have to decide, today, whether anything in
> it can be sent to the client.

Build the thing that would let you answer that question: **a verification checklist for
AI-assisted work in Excel**, written so that someone who was not there can apply it.

It must be specific to this kind of work rather than generic advice, and every item must be
something a person can actually do and record the result of. Use this module's dataset for your
worked examples.

**Expected outputs, Tier 3**

A checklist of six to ten items. A strong one covers at least these, in some form:

1. **Which file was this measured on?** Raw 1,025 rows or cleaned 1,000. State how to tell:
   `=COUNTA(...)` on the Invoice ID column, and total Sales of ₦33,156,782.40 against
   ₦32,296,674.90.
2. **Does every total reconcile?** Parts must add to the whole. Three branch totals to
   ₦32,296,674.90; six product lines to the same figure.
3. **Was every figure rebuilt by a second, independent method?** A second prompt to the same
   assistant is not a second method.
4. **Do the formulas reference the table by name**, so a stale range cannot silently point at old data?
5. **Was any figure that depends on a judgement call recorded with the judgement attached?** The
   rated-7-or-above count is 496 or 501 depending on how blank Ratings were treated, and a number
   that moves on a decision must travel with the decision.
6. **Is the deduplication column recorded?** 1,000 rows means Invoice ID; 1,006 means every column
   was left ticked and six duplicated sales are still in the file.
7. **Was the prompt log kept**, and does each entry say how the output was verified rather than that
   it looked correct?

Then apply your own checklist to your own module workbook and report honestly what fails.

---

## The core exercise, in two versions

The core exercise for this topic is unusual, because the topic **is** the AI-augmented workflow. The
pairing is therefore between generating with an assistant and verifying without one.

### Version A, without AI (assessed)

Build every known total in the table at the top of this pack by hand, from `CleanSales`, with no
assistance. This is assessed, and it is the prerequisite for everything else here: the verification
half of this topic cannot be done by someone who cannot produce the reference figures themselves.

### Version B, with AI (not assessed, still submitted)

Tiers 1 and 2 in full, with the prompt log and verification note attached to each.

**Version B deliverable.** For every AI interaction in this lab: the exact prompt, the exact output,
the independent method you checked it with, what that method returned, and whether they matched. Any
entry reading "looked correct" counts as a missing entry.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 30 minutes |
| Tier 2, Semi-guided | 30 minutes |
| Tier 3, Independent | 30 minutes |
| **Total** | **90 minutes** |

## Submission checklist

- [ ] Known totals written down before any AI tool was opened
- [ ] Vague and specific prompts both kept, with both answers
- [ ] AI-generated satisfaction formula agreeing with the Topic 2.2 manual version
- [ ] AI explanation tested by changing an input, not just read
- [ ] VLOOKUP fix applied and tested on real data
- [ ] Ikeja total verified at ₦10,620,037.05, with the AI's answer recorded whatever it was
- [ ] Tier 2 three-column comparison table, reconciling to ₦32,296,674.90
- [ ] Tier 3 checklist of six to ten items, applied to your own workbook with honest findings
- [ ] Full prompt log, with a verification method recorded for every entry

---

## Hints for Tier 3

<details>
<summary>Hint 1</summary>

A useful checklist item names a specific thing to check and a specific expected value. "Check the
totals are right" cannot be applied by someone who was not there. "Confirm the three branch totals
add to ₦32,296,674.90" can be applied by anyone, and the answer is either yes or no.
</details>

<details>
<summary>Hint 2</summary>

The most valuable items on your list are the ones that catch a **plausible** error rather than an
obvious one. A wrong answer that errors gets caught anyway. Think about the errors this module has
actually shown you: the right formula on the wrong file, the right tool with the wrong column ticked,
and a figure that changes depending on a judgement nobody recorded.
</details>
