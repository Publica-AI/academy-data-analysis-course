# Module Demo Guide - Data Storytelling and Visualisation (Week 7)
**Module 6 | Estimated duration: 65 minutes**

---

## The Story

AJEBO Finance MFB, a Nigerian microfinance bank with branches in Lagos, Abuja, Port Harcourt, Kano, Ibadan and a rural northern catchment, needs a defensible answer for its credit committee: should Kano branch's lending criteria change? This demo takes AJEBO's raw home loan application export through the same journey a working analyst follows this week: clean it, chart it honestly, turn it into a narrative someone can act on, publish it as a portfolio piece, and reproduce the narrative once more with an AI assistant under full verification discipline.

**What this demo builds:**

- A cleaned, validated, documented AJEBO loan-applications dataset, built with a 17-step pandas workflow and wrapped in a single repeatable function (Topic 6.1)
- A set of honest, self-explanatory charts that answer specific branch-performance questions, using the Question, Data Type, Comparison, Chart framework (Topic 6.2)
- A Context, Finding, Implication, Recommendation narrative for Kano's approval rate that passes the "so what" test (Topic 6.3)
- A public GitHub repository with a generated README an employer could open and understand in ninety seconds (Topic 6.4)
- An AI-drafted narrative, red-pen marked up, verified against source data, and rebuilt into a trustworthy final version (Topic 6.5)

---

## Prerequisites

1. Python environment with pandas, numpy, matplotlib and seaborn installed, in Jupyter (or Google Colab)
2. `ajebo_finance_loan_applications_RAW.csv` in the working directory (412 rows, 15 columns)
3. A GitHub account, ready to create a new public repository
4. Access to a free AI assistant, with the data-safety habit from Topic 6.1 already understood
5. The Module 6.1 cleaning notebook, the Module 6.2 visualisation notebook and the Module 6.3 narrative available, since Topic 6.4 publishes them as-is

> **Instructor note:** generate and save `ajebo_finance_loan_applications_CLEANED.csv` (356 rows) before this demo starts. Topics 6.2 through 6.5 all read from that cleaned file, not from the raw export, so the demo should not be waiting on Part 1's pipeline to finish before the later Parts can run.

---

## Dataset / Project Setup (before the demo starts)

- Confirm `ajebo_finance_loan_applications_RAW.csv` is in place: 412 rows, 15 columns (8 categorical, 5 numerical, 2 other: Application_ID and Application_Date).
- Confirm Application_ID is a synthetic reference, so the file is safe to explore now and safe to upload to an AI tool later in the demo.
- Have the pre-built Module 6.1 cleaning notebook and the already-generated `ajebo_finance_loan_applications_CLEANED.csv` open as the fallback, in case any live cell fails.

---

## Demo Steps

### Part 1 - The Cleaning and Transformation Workflow (Topic 6.1) (18 min)

> "AJEBO's credit committee is meeting this week, and whatever number we hand them, they will act on it. Before we chart anything, we need a dataset nobody can pick apart. Every new file starts the same way: shape and structure."

```python
df = pd.read_csv('ajebo_finance_loan_applications_RAW.csv')
df.shape   # (412, 15)
df.head()
df.info()
df.describe()
```

> "Application_Date is still text, not a date. Loan_Amount_NGN shows 405 non-null out of 412, our first hint of gaps. None of this throws an error. That is exactly the danger."

```python
df.isna().sum()
(df.isna().mean() * 100).round(1)
# Credit_History   35   (8.5%)
# Employment_Type  20   (4.9%)
# Gender           14   (3.4%)
```

```python
df.duplicated().sum(), df['Application_ID'].duplicated().sum()   # 12, 12
df = df.drop_duplicates()   # 412 rows -> 400 rows
```

> "Both duplicate checks agree at 12. That agreement is what gives us confidence these are genuine repeats, not two applicants who happen to share values."

```python
df['Branch_Region'] = df['Branch_Region'].str.strip().str.title()
df['Branch_Region'].nunique()   # 6, the real AJEBO branches
```

```python
pd.to_numeric(df['Dependents'], errors='coerce')   # '3+' becomes NaN
df['Dependents'] = df['Dependents'].astype('category')
df['Application_Date'] = pd.to_datetime(df['Application_Date'], format='mixed', dayfirst=True)
future = df[df['Application_Date'] > pd.Timestamp.today()]   # 1 row, dated 2027-03-15
```

