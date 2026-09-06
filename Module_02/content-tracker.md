# Module 2 Content Tracker: Excel for Data Analysis

**Module 2 | Weeks 2 to 3 | Closing assessment: Block 1 mini-assessment, covering Modules 1 and 2**

This tracker records, per artefact: what it is, whether it was AI-drafted, its current review stage,
the dataset it depends on, and anything still outstanding. It is the quality-control record the
Content Creator Guide requires, and disclosure of AI drafting here is information for the reviewer
rather than a mark against the author.

**Review stages:** `creator self-check` (author has verified it) to `peer review` (a second person has
attempted it cold) to `sign-off` (programme lead has approved it for delivery).

---

## 1. Dataset and licence

| Item | Detail |
|---|---|
| **Dataset family** | Ilesanmi Stores point-of-sale export, one family across all seven topics, the labs and the mini project |
| **Files** | `Ilesanmi_Sales_Raw_Export.csv` and `.xlsx` (1,025 rows, issued to trainees); `Ilesanmi_Sales_Clean_AnswerKey.xlsx` (1,000 rows, instructor only) |
| **Source** | Adapted from the public "Supermarket Sales" dataset on Kaggle, originally a three-branch retail chain in Myanmar |
| **Licence** | Kaggle public dataset, educational reuse permitted. Confirmed before the module was built on it |
| **Adaptation** | Branch and city labels replaced with Ikeja (Lagos), Wuse (Abuja) and Trans-Amadi (Port Harcourt); monetary values rescaled by a constant factor of 100 to give plausible Naira amounts; five categories of fault injected by script. Row counts, distributions and all internal arithmetic relationships unchanged from the source |
| **Personal data** | None. The source dataset contains no personal data and none was introduced, so the file is safe for trainees to upload to AI tools |
| **Dictionary** | `Datasets/README.md`, which also records every injected fault and the expected outcome of repairing it |

---

## 2. Artefacts

### Demo guides

| Artefact | What it is | AI-drafted | Review stage | Dataset | Outstanding |
|---|---|---|---|---|---|
| `module-demo/demo-guide.md` | 70-minute module demo covering all seven topics | Yes, corrected against executed figures | creator self-check | Both files | Peer review not yet done |
| `.../01-.../demo/demo-guide.md` | Topic 2.1 demo, 28 to 32 minutes | Yes, corrected | creator self-check | Raw export | Peer review |
| `.../02-.../demo/demo-guide.md` | Topic 2.2 demo, 33 to 37 minutes | Yes, corrected | creator self-check | Raw export | Peer review |
| `.../03-.../demo/demo-guide.md` | Topic 2.3 demo, 33 to 37 minutes | Yes, corrected | creator self-check | Both files | Peer review |
| `.../04-.../demo/demo-guide.md` | Topic 2.4 demo, 28 to 32 minutes | Yes, corrected | creator self-check | Answer key | Peer review |
| `.../05-.../demo/demo-guide.md` | Topic 2.5 demo, 28 to 32 minutes | Yes, corrected | creator self-check | Answer key | Peer review |
| `.../06-.../demo/demo-guide.md` | Topic 2.6 demo, 28 to 32 minutes | Yes, corrected | creator self-check | Both files | Peer review |
| `.../07-.../demo/demo-guide.md` | Topic 2.7 demo, 33 to 37 minutes | Yes, corrected | creator self-check | Answer key | Peer review; mini-assessment date and format to be confirmed by the programme team |

### Lab packs

