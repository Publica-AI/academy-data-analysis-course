# Tier 3 Worked Solution, Topic 2.7

## The task

Write a verification checklist for AI-assisted Excel work, then apply it to your own workbook.

## Model checklist

Every item names a specific check and a specific expected value, so that someone who was not there
can apply it and record a yes or no.

| # | Check | How to apply it | Expected |
|---|---|---|---|
| 1 | Which file was this measured on? | `=COUNTA(CleanSales[Invoice ID])` and `=SUM(CleanSales[Sales])` | 1,000 and ₦32,296,674.90 for the cleaned file. 1,025 and ₦33,156,782.40 means the raw export. 1,006 and ₦32,517,975.00 means a whole-row deduplication |
| 2 | Which column defined a duplicate? | The row count says it | 1,000 means Invoice ID. 1,006 means every column was left ticked and six duplicated sales remain |
| 3 | Do the parts add to the whole? | Three branch totals, and six product line totals, each summed and compared to `=SUM(CleanSales[Sales])` | Both reconcile to ₦32,296,674.90, difference exactly 0 |
| 4 | Was every figure rebuilt independently? | Each headline figure produced by two methods that do not share a source, for example a pivot and a SUMIF | Both agree. A second prompt to the same assistant does not count as a second method |
| 5 | Do formulas name the table? | Read the formula bar on each summary cell | Structured references such as `CleanSales[Sales]`, not `$A$2:$A$1001`, so a stale range cannot point at old data |
| 6 | Are judgement-dependent figures recorded with the judgement? | Look for a stated treatment of the nine blank Ratings | `=COUNTIF(CleanSales[Rating],">=7")` is 496 with blanks left in place and 501 if filled. Either is acceptable; an unlabelled figure is not |
| 7 | Are the arithmetic relationships intact? | Spot-check `cogs = Unit price × Quantity` across the table | Holds on all 1,000 rows. Five failures means the sign-flipped quantities were never repaired |
| 8 | Is there a prompt log, and does it record verification? | Read it | Every entry names the method used to check the output and what that method returned. "Looked correct" is a missing entry |

## What makes a weak checklist

Generic items that cannot be actioned: "check the data is accurate", "make sure the AI output is
correct", "use good prompts". None can be applied by a colleague, and none produces a yes or no.

The strongest items are the ones catching a **plausible** error rather than an obvious one. Items 1,
2 and 6 above are the three that catch the specific failures this module has demonstrated: the right
formula on the wrong file, the right tool with the wrong column ticked, and a figure that moves on an
unrecorded judgement.

## Applying it honestly to your own workbook

This is the part most likely to be skipped and the part worth the most credit. A trainee who applies
the checklist and reports that their own file fails item 6, because they never recorded how they
treated the blank Ratings, has done the exercise properly. A trainee who reports that their workbook
passes every item, on a first attempt, has probably not applied it.

Full credit requires at least one honest failure or one item the trainee cannot answer about their
own work.

## Marking notes

- Six to ten items, each with a specific expected value: the requirement.
- At least three items using this dataset's real figures: what makes it a checklist rather than an
  essay.
- The self-application, with honest findings: the assessed part.
