# Module Demo Guide - Python for Data Analysis (Week 6)
**Module 5, Week 6 | Estimated duration: 60-75 minutes**

---

## The Story

**Everstock Distribution**, a wholesale FMCG distributor supplying rice, cooking oil, detergent, beverages and flour to shops across four branches: Lagos, Abuja, Kano and Ibadan. Ngozi, the regional operations analyst, has been building her monthly branch report in Excel for two years. The file now has twenty transactions this month alone, four branches feeding into it, and a pricing team that keeps asking questions Excel takes too long to answer. Her manager wants one thing: the same report, produced faster, and provably correct.

**What this demo builds:**
A single Colab notebook that takes `Optimum_branch_sales.csv` from raw file to verified business answers, tying together every topic from Week 6:
- Python fundamentals applied to real analyst tasks: variables, lists, dictionaries, loops, functions and reading a real error message (Topic 5.1)
- Loading `Optimum_branch_sales.csv` into a DataFrame and inspecting it before trusting it (Topic 5.2)
- Filtering, sorting, grouping, aggregating and building a verified calculated column with pandas and NumPy (Topic 5.3)
- Using an AI assistant to draft, explain and debug pandas code, without skipping verification (Topic 5.4)

---

## Prerequisites

1. Google Colab account ready, or a local Jupyter environment with Python 3, pandas and numpy installed
2. `Optimum_branch_sales.csv` available to upload, or ready to generate from the setup cell below
3. Access to an AI assistant (Claude or ChatGPT) for Part 4
4. Trainees have completed Topics 5.1-5.3 individually; this session is the synthesis, not the first introduction to any of them

> **Instructor note:** this guide shows column dtypes as `object` for text columns, the classic pandas display. On newer pandas releases with the opt-in string dtype enabled, the same columns may print as `string` instead. Reassure trainees the behaviour is identical, only the printed label differs, and it does not affect anything else in this guide.

---

## Dataset / Project Setup (before the demo starts)

1. Have `Optimum_branch_sales.csv` ready to upload to Colab, or paste the setup cell below into the first cell of a fresh notebook so it writes the file itself:

```python
with open("Optimum_branch_sales.csv", "w") as f:
    f.write("""TransactionID,Branch,Region,Customer,Product,Sales,Cost,Profit,Price,Date
1,Lagos,South West,Sunrise Stores,Rice 50kg,145000,123250,21750,29000,2026-01-05
2,Abuja,North Central,Greenfield Traders,Cooking Oil 25L,98000,83300,14700,,2026-01-05
3,Kano,North West,Kings Mart,Detergent Carton,52000,44200,7800,13000,2026-01-06
4,Lagos,South West,Delta Provisions,Beverages Crate,132000,112200,19800,11000,2026-01-06
5,Ibadan,South West,Horizon Retailers,Flour 50kg,87000,73950,13050,,2026-01-07
6,Abuja,North Central,Prime Foods Ltd,Rice 50kg,156000,132600,23400,31000,2026-01-07
7,Kano,North West,Unity Traders,Cooking Oil 25L,64000,54400,9600,16000,2026-01-08
8,Lagos,South West,Coastal Mart,Detergent Carton,45000,38250,6750,,2026-01-08
9,Ibadan,South West,Sunrise Stores,Beverages Crate,119000,101150,17850,9800,2026-01-09
10,Abuja,North Central,Greenfield Traders,Flour 50kg,102000,86700,15300,25500,2026-01-09
11,Kano,North West,Kings Mart,Rice 50kg,178000,151300,26700,29500,2026-01-10
12,Lagos,South West,Delta Provisions,Cooking Oil 25L,93000,79050,13950,15800,2026-01-10
13,Ibadan,South West,Horizon Retailers,Detergent Carton,38000,32300,5700,12500,2026-01-11
14,Abuja,North Central,Prime Foods Ltd,Beverages Crate,141000,119850,21150,10200,2026-01-11
15,Kano,North West,Unity Traders,Flour 50kg,76000,64600,11400,24000,2026-01-12
16,Lagos,South West,Coastal Mart,Rice 50kg,205000,174250,30750,30500,2026-01-12
17,Ibadan,South West,Sunrise Stores,Cooking Oil 25L,58000,49300,8700,,2026-01-13
18,Abuja,North Central,Greenfield Traders,Detergent Carton,49000,41650,7350,13200,2026-01-13
19,Kano,North West,Kings Mart,Beverages Crate,167000,141950,25050,10500,2026-01-14
20,Lagos,South West,Delta Provisions,Flour 50kg,110000,93500,16500,26000,2026-01-14
""")
print("Optimum_branch_sales.csv is ready.")
```

2. Have the fallback notebook (`Module_5_Demo_Fallback.ipynb`) open in a second tab, fully pre-run, in case a live cell fails.

---

## Demo Steps

### Part 1 - Python Fundamentals for Analysts (10 min)

> "Before Ngozi trusts a single number from pandas, she needs to trust the Python underneath it. Let's rebuild the habits from 5.1 on this month's real numbers."

