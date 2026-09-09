# Demo Guide - Python Fundamentals Consolidated
**Module 5, Topic 5.1 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Apply variables, lists and dictionaries to real Optimum transaction figures, not toy examples
- Apply a conditional and a loop to enforce a real business rule across several transactions at once
- Import a library and call a function to answer a calculation question without doing the arithmetic by hand
- Read a real Python error message and identify what it means before touching the code
- Locate the exact cause of a broken cell, fix one thing, rerun, and verify the result against a number already known to be correct

---

## Setup - Before the Demo Starts

1. Trainees have completed Python Zero: Colab basics, variables, data types, lists, dictionaries, `if` statements, `for` loops, libraries and imports, and basic functions.
2. Google Colab open with a single blank notebook, no file upload needed for this topic.
3. No dataset file is loaded yet. This topic works entirely with small Python objects built from real Optimum figures, ahead of loading the full file in Topic 5.2.

> **Instructor note:** every number used in this demo is a real figure from `Optimum_branch_sales.csv` (Lagos branch, TransactionIDs 1, 4, 8 and 12), copied in by hand rather than loaded with pandas. This is deliberate: trainees should see the fundamentals hold up on real business numbers before pandas does the loading for them next topic. Do not let trainees load the CSV early, even if asked, that undercuts the point of this topic.

---

## Demo Steps

### Part 1 - Variables, Lists and Dictionaries on Real Figures (8 min)

> "Everything in this demo is a real number from Optimum's own file, the same one we will load properly next topic. Let's start with what you already know from Python Zero: variables, a list, and a dictionary, applied to Lagos's actual transactions instead of a made-up example."

```python
branch_name = "Lagos"
daily_sales = [145000, 132000, 45000, 93000]
transaction = {"branch": "Lagos", "product": "Rice 50kg", "date": "2026-01-05"}

print(transaction["branch"])
```

Output:
```text
Lagos
```

> "Four of Lagos's real transaction totals in one list, and one full transaction record as a dictionary. That is exactly the shape pandas will expect from us the moment we load the whole file next topic, a table is just many of these dictionaries, one per row."

### Part 2 - Conditions and Loops: Applying a Business Rule (8 min)

> "Optimum's regional manager has a standing rule: flag any transaction at or above ₦100,000 for review. Let's apply that rule to all four of Lagos's transactions in one pass."

**Ask students:** "Before I run this, which of these four values do you expect to come back as 'Below target': 145000, 132000, 45000, or 93000?"

> "Hold that thought, let's run it and check."

```python
target = 100000
for sale in daily_sales:
    if sale >= target:
        print(sale, "Above target")
    else:
        print(sale, "Below target")
```

Output:
```text
145000 Above target
132000 Above target
45000 Below target
93000 Below target
```

> "45000 and 93000, exactly as most of you predicted, both fall below the ₦100,000 line. Two of Lagos's four transactions need review this week. This is the same check we will run properly across all four branches at once, the moment we load the real file next topic, one loop becomes one line of pandas."

### Part 3 - Importing a Library and Calling a Function (7 min)

> "Ngozi does not want to average four numbers by hand every week, and she should not have to. Let's import a library built for exactly that, and wrap it in a function we can reuse."

```python
import statistics

def average_sale(sales_list):
    return statistics.mean(sales_list)

average_sale(daily_sales)
```

Output:
```text
103750
```

> "One hundred and three thousand, seven hundred and fifty Naira, Lagos's average transaction size across these four. We defined this function once, it will work on any branch's list we hand it, which is exactly what we will do once every branch is loaded together in Topic 5.3."

### Part 4 - Reading a Real Error Message (7 min)

> "Sometimes a branch manager still emails Ngozi a price with the Naira symbol attached, instead of a plain number. Let's see what Python actually does with that, and read the error calmly instead of guessing."

```python
def clean_price(value):
    return float(value)

clean_price("₦29,000")
```

Output:
```text
ValueError: could not convert string to float: '₦29,000'
```

> "Read the last line first, it names the problem. float() needs digits only, the ₦ symbol and the comma are not valid parts of a number. That is the whole message of this topic in one line: an error is Python telling you exactly what is wrong, not a verdict on you."

### Part 5 - Debugging a Broken Cell, Step by Step (10 min)

> "Let's fix it properly: locate the exact cause, change one thing, rerun, and verify against a number we can check independently. That figure, ₦29,000, is the real Price recorded for Lagos's first Rice 50kg transaction this month."

```python
def clean_price(value):
    value = value.replace("₦", "").replace(",", "")
    return float(value)

clean_price("₦29,000")
```

Output:
```text
29000.0
```

> "Twenty-nine thousand. That is the exact Price we will see for this same transaction the moment we load `Optimum_branch_sales.csv` next topic, and that match is our verification, not a feeling that it looks right."

---

## Final State of the Notebook

By the end of this demo, the notebook holds the following, carried forward into Topic 5.2's live session:

```python
branch_name = "Lagos"
daily_sales = [145000, 132000, 45000, 93000]
transaction = {"branch": "Lagos", "product": "Rice 50kg", "date": "2026-01-05"}

target = 100000

def average_sale(sales_list):
    return statistics.mean(sales_list)

def clean_price(value):
    value = value.replace("₦", "").replace(",", "")
    return float(value)
```

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| `NameError: name 'average_sale' is not defined` when a trainee runs Part 3's function call before running the `def` cell above it | "Cells run in the order you execute them, not the order they sit on the page. Run the definition cell first, then the cell that calls it." |
| Trainee writes `average_sale` without the parentheses and gets `<function average_sale at 0x...>` instead of a number | "That shows you the function itself, not its result. A function only runs when you call it with parentheses, `average_sale(daily_sales)`, not just its name." |
| Trainee types the currency value without quotation marks, `clean_price(₦29,000)`, and gets a `SyntaxError` before the cell even runs | "That is not a runtime error, Python could not even read the line. ₦ is not a valid character outside a string. Wrap the whole value in quotation marks so Python treats it as text first." |

---

## Up Next

Topic 5.2 loads `Optimum_branch_sales.csv` properly with pandas, turning the single dictionary and list from this demo into a full DataFrame of every branch's transactions at once.
