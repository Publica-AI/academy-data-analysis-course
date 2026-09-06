# Solution Workbook Notes, Topic 2.5

> ### Status: built, executed and tested
>
> **`2.5_lab_solution.xlsx` ships with this lab pack** (223 KB). It was built in Microsoft Excel through
> the COM automation interface, not written out as XML, so every table, formula, pivot table,
> chart and slicer in it is a real Excel object. Excel then recalculated the whole workbook from
> scratch and every figure below was read back out and asserted against values recomputed
> independently from the datasets with pandas. Nothing in it is a cached number that nobody checked.
>
> This file remains the specification. If the workbook and this file ever disagree, the workbook
> is wrong, because this is what the test asserts against.

## File

`2.5_lab_solution.xlsx`, continuing from the Topic 2.4 solution workbook.

## Sheet: Dashboard

One screen, no scrolling at 100 per cent zoom on a 1366 by 768 display. Gridlines hidden. Contents:

| Position | Chart | Must show |
|---|---|---|
| Top left | Sales by Branch, horizontal bar, sorted | Trans-Amadi ₦11,056,870.65, Ikeja ₦10,620,037.05, Wuse ₦10,619,767.20, with data labels because the second and third are ₦269.85 apart |
| Top right | Sales by Product line, sorted bar | Food and beverages ₦5,614,484.40 down to Health and beauty ₦4,919,373.90 |
| Bottom | Sales by Product line clustered by Branch | Ikeja led by Home and lifestyle ₦2,241,719.55, Wuse by Sports and travel ₦1,998,819.90, Trans-Amadi by Food and beverages ₦2,376,685.50 |
| Top strip | Branch slicer | Connected to all three charts via Report Connections |

Every chart carries a specific title naming measure, dimension and period. No legend on any
single-series chart. No default gridlines inside the plot areas.

## Sheet: Chart Choice Evidence

Kept deliberately, not deleted, because the comparison is the teaching content:

- The Payment method **pie** chart: Ewallet 345, Cash 344, Credit card 311.
- The Payment method **bar** chart, sorted, with data labels, same three values.
- A text cell stating that Ewallet leads Cash by one transaction out of 1,000, that the three are
  34.5, 34.4 and 31.1 per cent, and that this is why the bar chart is the one that would be sent.

## Sheet: Dashboard Test Log

The manager's question written out in full, the timed cold-read result, the answer to the unprepared
second question with its supporting figure, the slicer test result button by button, and the
one-sentence statement of why a silently disconnected slicer is more dangerous than a broken chart.

## Before sign-off

1. Open the Dashboard sheet at 100 per cent zoom and confirm nothing requires scrolling.
2. Click every slicer button and confirm all three charts move on every click.
3. Confirm no chart still carries the title `Chart Title` or `Sum of Sales`.
4. Confirm the Sales by Branch chart carries data labels. Without them the Ikeja and Wuse bars are
   indistinguishable and the chart cannot answer the question it exists for.

## Note on the shipped workbook

All four pivots and the Payment pivot share a single PivotCache, which is what allows one Branch slicer to drive every chart. A slicer sharing no cache with a pivot cannot be connected to it, and that is the most common reason a hand-built dashboard has a chart that will not respond.
