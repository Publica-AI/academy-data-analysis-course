# Demo Guide - Limits, Risks and the Verification Checklist
**Module 8, Topic 8.5 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Naming the four ways AI output fails in analysis, each with an example from this module
- Applying the five-question verification checklist to a finished deliverable
- Recognising the failure that passes every technical check and is still wrong
- Reporting "these numbers cannot be compared yet" as a finding rather than a failure
- Assembling the checklist and prompt log that ship with every AI-assisted submission

---

## Setup - Before the Demo Starts

1. `swiftroute_q3_cleaned.xlsx` and `swiftroute_q3_raw.xlsx` in this folder
2. `margin_trap.py` in this folder, run once before the session so you know the output
3. `verification-checklist.md` printed, one per trainee
4. A free-tier AI assistant open in a browser tab
5. Trainees' own Topic 8.1 to 8.4 outputs to hand, because Part 4 runs the checklist against their work, not yours

> **Instructor note:** frame this as synthesis, not new material. Every failure mode below already happened to the room earlier this module. Let them recognise it before you name it.

> **Instructor note:** do not reveal the margin result in Part 3 before running it. The value of that moment is the room agreeing the analysis is sound and then being asked one more question.

---

## Demo Steps

### Part 1 - Four Ways It Fails (10 min)

> "Four failure modes. You have met all four already this module, which is why we are naming them now rather than in Topic 8.1."

**1. Hallucinated values.** A figure that is not in the data at all, stated fluently.

> "Topic 8.1. We asked the assistant how many duplicate ids there were before it had scanned the column. It answered. The real number is forty, and it had no way to know that."

**2. Plausible wrong code.** It runs, returns no error, and computes the wrong thing.

> "Topic 8.4. The report derived its window from the earliest and latest date, and two rows dated 2027 turned a three-month report into a five-month one. Correct code, wrong window."

**3. Silent assumption changes.** It decides something you never agreed to and does not mention it.

> "Topic 8.1 again. A general date parser reading `03-08-2026`. Third of August or eighth of March. Every row stays a valid date, so nothing errors, and about a third of the quarter moves month."

**4. Correct arithmetic, wrong question.** Every number checks out and the conclusion is nonsense.

> "You have not met this one yet. It is the rest of this session, and it is the one that ends careers."

---

### Part 2 - The Five Questions (6 min)

**Hand out `verification-checklist.md` and read the five questions.**

1. Did I run it?
2. Does one number reconcile from a second direction?
3. Does it hold under a filter?
4. Can I explain every line?
5. Does the answer make business sense?

> "The first four are technical and you have been doing them all module. The fifth is not technical at all, and it is the only one that catches failure mode four. Watch."

---

### Part 3 - Correct Arithmetic, Wrong Question (14 min)

> "Adaeze asks a reasonable question: which of our fourteen routes actually makes money? We have delivery revenue and we have a fuel cost sheet. This is a join and a subtraction."

**Run `margin_trap.py` and put the table on screen.**

**Walk questions one to four, out loud, and pass every one.**

| Question | Verdict |
|---|---|
| Did I run it? | Yes, that output is what came back |
| Does a number reconcile from a second direction? | Yes, revenue by route sums to the quarter total of ₦12,191,640 |
| Does it hold under a filter? | Yes, checked per route and per month, all 42 fuel rows matched |
| Can I explain every line? | Yes, it is a group-by, a join and a subtraction |

> "Four out of four. On any normal day this ships."

**Now show the totals.**

| | Q3 2026 |
|---|---|
| Delivery revenue | ₦12,191,640 |
| Fuel cost | ₦23,352,881 |
| Margin | -₦11,161,241 |
| Routes with a positive margin | 0 of 14 |

**Ask students:** "Question five. Does that make business sense?"

*(Give it real silence. Someone will say it.)*

> "SwiftRoute lost money on every single route, for an entire quarter, and nobody mentioned it. Twice as much on fuel as it earned on deliveries. If that were true, this would not be a delivery report, it would be an emergency board meeting."

**Show that both sheets are individually fine.**

> "Fuel works out at three point three eight kilometres per litre at about nine hundred and fifty-five naira a litre. That is realistic for a Nigerian van fleet. The mean fee is three thousand three hundred and eighty-eight naira for a twenty-three kilometre run. Also realistic. Neither sheet is wrong."

> "What is wrong is the comparison. The fuel sheet is a fleet level bill. The delivery sheet is a three thousand six hundred row extract, about three deliveries per route per day. They are not at the same grain, and nothing in the arithmetic could ever have told you that."

**Write the actual deliverable on the board.**

> "The finding is not 'every route is loss making'. The finding is 'these two sheets cannot be compared until someone tells us what the delivery extract is a sample of'. That sentence is what you send Adaeze, and it is worth more than the fourteen numbers."

---

### Part 4 - Run It on Your Own Work (10 min)

> "Open your own Topic 8.2 forecast. Not mine. Run all five questions on it now, in pairs, and write the answers down."

*(Circulate. Push hard on question five specifically.)*

**Debrief with the two that usually surface:**

> "Question five on a forecast: is four thousand and forty-nine deliveries plausible against three thousand six hundred last quarter? Yes, a twelve per cent rise, and you can defend it. Now do the same for the range, and notice that the range is the honest part."

> "Question two catches the other one. If you cannot say which second calculation you checked a number against, you have not verified it, you have re-read it."

**Show what gets submitted.**

> "Every AI-assisted deliverable from here to your capstone ships with two things attached: this checklist, one line of evidence per question, and a prompt log listing what you asked and what you changed about each answer before using it. An answer you changed nothing about is itself worth flagging."

---

## Final State of the Deliverable

A completed `verification-checklist.md` with one line of evidence against each of the five questions, plus a prompt log. Both are assessed with the Module 8 pipeline output and both carry forward into the capstone as the Level 4 fluency artefact.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| A trainee reports the margin table as a finding | "Read them their own question five answer back. Fourteen loss-making routes and no one noticed is not a finding, it is a signal that the comparison is wrong." |
| A trainee blames the fuel data for being wrong | "It is not wrong. Show them the kilometres per litre and the price. Both sheets are sound. The pairing is what fails." |
| Question 5 is answered with a single yes | "Ask who would object and why. If nobody could possibly object, the question was not asked properly." |
| A trainee thinks the checklist only applies to AI output | "Ask them which of the five questions they would want skipped on work they wrote themselves at five to five on a Friday." |
| The prompt log lists only successful prompts | "The prompt that produced a wrong answer is the most useful line in the log. It is evidence you were checking." |
| A trainee cannot find a second direction for question 2 | "Every total has one. A sum has a count, a rate has a numerator and a denominator, a join has a row count you can predict before you run it." |

---

## Up Next

The capstone proposal panel, the closing assessment for this module. Five minutes each, in front of a small group, using everything from this module on your own project instead of SwiftRoute's data. The verification discipline you just practised is what the panel will push on hardest.
