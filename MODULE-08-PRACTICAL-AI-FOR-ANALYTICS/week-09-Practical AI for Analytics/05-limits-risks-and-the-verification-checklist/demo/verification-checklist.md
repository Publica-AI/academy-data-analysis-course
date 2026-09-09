# The Verification Checklist

**Module 8, Topic 8.5 | Apply to every AI-assisted deliverable, every time**

This is the single tool that catches all four failure modes below. It is short on purpose.
A checklist nobody runs is worse than no checklist, because it creates the impression that
something was checked.

Run it on your own work as well as on AI output. The failure modes are not unique to
machines.

---

## The five questions

| # | Question | What passing looks like |
|---|---|---|
| 1 | **Did I run it?** | The code, query or formula was executed against the real file, and the output pasted here is what actually came back. Not what should have come back. |
| 2 | **Does one number reconcile from a second direction?** | At least one headline figure was recomputed a different way, on a different surface, and matched. A total from a pivot checked against a row count, a measure checked against a filtered table. |
| 3 | **Does it hold under a filter?** | The result was checked in at least one narrowed state, not only at the grand total. Errors that cancel at the total show up here. |
| 4 | **Can I explain every line?** | You can walk a partner through the code or formula line by line without help. If you cannot, it does not ship, no matter who or what wrote it. |
| 5 | **Does the answer make business sense?** | Someone who knows the business would not immediately object. This is the question that catches the confident, correctly calculated, completely wrong answer. |

Question 5 is the one people skip, and it is the one that saves careers.

---

## The four failure modes, with an example from this module

### 1. Hallucinated values

The tool states a figure that is not in the data at all. Fluent, specific, and invented.

**From this module:** ask an assistant to summarise the Q3 file without giving it the file
and it will happily produce delivery counts and revenue totals of the right shape and the
wrong value. Caught by question 1.

### 2. Plausible wrong code

The code runs, returns no error, and computes the wrong thing.

**From this module, Topic 8.4:** the first version of the report derived its reporting
window from the minimum and maximum parsed date. Two rows dated 2027 were enough to produce
a report spanning July 2026 to February 2027, with five periods where three were real. The
code was correct. The window was not. Caught by question 5, and by the refresh test.

**From Module 7, Topic 7.5:** a measure with a hardcoded denominator of 41280 reads exactly
right at the grand total and collapses to 5.1 per cent under a route filter. Caught by
question 3.

### 3. Silent assumption changes

The tool quietly decides something you never agreed to, and does not mention it.

**From this module, Topic 8.1:** hand a general date parser the Q3 file and it will read
`03-07-2026` as either the third of July or the seventh of March depending on its own
default. Every affected row still holds a valid date, so nothing errors, and roughly a
third of the quarter moves month. Caught by question 2.

### 4. Correct arithmetic, wrong question

Every number checks out and the conclusion is still nonsense, because nobody asked whether
the comparison was legitimate.

**From this module:** ask for margin by route across the Q3 files and you get 14 confident
negative numbers. The arithmetic is right. Fuel costs ₦23,352,881 against delivery revenue
of ₦12,196,290, so every route loses money. What no tool asks is whether a fleet level fuel
bill can be compared against a 3,600 row delivery extract at all. Run `margin_trap.py` in
this folder to see it happen. Caught by question 5, and only by question 5.

---

## How to submit it

Attach a completed copy to any AI-assisted deliverable. One line per question. "Yes" on its
own is not an answer.

| # | Question | Your evidence |
|---|---|---|
| 1 | Did I run it? |  |
| 2 | Does one number reconcile from a second direction? |  |
| 3 | Does it hold under a filter? |  |
| 4 | Can I explain every line? |  |
| 5 | Does the answer make business sense? |  |

**Prompt log.** List the prompts that produced anything in the deliverable, and note what
you changed about each answer before using it. An unchanged answer is a finding in itself,
and worth saying so explicitly.