> "Dependents contains '3+' as text. Forcing it numeric would crash. That is not a bug to fix, it is a sign the column should stay categorical."

```python
df['Gender'] = df['Gender'].fillna('Not Stated')
df['Employment_Type'] = df['Employment_Type'].fillna('Not Stated')
df['Dependents'] = df['Dependents'].astype(object).fillna('Not Stated').astype('category')
df['Loan_Amount_NGN'] = df['Loan_Amount_NGN'].fillna(df['Loan_Amount_NGN'].median())
df['Loan_Term_Months'] = df['Loan_Term_Months'].fillna(df['Loan_Term_Months'].median())
df = df.dropna(subset=['Credit_History'])   # 35 rows dropped
```

> "Credit_History is the strongest driver of approval in this dataset. Imputing its 35 missing values would quietly manufacture a pattern that is not real, so those rows are dropped, not guessed at."

```python
q1, q3 = df['Monthly_Income_NGN'].quantile([0.25, 0.75])
upper = q3 + 1.5 * (q3 - q1)
outliers = df[df['Monthly_Income_NGN'] > upper]
outliers['Employment_Type'].value_counts()   # mostly Self-Employed
```

> "The IQR rule flags these incomes, but most of them are Self-Employed applicants, exactly the customers a branch manager most wants visibility on. Flagged is a starting point for investigation, not an automatic deletion order, so these stay."

```python
df['Monthly_Income_NGN'] = df['Monthly_Income_NGN'].abs()          # 2 negative incomes corrected
df = df[df['Loan_Term_Months'] != 0]                                 # 1 zero-month row removed
df = df[df['Application_Date'] <= pd.Timestamp.today()]              # 1 future-dated row removed

df['Total_Household_Income_NGN'] = df['Monthly_Income_NGN'] + df['Coapplicant_Income_NGN']
df['Loan_To_Income_Ratio'] = (df['Loan_Amount_NGN'] / df['Total_Household_Income_NGN']).round(2)
df['Application_Year'] = df['Application_Date'].dt.year
```

> "Two negative incomes corrected with abs(), because that is almost certainly a sign error. The zero-month term and the 2027 application date cannot be safely guessed at, so those rows are gone."

```python
assert df.isna().sum().sum() == 0
assert df['Application_ID'].nunique() == len(df)
assert (df['Monthly_Income_NGN'] >= 0).all()
assert (df['Loan_Term_Months'] > 0).all()
assert df['Application_Date'].max() <= pd.Timestamp.today()
assert df['Branch_Region'].nunique() == 6
print('All validation checks passed.')
```

> "Every check that matters, turned into an assertion, plus a cleaning log recording each decision and why it was made, all wrapped inside one `clean_ajebo_data()` function. Run it twice on the same raw file and it produces identical output, 356 rows, every time. That is what the rest of today builds on."

---

### Part 2 - Visualisation Principles and Chart Choice (Topic 6.2) (15 min)

> "Same question the credit committee actually asked: which branch should we be worried about? Let's answer it two ways and time ourselves."

```python
summary = df.groupby('Branch_Region').agg(
    Applications=('Application_ID', 'count'),
    Approval_Rate=('Loan_Status', lambda s: (s == 'Approved').mean())
)
```

Abuja 62 apps / 74% approved, Ibadan 41 / 73%, Kano 32 / 50%, Lagos 109 / 77%, Port Harcourt 45 / 76%, Rural North 67 / 78%.

> "As a table, you have to scan every row to find the outlier. Now the chart."

```python
order = summary['Approval_Rate'].sort_values().index
ax.barh(order, summary.loc[order, 'Approval_Rate'] * 100)   # Kano highlighted
```

> "The chart does the comparison for you, in under a second. That is the whole rule: pick the format that lets the reader answer fastest, not the format that is fastest to build."

Before/after, comparison: a pie chart of average loan amount by employment type (two independent averages plotted as slices of a whole they do not share) rebuilt as a bar chart.

Before/after, distribution: `Monthly_Income_NGN` plotted bar-by-row-order (a meaningless x-axis) rebuilt as a histogram, right-skewed, median line marked.

Before/after, relationship: an oversized, fully opaque scatter of income against loan amount rebuilt with alpha transparency and sensible marker size, split by employment type, showing income and loan size track together (r = 0.72).

