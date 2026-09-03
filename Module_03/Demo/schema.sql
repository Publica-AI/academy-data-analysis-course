-- Reference / checkpoint file — NOT a script to run instead of typing the SQL live.
--
-- This is the eko_traders schema in its final state, used across every Module 3
-- topic demo (3.1-3.6): all 5 OLTP tables, the 4 warehouse tables from Topic 3.5,
-- and the join_demo_customers view that Topics 3.4 and 3.6 use to keep join row
-- counts hand-countable. All sample data matches what is typed live in each demo.
--
-- Use this to check your schema if something isn't matching, or to rebuild the
-- database from scratch. SQLite: sqlite3 eko_traders.db < schema.sql

-- ============================================================
-- OLTP SCHEMA (3.1-3.4, 3.6)
-- ============================================================

CREATE TABLE customers (
    customer_id     INTEGER PRIMARY KEY,
    full_name       TEXT NOT NULL,
    city            TEXT NOT NULL,
    phone           TEXT,
    membership_tier TEXT NOT NULL,
    total_spent     INTEGER NOT NULL,
    joined_date     TEXT NOT NULL
);

CREATE TABLE products (
    product_id   TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category     TEXT NOT NULL,
    unit_price   INTEGER NOT NULL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,
    status      TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id      INTEGER NOT NULL,
    product_id    TEXT NOT NULL,
    quantity      INTEGER NOT NULL,
    line_total    INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id   INTEGER PRIMARY KEY,
    order_id     INTEGER NOT NULL,
    amount       INTEGER NOT NULL,
    payment_date TEXT NOT NULL,
    method       TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

INSERT INTO customers (customer_id, full_name, city, phone, membership_tier, total_spent, joined_date) VALUES
(101, 'Chidinma Okafor', 'Lagos',         '+234 803 555 0101', 'Gold',   185000, '2025-03-14'),
(102, 'Tunde Bakare',    'Ibadan',        '+234 805 555 0102', 'Silver',  62000, '2025-05-02'),
(103, 'Aisha Mohammed',  'Abuja',         '+234 806 555 0103', 'Gold',   210000, '2024-11-20'),
(104, 'Emeka Nwosu',     'Lagos',         '+234 807 555 0104', 'Bronze',  18000, '2026-01-09'),
(105, 'Ngozi Eze',       'Port Harcourt', '+234 808 555 0105', 'Silver',  74500, '2025-08-30'),
(106, 'Yusuf Ibrahim',   'Lagos',         '+234 809 555 0106', 'Gold',   132000, '2025-02-17'),
(107, 'Habiba Sule',     'Abuja',         '+234 810 555 0107', 'Silver',  45000, '2025-06-11'),
(108, 'Chinedu Obi',     'Port Harcourt', NULL,                'Bronze',  12500, '2025-09-02'),
(109, 'Fatima Bello',    'Kano',          '+234 812 555 0109', 'Gold',    98000, '2025-04-25'),
(110, 'Ikechukwu Umeh',  'Ibadan',        NULL,                'Bronze',  21000, '2025-07-19');

INSERT INTO products (product_id, product_name, category, unit_price) VALUES
('P1', 'Rice Bag 5kg',      'Groceries',   8000),
('P2', 'Bluetooth Speaker', 'Electronics', 25000),
('P3', 'Biscuit Pack',      'Snacks',      1500),
('P4', 'Wireless Earbuds',  'Electronics', 18000),
('P5', 'Cooking Oil 2L',    'Groceries',   6000);

INSERT INTO orders (order_id, customer_id, order_date, status) VALUES
(5001, 101, '2026-01-05', 'Delivered'),
(5002, 101, '2026-02-10', 'Delivered'),
(5003, 103, '2026-03-05', 'Delivered'),
(5004, 104, '2026-04-02', 'Cancelled');

INSERT INTO order_items (order_item_id, order_id, product_id, quantity, line_total) VALUES
(1, 5001, 'P1', 2, 16000),
(2, 5002, 'P4', 1, 18000),
(3, 5003, 'P2', 1, 25000),
(4, 5004, 'P5', 3, 18000);

INSERT INTO payments (payment_id, order_id, amount, payment_date, method) VALUES
(1, 5001, 16000, '2026-01-05', 'Card'),
(2, 5002, 18000, '2026-02-10', 'Transfer'),
(3, 5003, 25000, '2026-03-05', 'Card');

-- Topics 3.4 and 3.6 use this view: 5 customers, 4 orders, small enough to
-- predict row counts by hand. The full customers table (10 rows) is used
-- everywhere else. Joining against customers instead of this view in a
-- 3.4/3.6 demo will not reproduce the row counts in those guides.
CREATE VIEW join_demo_customers AS
SELECT * FROM customers WHERE customer_id BETWEEN 101 AND 105;

-- ============================================================
-- WAREHOUSE / STAR SCHEMA (3.5)
-- ============================================================

CREATE TABLE dim_date (
    date_key  TEXT PRIMARY KEY,
    full_date TEXT NOT NULL,
    month     TEXT NOT NULL,
    quarter   TEXT NOT NULL,
    year      INTEGER NOT NULL
);

CREATE TABLE dim_customer (
    customer_key    INTEGER PRIMARY KEY,
    full_name       TEXT NOT NULL,
    city            TEXT NOT NULL,
    membership_tier TEXT NOT NULL
);

CREATE TABLE dim_product (
    product_key  TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category     TEXT NOT NULL
);

CREATE TABLE fact_sales (
    sale_key     TEXT PRIMARY KEY,
    date_key     TEXT NOT NULL,
    customer_key INTEGER NOT NULL,
    product_key  TEXT NOT NULL,
    quantity     INTEGER NOT NULL,
    line_total   INTEGER NOT NULL,
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);

INSERT INTO dim_date (date_key, full_date, month, quarter, year) VALUES
('D1', '2026-01-10', 'January',  'Q1 2026', 2026),
('D2', '2026-02-14', 'February', 'Q1 2026', 2026),
('D3', '2026-03-05', 'March',    'Q1 2026', 2026),
('D4', '2026-04-02', 'April',    'Q2 2026', 2026);

INSERT INTO dim_customer SELECT customer_id, full_name, city, membership_tier FROM customers;
INSERT INTO dim_product SELECT product_id, product_name, category FROM products;

INSERT INTO fact_sales (sale_key, date_key, customer_key, product_key, quantity, line_total) VALUES
('F1', 'D1', 101, 'P1', 2, 16000),
('F2', 'D1', 103, 'P2', 1, 25000),
('F3', 'D2', 106, 'P3', 5, 7500),
('F4', 'D2', 101, 'P4', 1, 18000),
('F5', 'D3', 104, 'P5', 3, 18000),
('F6', 'D4', 103, 'P2', 1, 25000);
