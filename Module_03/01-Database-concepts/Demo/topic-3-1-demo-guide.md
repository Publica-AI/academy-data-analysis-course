# Demo Guide - Database Concepts and Relational Thinking
**Module 3, Topic 3.1 | Estimated duration: 30-35 minutes**

---

## What This Demo Teaches

- Reading a relational schema and explaining what each table represents
- Identifying a primary key and explaining why it must be unique
- Identifying a foreign key and tracing what it points to
- Explaining, with a concrete example, why a database beats a spreadsheet for this data

---

## Setup — Before the Demo Starts

1. SQLite ready — classroom CLI or DB Browser for SQLite.
2. `eko_traders.db` copied into the working folder (build from `schema.sql` if starting fresh: `sqlite3 eko_traders.db < schema.sql`).
3. Terminal or DB Browser open and connected to `eko_traders.db`.

> **Tell students:** "Everything we do for the rest of this module runs against this one database. Today we are not writing queries yet, we are just learning to read what is already here."

---

## Demo Steps

### Part 1 — Look at the tables (8 min)

```sql
.tables
```

```sql
.schema customers
.schema orders
```

> "Five tables: customers, products, orders, order_items, payments. Two of them, customers and orders, are what we will spend today on."

```sql
SELECT * FROM customers LIMIT 3;
```

> "One row per customer. That is the table's grain, what one row represents. Every table in this database has a grain, and it is the first thing to check before writing any query."

---

### Part 2 — Primary keys (7 min)

```sql
SELECT customer_id, full_name FROM customers;
```

> "customer_id is the primary key. Every value here is unique, no repeats. That is what makes a primary key a primary key, not that it is the first column, not that it is a number."

**Ask students:** What would break if two customers both had customer_id 101?

> "A query joining on customer_id would not know which Chidinma or whoever else shares that number to match. Primary keys exist so a row can be found unambiguously."

---

### Part 3 — Foreign keys (8 min)

```sql
.schema orders
```

```sql
SELECT * FROM orders;
```

> "orders has its own primary key, order_id. It also has a customer_id column, and that is a foreign key. It does not identify an orders row, it points outward, back to a row in customers."

```sql
SELECT o.order_id, o.status, c.full_name
FROM orders o, customers c
WHERE o.customer_id = c.customer_id;
```

> "We have not covered JOIN syntax yet, that is Topic 3.4, but this is the idea: the foreign key is how these two tables connect. customer_id 101 in orders and customer_id 101 in customers are the same person."

---

### Part 4 — Why a database, not a spreadsheet (7 min)

> "Imagine this data as a spreadsheet instead. Two staff members open it at the same time and both edit Chidinma's phone number. What happens?"

**Ask students:** What would you expect a spreadsheet to do in that situation?

> "One edit silently overwrites the other, and nobody is told. A database can enforce rules a spreadsheet cannot: customer_id must be unique, a foreign key must point to a row that actually exists, and two people editing at once do not corrupt each other's work silently."

```sql
INSERT INTO customers (customer_id, full_name, city, membership_tier, total_spent, joined_date)
VALUES (101, 'Duplicate Test', 'Lagos', 'Bronze', 0, '2026-01-01');
```

> "That fails, UNIQUE constraint on the primary key. This is the database refusing to let bad data in. A spreadsheet would just let it happen."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Confusing which table "owns" customer_id | "It is the primary key in customers, where it identifies the row. In orders it is a foreign key, it identifies which customer, not which order." |
| Assuming a foreign key must have a matching column name | "The column names happen to match here for clarity, but a foreign key just needs to reference a primary key's values, the name itself is your choice." |
| Trying to guess the JOIN syntax early | "We are deliberately not teaching JOIN today, that is 3.4. For now just trace the relationship by eye." |

---

## Up Next

Topic 3.2 - Core Querying. Now that you can read the schema, you start asking it questions with SELECT, WHERE and ORDER BY.
