# Demo Guide - The Cleaning and Transformation Workflow
**Module 6, Topic 6.1 | Estimated duration: 75-90 minutes**

---

## What This Demo Teaches

- Profile a raw dataset before touching a single value: shape, structure, dtypes.
- Detect every category of data problem (missing values, duplicates, inconsistent
  categories, invalid values, wrong dtypes, mixed date formats) before fixing any of them.
- Apply the correct fix for each problem type, deciding column by column instead of
  applying one blanket rule to the whole dataset.
- Build derived columns only from inputs that have already been cleaned.
- Turn the same detection checks into pass/fail validation assertions.
- Document every decision in a plain-language cleaning log.
- Wrap the full sequence into one repeatable, reusable function.

---

## Setup - Before the Demo Starts

1. `ajebo_finance_loan_applications_RAW.csv` loaded and accessible to every trainee (this
   is AJEBO Finance MFB's home loan applications file, the dataset used across all of
   Module 6).
2. Python environment with pandas and numpy ready (Google Colab or local Jupyter).
3. Trainees have not yet opened the file. Preserve the "first look" moment for Part 1,
   do not pre-empt it in setup.
4. Fallback: a finished, fully executed notebook open in a second window, in case a live
   step fails.

> **Instructor note:** do not flag the deliberately-injected future date using
> `pd.Timestamp.today()`. This file also contains several legitimately far-dated
> applications, some into December 2026, so checking against the live clock will catch a
> different, growing number of "future" rows every time this demo is taught, since more
> of those legitimate dates fall into the past as real time moves on and more of the
> file's outer edge falls into the future depending on the day you run it. Use a fixed
> reference date instead:
> `DATA_BUILD_DATE = pd.Timestamp('2026-12-31')`. If this demo's future-date check ever
> returns a count higher than 1, that is this exact bug coming back, not a new problem in
> the data.

---

## Demo Steps

### Part 1 - First look and profiling (8 min)

> "Before I touch a single value, I want to know what I'm working with. Three lines,
> every time you open a new file."

```python
df = pd.read_csv('ajebo_finance_loan_applications_RAW.csv')
df.shape
df.head()
```

Result: `(412, 15)`. Head shows real values immediately, including a lowercase
`port harcourt` and a `Port  Harcourt` with a double internal space sitting in the
same column.

> "Notice I haven't fixed anything. I'm building a mental map before I decide what to do
> about any of it."

**Ask students:** "Before I run `info()` or `describe()`, guess how many of these 15
columns have missing values, just from eyeballing `head()`."

> Take two guesses out loud, do not confirm either way yet. Come back to this once
> `isna().sum()` runs in Part 2.

---

### Part 2 - Finding every problem before fixing anything (18 min)

> "Detection and fixing are two different jobs. Today we only count and understand the
> damage first."

```python
df.info()
df.describe()
```

Point out live: `Application_Date` is stored as text, not a real date (shown as `object`
or `str` depending on your pandas version), and `Monthly_Income_NGN`'s minimum
in `describe()` is negative, which is impossible for an income figure.

```python
df.isna().sum()
(df.isna().mean() * 100).round(1).sort_values(ascending=False)
```

Result: `Credit_History` has the most gaps (36, 8.7%), followed by `Employment_Type` (21,
5.1%), `Gender` (14, 3.4%), `Dependents` (12, 2.9%), `Loan_Term_Months` (8, 1.9%),
`Loan_Amount_NGN` (7, 1.7%).

> "Come back to your guesses from Part 1. Most people underestimate this."

```python
df.duplicated().sum(), df['Application_ID'].duplicated().sum()
```

Result: `(12, 12)`. Both checks agree, which is itself worth a sentence: if they
disagreed, that would be a separate problem to chase down.

```python
df['Branch_Region'].value_counts(dropna=False)
```

Result: 13 distinct strings for what should be 6 real branches (`lagos`, `Lagos `,
`LAGOS`, `abuja`, `port harcourt`, `Port  Harcourt` all sitting alongside their clean
counterparts).