```python
appr = df.groupby('Employment_Type')['Loan_Status'].apply(lambda s: (s == 'Approved').mean()) * 100
# Salaried 75.0%, Self-Employed 71.6%
```

> "Plotted with the axis starting at 65, this 3.4-point gap looks like a canyon. Plotted from zero, it is what it actually is: a small difference. Same numbers, two very different impressions, depending only on where the axis starts."

Close by running the Visualisation Checklist against the finished Kano chart out loud: title states a finding, axis starts at zero, both axes labelled, sorted by value, colour encodes something real, sample size shown.

---

### Part 3 - Insight Narrative and Business Communication (Topic 6.3) (10 min)

> "We now have a chart. AJEBO's credit committee does not want a chart, they want to know what to do. Turning 'Kano's approval rate is 50%' into something someone can act on is today's job."

```python
kano = branch_stats.loc['Kano']        # approval_rate 0.50, n=32
ibadan = branch_stats.loc['Ibadan']    # approval_rate 0.73, n=41
se = np.sqrt(kano.approval_rate * (1 - kano.approval_rate) / kano.n)
kano_ci = (kano.approval_rate - 1.96 * se, kano.approval_rate + 1.96 * se)   # roughly 33% - 67%
```

> "Every number in the narrative I am about to write came out of that cell two minutes ago, not out of memory. That traceability is the actual discipline this topic teaches."

Build the four-part narrative live:

- **Context.** AJEBO's credit committee reviews branch performance quarterly and is deciding whether Kano's lending criteria need to change.
- **Finding.** Kano's approval rate is 50%, the lowest of the six branches, 23 points below the next-lowest, Ibadan, at 73%. Kano's sample is small (32 applications), giving a wide 95% confidence interval of roughly 33% to 67%.
- **Implication.** The gap could reflect a genuine difference in local applicant risk, an inconsistency in how loan officers at that branch apply the criteria, or simply be noise given the small sample. The approval rate alone cannot distinguish between these.
- **Recommendation.** Before changing Kano's lending policy, pull a manual sample of Kano's rejected applications and compare stated rejection reasons against a comparably-sized branch (Ibadan, n=41). Revisit the approval rate once Kano's sample reaches roughly 60 to 80 applications.

> "'Investigate further' is not a recommendation. 'Pull a manual sample of Kano's last 20 rejections and compare against Ibadan's' is, because it names a next action and a way to know it worked."

Show the same r = 0.72 finding written twice: once for a technical audience ("a Pearson correlation of 0.72... income could serve as a reasonable single-variable proxy in a loan-sizing model") and once for the credit committee ("applicants who earn more tend to ask for bigger loans, which makes income a solid first check when a loan request looks unusually large"). Same fact, different vocabulary, nothing overstated in either direction.

---

### Part 4 - GitHub for Portfolios (Topic 6.4) (8 min)

> "None of this exists to an employer until it lives somewhere they can open it. Three concepts get us there: repo, commit, README."

Create a public repository, for example `ajebo-loan-analysis`.

```python
SUSPICIOUS_COLUMN_KEYWORDS = ['name', 'email', 'phone', 'address', 'ssn', 'nin', 'bvn', 'dob']
# scan column names and string columns for email- and phone-shaped values
# AJEBO's data passes clean: Application_ID is a synthetic reference
```

> "The same data-protection discipline from Part 1, now applied to a public space, before a single file is added."

Add the cleaned dataset, the Module 6.1 and 6.2 notebooks, and the Module 6.3 narrative. Then generate the README live from the same figures already computed in Parts 1 to 3:

```python
readme_stats = {
    'total_rows': 356, 'n_branches': 6,
    'kano_rate': 50, 'kano_n': 32,
    'next_lowest_name': 'Ibadan', 'next_lowest_rate': 73,
    'income_loan_corr': 0.72,
}
# title, business problem, data source and safety line, method (linked to each notebook),
# two embedded key findings (Kano's chart, the income-vs-loan scatter), tools, reproduce steps
```

> "Notice this README is built the same way as the narrative: every number pulled from a calculation, not typed by hand."

Check the business-problem line names the actual lowest branch dynamically, pulled from `readme_stats`, not a hardcoded name left over from an earlier draft. Commit with a descriptive message, push, and copy the repository URL as the portfolio link.

---

### Part 5 - AI-Assisted Exploration and Drafting (Topic 6.5) (12 min)

