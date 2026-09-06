# Lab Exercise Pack, Topic 2.5: Charts and Dashboard Reporting

**Module 2 (Weeks 2 to 3) | Total time-box: 85 minutes | Dataset: your cleaned `CleanSales` table (1,000 rows) and the pivot tables from Topic 2.4**

By the end of this topic, the trainee can choose the correct chart type for a stated question, build
clearly labelled charts, and assemble them into a one-screen dashboard that answers a manager's
questions.

> **A note on which file you are using.** From here on, every figure is a **cleaned-file** figure,
> measured on the 1,000-row `CleanSales` table you produced in Topic 2.3. If a total in this lab does
> not match, check the table name in Table Design before you check anything else. The same formulas
> against the raw 1,025-row export return different and equally valid numbers, and mistaking one for
> the other is the most common way work in this module goes wrong.

## The situation

Write the manager's question at the top of a blank sheet before you build anything:

> **"Which branch is performing best, and what is driving it?"**

Everything in this lab is judged against that sentence. A chart that does not help answer it does not
belong on the dashboard, however good it looks.

---

## Tier 1, Guided (30 minutes)

1. From the Branch by Sales pivot, Insert, PivotChart, choose a **horizontal bar chart**. Sort largest
   at the top. Trans-Amadi leads.
2. Replace `Chart Title` with a title that states the measure, the dimension and the period, for
   example `Total Sales by Branch, January to March 2019`.
3. Remove the legend. There is one series, so the legend repeats the title and adds nothing.
4. Delete the default gridlines and apply one highlight colour to the leading bar.
5. Build a second chart from the Product line pivot: a **sorted bar chart** of Sales by Product line.
6. Now build a chart badly on purpose. Make a **pie chart** of Payment method counts: Ewallet 345,
   Cash 344, Credit card 311. Look at it and try to answer "which payment method is most common?"
   at a glance. You will not be able to, because Ewallet leads Cash by one transaction.
7. Rebuild the same data as a sorted bar chart with data labels, and keep **both**. You will need the
   pair for Tier 3.
8. Create a new sheet named `Dashboard`. Hide gridlines (View, untick Gridlines). Move the two bar
   charts onto it, align their edges, and put Sales by Branch in the **top left**.
9. Add the Branch slicer from Topic 2.4 and use Report Connections to link it to both charts.
10. Click each slicer button in turn and watch both charts respond together. If one does not move,
    the connection was missed.

### Expected output, Tier 1

| Chart | What it must show |
|---|---|
| Sales by Branch | Trans-Amadi ₦11,056,870.65, Ikeja ₦10,620,037.05, Wuse ₦10,619,767.20 |
| Sales by Product line | Food and beverages ₦5,614,484.40 leading, Health and beauty ₦4,919,373.90 last |
| Payment method | Ewallet 345, Cash 344, Credit card 311 |
| Dashboard | One screen, no scrolling, gridlines hidden, both charts responding to one slicer |

The Product line chart is the argument for the bar chart in one picture: six categories spanning
₦4,919,373.90 to ₦5,614,484.40, a spread of about 12 per cent, which no pie chart can rank.

---

## Tier 2, Semi-guided (25 minutes)

**Task.** The Tier 1 dashboard answers "which branch is performing best". It does not yet answer
"and what is driving it". Add exactly **one** chart that does, and be prepared to defend both the
chart you added and the charts you chose not to add.

**Expected result.** Your added chart must let a reader see that the three branches lead on
**different** product lines:

| Branch | Leading product line | Its Sales |
|---|---|---|
| Ikeja | Home and lifestyle | ₦2,241,719.55 |
| Wuse | Sports and travel | ₦1,998,819.90 |
| Trans-Amadi | Food and beverages | ₦2,376,685.50 |

A clustered bar chart of Product line by Branch is one good answer. A single-branch chart driven by
the slicer is another. Both are defensible; what is marked is whether a reader can reach the finding
without being told it.

**Deliverable.** The updated dashboard, plus three sentences: what you added, why that chart type,
and what you rejected and why.

---

## Tier 3, Independent (30 minutes)

