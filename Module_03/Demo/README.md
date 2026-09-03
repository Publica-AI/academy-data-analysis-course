# Eko Traders demo database — Module 3 (SQL & Databases)

`eko_traders.db` is a single SQLite file covering every worked example, live
demo, and guided-practice query across all six topics (3.1–3.6). It replaces
the various individually-named fallback files mentioned in each deck's
speaker notes (`customers.db`, `customers_finished.db`,
`customers_aggregation_finished.db`, `customers_orders_joins_finished.db`,
`eko_traders_warehouse_finished.db`, etc.) with one consistent source, so
every number shown on every slide is reproducible from the same file.

Every headline figure used across the six decks has been checked against
this file programmatically (see `build_db.py`) — all ten checks pass.

## Tables

**OLTP schema (3.1–3.4, 3.6)**
| Table | Rows | Used in |
|---|---|---|
| `customers` | 10 | 3.1–3.4, 3.6 |
| `products` | 5 | 3.1, 3.4 |
| `orders` | 4 | 3.1, 3.4, 3.6 |
| `order_items` | 4 | 3.1 (schema only) |
| `payments` | 3 | 3.1 (schema only) |

**Warehouse / star schema (3.5)**
| Table | Rows | Used in |
|---|---|---|
| `dim_date` | 4 | 3.5 |
| `dim_customer` | 10 | 3.5 |
| `dim_product` | 5 | 3.5 |
| `fact_sales` | 6 | 3.5 |

## One thing to know before demoing 3.4 or 3.6

3.4 and 3.6 deliberately use a **small 5-customer / 4-order slice**
(customer_id 101–105: Chidinma, Tunde, Aisha, Emeka, Ngozi) so trainees can
predict row counts by hand. 3.2, 3.3 and 3.5 use the **full 10-customer
table**.

A view, `join_demo_customers`, already scopes this for you — use it in
place of `customers` when running the 3.4/3.6 join examples live:

```sql
SELECT c.full_name, o.order_id, o.status
FROM join_demo_customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

If you instead join against the full `customers` table, INNER JOIN will
return 4 rows and LEFT JOIN will return 11 (not 6) — correct behavior, just
not the number shown on the 3.4 slides, since customers 106–110 also have
no orders.

## Reproducing each deck's headline numbers

| Topic | Query | Expected |
|---|---|---|
| 3.2 | `SELECT COUNT(*) FROM customers WHERE city = 'Lagos'` | 3 |
| 3.3 | `SELECT COUNT(*), COUNT(phone) FROM customers` | 10, 8 |
| 3.3 | `SELECT SUM(total_spent) FROM customers` | 858000 |
| 3.3 | Gold tier avg spend (`GROUP BY membership_tier HAVING AVG(total_spent) > 80000`) | 156250 |
| 3.4 | INNER JOIN `join_demo_customers` × `orders` | 4 rows |
| 3.4 | LEFT JOIN `join_demo_customers` × `orders` | 6 rows |
| 3.4 | Customers with no orders (LEFT JOIN + IS NULL) | Tunde, Ngozi |
| 3.5 | Electronics revenue, Q1 2026 | 43000 |
| 3.5 | Groceries revenue, Q1 2026 | 34000 |
| 3.5 | Snacks revenue, Q1 2026 | 7500 |
| 3.6 | Unique customers who ordered in Q1 2026 | 2 (not 3 — the AI's original bug) |

## Files

- `eko_traders.db` — the database itself (SQLite 3). Open directly in the
  classroom SQLite environment, DB Browser for SQLite, or any SQLite client.
- `build_db.py` — the script that generates it, including the sanity checks
  above. Re-run with `python3 build_db.py` to rebuild from scratch or verify
  the numbers still reconcile after any edits.