| Artefact | What it is | AI-drafted | Review stage | Dataset | Outstanding |
|---|---|---|---|---|---|
| `.../01-.../lab/lab-pack.md` | Topic 2.1 lab, three tiers, 75 minutes | Yes | creator self-check | Raw export | Peer review; test-solve by a second person |
| `.../02-.../lab/lab-pack.md` | Topic 2.2 lab, three tiers, 90 minutes | Yes | creator self-check | Raw export | Peer review; test-solve |
| `.../03-.../lab/lab-pack.md` | Topic 2.3 lab, three tiers, 105 minutes | Yes | creator self-check | Raw export | Peer review; test-solve |
| `.../04-.../lab/lab-pack.md` | Topic 2.4 lab, three tiers, 80 minutes | Yes | creator self-check | Cleaned file | Peer review; test-solve |
| `.../05-.../lab/lab-pack.md` | Topic 2.5 lab, three tiers, 85 minutes | Yes | creator self-check | Cleaned file | Peer review; test-solve |
| `.../06-.../lab/lab-pack.md` | Topic 2.6 lab, three tiers, 85 minutes | Yes | creator self-check | Raw export | Peer review; test-solve |
| `.../07-.../lab/lab-pack.md` | Topic 2.7 lab, three tiers, 90 minutes | Yes | creator self-check | Cleaned file | Peer review; test-solve |

Every lab pack contains a Version A (no AI, assessed) and Version B (with AI, prompt log and
verification note required) of its core exercise, as Section 5 of the Content Creator Guide requires.

### Lab solution files

| Artefact | What it is | AI-drafted | Review stage | Dataset | Outstanding |
|---|---|---|---|---|---|
| `.../NN-.../lab/solutions/tier-1-solution.md` | Worked Tier 1 solution, all seven topics | Yes, figures executed | creator self-check | As per topic | Peer review |
| `.../NN-.../lab/solutions/tier-2-solution.md` | Worked Tier 2 solution, all seven topics | Yes, figures executed | creator self-check | As per topic | Peer review |
| `.../NN-.../lab/solutions/tier-3-solution.md` | Worked Tier 3 solution, all seven topics | Yes, figures executed | creator self-check | As per topic | Peer review |
| `.../NN-.../lab/solutions/solution-notes.md` | Specification for the solution workbook, all seven topics | Yes | creator self-check | As per topic | Peer review |

### The seven `.xlsx` lab solution workbooks: built, executed and tested

| Workbook | Size | Contents | Verified |
|---|---|---|---|
| `2.1_lab_solution.xlsx` | 179 KB | `RawSales` 1,025 rows, 5 calculated columns, Checks and Findings sheets | 16 assertions |
| `2.2_lab_solution.xlsx` | 246 KB | `RawSales` plus 6 more calculated columns, Lookups and Summary sheets | 16 assertions |
| `2.3_lab_solution.xlsx` | 233 KB | `RawSales` 1,025 and `CleanSales` 1,000 side by side, Cleaning Log, Verification, Colleague Note | 16 assertions |
| `2.4_lab_solution.xlsx` | 185 KB | `CleanSales`, 4 pivot tables on a shared cache, a Branch slicer connected to all four, Verification, Findings | 26 assertions |
| `2.5_lab_solution.xlsx` | 223 KB | `CleanSales`, 5 pivots, 3 dashboard charts plus the pie-versus-bar evidence pair, connected slicer, Dashboard Test Log | 28 assertions |
| `2.6_lab_solution.xlsx` | 131 KB | A real Power Query with all ten Applied Steps, materialised `CleanSales`, Step Order Evidence, Refresh Test | 24 assertions |
| `2.7_lab_solution.xlsx` | 128 KB | `CleanSales`, Known Totals, AI Comparison, Product Line Check with a live reconciliation, Verification Checklist | 26 assertions |

These were built in Microsoft Excel 16.0 through the COM automation interface rather than written out
as XML, so every table, formula, pivot table, chart and slicer is a real Excel object. Excel then
recalculated each workbook from scratch, and every figure was read back and asserted against values
recomputed independently from the datasets with pandas. **154 assertions, all passing.**

Two of those assertions test behaviour rather than numbers, because the notes promise it:

- Clearing the tax rate in `B1` of the 2.1 workbook sends the Tax Check total to zero, and restoring
  it brings the total back. That is what proves the absolute reference is real rather than a
  hard-coded number.
- Applying a stale Product line filter to the 2.4 pivot drives the `Pivot minus SUMIF` cell away from
  zero, and clearing the filter returns it to zero. That is what proves the reconciliation cell
  actually detects the fault it exists to detect.

