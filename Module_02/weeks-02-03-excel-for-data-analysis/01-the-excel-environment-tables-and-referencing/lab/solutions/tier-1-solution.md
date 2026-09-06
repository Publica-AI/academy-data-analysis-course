# Tier 1 Worked Solution, Topic 2.1

Every figure here was recomputed from `Datasets/Ilesanmi_Sales_Raw_Export.csv` with pandas before
being written down. A trainee's workbook is correct when it reproduces all six.

## Steps, with the reasoning

**Steps 1 to 3, the environment.** Ctrl+End lands on the intersection of the last used row and
column. With one header row plus 1,025 data rows, that is **row 1026**. The Status bar figures for
the Sales column are Sum ₦33,156,782.40, Count 1,025 and Average ₦32,348.08. They are
worth pausing on because they are the same aggregates trainees are about to write formulas for, and
Excel gave them away for free.

**Steps 4 and 5, the table.** Ctrl+T with My table has headers ticked. Unticked, Excel invents
`Column1` to `Column17` and pushes the real headers into row 1, which is the single most common
Ctrl+T mistake and is worth letting a trainee make once. Rename to `RawSales` in Table Design.

**Steps 6 to 9, the two reference types.**

```
A1: Tax rate          B1: 0.05
Subtotal   =[@[Unit price]]*[@Quantity]
Tax Check  =[@Subtotal]*$B$1
```

The structured references `[@[Unit price]]` and `[@Quantity]` are relative by nature: they mean
"this row's value", so they follow the formula down. `B1` must be locked with F4, because every row
needs the same rate. Copied down unlocked it becomes `B2`, `B3` and so on, which are empty cells, so
the products collapse to zero. There is no error message, which is the point of the exercise.

## Expected figures

| Check | Expected | How it was verified |
|---|---|---|
| Rows in `RawSales` | 1,025 | `len(raw)` |
| Last cell (Ctrl+End) | Row 1026 | 1,025 data rows plus one header |
| `=SUM(RawSales[Tax Check])` | ₦1,565,351.20 | `((raw['Unit price']*raw['Quantity'])*0.05).sum()` |
| `=SUM(RawSales[Tax 5%])` | ₦1,578,894.40 | `raw['Tax 5%'].sum()` |
| `=SUM(RawSales[cogs])` | ₦31,577,888.00 | `raw['cogs'].sum()` |
| `=SUM(RawSales[Subtotal])` | ₦31,307,024.00 | `(raw['Unit price'] * raw['Quantity']).sum()` |

## The deliberate loose end

Two pairs of totals disagree, and they disagree for one reason.

| Pair | Gap |
|---|---|
| `cogs` minus `Subtotal` | ₦270,864.00 |
| `Tax 5%` minus `Tax Check` | ₦13,543.20 |

₦13,543.20 is exactly five per cent of ₦270,864.00, because Tax Check is Subtotal
multiplied by the rate, so it inherits the Subtotal fault at one twentieth of the size. Both gaps
come from the same five rows.

**This is worth being careful about when marking.** Row by row, Tax Check matches Tax 5% on 1,020 of
the 1,025 rows, so a trainee sampling a handful of rows will correctly report that it matches, and
that check does prove the `$B$1` reference held. The totals are the thing that does not match, and
noticing that is the Tier 2 hook. Do not resolve it in Tier 1.

The five sign-flipped quantities are therefore already visible in this file to anyone who checks the
arithmetic, three topics before anyone is told they exist.

## Common wrong answers

| What the trainee gets | What went wrong |
|---|---|
| Tax Check total of 0, or a column of zeros below row 1 | `B1` was left relative, so the reference walked off the rate |
| Tax Check total that is a long way out but not zero | The rate cell holds `5` or `5%` typed as text rather than `0.05` |
| Subtotal that stops filling partway down | The formula was dragged rather than entered once and allowed to auto-fill, or the table was never created |
| A total matching cogs exactly (₦31,577,888.00) | The Subtotal column references `cogs` rather than recomputing it, so it proves nothing |
