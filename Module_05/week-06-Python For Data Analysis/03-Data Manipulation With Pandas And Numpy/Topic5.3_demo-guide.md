# Demo Guide - Data Manipulation with pandas and NumPy
**Module 5, Topic 5.3 | Estimated duration: 45-50 minutes**

---

## What This Demo Teaches

- Filter a DataFrame with a Boolean condition and sort the result
- Group transactions by a category and aggregate each group with several summary statistics at once
- Create a calculated column and verify it against a figure the source system already recorded
- Use NumPy for a simple conditional calculation
- Reproduce an analysis Optimum's finance manager already builds in Excel, and confirm the two match exactly

---

## Setup - Before the Demo Starts

1. Continuing in the same notebook as Topics 5.1 and 5.2, with `df` already loaded from `Optimum_branch_sales.csv`.
2. No new file needed, everything in this demo builds on the DataFrame already sitting in memory.
3. Trainees have completed Topic 5.2: loading, inspecting, selecting and filtering.

> **Instructor note:** the single most common trap in this topic is chaining `.sort_values("ColumnName", ...)` directly onto a `groupby(...)["Column"].sum()` result. That result is already a single-column Series, not a DataFrame, and a Series has no column to sort by. Verified live: `df.groupby("Region")["Sales"].sum().sort_values("Sales", ascending=False)` raises `TypeError: Series.sort_values() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given`. Drop the column name and keep only `ascending=False`. If a trainee hits this, it is worth pausing the whole room for, it comes up constantly.

---

## Demo Steps

### Part 1 - Filtering and Sorting (8 min)

> "Topic 5.2 told us ten transactions clear ₦100,000. Optimum's regional manager doesn't just want the count, she wants to see them, biggest first."

```python
high_value = df[df["Sales"] > 100000]
high_value.sort_values("Sales", ascending=False)[["Branch", "Customer", "Product", "Sales"]].head(3)
```

Output:
```text
Branch     Customer         Product  Sales
 Lagos Coastal Mart       Rice 50kg 205000
  Kano   Kings Mart       Rice 50kg 178000
  Kano   Kings Mart Beverages Crate 167000
```

> "Coastal Mart's Rice 50kg order in Lagos is the single biggest transaction this month, at ₦205,000. Filter first, then sort, exactly the order Excel's filter arrow and sort button would run in."

### Part 2 - Grouping: One Category, One Aggregate (8 min)

**Ask students:** "Which region do you expect to come out on top for total Sales, and why? Think back to what Topic 5.2 already told us about how many transactions come from each branch."

> "Let's check."

```python
df.groupby("Region")["Sales"].sum()
```

Output:
```text
Region
North Central     546000
North West        537000
South West       1032000
Name: Sales, dtype: int64
```

> "South West, Lagos and Ibadan combined, outsells the other two regions put together. In Excel, this is a PivotTable: drag Region into Rows, drag Sales into Values. Here, it's one line, and the instructor note above is exactly the trap waiting on the next step, so watch closely."

### Part 3 - Multiple Aggregations at Once (7 min)

> "One total tells us who's ahead. Three numbers tell us why. Let's get the sum, the average and the count together, in one table."

```python
df.groupby("Region")["Sales"].agg(["sum", "mean", "count"])
```

Output:
```text
                   sum      mean  count
Region
North Central   546000  109200.0      5
North West      537000  107400.0      5
South West     1032000  103200.0     10
```

> "South West has the most transactions and the highest total, but the lowest average transaction size. That's a genuinely different story from the one total alone told us, and it's the kind of nuance a manager needs before making a decision."

### Part 4 - Calculated Columns, Verified Against the Source (8 min)

> "Optimum's system already records a Profit figure for every transaction. Let's not take that on faith, let's recompute it independently from Sales and Cost, and check the two match, on every single row."

```python
df["Profit_check"] = df["Sales"] - df["Cost"]
(df["Profit_check"] == df["Profit"]).all()
```

Output:
```text
True
```

> "Every row matches. That's not a formatting check, that's proof the Sales, Cost and Profit columns are internally consistent before we build anything else on top of them."

### Part 5 - NumPy for a Conditional Calculation (6 min)

> "pandas is built on NumPy, and NumPy gives us a fast way to flag a condition across an entire column at once."

```python
import numpy as np

df["Sales_Tier"] = np.where(df["Sales"] > 100000, "High", "Low")
df["Sales_Tier"].value_counts()
```

Output:
```text
Sales_Tier
High    10
Low     10
Name: count, dtype: int64
```

> "Exactly the same ten transactions from Part 1, now labelled permanently on every row instead of recalculated each time we need them."

### Part 6 - Reproducing Optimum's Excel Analysis (10 min)

> "Here's the real test. Optimum's finance manager already builds this exact analysis in Excel every month: total Sales and average profit margin by region, sorted largest to smallest. Let's reproduce it in pandas and see if the two agree."

```python
df["Margin_%"] = (df["Profit"] / df["Sales"] * 100).round(1)
df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Margin=("Margin_%", "mean"),
).sort_values("Total_Sales", ascending=False)
```

Output:
```text
               Total_Sales  Avg_Margin
Region
South West         1032000        15.0
North Central       546000        15.0
North West          537000        15.0
```

> "Every region comes out at exactly 15.0%. That matches Optimum's Excel PivotTable exactly, and it tells the finance manager something real: every product is priced at a uniform 15% margin, company-wide. Python did not replace the analytical thinking here, it changed how we executed it, and let us check our own work along the way."

---

## Final State of the Notebook

By the end of this demo, `df` carries five new columns beyond what Topic 5.2 loaded: `Profit_check`, `Sales_Tier` and `Margin_%`, all built and verified live in this session, plus everything from Topics 5.1 and 5.2 still intact.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| `TypeError` after chaining `.sort_values("Sales", ...)` onto a `groupby(...)["Sales"].sum()` result | "That `.sum()` already returned a single column, a Series, which has no column named Sales to sort by. Drop the column name from `sort_values()` and keep only `ascending=False`." |
| `df.sort_values(...)` or `df.groupby(...)` appears to do nothing to `df` | "Those methods return a new result, they do not change `df` itself. Either reassign it, `df = df.sort_values(...)`, or use the result directly, exactly like every cell in this demo does." |
| Trainee groups by Branch when the question asks about Region, and gets a real but wrong-shaped answer | "This will not raise an error, it will just quietly answer a different question. Reread the business question before writing the code, Optimum has four branches but only three regions." |

---

## Up Next

Topic 5.4 takes this same verified analysis and asks an AI assistant to extend it, then teaches trainees to catch the AI's mistakes before trusting a single number it produces.