> "Last pass, and the fastest one. An AI assistant can explore this same dataset and draft a narrative in seconds. It can also state a wrong number in exactly the same confident tone as a right one. Catching that before it reaches anyone is today's job."

Re-confirm the data-safety check before uploading anything to the AI tool, then send a prompt that gives context, the data, a specific task and an output format, explicitly asking the assistant to show which columns and calculation produced each claim.

Bring up the AI-drafted narrative for the red-pen exercise:

> "AJEBO Finance has seen strong growth in loan applications throughout 2025 and 2026... Kano branch has the lowest approval rate at approximately 35%, suggesting the branch may need additional support... This is likely because Kano serves a riskier customer base... Self-employed applicants tend to request larger loans because they have more unpredictable income needs... Overall, AJEBO's loan book appears healthy, with no major causes for concern."

> "Mark this up before I show the answer. Aim for at least six problems."

Walk the flagged issues against the figures already verified in Parts 1 to 3:

1. Wrong trend: volume has actually softened since mid-2025, roughly 23%, not grown.
2. Wrong number: 35% against the verified 50%.
3. Unverifiable claim presented as fact: nothing in the dataset shows customer risk by branch.
4. Missing context: no mention of Kano's n = 32 or its wide confidence interval.
5. Overclaimed causation: the loan-size gap is real (NGN 3.82m vs NGN 3.13m), but "unpredictable income needs" is invented, not observed.
6. Vague and unmeasured: "strong relationship" with no r-value given.
7. Contradictory summary: "healthy... no major concerns" directly undercuts the Kano paragraph two lines above.

> "Treating a confident tone as evidence is the single habit this whole topic exists to break."

Rebuild the Kano paragraph using the same Context, Finding, Implication, Recommendation structure from Part 3, as a full rebuild from verified facts, not a polish pass on the AI's wording. Show what gets submitted alongside it: a prompt log of every prompt used, in order, and a verification note per retained claim, for example "AI said 35%, corrected to 50%, source: Part 1 / Part 3 notebook."

---

## Demo Wrap-Up

By the end of this demo, AJEBO's raw loan-application export has become five connected deliverables, each built and verified this session:

| Feature / capability | Topic it came from | What it shows |
|---|---|---|
| Cleaned, validated, repeatable `clean_ajebo_data()` pipeline, 356 rows | Topic 6.1 | Raw data is now trustworthy, documented and reproducible on any future export |
| Sorted, honest bar chart of branch approval rates | Topic 6.2 | Kano is visibly the lowest-performing branch, in under a second, without distortion |
| Context, Finding, Implication, Recommendation narrative for Kano | Topic 6.3 | A specific, falsifiable next action the credit committee can actually act on |
| Public GitHub repository with a generated README | Topic 6.4 | A portfolio link an employer can open and understand in ninety seconds |
| Red-pen corrected, verified AI-assisted narrative with prompt log | Topic 6.5 | The same finding, drafted faster with AI, trustworthy only because every claim was checked |

> "This is what a week of real analyst work looks like: one dataset, cleaned once, questioned honestly, explained clearly, published publicly, and checked twice, once by hand and once against an AI draft. That is the job trainees are preparing for."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| `df.info()` still shows Application_Date as an object after "fixing" it | "Check that the result was reassigned: `df['Application_Date'] = pd.to_datetime(...)`, not just called on its own. Pandas does not change a column in place." |
| Branch_Region still shows more than 6 unique values after cleaning | "`str.title()` alone will not fix a double internal space like 'Port  Harcourt'. That needs the extra regex step to collapse whitespace before `.title()` runs." |
| The validation `assert` block fails on the Credit_History check | "That usually means the missing-values cell, with `dropna(subset=['Credit_History'])`, either ran out of order or did not run at all. Re-run it, then re-run the assertions." |
| A trainee looks at the before pie chart and says it still looks fine | "Ask what the two percentages on the pie actually represent. Each average's share of the sum of both averages, not the averages themselves. That number has no business meaning." |
| The generated README's business-problem line still says 'Kano' after the data changes | "That is the deliberate drafting bug from Part 4. Check whether the branch name was typed by hand or pulled from `readme_stats`. If it is hardcoded, the rest of the document updated and that line did not." |
| A trainee marks the AI's red-pen draft as mostly fine | "Ask for the exact number behind 'strong relationship' or 'approximately 35%'. If they cannot point to the cell that produced it, the sentence is not verified yet, whatever it sounds like." |
