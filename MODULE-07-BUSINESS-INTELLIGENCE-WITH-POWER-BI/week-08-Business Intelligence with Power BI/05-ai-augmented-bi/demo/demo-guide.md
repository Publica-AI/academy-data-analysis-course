# Demo Guide - AI-Augmented BI
**Module 7, Topic 7.5 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Prompting an AI assistant for a DAX measure with full schema context, and seeing what happens when that context is missing
- Reading an AI-written measure aloud and identifying the filter context it assumes
- Auditing four AI-written measures against source data rather than trusting them on sight
- Diagnosing two specific, real DAX faults: a hardcoded denominator, and a numerator copied into a denominator
- Interrogating an AI assistant using four specific challenge moves rather than accepting a first answer

---

## Setup - Before the Demo Starts

1. `7.3_solution.pbix` open, with the six verified measures from Topic 7.3 already in place
2. A free-tier AI assistant open in a browser tab, ready to receive a live prompt
3. Printed copies of the four audit measures (Measures A, B, C, D) ready to hand out, not shown on screen until the reveal
4. Confirm in advance whether the room has access to Copilot in Power BI, so the honest-positioning section is delivered accurately

> **Instructor note:** do not annotate or hint at which of the four measures are correct before trainees have worked through the audit themselves. The exercise only works if the room decides, not the instructor.

### If `7.3_solution.pbix` does not exist yet

No new file needs building for this demo beyond what Topic 7.3 already produces. Follow the 7.3 demo guide's Setup and Demo Steps first, in full, so the six verified measures already exist before this session starts. Nothing further needs constructing in advance; Measures A to D in Part 3 below are typed live during the audit debrief, not pre-built.

---

## Demo Steps

### Part 1 - Prompt Blind, Then Watch It Fail (10 min)

**In the AI assistant, type a deliberately underspecified prompt:** "Write a DAX measure for on-time rate."

> "Watch what comes back. It will look completely plausible."

**Paste the returned measure into Power BI as a new measure. Add it to a card with no filters. Note the value.**

**Now filter the same visual to LAG-07, the worst route from Topic 7.2.**

> "You already know the real number for LAG-07. Sixty-one point four percent. Read what the card says now."

*(This step is genuinely live and the exact wrong number will vary by which measure the assistant returns - the point being demonstrated is that an unfiltered check can pass while a filtered check fails, not a specific number.)*

> "This is not a bad prompt. It is a good, confident answer to a question the assistant did not know it was being asked, because it never saw your model, only your words."

---

### Part 2 - A Better Prompt (7 min)

**Re-prompt, this time supplying full context:**

> "You are a Power BI developer. I have a star schema. Fact: swiftroute_deliveries, 41,280 rows, one row per delivery. Status values are: On time, Late. Dimensions: riders, routes, customers_business, dates, marked as a date table. I need a measure for on-time rate that responds correctly to any filter, including a single route. Give me the measure, then explain in plain English what filter context it assumes."

> "Look at the difference in structure, not just the result. Role, schema, grain, the actual values in the Status column, and the constraint that forces filter-context correctness. That last line, respond correctly to any filter, is the one most people leave out, and it is exactly the line that would have caught the fault from Part 1."

---

### Part 3 - The Audit (18 min)

**Hand out the printed sheet with four measures:**

```dax
Measure A:
Total Late = CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "Late" )

Measure B:
On-Time Rate = DIVIDE ( [On-Time Deliveries], 41280 )

Measure C:
Late Rate = DIVIDE (
    CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "Late" ),
    CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "Late" )
)

Measure D:
Deliveries Previous Month = CALCULATE ( [Total Deliveries], PREVIOUSMONTH ( dates[DateKey] ) )
```

> "Two are correct. Two are not, and one of those returns a plausible number rather than an error. In pairs: state whether each is correct, prove your verdict in Power BI against source data, and for each fault write the prompt you would use to challenge the assistant that wrote it."

*(Circulate. Do not confirm or deny any verdict during this time.)*

**Debrief Measure B:** build it live, show it reads correctly at the unfiltered total (82.0%, since 41,280 genuinely is the grand total), then filter to LAG-07 and show it collapsing to 5.1% against the true 61.4%.

> "The denominator is the literal number 41280, not a reference to Total Deliveries. It never moves when the numerator does. This is exactly why you check more than one filter state, never just the total."

**Debrief Measure C:** build it live, show it returns exactly 100% in every context.

> "Numerator and denominator are the identical CALCULATE expression. Late divided by late is always one hundred percent. This one fails the very first prediction you make, which is why it is the easier of the two faults to catch."

**Confirm A and D are correct**, matching the patterns from Topic 7.3.

---

### Part 4 - Four Moves to Use on Any AI Output (5 min)

> "Four things to say back to an assistant, every time, and I want you to have these written down before you leave today."

List and briefly demonstrate each, live, on the assistant:
1. "Explain what filter context this assumes."
2. "Show me a second way to write this, and the trade-off."
3. "What would make this measure return a wrong number?"
4. "I ran it and got five percent, I expected sixty-one, where would you look first?"

> "That fourth one turns a one-shot request into an actual dialogue. That is the whole of Level 3."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Measure B looks correct because the room only checked the total | "That is precisely the trap. Ask them to filter to any single route before finalising a verdict." |
| Trainees assume Measure C is correct because it returns a formatted percentage | "A percentage format does not mean a percentage is meaningful. Ask what the numerator and denominator actually are, character by character." |
| A trainee argues Measure A is wrong because 'AI wrote it and AI gets things wrong' | "Verdict must come from checking against source data, not from a general suspicion of AI. Ask them to actually run and reconcile Measure A before ruling on it." |
| Confusion about why Measure D uses PREVIOUSMONTH instead of DATEADD | "Both are valid time-intelligence patterns with the same effect. PREVIOUSMONTH is simply a different, equally correct way to write it - this is not the fault to look for." |

---

## Up Next

Topic 7.6 - Capstone Kick-off. Submit the marked-up audit sheet from Part 3 today - it is the assessed Level 3 evidence for this topic. Next session, the capstone actually starts.