> Your dashboard goes to the regional manager tomorrow. Before it does, test it the way a sceptical
> colleague would.

Do all three of these and write up what happened:

1. **The cold question test.** Hand your dashboard to someone who has not seen it and ask them the
   manager's question. Time how long they take. Then ask a second question you did not prepare for:
   *"which branch should we worry about?"* If either answer takes more than a few seconds to find,
   rearrange the dashboard rather than adding another chart.
2. **The slicer test.** Click every slicer button, including multi-select. Confirm every chart moves
   every time. Then deliberately disconnect one chart, look at the result, and describe in one
   sentence why this failure is more dangerous than a chart that simply breaks.
3. **The honest chart test.** Put your Payment method pie chart and bar chart side by side and write
   two sentences on which one you would send to the manager and why. Include the actual figures.

**Expected outputs, Tier 3**

- The cold question answer should be **Trans-Amadi**, and the reader should reach it from the top-left
  chart without clicking anything.
- The second question has no single right answer, which is the point. **Wuse** is defensible on the
  lowest revenue (₦10,619,767.20) and the lowest average rating; **Ikeja** is defensible on
  having the most transactions (340) and still not leading on revenue. Either is full credit with the
  figures attached. A confident answer with no figure behind it is not.
- The disconnected-slicer sentence must land on this: the dashboard keeps working and shows no error,
  so two charts show one branch while the third shows all three, and the reader has no way to tell.
- The pie versus bar answer must use the real numbers. Ewallet 345, Cash 344 and Credit card 311 are
  34.5, 34.4 and 31.1 per cent of 1,000 transactions, and a one-transaction lead cannot be seen in a
  pie chart at any size.

---

## The core exercise, in two versions

The core exercise for this topic is **choosing a chart type for a stated question and defending the
choice**.

### Version A, without AI (assessed)

Complete Tier 1 steps 1 to 7 and Tier 2 with no AI assistance. The judgement about which chart
answers which question is exactly the judgement being assessed, and it is not one to outsource.

### Version B, with AI (not assessed, still submitted)

1. Describe your data to an AI assistant in plain English, including the actual Payment method
   figures, and ask which chart type it recommends and why.
2. Ask it a second time, this time telling it the three values are 345, 344 and 311 out of 1,000.
   Note whether its recommendation changes once it has the numbers rather than just the column names.
3. Ask it to write a one-sentence title for your Sales by Branch chart. Compare it against yours.
4. **Verify.** Whatever it recommends, check the recommendation against the data, not against how
   reasonable it sounds. A pie chart recommendation for three near-equal values is wrong regardless
   of how well it is argued.

**Version B deliverable.** Both prompts, both recommendations, one sentence on whether supplying the
actual figures changed the advice, and one sentence on whether you would use its chart title.

---

## Time-box summary

| Tier | Time-box |
|---|---|
| Tier 1, Guided | 30 minutes |
| Tier 2, Semi-guided | 25 minutes |
| Tier 3, Independent | 30 minutes |
| **Total** | **85 minutes** |

## Submission checklist

- [ ] The manager's question written down before any chart was built
- [ ] Sales by Branch bar chart, sorted, specific title, no legend, Trans-Amadi leading
- [ ] Sales by Product line bar chart, sorted
- [ ] Payment method shown both ways, pie and bar, both kept
- [ ] Dashboard sheet, one screen, gridlines hidden, most important chart top left
- [ ] Slicer connected to every chart, tested button by button
- [ ] Tier 2 chart added, with the three-sentence defence
- [ ] Tier 3 write-up covering all three tests, with figures
- [ ] Version B prompt log and verification note included

---

## Hints for Tier 2

<details>
<summary>Hint 1</summary>

You already built the data for this in Topic 2.4. The Branch by Product line cross-tab holds exactly
the comparison you need, and a chart can be inserted straight from it without building anything new.
</details>

<details>
<summary>Hint 2</summary>

Six product lines across three branches is eighteen bars, which is at the edge of readable. Two ways
out: cluster by branch so each group has six bars and the comparison is within a group, or show one
branch at a time and let the slicer do the switching. Either is defensible. Choosing eighteen bars
with no grouping and no slicer is not.
</details>
