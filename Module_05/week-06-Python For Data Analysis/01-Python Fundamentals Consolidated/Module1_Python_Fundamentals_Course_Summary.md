# Module 1: Python Fundamentals — Course Summary

**Prepared for:** Module 5, Topic 5.1 (Python Fundamentals, Consolidated)
**Scope reviewed:** Module 1, Topics 1–10 — *Introduction to Python* through *Functions*
**Source:** Publica Academy course `01M03D8D60NAVJ2DR2N1J7C44Q` + the published codebooks in
`Publica-AI/data-science-ai/module-01-python-fundamentals`
**Date:** 9 September 2026

---

## 1. What the module is

Module 1 is the zero-assumptions Python foundation of the programme. Its stated prerequisites are
*"basic computer literacy"* and *"no prior programming experience required."*

- **19 lessons**, roughly **600 minutes** of taught content, ending in a **50-question multiple-choice quiz**.
- Each lesson ships with a **Canva slide deck** and a **Jupyter codebook** on GitHub.
- Codebooks follow a consistent shape: concept → worked code examples → class activities →
  practice question → mini project → recap.
- The module's own project is a **Student Grade Calculator** (100 points, submitted as a Python script).

**The trainees you are teaching in 5.1 have completed Topics 1–10 only.** Topics 11–18 come afterwards.

---

## 2. What students have actually been taught (Topics 1–10)

| # | Topic | Content covered |
|---|-------|-----------------|
| 1 | Introduction to Python | Programming as precise step-by-step logic; debunking the "maths genius" myth; Python in web development, data science and automation; environment setup; first script; REPL vs `.py` files |
| 2 | Python Syntax & Basics | Indentation as syntax (4 spaces); comments and *why* over *what*; `print()` with `sep` and `end`; `input()` — **always returns a string** |
| 3 | Variables & Data Types | Variables as named containers; `=` vs `==`; `snake_case`; `int`, `float`, `str`, `bool`; `type()`; casting with `int()` / `float()` / `str()`; the input-then-cast pattern |
| 4 | Operators & Expressions | `+ - * / // % **`; `/` always returns float; `//` floors; `%` remainder and the even/odd test; `+= -= *= /=`; comparisons; `and` / `or` / `not`; operator precedence |
| 5 | Conditional Statements | `if`, `if/else`, `if/elif/else`; first match wins; truthy and falsy values (`0`, `""`, `[]`, `None`) |
| 6 | Loops | `while` and the infinite-loop trap; `for`; `range(start, stop, step)` with exclusive stop; `break`; `continue`; `enumerate()` |
| 7 | Strings | Indexing and negative indexing; slicing incl. `[::-1]`; **immutability**; `.lower()` `.upper()` `.strip()` `.replace()` `.split()` `.join()` `.find()` `.count()`; **f-strings** with format specs |
| 8 | Lists & Tuples | Creation, indexing, slicing; `.append()` `.insert()` `.pop()` `.remove()` `.sort()`; iteration; tuples and immutability; unpacking |
| 9 | Sets & Dictionaries | Sets and uniqueness; union / intersection / difference / symmetric difference; dictionaries as key-value records; `.get()`; add, update, delete; `.keys()` `.values()` `.items()` |
| 10 | Functions | `def` and calling; parameters vs arguments; `return` vs `print`; `None` when no return; default arguments; local vs global scope and the `global` keyword |

**Worked style:** examples are everyday and concrete — student records, product prices, shopping baskets,
BMI classifiers, loan eligibility, receipts. Names used throughout are West African
(Amara, Kofi, Ama, Abena, Accra, Kumasi).

---

## 3. What students have **not** yet been taught

This is the most important finding for Topic 5.1. These sit **after** Functions in Module 1:

| # | Topic | Consequence for 5.1 |
|---|-------|---------------------|
| 11 | Error Handling & Debugging | `try` / `except` is unknown |
| 12 | Modules & Packages | **`import` has not been formally taught** |
| 13 | File Handling | `open()` and file I/O are unknown |
| 14–15 | OOP Basics & Core Concepts | classes and objects are unknown |
| 16 | External Libraries | `pip` and third-party packages are unknown |
| 17–18 | Algorithms; Python for Real-World Tasks | — |

---

## 4. How this compares with the current Topic 5.1 material

The existing `Module_5.1_Python_Fundamentals_Consolidated.ipynb` and its deck assume a "Python Zero"
syllabus of: variables → lists/dicts → conditions/loops → imports → functions → error messages → debugging.
Compared against what Module 1 actually delivers:

### 4.1 Assumed but not yet taught — needs care
- **`import statistics`** and the "Importing libraries" section. Imports are **Topic 12**, which comes
  after Functions. Most trainees will be meeting `import` for the first time.
- **"Reading Python error messages"** and the **"Debug it: before and after"** section. Formal error
  handling is **Topic 11**, also later. Trainees have *encountered* errors (`IndentationError`,
  `ValueError`) in activities, but have not been taught a debugging method.

> Neither section should be cut — both are genuinely needed before pandas. They simply should be framed
> as **new material**, not as revision.

### 4.2 Taught in Module 1 but absent from the current 5.1 recap
- Operators beyond the basics — `//`, `%`, `**`, and operator precedence
- **Strings** as a whole: slicing, immutability, methods, and **f-strings** (used constantly in 5.2+)
- **Tuples** and unpacking
- **Sets** and set operations
- Truthy / falsy values
- `break`, `continue`, `enumerate()`
- **Default arguments** and **variable scope**

### 4.3 Sequencing difference
The current 5.1 notebook introduces lists and dictionaries immediately after variables. In Module 1,
**strings (Topic 7) come before lists (Topic 8) and dictionaries (Topic 9)**, and all three come *after*
conditionals and loops. Following the delivered order will feel more familiar to trainees.

---

## 5. Recommendations for Topic 5.1

1. **Introduce `import` explicitly** as new material before reaching `import pandas as pd`.
2. **Add a strings segment** — f-strings in particular, since every later topic formats output with them.
3. **Keep the error-reading and debugging sections**, but present them as new skills rather than revision.
4. **Reorder the recap** to follow the delivered sequence: syntax → variables/types → operators →
   conditionals → loops → strings → lists/tuples → sets/dicts → functions.
5. **Lead with the high-frequency mistakes** — uncast `input()`, `range()` off-by-one,
   `.pop()` vs `.remove()`, uncaptured string methods, and calling a function without `()`.

---

## 6. Assessment

Module 1 closes with a **50-question multiple-choice quiz**, weighted towards beginner difficulty and
covering environment setup (Anaconda, Jupyter, code vs markdown cells, `Shift + Enter`, kernel restart)
alongside the language fundamentals.

> Note: lesson 1's written description references **Anaconda and Jupyter Notebook**, while its micro-lesson
> detail describes **python.org and VS Code**. The quiz follows the Anaconda/Jupyter line. Worth confirming
> with the Module 1 owner which environment trainees actually used, so 5.1 opens in the same tool.

---

## 7. Companion files

| File | Purpose |
|------|---------|
| `Module_5.1_Recap_Module1_Python_Fundamentals.pptx` | 15 recap slides to merge into the 5.1 deck |
| `Module_5.1_Recap_Module1_Python_Fundamentals.ipynb` | 55-cell runnable recap notebook with 9 exercises |
