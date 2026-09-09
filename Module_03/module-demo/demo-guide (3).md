# Module Demo Guide - SQL and Databases (Module 3)
**Module 3 | Estimated duration: 70 minutes**

---

## The Story

**Eko Traders** is a growing Nigerian retail chain with branches in Lagos, Ibadan, Abuja, Port Harcourt and Kano. Damilola Ade has just joined as a junior data analyst. Her first week's task: get comfortable with the company's live database, answer a real question for the Lagos branch manager, build a summary report for finance, and start using AI to speed up her queries without letting it quietly ship a wrong number.

**What this demo builds:**

A single working session that takes Damilola (and the trainees playing her role) from reading Eko Traders' raw schema to auditing an AI-written query with confidence:

- Reads Eko Traders' relational schema and identifies the primary and foreign keys linking `customers`, `orders`, `order_items`, `products` and `payments` (Topic 3.1)
- Writes SELECT, WHERE and ORDER BY queries to answer a real question from the Lagos branch manager (Topic 3.2)
- Builds a GROUP BY / HAVING summary report and verifies its totals against a known reference figure before trusting it (Topic 3.3)
- Joins customers to orders with INNER and LEFT JOIN, predicting each join's row count before running it, then answers a layered question with a subquery (Topic 3.4)
- Explains why a two-year historical report shouldn't run against the live database, and reads a small star schema built from the same data (Topic 3.5)
- Uses AI to draft a query from a prompt, audits it with the module's five-check checklist, and catches a real bug before it reaches a stakeholder (Topic 3.6)

---

## Prerequisites

1. A SQLite environment ready for trainees: the classroom SQLite CLI, or DB Browser for SQLite.
2. `eko_traders.db` copied into each trainee's working folder (from this module's `module-demo/` folder).
3. Trainees have completed the labs for 3.1–3.5, or this session is being run as the whole-module synthesis review directly before the graded query set.
4. An AI assistant available and open for Part 6, the same one used in the 3.6 lab.

> **Instructor note:** `eko_traders.db` contains two customer scopes. Topics 3.2, 3.3 and 3.5 use the full 10-row `customers` table. Topics 3.4 and 3.6 deliberately use a smaller 5-customer, 4-order slice (customer_id 101–105) so row counts stay hand-countable. A view called `join_demo_customers` already scopes this for you. If you join against the full `customers` table in Part 4 by mistake, the LEFT JOIN will return 11 rows, not 6, because customers 106–110 also have no orders. Use `join_demo_customers`, not `customers`, for every query in Parts 4 and 6.

---

## Dataset / Project Setup (before the demo starts)

1. Copy `eko_traders.db` to a shared location trainees can reach, or have them copy it into their own project folder.
2. Open it once yourself and confirm the load succeeded:
   ```sql
   SELECT COUNT(*) FROM customers;   -- expect 10
   SELECT COUNT(*) FROM orders;      -- expect 4
   SELECT COUNT(*) FROM fact_sales;  -- expect 6
   ```
3. Confirm the view exists: `SELECT * FROM join_demo_customers;` should return exactly 5 rows (customer_id 101–105).
4. Have the AI assistant used in Part 6 open and signed in before the demo starts, so Part 6 doesn't lose time to a login screen.

---

## Demo Steps

### Part 1 - Database concepts and relational thinking (8 min)

> "Before Damilola writes a single query, she needs to read the schema she's about to work in. Let's look at what she's given."

**Show the schema:**
```sql
.schema customers
.schema orders
```

```sql
SELECT * FROM customers LIMIT 3;
SELECT * FROM orders;
```

> "`customers` has one row per person: `customer_id` is the primary key, never repeated. `orders` has its own primary key, `order_id`, but also a `customer_id` column. That's a foreign key, pointing back to whose order it is. One customer can have several orders, which is exactly why these are two tables and not one."

**Ask students:** Why can't Eko Traders just add an `orders` column onto the `customers` table and list every order a customer has made inside it?

> "Because a customer can have more than one order, and a single column can't hold a variable number of values cleanly. That's what a foreign key and a second table solve, and it is the same reasoning as the module's 'grain' concept: one row should represent one clear thing."

---

### Part 2 - Core querying: SELECT, WHERE, ORDER BY (10 min)

> "The Lagos branch manager wants a quick answer: which Lagos customers are Gold tier, ranked by how much they've spent? Let's build that up clause by clause."

```sql
SELECT full_name, city, membership_tier, total_spent
FROM customers
WHERE city = 'Lagos' AND membership_tier = 'Gold'
ORDER BY total_spent DESC;
```

> "SELECT picks the columns. WHERE narrows to Lagos, Gold tier only. ORDER BY puts the highest spender first. Three clauses, same fixed order every time."

**Run it and check the result:**
Expect 2 rows: Chidinma Okafor (185000), Yusuf Ibrahim (132000).

> "Two names, ranked by spend. That's the branch manager's list, straight from one query."

---

### Part 3 - Aggregation and grouping (12 min)

> "Now finance wants something different: not individual customers, but totals, spend and customer count by city."

```sql
SELECT city, COUNT(*) AS customer_count, SUM(total_spent) AS total_spend
FROM customers
GROUP BY city
ORDER BY total_spend DESC;
```

> "GROUP BY collapses the ten customers into five city rows. Before we trust these numbers, we verify: does the grand total match something we already know?"

```sql
SELECT SUM(total_spent) FROM customers;
```

> "858000. That's the number finance has been quoting all along. It matches, so this report is safe to send."

**Ask students:** What would you check first if that total had come back as 900000 instead?

> "Not whether finance's figure is wrong. Check your own query first. A duplicate row, a WHERE clause that dropped some customers, or a NULL being silently skipped by SUM are all more likely than someone else's number being wrong."

