# Demo Guide - The AI-Augmented Pipeline End to End
**Module 8, Topic 8.1 | Estimated duration: 45-50 minutes**

---

## What This Demo Teaches

- Reading a raw file for faults before touching it, and writing down what you expect to find
- Using an AI assistant at each stage of the pipeline while staying the judge of correctness
- Cleaning as a documented, repeatable script rather than a set of manual edits
- Deciding, out loud, which faults can be repaired by rule and which must go back to the business
- Applying the five-question verification checklist so that every claim in the output is checked
- Reporting a figure with its provenance, so a reader can reproduce it

---

## Setup - Before the Demo Starts

1. `swiftroute_q3_raw.xlsx` in this folder, unopened. Three sheets: `deliveries` (3,640 rows), `fuel_cost` (42 rows), `customer_complaints` (175 rows)
2. `swiftroute_q3_answer_key.xlsx` available to you, not shown to the room until Part 5
3. `SWIFTROUTE_Q3_FAULT_LOG.md` read in advance, so you know all seven faults before you start looking for them live
4. A free-tier AI assistant open in a browser tab. The file contains no real personal data, so it is safe to upload
5. Python with pandas and openpyxl available, and `clean_swiftroute_q3.py` in this folder as the fallback if the live build stalls

> **Instructor note:** run `python verify_swiftroute_q3.py` once before the session. It checks all 32 claims about this dataset against the actual workbooks and should print "All fault log claims verified". If it does not, the file has been edited or regenerated and the numbers below will not match.

> **Instructor note:** the fault log says 116 blank statuses. A cleaned table has 115, because one blank row is also one of the 40 duplicates. Do not correct a trainee who reports either number until you have asked them in which order they cleaned.

---

## Demo Steps

### Part 1 - Look Before You Clean (8 min)

> "Adaeze has sent over the Q3 export and wants a short report by Friday. Before I write a single line, I am going to spend eight minutes doing nothing but looking. Every minute here saves ten later."

**Open the `deliveries` sheet. Scroll. Say what you see, in this order.**

- The `date` column is left aligned, so Excel is treating it as text, not dates
- Scroll and you find several date shapes: `2026-07-14`, `03/08/2026`, `07-22-2026`, `9 Sep 2026`, `15.08.2026`
- `fee_naira` reads `₦45,320`, again text, because of the symbol and the comma
- Some `rider_name` cells sit slightly further right than others, which is a trailing space
- `route_code` shows both `LAG-07` and `LAG07`

> "Five formats in one date column. Here is the one that will hurt you. Zero three, zero eight, twenty twenty-six. Is that the third of August or the eighth of March? Both readings are valid dates, so nothing will error. About a third of this quarter can silently move month, and your report will look completely fine."

**Ask students:** "Which of the faults I have just listed is the most dangerous?"

> "Not the naira signs, because they break loudly the moment you try to sum. The dates, because they break quietly."

---

### Part 2 - Ask the Assistant, Then Check What It Says (8 min)

**Upload the file to the assistant. Prompt:**

> "This is a delivery export from a Nigerian logistics company for Q3 2026. List every data quality problem you can find in the deliveries sheet, with the number of rows affected for each. Do not fix anything yet."

**Read the reply aloud. Then open the fault log and compare, item by item.**

> "It found the mixed dates and the naira text, because those are visible in any sample of rows. Now watch what a sample cannot show you."

**Ask it directly: "How many duplicate delivery_ids are there?" then check the real answer.**

The real answers, all verified: 40 duplicated ids, 628 rows with an altered rider name across 620 distinct ids, 116 blank status rows, 288 LAG-07 rows split 144 hyphenated and 144 not, and six impossible values.

> "The assistant is good at describing what a file looks like and unreliable at counting what is in it, because it is reasoning about a sample, not scanning the column. Description, yes. Counts, never without checking."

---

### Part 3 - Clean by Rule, Live (12 min)

**Write the cleaning in a script, narrating each decision. The finished version is `clean_swiftroute_q3.py`.**

```python
df = df.drop_duplicates(subset="delivery_id", keep="first")     # 3,640 -> 3,600
df["date"] = df["date"].map(parse_date)                          # five known formats, in order
df["fee_naira"] = df["fee_naira"].map(money_to_int)              # strip the symbol and commas
df["rider_name"] = df["rider_name"].str.strip().str.title()
df["route_code"] = df["route_code"].str.upper().str.replace(r"^([A-Z]{3})(\d{2})$", r"\1-\2", regex=True)
df["duration_min"] = pd.to_numeric(df["duration_min"]).abs()
```

