# Demo Guide - AI-Augmented SQL
**Module 3, Topic 3.6 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Writing a precise natural-language prompt that produces a correct SQL query
- Reading an AI-written query critically before running it
- Predicting a result before running an AI-written query
- Verifying an AI-written query's result and fixing it when it is wrong

---

## Setup — Before the Demo Starts

1. SQLite ready, connected to `eko_traders.db`, using `join_demo_customers` as in 3.4.
2. An AI assistant open and signed in.

> **Tell students:** "AI is about to write full queries for you, for the first time this module. Everything else stays the same, you still predict, you still verify, you just aim it at someone else's SQL now."

---

## Demo Steps

### Part 1 — A vague prompt versus a precise one (8 min)

> "Here is a vague prompt: 'count customers who ordered in Q1 2026'."

**Ask students:** What has this prompt left ambiguous?

> "It does not say unique customers, it does not give exact date bounds, and it does not say what shape the answer should take. AI will fill those gaps with an assumption, and that assumption might not be the one you meant."

> "A precise version: 'using our customers and orders tables, count the DISTINCT customers who placed at least one order between 2026-01-01 and 2026-03-31 inclusive, return a single number.'"

---

### Part 2 — Auditing the AI's query (12 min)

> "Using the vague prompt, an AI assistant wrote this back."

```sql
SELECT COUNT(*) AS customer_count
FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= '2026-01-01' AND o.order_date <= '2026-03-31';
```

> "Before running it, predict. Chidinma ordered twice in Q1, Aisha once. That is 2 unique customers."

```sql
-- run it
```

> "3, not 2. Mismatch. Time to find it, not to shrug and paste it in."

**Ask students:** Where is the bug?

> "The JOIN produces one row per order, not per customer. Chidinma's two orders each add 1 to COUNT(*), she is counted twice. The vague prompt never said unique, and AI did not assume it either."

---

### Part 3 — Fixing and re-verifying (8 min)

```sql
SELECT COUNT(DISTINCT c.customer_id) AS customer_count
FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date BETWEEN '2026-01-01' AND '2026-03-31';
-- expect 2, matching the prediction
```

> "COUNT(DISTINCT customer_id) instead of COUNT(*). Now it matches the prediction from Part 2."

---

### Part 4 — The five-check habit (7 min)

> "Run these five checks on any AI-written query before trusting it: does the schema match what AI assumed, are the clauses in the right order, is the join type right for this question, what did you predict, and does the result match that prediction."

**Ask students:** Which of these five checks caught today's bug?

> "The predict step. Everything else about that query was syntactically fine, it ran without error. Only comparing the result to a prediction caught it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trusting a query because it ran without error | "Running is not the same as correct. This entire demo is a query that ran perfectly and returned the wrong number." |
| Skipping the prediction step because AI "usually gets it right" | "The prediction is what catches the times it does not. Skipping it defeats the entire point." |
| Assuming COUNT(DISTINCT ...) is always the fix | "Only when the question means unique. Confirm what the business question actually asked before assuming which fix applies." |

---

## Up Next

The Module 3 graded query set. Revisit each topic's recap and, for every practice query from here on, ask: did I predict first, and did I verify against something known.