```python
neg_income = df[df['Monthly_Income_NGN'] < 0]
zero_term = df[df['Loan_Term_Months'] == 0]
len(neg_income), len(zero_term)
```

Result: `(2, 1)`.

> "One more trap before we start fixing anything."

```python
pd.to_numeric(df['Dependents'], errors='coerce').isna().sum(), df['Dependents'].isna().sum()
```

Result: `(65, 12)`. The gap of 53 is entirely `'3+'` being coerced to `NaN`.

**Ask students:** "If I ran `df['Dependents'].astype(int)` right now, what happens the
moment pandas reaches a row with `'3+'`?"

> "It raises a `ValueError`. The column has to stay categorical. This is not a case
> where the fix is a better conversion, the fix is deciding the column should never be
> numeric at all."

---

### Part 3 - Fixing everything, in order (25 min)

> "Same order every time: duplicates first, since everything downstream should be
> counted once."

```python
df = df.drop_duplicates()
assert df['Application_ID'].nunique() == len(df)
```

Result: 412 rows become 400. Assertion passes silently, which is the proof.

> "Now the region names. `strip()` and `title()` handle most of it, but watch the double
> space in Port Harcourt, that needs an explicit whitespace collapse too."

```python
df['Branch_Region'] = (df['Branch_Region']
                        .str.strip()
                        .str.replace(r'\s+', ' ', regex=True)
                        .str.title())
df['Branch_Region'].nunique()
```

Result: `6`. Exactly the six real branches, nothing left over.

> "Same pattern for the other text columns, plus a mapping dictionary for values that
> need real relabelling, not just a case change."

```python
marital_map = {'Y': 'Married', 'N': 'Single'}
employ_map = {'Self Employed': 'Self-Employed'}

def clean_text(series, mapping=None):
    s = series.str.strip().str.replace(r'\s+', ' ', regex=True).str.title()
    return s.replace(mapping) if mapping else s

df['Gender'] = clean_text(df['Gender'])
df['Marital_Status'] = clean_text(df['Marital_Status'], marital_map)
df['Employment_Type'] = clean_text(df['Employment_Type'], employ_map)
```

> "Dates next. Three formats live in this one column, and there is one date that should
> not exist at all."

```python
df['Application_Date'] = pd.to_datetime(df['Application_Date'], format='mixed', dayfirst=True)

DATA_BUILD_DATE = pd.Timestamp('2026-12-31')
future = df[df['Application_Date'] > DATA_BUILD_DATE]
len(future)
```

Result: `1`. Exactly the single deliberately-injected 2027 application. (See the
Instructor note in Setup: using the live clock here instead of `DATA_BUILD_DATE` would
return a different, larger number depending on the day this demo is run.)

> "Missing values now, and this is a decision, not a formula. Every column gets its own
> reasoning, said out loud."

```python
df['Gender'] = df['Gender'].fillna('Not Stated')
df['Loan_Amount_NGN'] = df['Loan_Amount_NGN'].fillna(df['Loan_Amount_NGN'].median())
df['Loan_Term_Months'] = df['Loan_Term_Months'].fillna(df['Loan_Term_Months'].median())
df['Employment_Type'] = df['Employment_Type'].fillna('Not Stated')
df['Dependents'] = df['Dependents'].astype(object).fillna('Not Stated').astype('category')
df = df.dropna(subset=['Credit_History'])
```

> "Gender and Employment_Type are low-stakes: an explicit 'Not Stated' keeps the gap
> honest instead of hiding it in the majority category. Credit_History is different, it
> is the strongest single predictor of approval in this dataset, so imputing it risks
> manufacturing a pattern that is not real. We drop those 35 rows instead of guessing."

> "Last three errors: correct where you have solid grounds, remove where you do not."

```python
df['Monthly_Income_NGN'] = df['Monthly_Income_NGN'].abs()
df = df[df['Loan_Term_Months'] != 0]
df = df[df['Application_Date'] <= DATA_BUILD_DATE]
```

> "Taking the absolute value of a negative income is defensible because the rest of that
> row looks entirely normal. A zero-month term and an impossible date cannot be safely
> guessed, so those rows are removed."

