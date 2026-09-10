# Module Demo Guide - Foundations of Data Analysis and the AI-Augmented Analyst (Week 1)
**Module 1 | Estimated duration: 70 minutes**

---

## The Story

Naija Swift Logistics is a Lagos-based delivery firm operating out of three branches: Ikeja, Lekki and Yaba. Customer complaints about late deliveries have risen this month, and the operations manager has asked the firm's newest analyst to find out what is actually happening and recommend where to act first. Over the course of this demo, the trainee plays that analyst, working through the same delivery_log.csv file used in every topic this week to turn a vague complaint into a verified, communicated recommendation.

**What this demo builds:**

- A manually verified set of branch delay averages that answers the operations manager's original question (Topic 1.1)
- A fully typed and classified version of delivery_log.csv, with the analyst's own position on the data team made explicit (Topic 1.2)
- A configured AI toolkit (Claude, ChatGPT, Gemini, Google Colab, publica.academy) and a firsthand, caught AI error that sets the tone for the rest of the programme (Topic 1.3)
- A four-ingredient prompt that finds real data-quality problems in the delivery log, built through visible iteration from a weak first attempt (Topic 1.4)
- A formally verified, communication-ready recommendation, backed by a documented decision to decline an unsafe data request (Topic 1.5)

---

## Prerequisites