> "Look at the date function. It tries five named formats in order and returns nothing if none of them fit. What it never does is fall back to a general parser, because a general parser will guess, and on a day of twelve or less it guesses silently."

> "Duplicates first, before anything else. Clean in the wrong order and you carefully repair forty rows that you are about to delete."

---

### Part 4 - The Two Faults You Must Not Fix (7 min)

> "Two faults left, and I am going to leave both of them broken on purpose."

**The 116 blank statuses.**

> "A blank status is not a Delivered status. If I fill these in, I have invented 116 outcomes and nothing downstream will ever know. They become an explicit unknown, they get counted, and the count goes in the report."

**The two dates in 2027.**

> "SR-Q3-000794 reads 2027-02-03 and SR-Q3-001458 reads 14.01.2027. Both are outside the quarter. I can tell you they are wrong. I cannot tell you what they should be, because nothing in this file knows. They become blank, they get counted, and someone emails operations."

**Ask students:** "The answer key has a true value for both of those rows. Why can I not just use it?"

> "Because in real work there is no answer key. The key exists here so I can measure how close the cleaning got, and that is all it is for."

---

### Part 5 - Verify, Then Report (12 min)

**Run the script. Read the expected-output checks aloud as they print.**

| Check | Expected |
|---|---|
| Rows after de-duplication | 3,600 |
| Distinct delivery_id | 3,600 |
| Distinct route_code | 14 |
| Rows with a usable date | 3,598 |
| Rows with a known status | 3,485 |
| Negative durations remaining | 0 |
| Total fee | ₦12,196,290 |

**Now open the answer key and compare, column by column.**

> "Rider name, route code, fee and duration match the answer key on all three thousand six hundred rows. Date matches on three thousand five hundred and ninety-eight, and the two it misses are exactly the two I refused to guess. Status matches on three thousand four hundred and eighty-five, and the misses are the blanks I refused to guess. Every single difference between my output and ground truth is a place where I chose to say I do not know."

**Run the five-question checklist against the result, out loud.**

1. Did I run it? Yes, the output above is what came back.
2. Does one number reconcile from a second direction? The fee total was checked against a separate sum of the raw column after stripping symbols.
3. Does it hold under a filter? Route counts were checked per route as well as in total.
4. Can I explain every line? Yes, that is what the last twelve minutes were.
5. Does it make business sense? 3,600 deliveries over 14 routes in a quarter, about three per route per day. Plausible for last-mile in Lagos.

> "That fifth question is the one people skip. Hold on to it, because Topic 8.5 is built entirely on a case where the first four pass and the fifth one saves you."

---

## Final State of the Pipeline

`swiftroute_q3_cleaned.xlsx`, four sheets: `deliveries_clean` (3,600 rows, typed), `fuel_cost` and `customer_complaints` carried through untouched, and `cleaning_log` recording every step that ran. This file is carried forward into Topics 8.2, 8.3 and 8.5.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Row count reads 3,640 after cleaning | "De-duplication has not run, or ran on the wrong column. It must be on delivery_id, keeping the first occurrence." |
| Total fee comes out far too small | "The naira symbol and the comma are still in the text, so the conversion returned nothing for most rows. Strip every non-digit before converting." |
| Around a third of dates land in the wrong month | "A general date parser was used instead of the five named formats. Nothing errored, which is exactly why this is the dangerous one. Parse by explicit format." |
| Reported 116 unknown statuses rather than 115 | "Both numbers are right, for different orderings. 116 rows are blank in the raw sheet, but one of them is also a duplicate, so 115 survive de-duplication. Which did you do first?" |
| A trainee fills the blank statuses with Delivered | "You have just invented 115 outcomes. Ask them how a reader of the report would ever find out." |
| The assistant's fault counts do not match the fault log | "That is the demonstration, not a problem. It is describing a sample. Counts come from the file, never from the assistant." |

---

## Up Next

Topic 8.2 - Forecasting with AI Support. You now have a clean quarter of deliveries and a number Adaeze trusts. The next question she asks is the one this topic answers: what happens next quarter, and how sure are you?
