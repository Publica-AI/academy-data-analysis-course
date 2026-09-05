# Demo Guide - Core Querying: SELECT, WHERE, ORDER BY
**Module 3, Topic 3.2 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Selecting specific columns instead of every column
- Filtering rows with WHERE and comparison operators
- Combining conditions with AND / OR
- Sorting results with ORDER BY, ascending and descending

---

## Setup — Before the Demo Starts

1. SQLite ready, connected to `eko_traders.db` (rebuild from `schema.sql` if needed).
2. Confirm the table loaded: `SELECT COUNT(*) FROM customers;` should return 10.

> **Tell students:** "Every query today runs against the same customers table from 3.1. We are not changing the schema, we are asking it questions."

---

## Demo Steps

### Part 1 — SELECT and columns (7 min)

```sql
SELECT * FROM customers;
```

> "Every column, every row. Fine for a quick look, but messy for a real report."

```sql
SELECT full_name, city FROM customers;
```

> "Two columns, all ten rows. Naming your columns is the default in real work, SELECT * is for exploring only."

---

### Part 2 — WHERE and comparison operators (10 min)

```sql
SELECT full_name, city FROM customers WHERE city = 'Lagos';
```

> "Three rows. WHERE keeps the ones that pass the test, drops the rest."

```sql
SELECT full_name, total_spent FROM customers WHERE total_spent > 100000;
```

**Ask students:** Before I run this, how many rows do you expect?

> "Three: Chidinma, Aisha, Yusuf, everyone above the 100000 mark. Predicting before running is a habit that starts here and never stops for the rest of this module."

```sql
-- what happens without quotes
SELECT * FROM customers WHERE city = Lagos;
```

> "Error. Lagos without quotes looks like a column name to SQLite, not a text value. Always quote text."

---

### Part 3 — AND / OR (8 min)

```sql
SELECT full_name FROM customers WHERE city = 'Lagos' AND membership_tier = 'Gold';
-- expect 2 rows
```

```sql
SELECT full_name FROM customers WHERE city = 'Lagos' OR city = 'Ibadan';
-- expect 5 rows
```

> "AND narrows, both conditions must hold. OR widens, either one qualifies. Same two conditions, opposite effect on the row count, depending only on which word you use."

---

### Part 4 — ORDER BY (8 min)

```sql
SELECT full_name, total_spent FROM customers ORDER BY total_spent;
```

> "Ascending, lowest first, that is the silent default."

```sql
SELECT full_name, total_spent FROM customers ORDER BY total_spent DESC;
```

> "DESC flips it, highest spender first. 'Top N' questions almost always mean DESC."

```sql
SELECT full_name, city, total_spent
FROM customers
WHERE membership_tier = 'Gold'
ORDER BY total_spent DESC;
```

> "SELECT, FROM, WHERE, ORDER BY, in that fixed order. Every query for the rest of this module follows this same skeleton, clauses just get added to it."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Forgetting quotes around text values | "SQLite reads unquoted Lagos as a column name. Text always needs single quotes." |
| Writing WHERE after ORDER BY | "The order is fixed: SELECT, FROM, WHERE, ORDER BY. Swapping WHERE and ORDER BY is a syntax error." |
| Expecting AND to return more rows than OR | "Walk through one row by hand against both conditions. AND needs both true, so it can only keep as many or fewer rows than OR." |

---

## Up Next

Topic 3.3 - Aggregation and Grouping. Instead of a list of matching rows, you start asking for totals, counts and averages.