**Variables, lists and dictionaries:**
```python
branch_name = "Lagos"
daily_sales = [145000, 132000, 93000, 205000, 110000]
transaction = {"branch": "Lagos", "amount": "15,000", "date": "2026-01-05"}

print(transaction["branch"])
```
Output: `Lagos`

**A loop applying a business rule:**
```python
target = 100000
for sale in daily_sales:
    if sale >= target:
        print(sale, "Above target")
    else:
        print(sale, "Below target")
```
Output:
```
145000 Above target
132000 Above target
93000 Below target
205000 Above target
110000 Above target
```

> "Four of Lagos's five transactions clear target. That's the same check we'll do properly, across all four branches, with pandas in a few minutes."

**A function, and the error it will hit on real data:**
```python
def clean_amount(value):
    return float(value)

clean_amount("\u20a615,000")
```
Output:
```
ValueError: could not convert string to float: '\u20a615,000'
```

> "This is the exact error Ngozi's Excel export produces the moment a price gets typed with a currency symbol. Strip it, then convert."

```python
def clean_amount(value):
    value = value.replace("\u20a6", "").replace(",", "")
    return float(value)

clean_amount("\u20a615,000")
```
Output: `15000.0`

---

### Part 2 - Loading and Inspecting the Data (15 min)

> "Ngozi's Excel file has grown to twenty rows this month and it will not stop growing. Let's load it properly and inspect it before trusting a single figure."

```python
import pandas as pd

df = pd.read_csv("Optimum_branch_sales.csv")
df.head()
```
Shows the first 5 rows: Lagos, Abuja, Kano, Lagos, Ibadan, with columns TransactionID, Branch, Region, Customer, Product, Sales, Cost, Profit, Price, Date.

**First inspection:**
```python
df.shape
```
Output: `(20, 10)`

```python
df.info()
```
Confirms 20 entries, 10 columns, and that `Price` has only 16 non-null values against 20 for every other column.

```python
df.dtypes
```
Output:
```
TransactionID      int64
Branch            object
Sales              int64
Price            float64
Date              object
```

> "int64 for whole numbers, float64 for Price, because it has decimals and missing values, object for text. Nothing here is decoration, it's telling us where to look next."

**Missing values, before anything else:**
```python
df.isna().sum()
```
Output: `Price    4` (every other column shows 0).

> "Four transactions this month have no recorded unit price. Ngozi needs to know that before she calculates anything involving Price, not after a report goes out wrong."

**Selecting and filtering:**
```python
df["Sales"]                      # a Series, one column
df[["Sales", "Profit"]]          # a DataFrame, two columns

df[df["Sales"] > 150000]
```
The filter returns 4 rows: Prime Foods Ltd (Abuja, 156000), Kings Mart (Kano, 178000), Coastal Mart (Lagos, 205000), Kings Mart (Kano, 167000).

> "Four transactions above \u20a6150,000, from three different customers, Kings Mart appears twice. That is the kind of one-line answer that used to take Ngozi a pivot table and a filter dropdown."

---

### Part 3 - Filtering, Grouping and Calculated Columns (22 min)

> "This is where Excel starts to strain and pandas doesn't. Same questions Ngozi already knows how to ask, answered a different way."

**Sorting:**
```python
df.sort_values("Sales", ascending=False).head(3)
```
Output: Coastal Mart / Lagos / Rice 50kg / 205000, then Kings Mart / Kano / Rice 50kg / 178000, then Kings Mart / Kano / Beverages Crate / 167000.

**Grouping, the pandas PivotTable:**
```python
df.groupby("Region")["Sales"].sum()
```
Output:
```
North Central     546000
North West        537000
South West       1032000
```

> "South West, which is Lagos and Ibadan combined, outsells the other two regions put together. Drag Region into a PivotTable's Rows and Sales into Values in Excel, and you get the same three numbers."

**Multiple aggregations at once:**
```python
df.groupby("Region")["Sales"].agg(["sum", "mean", "count"])
```
Output:
```
                   sum      mean  count
North Central   546000  109200.0      5
North West      537000  107400.0      5
South West     1032000  103200.0     10
```

> "South West has the most transactions and the highest total, but the lowest average transaction size. Three numbers, not one, tell Ngozi's manager the real story."

**A calculated column, verified against the source:**
```python
df["Profit_check"] = df["Sales"] - df["Cost"]
(df["Profit_check"] == df["Profit"]).all()
```
Output: `True`

> "The source file already records a Profit column. Recomputing it independently and getting an exact match on all twenty rows is Ngozi's proof that Sales and Cost are internally consistent before she reports on either."

**NumPy, for a conditional flag:**
```python
import numpy as np

df["Sales_Tier"] = np.where(df["Sales"] > 100000, "High", "Low")
df["Sales_Tier"].value_counts()
```
Output: `High: 10, Low: 10`

**Combining everything into one answer:**