> **One outstanding item, not blocking.** The build machine did not have the
> `Microsoft.Mashup.OleDb` provider registered, so the Topic 2.6 Power Query could not be bound to a
> worksheet table headlessly. The query itself is real and complete, and its output ships as a
> materialised `CleanSales` table produced by identical logic. A facilitator binds the two in about
> thirty seconds through Close & Load To; the workbook carries a Read Me First sheet with the steps
> and the two figures to confirm. Nothing in the teaching content depends on it, and it matters only
> for demonstrating a live Refresh All in the room.

### Assessment

| Artefact | What it is | AI-drafted | Review stage | Dataset | Outstanding |
|---|---|---|---|---|---|
| `MCQ/module-02-mcq.json` | 57-item formative check bank with explanations | Yes, every computational answer executed | creator self-check | Both files | Peer review: a colleague to attempt each item cold |
| `MCQ/module-02-mcq.csv` | The same bank in CSV, generated from the JSON | Generated | creator self-check | Both files | Regenerate from the JSON after any edit; the two must never be edited separately |
| `mini-project/module-02-mini-project-brief.md` | 3 to 5 hour consolidation project | Yes | creator self-check | Raw export | Peer review; a full test-solve to confirm the sizing |
| `mini-project/module-02-mini-project-rubric.md` | Six criteria, three levels each, 60 marks | Yes | creator self-check | n/a | Peer review; two reviewers to mark the same test submission and compare totals |

### Slides

| Artefact | Status |
|---|---|
| `.../NN-.../slides/*.pptx` | **Supplied separately by the module owner.** The seven `slides/` folders exist and are empty. No deck was created, modified or inspected during this pass, and the demo guides do not depend on any particular slide content |

---

## 3. Verification performed

Every figure quoted anywhere in this module was recomputed from
`Datasets/Ilesanmi_Sales_Clean_AnswerKey.xlsx` and `Datasets/Ilesanmi_Sales_Raw_Export.csv` with
pandas before it was written down, as Section 8 of the Content Creator Guide requires. Nothing was
carried over from memory, from an AI draft, or from the previous version of this module.

### Figures verified

| Measure | Cleaned, 1,000 rows | Raw export, 1,025 rows |
|---|---|---|
| Ikeja Sales | ₦10,620,037.05 | ₦11,062,565.85 |
| Wuse Sales | ₦10,619,767.20 | ₦10,755,627.75 |
| Trans-Amadi Sales | ₦11,056,870.65 | ₦11,338,588.80 |
| Chain total Sales | ₦32,296,674.90 | ₦33,156,782.40 |
| Transactions | 1,000 | 1,025 |
| Branch transaction counts | 340 / 332 / 328 | 353 / 338 / 334 |
| Rated 7 or above | 501 (blanks filled) or 496 (blanks left) | 508 |
| Average rating | 6.97 | 6.97 |
| Total quantity | 5,510 | 5,605 |
| Total cogs | ₦30,758,738.00 | ₦31,577,888.00 |
| Total Tax 5% | ₦1,537,936.90 | ₦1,578,894.40 |

Product line totals, cleaned: Food and beverages ₦5,614,484.40, Sports and travel
₦5,512,282.65, Electronic accessories ₦5,433,753.15, Fashion accessories
₦5,430,589.50, Home and lifestyle ₦5,386,191.30, Health and beauty ₦4,919,373.90.

Payment method counts, cleaned: Ewallet 345, Cash 344, Credit card 311. Customer type: Member 565,
Normal 435.

Deduplication outcomes: every column ticked leaves **1,006** rows (19 removed); Invoice ID alone
leaves **1,000** (25 removed). With Product line casing and spacing repaired first, an every-column
run leaves 1,004; with the dates repaired as well, 1,001. Invoice ID alone leaves 1,000 in any order.

The five sign-flipped quantities recover exactly from `cogs ÷ Unit price`: 1, 6, 7, 9 and 8.

### The toolchain, and how to re-run it

Everything in this module that can be checked mechanically is checked by scripts held in
`Module_02/checks/`, and the seven solution workbooks are built by those scripts rather than by
hand. See `Module_02/checks/README.md` for requirements and usage.

