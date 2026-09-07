# Demo Guide - Loading and Inspecting Data with pandas
**Module 5, Topic 5.2 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Import pandas and load `Optimum_branch_sales.csv` into a DataFrame
- Inspect a DataFrame's dimensions, data types and missing values before trusting it
- Select a single column and select multiple columns, and explain the difference between the two results
- Filter rows with a Boolean condition to answer a specific business question
- Answer a simple analytical question directly from the loaded data

---

## Setup - Before the Demo Starts

1. Continuing in the same notebook as Topic 5.1, with `branch_name`, `daily_sales`, `transaction`, `target`, `average_sale()` and `clean_price()` already defined from that demo.
2. `Optimum_branch_sales.csv` uploaded to this Colab session's file storage.
3. Trainees have completed Topic 5.1: applying fundamentals to real figures, reading an error message, and debugging a broken cell.

> **Instructor note:** if `df.dtypes` shows `str` instead of `object` for the text columns on your machine, that is a newer pandas release (3.0 and above) defaulting to a different internal string type. It does not change anything trainees see or do in this guide. Everything here was run and verified with `pd.set_option("future.infer_string", False)` set first, to keep the classic `object` labelling this guide shows.

---

## Demo Steps

### Part 1 - Import Pandas and Load the Real File (6 min)

> "Everything we did by hand last topic, one list here, one dictionary there, pandas does for a whole file at once. Let's bring in Optimum's actual transaction log."

```python
import pandas as pd

df = pd.read_csv("Optimum_branch_sales.csv")
df.head()
```

Output:
```text
   TransactionID  Branch         Region            Customer           Product   Sales    Cost  Profit    Price        Date
0              1   Lagos     South West      Sunrise Stores         Rice 50kg  145000  123250   21750  29000.0  2026-01-05
1              2   Abuja  North Central  Greenfield Traders   Cooking Oil 25L   98000   83300   14700      NaN  2026-01-05
2              3    Kano     North West          Kings Mart  Detergent Carton   52000   44200    7800  13000.0  2026-01-06
3              4   Lagos     South West    Delta Provisions   Beverages Crate  132000  112200   19800  11000.0  2026-01-06
4              5  Ibadan     South West   Horizon Retailers        Flour 50kg   87000   73950   13050      NaN  2026-01-07
```

> "Twenty transactions live in this file, we're only looking at the first five. Notice `branch_name` and `transaction` from Topic 5.1 are still sitting in this same notebook, untouched. `df` is a completely new object, a table instead of one dictionary."

### Part 2 - First Inspection: Shape, Types and Missing Values (10 min)

> "Before anyone reports a single number from this file, we check three things: how big is it, what type is each column, and where are the gaps. We already met one of these ideas last topic, when Price arrived as text with a Naira symbol attached."

```python
df.shape
```

Output:
```text
(20, 10)
```

**Ask students:** "Sales, Cost and Profit are all whole Naira amounts, and pandas shows them as `int64`. Given what we know about this file, do you expect Price to also come back as `int64`, or as `float64`? Why?"

> "Let's find out."

```python
df.dtypes
```

Output:
```text
TransactionID      int64
Branch            object
Region            object
Customer          object
Product           object
Sales              int64
Cost               int64
Profit             int64
Price            float64
Date              object
dtype: object
```

> "`float64`, and here's why: Price has at least one missing value somewhere in this file. pandas cannot represent a gap inside a column of whole numbers, so the moment one value is missing, the entire column becomes decimal-capable to make room for it. Let's confirm that's genuinely what's happening."

```python
df.isna().sum()
```

Output:
```text
TransactionID    0
Branch           0
Region           0
Customer         0
Product          0
Sales            0
Cost             0
Profit           0
Price            4
Date             0
dtype: int64
```

> "Four transactions are missing a Price. If we calculated something using Price on one of these rows without checking first, we'd get a silent gap, not the loud, readable error we practised handling last topic. That's exactly why this check happens before any calculation, not after."

### Part 3 - Selecting Columns: One vs Many (7 min)

> "Now that we trust what's in this file, let's start pulling pieces out of it. There are two ways to select columns, and they don't return the same kind of thing."

```python
df["Sales"]
```

Output:
```text
0    145000
1     98000
2     52000
Name: Sales, dtype: int64
```

```python
df[["Sales", "Profit"]]
```

Output (first two rows):
```text
    Sales  Profit
0  145000   21750
1   98000   14700
```

> "Single brackets and one name give you a Series, one labelled column on its own. Double brackets and a list of names give you a DataFrame, a smaller table. Run `type()` on each if anyone doubts it, they genuinely are different objects, not just displayed differently."

### Part 4 - Filtering Rows to Answer a Real Question (8 min)

> "Optimum's regional manager wants to know which transactions actually clear ₦100,000. This is the same rule from Topic 5.1's loop, applied to the whole file in one line instead of one branch's list."

```python
df[df["Sales"] > 100000]
```

Output:
```text
10 rows match, out of 20
```

> "Half of this month's transactions clear the threshold. In Excel, this is the filter arrow. Here, it's one line we can rerun on next month's file the moment it lands."

### Part 5 - Answering a Business Question Directly (7 min)

> "One more real question before we finish: which products have a transaction with no recorded Price?"

```python
df[df["Price"].isna()]["Product"]
```

Output:
```text
Cooking Oil 25L
Flour 50kg
Detergent Carton
Cooking Oil 25L
```

> "Cooking Oil appears twice. Somewhere among these four rows is very likely the same kind of currency-formatted price we cleaned by hand last topic, just not yet caught. Topic 5.3 is where we calculate with this data properly, and where a check like this one becomes the difference between a correct report and a silently wrong one."

---

## Final State of the Notebook

By the end of this demo, the notebook holds everything from Topic 5.1, plus:

```python
import pandas as pd

df = pd.read_csv("Optimum_branch_sales.csv")
```

`df` is now the live DataFrame every Part in Topic 5.3 builds on directly.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| `FileNotFoundError` when running `pd.read_csv("Optimum_branch_sales.csv")` | "Colab's file storage does not persist between sessions. Re-upload the CSV through the Files panel on the left, then run the cell again." |
| `KeyError: 'sales'` or similar, when a trainee types a column name in lower case | "pandas is case-sensitive and matches exactly. Run `df.columns` and compare it character by character against what you typed, this file uses Sales with a capital S." |
| Trainee treats `df["Sales"]` and `df[["Sales"]]` as identical because they print similarly | "They print similarly but are different objects, a Series and a DataFrame. Ask them to run `type()` on each and compare the results directly." |

---

## Up Next

Topic 5.3 takes this same loaded DataFrame and filters, sorts, groups and aggregates it, then adds a calculated column that gets checked against a figure Optimum's own system already recorded.
