# Lab Exercise Pack, Topic 2.2: Core Formulas and Functions

**Module 2 (Weeks 2 to 3) | Total time-box: 90 minutes | Dataset: `Datasets/Ilesanmi_Sales_Raw_Export.xlsx` (1,025 rows)**

By the end of this topic, the trainee can build solutions using logical (IF, IFS), lookup (VLOOKUP,
XLOOKUP, INDEX-MATCH), text (TRIM, LEFT, TEXTSPLIT), date and aggregate functions, choosing the
appropriate function for a stated problem.

## The situation

Carry forward the `RawSales` table you built in Topic 2.1, still 1,025 rows, still uncleaned. The
regional manager at Ilesanmi Stores has started asking questions, and Adaeze needs answers today
rather than after the cleaning pass. Every figure you produce in this lab is therefore a **raw
figure**, and part of the exercise is labelling it as such.

---

## Tier 1, Guided (30 minutes)

1. **Logical.** Add a column `Satisfaction` with
   `=IF([@Rating]>=7,"Satisfied","Needs Follow-up")`.
2. Rebuild it as three bands in a second column, `Satisfaction Band`:
   `=IFS([@Rating]>=8,"Highly Satisfied",[@Rating]>=7,"Satisfied",TRUE,"Needs Follow-up")`.
   Note how much easier the second one is to read than the nested IF it replaces.
3. **Lookup.** In a blank cell `F1`, type the Invoice ID `351-62-0822`. Next to it build
   `=XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])`. It should return **Wuse**.
4. Build the same answer two more ways and confirm all three agree:
   - `=VLOOKUP(F1,RawSales[#All],2,FALSE)`
   - `=INDEX(RawSales[Branch],MATCH(F1,RawSales[Invoice ID],0))`
   Then delete the `FALSE` from the VLOOKUP and look at what comes back. It does not error.
5. **Text.** Build `=LEFT([@[Invoice ID]],3)` in a column called `Branch Code`. On invoice
   `750-67-8428` it returns `750`.
6. Find a Product line value in ALL CAPS and run `=LEN()` on it and on a normally cased one. The
   character counts differ by one more than the casing explains, because of a trailing space.
   Confirm with `=LEN(TRIM([@[Product line]]))`.
7. **Aggregate.** Below the table build these five, and label each one "raw, 1,025 rows":
   - `=SUM(RawSales[Sales])`
   - `=AVERAGE(RawSales[Rating])`
   - `=COUNT(RawSales[Sales])`
   - `=COUNTIF(RawSales[Rating],">=7")`
   - `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])`

### Expected output, Tier 1

| Check | Expected |
|---|---|
| XLOOKUP on `351-62-0822` | Wuse |
| All three lookup methods agree | Yes |
| `=LEFT("750-67-8428",3)` | 750 |
| `=SUM(RawSales[Sales])` | ₦33,156,782.40 |
| `=AVERAGE(RawSales[Rating])` | 6.97 |
| `=COUNT(RawSales[Sales])` | 1,025 |
| `=COUNTIF(RawSales[Rating],">=7")` | 508 |
| `=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])` | ₦11,062,565.85 |

**Label those last two carefully.** They are raw-file figures. On the cleaned file in Topic 2.3 they
become 501 and ₦10,620,037.05, and only the cleaned pair is reportable to a client.

---

## Tier 2, Semi-guided (30 minutes)

**Task.** Build a small branch summary block that reports, for each of Ikeja, Wuse and Trans-Amadi,
the total Sales and the number of transactions, from the raw table. Then add a fourth line that
totals your three branch figures and proves they reconstruct the whole file.

**Expected result.**

| Branch | Total Sales (raw) | Transactions |
|---|---|---|
| Ikeja | ₦11,062,565.85 | 353 |
| Wuse | ₦10,755,627.75 | 338 |
| Trans-Amadi | ₦11,338,588.80 | 334 |
| **All three** | **₦33,156,782.40** | **1,025** |