---

### Part 4 - Derived columns and outlier check (8 min)

```python
q1, q3 = df['Monthly_Income_NGN'].quantile([0.25, 0.75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
outliers = df[df['Monthly_Income_NGN'] > upper]
outliers['Employment_Type'].value_counts()
```

Result: 11 outliers, all Self-Employed.

> "Every one of these flagged incomes belongs to a self-employed applicant. That is the
> dataset telling you this is a real feature of the business, not an error, self-employed
> income is naturally more variable. None of these get removed."

```python
df['Total_Household_Income_NGN'] = df['Monthly_Income_NGN'] + df['Coapplicant_Income_NGN']
df['Loan_To_Income_Ratio'] = (df['Loan_Amount_NGN'] / df['Total_Household_Income_NGN']).round(2)
df['Application_Year'] = df['Application_Date'].dt.year
```

> "Every one of these three columns only works because of a fix earlier in this session,
> the income columns were validated non-negative, and Application_Date is a real
> datetime now, not text."

---

### Part 5 - Validating and documenting (10 min)

```python
assert df.isna().sum().sum() == 0
assert df['Application_ID'].nunique() == len(df)
assert (df['Monthly_Income_NGN'] >= 0).all()
assert (df['Loan_Term_Months'] > 0).all()
assert df['Application_Date'].max() <= DATA_BUILD_DATE
assert df['Branch_Region'].nunique() == 6
print('All validation checks passed.')
print(f'Final shape: {df.shape}')
```

Result: `Final shape: (363, 18)`.

**Ask students:** "Every one of these assertions is a check we already wrote earlier in
this session, just run again. Why is re-running the same check better proof than writing
a brand new one?"

> "Because it closes the loop. If Part 2 found the problem and Part 5 confirms it is
> gone using the exact same test, there is no gap where a different definition of
> 'fixed' could sneak in."

> "Last step is writing down what happened and why, in plain language, before anyone
> else has to trust this file without reading the code."

```python
print(f'''
AJEBO Finance loan applications - cleaning log
Source file: ajebo_finance_loan_applications_RAW.csv (412 rows)

1. Removed 12 exact duplicate rows. Result: 400 unique applications.
2. Standardised Branch_Region, Gender, Employment_Type, Marital_Status casing and
   whitespace; mapped Y/N to Married/Single.
3. Parsed Application_Date from three mixed formats to one datetime column. Removed
   1 row dated after the fixed data build date (2026-12-31), unverifiable.
4. Missing values: Gender, Employment_Type, Dependents to Not Stated. Loan_Amount_NGN,
   Loan_Term_Months to median. Credit_History (35 rows) dropped, given its role as the
   strongest driver of Loan_Status.
5. Corrected 2 negative Monthly_Income_NGN values via abs(). Removed 1 row with
   Loan_Term_Months equal to 0, unverifiable.
6. Added Total_Household_Income_NGN, Loan_To_Income_Ratio, Application_Year.
7. All validation checks confirmed. Final shape: (363, 18).
''')
```

---

### Part 6 - Making it repeatable (8 min)

> "Everything today has a home in one function. Nothing new to learn here, just
> assembly."