| Script | What it does |
|---|---|
| `m2data.py` | Rebuilds the cleaned 1,000-row dataset from the raw export and confirms it matches the instructor answer key column by column |
| `build_21_22.py`, `build_23_27.py` | Build the seven `.xlsx` solution workbooks in Excel through COM |
| `test_workbooks.py` | Opens all seven in Excel, forces a full recalculation, and asserts every live figure against values recomputed from the datasets |
| `verify_module_02.py` | Checks the written material: every quoted figure, the MCQ structure and CSV/JSON parity, and the prose rules |
| `audit_module_02.py` | Checks structure, cross-references, relative links, encodings and workbook health |
| `build_mcq.py` | Regenerates the MCQ JSON and CSV from one source list so the two cannot drift |

Never edit a figure in the written material by hand. Change it in the dataset or in `m2data.py`,
rebuild, and let the suites report every place that needs updating.

### Checks run and passing

- 400 automated assertions over the written material, covering every figure above, every MCQ
  structural rule, and the prose rules, all passing.
- 154 further assertions over the seven solution workbooks, run inside Excel after a full
  recalculation, all passing.
- Every naira figure appearing anywhere in the MCQ bank is one the verification script recomputed;
  no figure can be introduced into the bank without being added to the executed fact table first.
- Every MCQ item has a non-empty explanation. Every multiple choice item has four unique options with
  the answer appearing verbatim among them. Every True or False item has exactly `True|False`.
- The CSV is generated from the JSON and asserted field-by-field identical to it.
- No em dashes, no American spellings, no old branch names, no old file names, no old-scale figures,
  and no banned outcome verbs anywhere in the module.
- No "all of the above" or "none of the above" in any item.

The one deliberate exception to the American-spelling rule is `PivotTable Analyze` in
`04-pivot-tables/demo/demo-guide.md`, which is the Excel ribbon tab's actual name and correct as a
user interface label. It is checked, allowed by name, and should not be "corrected".

---

## 4. Logged exceptions to the templates

### MCQ bank size: 57 items rather than 50

The MCQ template requires exactly 50 items per module. This bank holds **57**. This is a deliberate
decision, recorded here rather than left for a reviewer to notice, following the precedent set by
`my_resources/mcq-sizing-note.md` for Module 7.

The Content Creator Guide, Section 4, requires a mix of question types, specifically naming short
answer for formulas. The previous 50-item bank was 49 multiple choice and 1 true or false, which does
not meet that requirement. Six short-answer items were added, one each for Topics 2.1, 2.2, 2.3, 2.4,
2.6 and 2.7, each asking for a formula and the figure it returns. A seventh item was added to Topic
2.3 testing the every-column Remove Duplicates trap, which is the module's most consequential
misconception and was untested.

Topic 2.5, charts and dashboard reporting, carries no short-answer item. It is the one topic in the
module whose outcomes are visual rather than formula-shaped, and a short-answer item there would test
recall of a figure rather than the ability to produce a chart.

**Resulting distribution:**

| Topic | Title | Items | Beginner | Intermediate | Advanced |
|---|---|---|---|---|---|
| 2.1 | The Excel environment, tables and referencing | 8 | 2 | 4 | 2 |
| 2.2 | Core formulas and functions | 8 | 2 | 4 | 2 |
| 2.3 | Data cleaning in Excel | 10 | 2 | 4 | 4 |
| 2.4 | Pivot tables | 8 | 3 | 3 | 2 |
| 2.5 | Charts and dashboard reporting | 7 | 2 | 3 | 2 |
| 2.6 | Power query | 8 | 3 | 3 | 2 |
| 2.7 | AI-augmented excel | 8 | 2 | 3 | 3 |
| | **Total** | **57** | **16** | **24** | **17** |

That is 28 per cent beginner, 42 per cent intermediate and 30 per cent advanced, against the
template's 30 / 40 / 30 target. Topic 2.3 carries ten items rather than eight because it is the
module's load-bearing skill and the topic where all four of the corrected factual errors sat.

**Decision required from the programme lead:** whether to accept 57 items, or to trim to 50 by
removing seven multiple choice items. Trimming is straightforward and the short-answer items should
be the last thing cut, since they are what brings the bank into line with the Guide.