1. Trainee accounts confirmed on Claude, ChatGPT, Gemini, Google Colab and publica.academy (from Topic 1.3's setup exercise).
2. `delivery_log.csv` downloaded from the Week 1 downloads section of publica.academy and opened in a spreadsheet.
3. Topic 1.1's manually calculated branch averages (Ikeja 2.3 days, Lekki 1.1 days, Yaba 0.9 days) available to reference, either from the trainee's own worked example or the facilitator's copy.

> **Instructor note:** `delivery_log.csv` is deliberately dirty. It contains 12 exact duplicate rows, 2 impossible future delivery dates, 8 rows with inconsistent branch-name casing, and a handful of blank `delay_days` values for the most recent week. This is intentional, not a data error to be quietly fixed before the session. Part 4 of this demo uses an AI assistant to help find these problems, so leave the file exactly as downloaded.

---

## Dataset / Project Setup (before the demo starts)

1. Confirm `delivery_log.csv` is downloaded locally and opens correctly in the spreadsheet tool trainees will use (do not rely on a live download during the session).
2. Open a second, pre-built spreadsheet tab with the clean branch averages already calculated (Ikeja 2.3, Lekki 1.1, Yaba 0.9), kept hidden until Part 1's reveal, as the fallback if a live formula fails.
3. Have all four AI toolkit tabs (Claude, ChatGPT, Gemini, Google Colab) signed in and open before trainees arrive, so Part 3 does not lose time to login screens.
4. Pre-capture a screenshot of a wrong AI-generated total from the `order_value_naira` column, as the fallback for Part 3 if the live demonstration does not reproduce an error on the day.

---

## Demo Steps

### Part 1 - The Analytics Lifecycle and Data-Driven Decision Making (12 min)

> "The operations manager's complaint is simple: deliveries are late. That is not yet a question we can answer, so our first job is to turn it into one."

- Sharpen the business question live: "Which branch has the worst delivery delays, and by how much?"
- Open `delivery_log.csv` and confirm the columns available for Data Collection: `order_id`, `dispatch_date`, `delivery_date`, `branch`, `delay_days`, `order_value_naira`, `delivery_partner`, `complaint_notes`.
- Remove the 12 duplicate `order_id` rows and standardise the inconsistent branch-name casing as the Data Preparation step, narrating each fix.
- Calculate average `delay_days` per branch using a spreadsheet formula (Analysis).
- Reveal the fallback tab to confirm the live result matches: Ikeja 2.3 days, Lekki 1.1 days, Yaba 0.9 days.

> "Ikeja's average delay is more than double every other branch, and it is driving most of this month's complaints. That sentence, not the number alone, is the interpretation the operations manager actually needs."

### Part 2 - Data Types, Data Structures and the Data Team (10 min)

> "Before we go further, we need to be precise about what kind of data we are actually holding, because that decides what we are allowed to do with it."

- Type each column live: `order_id` (categorical identifier, not numerical), `dispatch_date` and `delivery_date` (date/time), `branch` and `delivery_partner` (categorical), `delay_days` and `order_value_naira` (numerical), `complaint_notes` (text).
- Open a few `complaint_notes` entries to show unstructured content sitting inside an otherwise structured file.
- Confirm the file overall is structured, since every record shares the same fixed set of columns.
- Place the analyst's own role on the data team: downstream of whoever collected this data (a data engineer role, even if informally filled), upstream of the operations manager who will act on the recommendation.

> "Getting the branch column typed and standardised correctly in Part 1 is exactly why our Part 1 averages can be trusted. Typing is not academic, it is what makes the calculation safe to run."

### Part 3 - The AI-Augmented Analyst and Toolkit Setup (14 min)

> "Now we bring AI into the workflow, but not before we have personally watched it get something wrong."

- Copy the `order_value_naira` column, with currency symbols and commas left in, and paste it as plain text into an assistant, asking for the total.
- Compare the assistant's stated total against the real spreadsheet SUM formula, live.
- If a mismatch appears, narrate it as the expected result; if not, use the pre-captured fallback screenshot to make the same point without losing pace.
- Walk through the toolkit: Claude and ChatGPT for structured reasoning and general drafting, Gemini where work already lives in Google tools, Google Colab for running real code from Week 6, publica.academy as the home base for downloads and quizzes.
- State plainly what changes (drafting speed, first-pass summaries) and what does not (the analyst still owns the question and still verifies).

> "That mismatch is not a reason to distrust AI tools. It is the reason we never skip verification, no matter how confident the answer sounds."

### Part 4 - Prompt Fundamentals for Data Work (16 min)

> "Let's put that lesson to work. We are going to ask an assistant to help us find problems in this file, and watch a weak prompt improve step by step."

- Write a first, deliberately weak prompt live: "What's wrong with my delivery data?" Show the generic, unusable answer it returns.
- Add a data description and a precise task: "Here is a delivery log with columns order_id, dispatch_date, delivery_date, branch and delay_days, 400 rows. Find rows where delay_days does not match delivery_date minus dispatch_date." Show the improved but still unstructured paragraph answer.
- Add an output format: "Return any mismatches as a table with columns order_id, expected_delay and actual_delay." Show the clean, usable table this produces, surfacing the two impossible future dates from the dataset.
- Manually recalculate one flagged row in the spreadsheet on screen to verify the assistant's table before trusting the rest.

> "Three tries, one ingredient sharpened each time. That is the whole skill: diagnose what was missing, fix only that, and always check the result yourself."

### Part 5 - Verification Habits and Responsible Use (16 min)

> "We now have a recommendation forming. Before it goes anywhere near the operations manager, it needs to be formally verified, and we need to be certain we have handled this data responsibly throughout."

- Formally verify the Part 1 claim, "Ikeja's average delay is 2.3 days, the highest of the three branches," by recalculating it independently against the cleaned data, confirming the two match.
- Recap the categories of data that must never be pasted into an AI tool: real customer names, phone numbers, addresses, payment details, or any real colleague or employer confidential information.
- Run the Part 5 scenario live: a manager asks for a real customer complaint log, with real names and phone numbers, to be pasted into an assistant for summarising. Decline on screen, explain why using the outline of the Nigeria Data Protection Act's unauthorised-transfer risk, and propose the safe alternative of anonymising the file first, the same way `delivery_log.csv` was prepared.
- Draft the final one-slide recommendation for the operations manager: finding, evidence, recommended action (a dispatch-process review for Ikeja).

> "Every step in this demo, from typing a column correctly to declining an unsafe request, was in service of one sentence the operations manager can now act on with confidence."

---

## Demo Wrap-Up

The finished artefact is a verified, one-slide recommendation for Naija Swift Logistics, backed by a fully cleaned dataset and a documented, safe use of AI tools throughout.

| Feature / capability | Topic it came from | What it shows |
|---|---|---|
| Branch delay averages (Ikeja 2.3, Lekki 1.1, Yaba 0.9 days), calculated from cleaned data | Topic 1.1 | The analytics lifecycle carried end to end, from a vague complaint to a specific, calculable answer |
| Every column in delivery_log.csv correctly typed and classified | Topic 1.2 | A structured dataset the trainee can justify column by column, and their own place on the data team |
| A caught AI error on the order_value_naira total, plus a working toolkit across all five programme tools | Topic 1.3 | AI tools used for speed, with the analyst's verification responsibility unchanged |
| A three-iteration prompt that surfaced real mismatched rows, including the two impossible future dates | Topic 1.4 | A well-built prompt using context, data description, task and output format, sharpened through iteration |
| A formally reverified branch average and a declined unsafe data request | Topic 1.5 | Verification and responsible data use applied under real, not hypothetical, pressure |

> "This is the same loop you will run every week for the next eleven weeks: ask a sharp question, prepare the data, use AI where it helps, and never hand over an answer you have not personally checked. Every analyst job you will apply for after this programme runs on exactly this discipline."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| Trainee tries to average `order_id` directly, since it looks numerical | Point back to Part 2: a data type is defined by what operations make sense on it, not by appearance. Ask what averaging two order IDs would even mean. |
| Trainee accepts the AI assistant's first total or count without checking it against the spreadsheet | Point back to Part 3's mismatch. Ask them to state, out loud, which of the three verification methods (recalculate, spot-check, cross-reference) they are about to use before moving on. |
| Trainee's first prompt attempt in Part 4 gets a poor answer and they assume the task is impossible | Remind them this is expected, not a failure. Ask which of the four ingredients, context, data description, task or format, is thinnest, and have them sharpen only that one. |
| Trainee forgets to standardise inconsistent branch-name casing before calculating averages, and gets a result that does not match the fallback tab | Have them re-check the branch column for variants like `" ikeja"` or `"LEKKI "` before recalculating; this is the exact Data Preparation step from Part 1. |
| Trainee hesitates to fully decline the Part 5 unsafe data request, offering to paste "just the phone numbers" | Clarify that partial personal data is still personal data under the categories in Part 5, and that the correct response is the full anonymise-first alternative, not a partial compromise. |