```python
def clean_ajebo_data(filepath, build_date='2026-12-31'):
    data = pd.read_csv(filepath)
    data = data.drop_duplicates()

    def _clean_text(series, mapping=None):
        s = series.str.strip().str.replace(r'\s+', ' ', regex=True).str.title()
        return s.replace(mapping) if mapping else s

    marital_map = {'Y': 'Married', 'N': 'Single'}
    employ_map = {'Self Employed': 'Self-Employed'}
    data['Branch_Region'] = _clean_text(data['Branch_Region'])
    data['Gender'] = _clean_text(data['Gender'])
    data['Marital_Status'] = _clean_text(data['Marital_Status'], marital_map)
    data['Employment_Type'] = _clean_text(data['Employment_Type'], employ_map)
    data['Dependents'] = data['Dependents'].astype('category')
    data['Branch_Region'] = data['Branch_Region'].astype('category')
    data['Application_Date'] = pd.to_datetime(data['Application_Date'], format='mixed', dayfirst=True)

    data['Gender'] = data['Gender'].fillna('Not Stated')
    data['Employment_Type'] = data['Employment_Type'].fillna('Not Stated')
    data['Dependents'] = data['Dependents'].astype(object).fillna('Not Stated').astype('category')
    data['Loan_Amount_NGN'] = data['Loan_Amount_NGN'].fillna(data['Loan_Amount_NGN'].median())
    data['Loan_Term_Months'] = data['Loan_Term_Months'].fillna(data['Loan_Term_Months'].median())
    data = data.dropna(subset=['Credit_History'])

    cutoff = pd.Timestamp(build_date)
    data['Monthly_Income_NGN'] = data['Monthly_Income_NGN'].abs()
    data = data[data['Loan_Term_Months'] != 0]
    data = data[data['Application_Date'] <= cutoff]

    data['Total_Household_Income_NGN'] = data['Monthly_Income_NGN'] + data['Coapplicant_Income_NGN']
    data['Loan_To_Income_Ratio'] = (data['Loan_Amount_NGN'] / data['Total_Household_Income_NGN']).round(2)
    data['Application_Year'] = data['Application_Date'].dt.year

    assert data.isna().sum().sum() == 0
    assert data['Application_ID'].nunique() == len(data)
    assert (data['Monthly_Income_NGN'] >= 0).all()
    assert (data['Loan_Term_Months'] > 0).all()
    assert data['Application_Date'].max() <= cutoff
    assert data['Branch_Region'].nunique() == 6
    return data

result_1 = clean_ajebo_data('ajebo_finance_loan_applications_RAW.csv')
result_2 = clean_ajebo_data('ajebo_finance_loan_applications_RAW.csv')
result_1.shape, result_1.equals(result_2)
```

Result: `((363, 18), True)`. Same file, run twice, byte-identical output. That is what
repeatable actually means.

> "Notice `build_date` is a parameter now, not a buried assumption. That is the fix for
> the exact bug flagged in this session's setup note, a fixed, explicit, overridable
> cutoff instead of a silently shifting one."

---

## Final State of the Notebook

```python
def clean_ajebo_data(filepath, build_date='2026-12-31'):
    # ... full function as shown in Part 6 ...
    return data
```

Final validated shape after running `clean_ajebo_data()`: **(363, 18)**.

Columns added beyond the original 15: `Total_Household_Income_NGN`,
`Loan_To_Income_Ratio`, `Application_Year`.

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Using `pd.Timestamp.today()` instead of a fixed `DATA_BUILD_DATE` for the future-date check, producing a different, usually larger, count of "future" rows depending on the day the demo is run. | "This file has genuine applications dated out to December 2026. Anything checked against the live clock will catch more of them as real time passes. Pin the cutoff to a fixed date, the same way we pin any other business rule." |
| Running `.str.strip().str.title()` on `Branch_Region` and declaring it fixed without checking `nunique()` afterwards, leaving `Port  Harcourt`'s internal double space uncollapsed. | "Title-casing fixes case and edge whitespace, not a double space in the middle of a string. Always re-check `value_counts()` or `nunique()` after a text fix, do not assume the fix was complete." |
| Calling `df['Dependents'].astype(int)` directly, which raises a `ValueError` on the first `'3+'` value. | "This is not a bug to work around, it is the dataset telling you the column should stay categorical. Use `pd.to_numeric(..., errors='coerce')` to test a conversion safely before committing to it." |
| Copying the `fillna('Not Stated')` pattern from Gender onto Credit_History because it is quicker than deciding column by column. | "Credit_History is the strongest predictor of the outcome in this dataset. Imputing it risks manufacturing a pattern that was never really there. Low-stakes and high-stakes columns do not get the same treatment, and that has to be a deliberate choice each time." |

---

## Up Next

Module 6.2 takes this exact cleaned file into chart-building, and the very first thing
it teaches is that a chart built on the messy version of `Branch_Region` would have
shown six branches as thirteen.
