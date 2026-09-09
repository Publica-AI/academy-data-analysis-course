# Module Demo Guide - Practical AI for Analytics (Week 9)
**Module 8 | Estimated duration: 70-75 minutes**

---

## The Story

SwiftRoute Logistics has closed its third quarter and Adaeze Nwosu, the operations manager,
needs a short written report for the board on Friday. She has three sheets in one workbook,
none of them clean, and four working days. This demo runs the whole job in one sitting with
an AI assistant at every stage, and the thing being taught is not speed. It is that the
analyst stays accountable for every number the assistant produces.

**What this demo builds:**

- A cleaned, documented, reproducible delivery table with every repair written as a rule and every unrecoverable value left explicitly unknown (Topic 8.1)
- A Q4 forecast with a defensible range, and a partial-period trap caught before it inverts the conclusion (Topic 8.2)
- A plain-language read of what clustering did and did not find in SwiftRoute's customers, and where an analyst hands over to a data scientist (Topic 8.3)
- The same report turned into a script that survives next quarter's file, proved by a test rather than by confidence (Topic 8.4)
- The five-question verification checklist applied to a finished analysis that passes four of the five and is still wrong (Topic 8.5)

---

## Prerequisites

1. Python with pandas, openpyxl, numpy, matplotlib and scikit-learn available. Google Colab works if local installs are a problem.
2. The Q3 workbook pair and fault log in this folder: `swiftroute_q3_raw.xlsx`, `swiftroute_q3_answer_key.xlsx`, `swiftroute_q3_cleaned.xlsx` and `SWIFTROUTE_Q3_FAULT_LOG.md`.
3. A free-tier AI assistant open in a browser tab. The dataset contains no real personal data, so it is safe to upload.
4. The five topic solution scripts available as fallbacks, each in its own topic folder: `clean_swiftroute_q3.py`, `build_forecast.py`, `customer_grouping.py`, `monthly_report.py` with `test_refresh.py`, and `margin_trap.py`.
5. Trainees have their Module 7 capstone sign-off form to hand, because Part 6 points at it.

> **Instructor note:** run `python verify_swiftroute_q3.py` and `python test_refresh.py` before the session. Between them they check 43 claims about this dataset and the automation. If either fails, stop and find out why before teaching from these numbers.

> **Instructor note:** this demo compresses five topics into seventy minutes, so no part gets taught properly here. The job of this session is to show the pipeline as one continuous piece of work, ending on the verification failure that only the whole pipeline can set up.

---

## Dataset / Project Setup (before the demo starts)

1. Copy the Q3 workbook to a local folder. Do not open and re-save it in Excel, because Excel will helpfully convert the text dates and destroy the demo's first teaching point.
2. Run each solution script once so nothing loads cold in front of the room.
3. Confirm the raw `deliveries` sheet reads 3,640 rows and the answer key reads 3,600.

---

## Demo Steps

### Part 1 - Raw File to Trusted Table (Topic 8.1) (16 min)

> "Three sheets, four days, and a board meeting. First thing I do is not clean. It is look."

**Scroll the `deliveries` sheet and name the faults aloud: five date shapes in one column, fees as text with a naira sign, trailing spaces on rider names, and both `LAG-07` and `LAG07`.**

> "Zero three, zero eight, twenty twenty-six. Third of August or eighth of March? Both are valid dates, so nothing will error, and about a third of the quarter can silently move month."

**Upload the file and ask the assistant to list the data quality problems with row counts. Then check the counts against the fault log.**

> "It described the file well and it counted badly, because it is reasoning about a sample. The real numbers: forty duplicate ids, six hundred and twenty-eight altered name rows, one hundred and sixteen blank statuses, two hundred and eighty-eight LAG-07 rows split evenly between two spellings, and six impossible values. Description from the assistant, counts from the file. Always."

**Clean by rule, live, and stop on the two you refuse to fix.**

> "One hundred and sixteen blank statuses become an explicit unknown, not Delivered. Two dates in 2027 become blank, not a guess. I can tell you they are wrong. Nothing in this file knows what they should be, so somebody emails operations."

**Run the checks.**

| Check | Expected |
|---|---|
| Rows after de-duplication | 3,600 |
| Distinct route codes | 14 |
| Rows with a usable date | 3,598 |
| Rows with a known status | 3,485 |
| Total fee | ₦12,196,290 |

> "Against the answer key, rider name, route code, fee and duration match on all three thousand six hundred rows. The only differences anywhere are the two dates and the blank statuses, which are precisely the places I chose to say I do not know."

---

### Part 2 - Forecast, and the Trap That Inverts It (Topic 8.2) (14 min)

**Group by calendar week. Fourteen weeks. Fit a line on all of them.**

> "Slope minus nought point three four seven. Shrinking. R-squared nought point zero zero zero eight. On this evidence I would tell Adaeze her business is flat to declining."

Pause.

> "Q3 starts on a Wednesday and ends on a Wednesday. The first week holds a hundred and ninety deliveries and the last holds a hundred and thirteen, against a typical two hundred and seventy. They are not low, they are short."

**Drop the two partial weeks. Refit on twelve.**

| | All 14 weeks | 12 complete weeks |
|---|---|---|
| Slope | -0.347 per week | +2.948 per week |
| R-squared | 0.0008 | 0.3262 |

> "Same file, same method, opposite conclusion, and the only change is which rows I was entitled to use."

**Project thirteen weeks and report it honestly.**

| Q4 2026 | Deliveries | Revenue |
|---|---|---|
| Point estimate | 4,049 | ₦13,386,188 |
| Range, one residual sd | 3,840 to 4,257 | ₦12,736,564 to ₦14,035,812 |
| Naive baseline, Q3 held flat | 3,570 | ₦12,074,790 |

