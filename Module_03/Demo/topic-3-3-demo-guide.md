# Demo Guide - Aggregation and Grouping
**Module 3, Topic 3.3 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Using COUNT, SUM, AVG, MIN and MAX to summarise a whole table
- Using GROUP BY to get one summary row per category instead of one number overall
- Filtering groups with HAVING, and explaining why WHERE cannot do this job
- Verifying a computed total against a known reference figure before trusting it

---

## Setup — Before the Demo Starts

1. SQLite ready, connected to `eko_traders.db`.
2. Confirm the table loaded: `SELECT COUNT(*) FROM customers;` should return 10.

> **Tell students:** "Today's number to remember is 858000, the total spend across all ten customers. We are going to reach it three different ways and it should not move."

---

## Demo Steps

### Part 1 — Aggregate functions on the whole table (8 min)

```sql
SELECT COUNT(*), SUM(total_spent), AVG(total_spent), MIN(total_spent), MAX(total_spent)
FROM customers;
```

> "One row back. Every aggregate collapses all ten customers into a single number, until we tell it to do otherwise with GROUP BY."

```sql
SELECT COUNT(*) AS all_rows, COUNT(phone) AS rows_with_phone FROM customers;
-- expect 10, 8
```

> "Two customers have no phone on file. COUNT(*) counts every row. COUNT(phone) skips the NULLs. Same table, two different questions."

---

### Part 2 — GROUP BY (10 min)

```sql
SELECT city, COUNT(*) AS customer_count, SUM(total_spent) AS total_spend
FROM customers
GROUP BY city
ORDER BY total_spend DESC;
```

> "Ten customers became five city rows. Lagos leads at 335000."

**Ask students:** What happens if I add full_name to the SELECT list here without changing GROUP BY?

```sql
SELECT city, full_name, SUM(total_spent) FROM customers GROUP BY city;
```

> "Error, or an arbitrary single name per city depending on the engine. Once you GROUP BY, every selected column has to be grouped or aggregated. full_name is neither."

---

### Part 3 — HAVING versus WHERE (10 min)

```sql
SELECT membership_tier, AVG(total_spent) AS avg_spend
FROM customers
GROUP BY membership_tier
HAVING AVG(total_spent) > 80000;
-- expect one row: Gold, 156250
```

> "HAVING filters the groups after they are built. WHERE cannot see AVG(total_spent) at all, because WHERE runs before grouping happens."

```sql
-- this fails
SELECT membership_tier, AVG(total_spent)
FROM customers
WHERE AVG(total_spent) > 80000
GROUP BY membership_tier;
```

> "That errors. Aggregates do not exist yet at the point WHERE runs. HAVING is the only clause that can filter on one."

---

### Part 4 — Verify before you trust it (7 min)

```sql
SELECT SUM(total_spent) FROM customers;
-- 858000
```

```sql
SELECT SUM(total_spend) FROM (
  SELECT city, SUM(total_spent) AS total_spend FROM customers GROUP BY city
);
-- also 858000
```

> "Same number, reached two different ways. That match is not a coincidence, it is what verification looks like. If these two numbers had disagreed, that would mean a bug, and the report should not go out until it is found."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Writing WHERE with an aggregate condition | "WHERE runs before GROUP BY, so it cannot test SUM or AVG. That condition always belongs in HAVING." |
| Adding a non-aggregated column to SELECT under GROUP BY | "Every column in SELECT has to be either the grouped column or wrapped in an aggregate, no third option." |
| Confusing COUNT(*) and COUNT(column) | "COUNT(*) counts rows. COUNT(column) counts non-NULL values in that column. They only match when the column has no NULLs." |

---

## Up Next

Topic 3.4 - Joins and Subqueries. Aggregation so far has stayed inside one table. Next you combine customers with orders, and predicting a join's row count becomes a required step, not just good practice.