Your three branch totals must add to the chain total, and your three transaction counts must add to
1,025. If either fails, a branch name is spelled differently somewhere in the file or a condition is
picking up the wrong rows.

**Deliverable.** The block, plus one sentence stating why adding the three parts back to the whole is
a worthwhile check rather than busy work.

---

## Tier 3, Independent (30 minutes)

> The regional manager asks Adaeze a question by phone: **"how many Health and beauty transactions
> did the Wuse branch handle, and what did they come to?"**

Answer it from the raw table. The question names two conditions at once, which is one more than
`COUNTIF` and `SUMIF` take, so part of this exercise is recognising that you need the plural forms
and finding them yourself.

Then do the harder half. Write two sentences telling the manager what your figures do and do not
mean, given that this file has not been cleaned yet.

**Expected outputs, Tier 3**

| Measure | Expected (raw file) |
|---|---|
| Health and beauty transactions in Wuse | 53 |
| Their total Sales | ₦1,998,066.00 |

The two sentences should say, in some form, that these are counts and totals over a file still
containing 25 duplicated invoices and 102 miscased Product line entries, so the true figures are
lower, and that the Product line condition in particular is unreliable until the casing and spacing
are repaired.

---

## The core exercise, in two versions

The core exercise for this topic is **the conditional aggregate**: answering "how much, for which
rows" from a stated business question.

### Version A, without AI (assessed)

Complete Tier 2 with no AI assistance. Choose the function family yourself before writing anything,
and be able to say out loud why a conditional aggregate rather than a lookup answers this question.

### Version B, with AI (not assessed, still submitted)

Take the Tier 3 question, the two-condition one, to an AI assistant.

1. Write a prompt that gives it enough to work with: the table name, the exact column names, the two
   conditions, and the fact that the branch value is spelled `Wuse`.
2. Take the formula it returns and run it.
3. **Verify it.** Build the answer a second, independent way, for example with a PivotTable, or by
   filtering the table on both conditions and reading the Status bar. Two routes to 53 and
   ₦1,998,066.00 is verification; one route plus confidence is not.
4. Now try it badly on purpose. Prompt again without naming the branch spelling, or calling the
   branch "Abuja" instead of "Wuse", and see what comes back. Record what happened.

**Version B deliverable.** The prompt used, the formula returned, the figure it produced, the second
independent method you checked it with and what that returned, and one sentence on what the
deliberately vague prompt did differently.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 30 minutes |
| Tier 2, Semi-guided | 30 minutes |
| Tier 3, Independent | 30 minutes |
| **Total** | **90 minutes** |

## Submission checklist

- [ ] Satisfaction and Satisfaction Band columns both present
- [ ] Three lookup methods all return Wuse for `351-62-0822`
- [ ] Five aggregate cells present and labelled as raw, 1,025-row figures
- [ ] `=COUNTIF(RawSales[Rating],">=7")` reads 508, and is labelled raw
- [ ] Tier 2 branch block reconciles to ₦33,156,782.40 and 1,025
- [ ] Tier 3 answers 53 and ₦1,998,066.00 with the two-sentence caveat
- [ ] Version B prompt log, second method, and verification note included

---

## Hints for Tier 3

<details>
<summary>Hint 1</summary>

`COUNTIF` and `SUMIF` each take one condition. The functions that take several are named with an S
on the end, and their argument order is different from the singular versions: the range being summed
comes first, not last. Check the argument order in Excel's own tooltip before assuming it matches.
</details>

<details>
<summary>Hint 2</summary>

If your count comes back lower than expected, the Product line condition is the suspect rather than
the Branch one. 102 rows in this file hold the Product line in ALL CAPS with a trailing space.
Excel's criteria matching is not case sensitive, so casing alone will not break it, but a trailing
space will. Try `"Health and beauty*"` with the wildcard and compare the two answers, then decide
which one you would actually report and why.
</details>