> "Ngozi's actual question this month: among high-value transactions, which region is winning, on sales, on profit, and on volume?"

```python
high_value = df[df["Sales"] > 100000].copy()
high_value["Estimated_Units"] = np.round(high_value["Sales"] / high_value["Price"], 1)
high_value = high_value.sort_values("Sales", ascending=False)

high_value.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Estimated_Units=("Estimated_Units", "sum"),
    Transactions=("Sales", "count"),
)
```
Output:
```
               Total_Sales  Total_Profit  Total_Estimated_Units  Transactions
South West          711000        106650                   40.0             5
North Central       399000         59850                   22.8             3
North West          345000         51750                   21.9             2
```

> "Filter, calculate, sort, group, aggregate, five operations, one answer: South West wins on every measure among high-value transactions. That's a five-minute pivot chain in Excel done in five lines here, and it's exactly reproducible next month."

---

### Part 4 - AI-Assisted Coding, Applied to This Same Data (15 min)

> "Ngozi is allowed to use AI for all of this. The rule is simple: AI can draft it, she has to be able to defend it."

**A weak prompt, then a strong one:**

Weak: `"Write pandas code."`

Strong:
```
I have a pandas DataFrame called df loaded from Optimum_branch_sales.csv with columns:
TransactionID, Branch, Region, Customer, Product, Sales, Cost, Profit, Price, Date.
Write code that finds the average profit margin (Profit as a percentage of Sales)
across all transactions, and tell me whether it's consistent or highly variable.
```

**Run the AI's answer, then check it, don't trust it:**
```python
df["Margin_%"] = df["Profit"] / df["Sales"] * 100
avg_margin = df["Margin_%"].sum()
print(avg_margin)
```
Output: `300.0`

> "An average per-transaction margin of 300% is impossible. Read that back before it goes anywhere: the AI used sum() where it needed mean(). Watch the code, not just the fact that it ran."

```python
avg_margin = df["Margin_%"].mean()
print(avg_margin)
```
Output: `15.0`

> "Fifteen percent, on every transaction, no exceptions. That's not just a fixed bug, it's a genuine finding, Everstock prices with a uniform margin company-wide."

**AI-assisted debugging, with a real error:**
```python
top_regions = df.groupby("region")["Sales"].sum()
```
Output:
```
KeyError: 'region'
```

> "Paste this exact error and the exact code to an AI, not 'it doesn't work'. The column is Region with a capital R, pandas is case-sensitive."

```python
top_regions = df.groupby("Region")["Sales"].sum()
```
Runs cleanly, same output as Part 3.

**Explain it back, on the spot:**

> "Pick any line from today's notebook and explain it out loud, right now, no notes. If you can't, that line doesn't leave this room yet."

---

## Demo Wrap-Up

The finished notebook takes `Optimum_branch_sales.csv` from a raw file to a verified regional performance answer, using every topic from this week.

| Capability | Topic it came from | What it shows |
|---|---|---|
| Clean a currency-formatted value without crashing | 5.1 | Python fundamentals: functions, error messages, debugging |
| Load and inspect a CSV before trusting it | 5.2 | `read_csv`, `.shape`, `.info()`, `.isna().sum()` |
| Select and filter to answer a specific question | 5.2 | Series vs DataFrame selection, Boolean filtering |
| Sort, group and aggregate by region | 5.3 | `.sort_values()`, `.groupby()`, `.agg()` |
| Add and verify a calculated column | 5.3 | `df["col"] = ...`, verification against source data |
| Flag and combine conditions with NumPy | 5.3 | `np.where()`, multi-step pipelines |
| Draft, verify and debug code with AI | 5.4 | Strong prompts, the verification checklist, Explain It Back |

> "This is the same report Ngozi used to spend an afternoon building in Excel. It now runs in under a minute, and every number in it has been checked, not assumed. That's the job: faster, not less rigorous."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| `ValueError: could not convert string to float` when running `clean_amount` on an uncleaned value | "float() needs digits only. The \u20a6 symbol and the comma are still in the string, strip both before converting, exactly like Part 1." |
| `df.dtypes` shows `string` instead of `object` for text columns | "That's a newer pandas display option, not an error. The columns still hold text and behave the same, only the printed label differs." |
| `KeyError` when grouping or filtering on a column name | "pandas is case-sensitive and exact-match. Run `df.columns` and compare it character by character against what you typed." |
| `TypeError` after chaining `.sort_values("Sales", ...)` onto a `groupby(...)["Sales"].sum()` | "That `.sum()` already returned a single column, a Series, which has no column named 'Sales' to sort by. Drop the column name from `sort_values()` and keep only `ascending=False`." |
| A trainee reports `df[["Sales"]]` and `df["Sales"]` as identical | "They print similarly but are different objects, a DataFrame and a Series. Ask them to run `type()` on each and compare." |
| AI-generated margin calculation returns 300% or another implausible percentage | "Don't debug the code first, question the number. An average per-transaction percentage over 100% is a sign `sum()` was used where `mean()` was needed." |
