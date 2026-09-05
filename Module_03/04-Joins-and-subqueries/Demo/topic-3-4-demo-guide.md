# Demo Guide - Joins and Subqueries
**Module 3, Topic 3.4 | Estimated duration: 40-45 minutes**

---

## What This Demo Teaches

- Combining two tables with INNER JOIN
- Combining two tables with LEFT JOIN, and explaining how it differs from INNER JOIN
- Predicting a join's row count before running it
- Using a subquery to answer a question that needs a list from one table first

---

## Setup — Before the Demo Starts

1. SQLite ready, connected to `eko_traders.db`.
2. Confirm the view loaded: `SELECT COUNT(*) FROM join_demo_customers;` should return 5.

> **Instructor note:** This topic uses `join_demo_customers`, not the full `customers` table. It is a 5-row slice (customer_id 101-105) with only 4 orders between them, small enough that every row count in this demo can be predicted on paper. Joining against the full 10-row `customers` table instead will not match the numbers below, because customers 106-110 also have no orders and will inflate a LEFT JOIN to 11 rows, not 6.

---

## Demo Steps

### Part 1 — INNER JOIN (10 min)

```sql
SELECT * FROM join_demo_customers;
SELECT * FROM orders;
```

> "Five customers, four orders. Chidinma has two, Aisha has one, Emeka has one, Tunde and Ngozi have none. Before I write the join, predict: how many rows should an INNER JOIN return?"

**Ask students:** What is your prediction, and why?

> "Four. INNER JOIN only keeps matched pairs, and there are four orders with a matching customer."

```sql
SELECT c.full_name, o.order_id, o.status
FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id;
-- expect 4 rows
```

> "Matches the prediction. Chidinma appears twice, once per order. Tunde and Ngozi do not appear at all."

---

### Part 2 — LEFT JOIN (10 min)

**Ask students:** Same tables, but LEFT JOIN instead. What do you predict now?

> "Six. The same four matched rows, plus one extra row each for Tunde and Ngozi, who have zero orders but still get kept."

```sql
SELECT c.full_name, o.order_id, o.status
FROM join_demo_customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
-- expect 6 rows
```

> "Tunde and Ngozi now appear once each, with NULL in the order columns. NULL here means no match was found, not zero, not an error."

---

### Part 3 — Finding the gap (8 min)

```sql
SELECT c.full_name
FROM join_demo_customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
-- expect Tunde Bakare, Ngozi Eze
```

> "LEFT JOIN plus IS NULL on a right-hand column. This is how you find rows in one table with nothing matching in another, one of the most useful patterns in SQL."

---

### Part 4 — Subqueries (10 min)

```sql
SELECT full_name
FROM join_demo_customers
WHERE customer_id IN (
  SELECT customer_id FROM orders WHERE status = 'Delivered'
);
-- expect Chidinma Okafor, Aisha Mohammed
```

> "The inner query runs first and produces a list, 101 and 103. The outer query then keeps only customers whose ID is in that list. No JOIN needed for this particular question."

**Ask students:** Why is Emeka not in this result, even though he placed an order?

> "His order was Cancelled, not Delivered. The inner query's WHERE excludes it, so 104 never makes it into the list."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Joining against `customers` instead of `join_demo_customers` | "Use the view. The full table has more zero-order customers and will not match the row counts we predicted." |
| Expecting LEFT JOIN to return fewer rows than INNER JOIN | "LEFT JOIN never returns fewer rows than INNER JOIN on the same tables, it only adds unmatched rows, never removes matched ones." |
| Forgetting the subquery's own WHERE clause | "The inner query needs its own condition, status = 'Delivered' here. Without it you get every customer who has ever ordered anything, delivered or not." |

---

## Up Next

Topic 3.5 - Warehousing Fundamentals. Two-table joins scale fine by hand. Next you learn why a live five-table join does not scale the same way for a two-year historical report, and what a warehouse does about it.