---

## 5. Corrections made in this pass

Four factual errors were found in the previous version of the guides, all verified by execution
against the dataset, and all corrected:

| # | Where | What was wrong | What it now says |
|---|---|---|---|
| 1 | `module-demo/demo-guide.md`, Parts 2 and 4 | Quoted cleaned branch totals while describing the raw file, then verified a cleaned pivot against a raw SUMIF and claimed they matched | Part 2 quotes the raw figures and labels them raw; Part 4 rebuilds the SUMIF on the cleaned table and explains why the raw figure is a different question, not a mismatch |
| 2 | `02-core-formulas-and-functions/demo/demo-guide.md`, Parts 4 and 5 | Said `=COUNTIF(RawSales[Rating],">=7")` returns 501 and the Ikeja SUMIF returns the cleaned total, both against the 1,025-row raw table; and checked a count against a row count of 1,000 while working on 1,025 rows | 508 and ₦11,062,565.85 against the raw table, 1,025 as the row count, plus the explicit teaching point that the same formula returns 508 raw and 501 cleaned with the arithmetic that connects them |
| 3 | `03-data-cleaning-in-excel` and `module-demo` | Claimed Remove Duplicates before trimming would find 19 duplicates instead of 25. False on this dataset: Invoice ID carries no formatting fault, so deduplicating on it returns 1,000 rows in any order | The column choice is what moves the count: every column ticked leaves 1,006, Invoice ID alone leaves 1,000. Cleaning first still matters, because it makes the six disguised copies visible and is what any whole-row rule would need, taking an every-column run from 1,006 to 1,004 to 1,001 without ever reaching 1,000 |
| 4 | `03-data-cleaning-in-excel/demo/demo-guide.md`, Part 5 | Told the instructor to flag the five negative quantities because the true value could not be confirmed. It can be | Walks the three-path decision and lands on Correct, showing the arithmetic for all five rows, and keeps the point that Remove is the option requiring justification |

Also corrected: the module demo header now reads Weeks 2 to 3 with the placeholder note removed; the
cleaned table is named `CleanSales` from Topic 2.3 onwards while `RawSales` refers only to the
1,025-row raw table in Topics 2.1 and 2.2; and Topic 2.7's unresolved "Up Next" note now names the
Block 1 mini-assessment.

---

## 6. Recurring "still fuzzy" items to watch in delivery

Section 9 of the Content Creator Guide asks that recurring points of confusion be logged here as
revision candidates. Three are predicted from the structure of this material and should be confirmed
or dismissed after the first delivery:

1. **Which file a figure came from.** Nearly every wrong answer available in this module is the right
   formula run against the wrong table. Worth watching whether trainees start labelling figures
   without being told to.
2. **The Remove Duplicates dialog default.** Whether trainees who saw the 1,006 result in Topic 2.3
   still reach for the default in the Topic 2.6 lab.
3. **Flag as the safe default.** Whether trainees generalise "flag anything unusual" from Topic 2.3
   rather than testing recoverability first. If they do, the Part 5 rewrite needs to be pushed harder
   in the slides as well as the demo.

---

## 7. One error found by building the workbooks

Building and executing the solution files caught a factual error in the written material that no
amount of proofreading would have found, and it is recorded here as evidence that the step was worth
taking.

The Topic 2.1 lab and its solution notes stated that `=SUM(RawSales[Tax Check])` returns
₦1,578,894.40 and matches the export's own Tax 5% column exactly. Excel returned
**₦1,565,351.20**. The reason is sound: `Tax Check` is `Subtotal` multiplied by the rate, and
`Subtotal` is negative on the five sign-flipped rows, so the column inherits the same fault at one
twentieth of the size. The ₦13,543.20 gap is exactly five per cent of the ₦270,864.00
gap between Subtotal and cogs, from exactly the same five rows.

The material now states the correct figure and uses the gap as a second, quieter route into the same
finding, which is a better exercise than the one originally written. Four files were corrected: the
Topic 2.1 lab pack, its Tier 1 solution, its solution notes, and the Topic 2.1 demo guide.