---

### Part 4 - Joins and subqueries (15 min)

> "Now Damilola needs something no single table can answer: which customers have never placed an order? For this, we use the smaller `join_demo_customers` view: 5 customers, 4 orders, small enough to count by hand."

**Predict first:**

> "Two of these five customers have never ordered. If I INNER JOIN customers to orders, I should get 4 rows, one per order. If I LEFT JOIN instead, I should get 6: the 4 matched orders, plus one extra row each for the two customers with none."

```sql
SELECT COUNT(*) FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id;
-- expect 4

SELECT COUNT(*) FROM join_demo_customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
-- expect 6
```

> "Both match the prediction. Now isolate the gap."

```sql
SELECT c.full_name
FROM join_demo_customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

Expect Tunde Bakare and Ngozi Eze.

> "That's the LEFT JOIN plus IS NULL pattern, one of the most useful things in this whole module. Now a layered question, without a JOIN at all: which customers have at least one Delivered order?"

```sql
SELECT full_name FROM join_demo_customers
WHERE customer_id IN (
  SELECT customer_id FROM orders WHERE status = 'Delivered'
);
```

Expect Chidinma Okafor and Aisha Mohammed.

> "The inner query builds the list of qualifying IDs first, then the outer query filters against it. Same predict-then-check habit, aimed at a subquery instead of a join."

---

### Part 5 - Warehousing fundamentals (10 min)

> "Finance now wants total revenue by product category for Q1 2026. Running that against five joined OLTP tables, live, would compete with the checkout system for resources. Instead, we use a small warehouse-shaped copy of the same data."

```sql
.schema fact_sales
.schema dim_product
```

> "`fact_sales` has one row per line item sold: its grain, plus foreign keys and numbers to sum. `dim_product` describes the product: name and category, nothing to aggregate. That split is the star schema."

```sql
SELECT p.category, SUM(f.line_total) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
JOIN dim_date d ON f.date_key = d.date_key
WHERE d.quarter = 'Q1 2026'
GROUP BY p.category
ORDER BY revenue DESC;
```

Expect Electronics 43000, Groceries 34000, Snacks 7500.

> "Same SELECT, JOIN, GROUP BY skills from Parts 2 to 4, just aimed at a fact table and a dimension table instead of two OLTP tables."

---

### Part 6 - AI-augmented SQL (15 min)

> "Last piece: Damilola asks an AI assistant to help her count how many unique customers ordered something in Q1 2026. Let's see what it gives her."

**Prompt used:**
> "Write a SQL query to count how many customers ordered something in the first quarter of 2026, using our customers and orders tables."

**What the AI wrote back:**
```sql
SELECT COUNT(*) AS customer_count
FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= '2026-01-01' AND o.order_date <= '2026-03-31';
```

> "Before running it, predict. Chidinma ordered twice in Q1, Aisha once. That's 2 unique customers. Let's run it and check."

```sql
-- returns 3, not 2
```

> "3, not 2. Something's wrong. The JOIN produces one row per order, not per customer. Chidinma's two orders each add 1 to COUNT(*), so she's counted twice. The prompt never said 'unique.'"

**The fix:**
```sql
SELECT COUNT(DISTINCT c.customer_id) AS customer_count
FROM join_demo_customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date BETWEEN '2026-01-01' AND '2026-03-31';
-- returns 2, matching the prediction
```

**Ask students:** If this had shipped as 3 in a board report, who would have caught it, and when?

> "Nobody, probably, until the numbers didn't reconcile somewhere downstream. That's the whole point of predicting before running: Damilola caught this before it ever left her screen."

---

## Demo Wrap-Up

| Capability | Topic it came from | What it shows |
|---|---|---|
| Reading `customers`/`orders` and naming primary and foreign keys | 3.1 | Schema literacy |
| Lagos Gold-tier customer list, filtered and sorted | 3.2 | SELECT / WHERE / ORDER BY |
| Spend-by-city report, verified against a known total | 3.3 | GROUP BY / HAVING and reference verification |
| INNER and LEFT JOIN with predicted row counts; IN-subquery | 3.4 | Joins, subqueries, row-count prediction |
| Category revenue from a star schema | 3.5 | OLTP vs. warehouse, fact and dimension tables |
| AI-drafted query, audited, bug found and fixed | 3.6 | Prompting, critical reading, verification |

> "Every query in this session used the same five clauses in the same order: SELECT, FROM, JOIN, WHERE, GROUP BY, ORDER BY. What changed across the module wasn't the syntax. It was Damilola's ability to predict what a query should return before trusting what it did return, whether she wrote it or AI did."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| LEFT JOIN in Part 4 returns 11 rows instead of 6 | "You're joining against the full `customers` table. Use `join_demo_customers`: the whole point of that view is to keep the row counts hand-countable for this exercise." |
| Forgetting quotes around `'Lagos'` or a date string | "Text values need single quotes. Without them, SQLite reads `Lagos` as a column name, not a value, and errors out." |
| GROUP BY error when a non-aggregated column sneaks into SELECT | "Once you GROUP BY, every column in SELECT must be either the grouped column or wrapped in an aggregate. Check what's in your SELECT list against what's in GROUP BY." |
| Part 6's AI gives a different (correct) query on a retry | "That can happen. The point isn't that AI always gets it wrong, it's that you predict and verify regardless of whether it's right or wrong. Ask them to still run the prediction step even if the first query looks fine." |
| Confusing WHERE and HAVING when filtering the Part 3 city report by a total threshold | "WHERE filters rows before grouping; HAVING filters groups after. A condition on SUM(total_spent) has to be HAVING, because WHERE runs before SUM exists." |