> "R-squared of nought point three three means the line explains about a third of the movement. So I give her the range and the assumption, not a single number with four significant figures."

---

### Part 3 - What Clustering Found, and What It Cannot Tell You (Topic 8.3) (10 min)

**Run the customer grouping and show the three groups among 1,193 customers.**

| Group | Customers | Mean deliveries | Mean fee | Mean distance |
|---|---|---|---|---|
| Frequent | 419 | 4.6 | ₦3,399 | 23 km |
| Occasional, short hops | 416 | 2.2 | ₦2,458 | 15 km |
| Occasional, long hauls | 358 | 2.2 | ₦4,444 | 32 km |

> "Nobody labelled these. There is no customer type column. And look at the last two: identical ordering frequency, separated entirely by distance and therefore by cost. That is a commercial distinction nobody at SwiftRoute had written down."

**Re-run it unscaled, then with five groups.**

> "Unscaled, only seventy-four per cent of customers land in a matching group, because fee runs to thousands and delivery count runs to twelve, so it is grouping on price while appearing to consider everything. Ask for five groups and you get five, equally convincing. The number of groups is your decision to defend, not the data's to hand you."

---

### Part 4 - Do It Once, Then Never By Hand Again (Topic 8.4) (12 min)

> "Adaeze wants this every quarter. Split the job: rules get automated, judgements stay with you."

**Four rules on the board: path as an argument, periods derived from the data, standardise before you join, assert what you expect.**

**Run `monthly_report.py`, then show the bug that rule two exists to prevent.**

> "The first version of this script reported five periods, July 2026 to February 2027, because it took its window from the earliest and latest date and two rows are dated 2027. Two rows out of three thousand six hundred changed the shape of the whole report. No error, no warning."

**Run `test_refresh.py`.**

> "It manufactures next quarter's file: every date moved on, a brand new route, forty rows arriving without the hyphen, two hundred rows gone, columns shuffled. Then it checks eleven things. Eleven passing is what makes this safe to hand over. My confidence is not."

---

### Part 5 - The Failure That Passes Every Check (Topic 8.5) (12 min)

*(The whole module has been AI-assisted. This part is where the judging is assessed.)*

> "Last question of the day, and the most reasonable one Adaeze has asked. Which of our fourteen routes makes money? We have revenue and we have a fuel sheet. This is a join and a subtraction."

**Run `margin_trap.py`. Walk questions one to four of the checklist and pass all four.**

| Question | Verdict |
|---|---|
| Did I run it? | Yes |
| Reconciles from a second direction? | Yes, route revenue sums to ₦12,191,640 |
| Holds under a filter? | Yes, all 42 fuel rows matched, per route and per month |
| Can I explain every line? | Yes |

**Then show the totals.**

| | Q3 2026 |
|---|---|
| Delivery revenue | ₦12,191,640 |
| Fuel cost | ₦23,352,881 |
| Margin | -₦11,161,241 |
| Routes with a positive margin | 0 of 14 |

**Ask students:** "Question five. Does that make business sense?"

*(Leave real silence.)*

> "Every route loses money, for a whole quarter, twice as much on fuel as it earns, and nobody mentioned it. Both sheets are individually sound: three point three eight kilometres per litre at about nine hundred and fifty-five naira, and a mean fee of three thousand three hundred and eighty-eight naira for a twenty-three kilometre run. What is wrong is the comparison. A fleet level fuel bill against a three thousand six hundred row extract at three deliveries per route per day. They are not at the same grain, and no step in the arithmetic could ever have told you."

> "The deliverable is one sentence: these two sheets cannot be compared until someone tells us what the delivery extract is a sample of. That is worth more than the fourteen numbers, and only question five gets you there."

---

## Demo Wrap-Up

| Capability | Topic it came from | What it shows |
|---|---|---|
| A cleaned table that matches ground truth everywhere except where it declines to guess | 8.1 | 3,600 rows, 3,598 dated, 3,485 with a known status, ₦12,196,290 |
| A forecast with a range, and the partial-period trap caught | 8.2 | Slope flips from -0.347 to +2.948 once two partial weeks are dropped |
| A grouping described in business language, with its two failure modes shown | 8.3 | Three groups over 1,193 customers, 74 per cent agreement once unscaled |
| A report that follows the file rather than the calendar | 8.4 | 11 refresh checks passing against a manufactured next-quarter file |
| A finished analysis rejected on the one question that is not technical | 8.5 | 4 of 5 checklist questions passed, 0 of 14 routes plausible |

> "Nothing you did today was slower because an assistant was in the room, and nothing you shipped was something you could not defend. That combination is the job now. It is also exactly what the panel will ask you about on your own project next session."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| Row count reads 3,640 after cleaning | "De-duplication has not run, or ran on the wrong column. It must be on delivery_id, keeping the first occurrence." |
| Around a third of dates land in the wrong month | "A general parser was used instead of the five named formats. Nothing errored, which is why this is the dangerous one." |
| Reported 116 unknown statuses rather than 115 | "Both are right, for different orderings. One blank row is also a duplicate. Which did you do first?" |
| A trainee reports a negative delivery trend | "Check whether the first and last calendar weeks are in the fit. Both are partial and both drag the line down." |
| A trainee quotes the forecast as a single number | "Ask what R-squared they got. A third of the variation explained does not support four significant figures." |
| A trainee reports the margin table as a finding | "Read their own question five answer back to them. Fourteen loss-making routes that nobody noticed is a signal about the comparison, not about the routes." |
| A trainee blames the fuel sheet for being wrong | "It is not wrong. Show them the kilometres per litre and the price per litre. The pairing fails, not the sheet." |
| The assistant's counts are taken as fact | "That is the demonstration. Description from the assistant, counts from the file." |
