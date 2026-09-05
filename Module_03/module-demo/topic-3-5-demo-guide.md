# Demo Guide - Warehousing Fundamentals
**Module 3, Topic 3.5 | Estimated duration: 30-35 minutes**

---

## What This Demo Teaches

- Explaining the difference between a transactional (OLTP) database and a data warehouse
- Identifying the fact table in a star schema
- Identifying dimension tables in a star schema
- Running a simple query against a star schema using skills already learned

---

## Setup — Before the Demo Starts

1. SQLite ready, connected to `eko_traders.db`.
2. Confirm the warehouse tables loaded: `SELECT COUNT(*) FROM fact_sales;` should return 6.

> **Tell students:** "Nothing in this database is new data. It is the same customers and products information, reshaped into four new tables: dim_date, dim_customer, dim_product, fact_sales."

---

## Demo Steps

### Part 1 — Why not just query the OLTP tables (8 min)

> "Imagine finance wants total revenue by product category, across two years, and the query runs directly against the live database the checkout app writes to every second."

**Ask students:** What is the risk of running that query there instead of somewhere else?

> "A heavy, multi-join query scanning years of history competes for the same resources as real customers checking out right now. That is the whole reason a separate warehouse exists, not because the OLTP tables are wrong, just because they are tuned for a different job."

---

### Part 2 — The star schema (10 min)

```sql
.schema fact_sales
.schema dim_product
```

> "fact_sales holds the numbers, quantity and line_total, plus foreign keys out to every dimension. Its grain is one row per line item sold. dim_product describes the product, name and category, nothing to sum."

```sql
SELECT * FROM fact_sales;
SELECT * FROM dim_product;
```

**Ask students:** Which of these two tables would you call the fact table, and which the dimension?

> "fact_sales is the fact table, numeric measures and foreign keys, one row per event. dim_product is a dimension, descriptive text, one row per product, far fewer rows than fact_sales and much slower to grow."

---

### Part 3 — Querying the star schema (10 min)

```sql
SELECT p.category, SUM(f.line_total) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
JOIN dim_date d ON f.date_key = d.date_key
WHERE d.quarter = 'Q1 2026'
GROUP BY p.category
ORDER BY revenue DESC;
```

> "SELECT, JOIN, GROUP BY, ORDER BY. Same clauses from 3.2 to 3.4, just aimed at a fact table and two dimensions instead of two OLTP tables."

Expect: Electronics 43000, Groceries 34000, Snacks 7500.

> "Three categories, ranked. Notice the Q2 2026 sale in fact_sales does not appear anywhere in this total, the WHERE clause correctly excluded it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Calling dim_product the fact table because it has "product" in fact_sales | "Look at the columns, not the name. Numbers to sum and foreign keys out mean fact. Descriptive text and one clear primary key mean dimension." |
| Assuming the warehouse tables contain different data from the OLTP tables | "Same underlying data, reshaped. dim_customer is built from the same customers table you already know." |
| Trying to write GROUP BY without JOIN-ing the needed dimension first | "category lives in dim_product, not fact_sales. If a column you need is in a dimension, that dimension has to be joined in first." |

---

## Up Next

Topic 3.6 - AI-Augmented SQL. The database concepts stop here. Next, AI starts writing full queries for you, and the whole module's habits, schema reading, predicting, verifying, get aimed at auditing someone else's SQL.
