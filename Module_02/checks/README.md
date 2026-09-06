# Module 2 build and verification toolchain

Everything in `Module_02/` that can be checked mechanically is checked by these scripts, and the
seven `.xlsx` lab solution workbooks are built by them rather than by hand. Run them from the
**repository root**.

## Requirements

| Requirement | Why | Notes |
|---|---|---|
| Python 3.12 with `pandas` and `openpyxl` | reads the datasets and recomputes every figure | already present |
| `pywin32` | drives Excel through COM | already present |
| Microsoft Excel (desktop, Windows) | builds and recalculates the workbooks | tested against Excel 16.0, x64 |

The Excel dependency applies only to `build_*.py` and `test_workbooks.py`.
`verify_module_02.py` and `build_mcq.py` are pure Python and run anywhere.

## The scripts

| Script | What it does |
|---|---|
| `m2data.py` | Loads the raw export and rebuilds the cleaned 1,000-row dataset by applying the five repairs the labs teach. Run directly to print every figure and confirm the result matches the instructor answer key column by column. |
| `xlbuild.py` | Excel COM helpers: structured tables, calculated columns, check rows, number formats. |
| `build_21_22.py` | Builds `2.1_lab_solution.xlsx` and `2.2_lab_solution.xlsx`. |
| `build_23_27.py` | Builds `2.3` to `2.7`. Takes optional arguments, for example `python ... build_23_27.py 24 25`. |
| `test_workbooks.py` | Opens all seven workbooks in Excel, forces a full recalculation, reads every live figure back and asserts it against values recomputed from the datasets. 154 assertions. |
| `verify_module_02.py` | Checks the written material: every quoted figure, the MCQ bank's structure and CSV/JSON parity, and the prose rules. 599 assertions. Run it from inside `Module_02/`. |
| `build_mcq.py` | Regenerates `MCQ/module-02-mcq.json` and the CSV from one source list, so the two files cannot drift. |

## Running everything

```bash
# from the repository root
python my_resources/checks/module_02/m2data.py                    # data sanity
python my_resources/checks/module_02/build_21_22.py               # build 2.1, 2.2
python my_resources/checks/module_02/build_23_27.py               # build 2.3 to 2.7
python my_resources/checks/module_02/test_workbooks.py            # 154 assertions, needs Excel

cd Module_02
python ../my_resources/checks/module_02/verify_module_02.py       # 599 assertions
```

Each script exits non-zero on any failure.

## Two behavioural tests worth knowing about

`test_workbooks.py` does not only compare numbers. It also confirms two things the solution notes
promise, by actually doing them:

1. **The absolute reference is real.** It clears the tax rate in `B1` of the 2.1 workbook, recalculates,
   and asserts the Tax Check total falls to zero, then restores the rate and asserts it comes back.
   A hard-coded number would not move.
2. **The reconciliation cell works.** It applies a stale Product line filter to the 2.4 pivot,
   recalculates, and asserts the `Pivot minus SUMIF` cell moves away from zero, then clears the
   filter and asserts it returns to zero.

## Known environment limitation

The `Microsoft.Mashup.OleDb` provider was not registered on the build machine, so the Topic 2.6
Power Query cannot be bound to a worksheet table headlessly. `build_23_27.py` therefore creates the
query as a real query object with all ten Applied Steps, and materialises its output into the
`CleanSales` table using identical logic in pandas. `test_workbooks.py` asserts that every named M
step is present and that the deduplication runs on Invoice ID alone.

On a machine where that provider is registered, a facilitator binds the two through Close & Load To
in about thirty seconds. The 2.6 workbook carries a Read Me First sheet with the steps and the two
figures to confirm.

## If a figure ever changes

Never edit a figure in the written material by hand. Change it in the dataset or in `m2data.py`,
rebuild, and let both test suites tell you every place that needs updating. `verify_module_02.py`
enforces this for the MCQ bank specifically: every Naira figure appearing anywhere in it must be one
the script recomputed, so a number cannot be introduced without being derived from the data first.
