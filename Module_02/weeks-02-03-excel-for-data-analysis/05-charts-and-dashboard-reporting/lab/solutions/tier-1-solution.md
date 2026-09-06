# Tier 1 Worked Solution, Topic 2.5

All figures recomputed from `Datasets/Ilesanmi_Sales_Clean_AnswerKey.xlsx` with pandas.

## Chart 1, Sales by Branch

Horizontal bar, sorted largest at the top.

| Branch | Sales |
|---|---|
| Trans-Amadi | ₦11,056,870.65 |
| Ikeja | ₦10,620,037.05 |
| Wuse | ₦10,619,767.20 |

Title: something equivalent to `Total Sales by Branch, January to March 2019`. Legend removed, since
there is one series. Gridlines removed. One highlight colour on the Trans-Amadi bar.

Worth naming out loud: the second and third bars will look **identical** at any normal chart size,
because Ikeja and Wuse are ₦269.85 apart on totals above ten million. That is not a flaw in the
chart, it is the chart telling the truth, and it is the argument for adding data labels when a
ranking is close enough that the reader would otherwise guess.

## Chart 2, Sales by Product line

Sorted bar chart, six categories:

| Product line | Sales |
|---|---|
| Food and beverages | ₦5,614,484.40 |
| Sports and travel | ₦5,512,282.65 |
| Electronic accessories | ₦5,433,753.15 |
| Fashion accessories | ₦5,430,589.50 |
| Home and lifestyle | ₦5,386,191.30 |
| Health and beauty | ₦4,919,373.90 |

The leader is about 12 per cent above the smallest, and the middle four sit within ₦100,000 of
each other. Six near-equal slices in a pie would be unreadable; six bars on a shared baseline are not.

## Chart 3 and 4, Payment method, deliberately both ways

Ewallet 345, Cash 344, Credit card 311, out of 1,000 transactions. As percentages: 34.5, 34.4 and
31.1.

The pie chart is the point of the exercise. Ewallet leads Cash by **one transaction**, and no pie
chart at any size can show that. The bar chart with data labels can. Keep both, because the
comparison is the lesson.

## Dashboard assembly

New sheet, gridlines hidden via View. Sales by Branch top left, because it answers the first half of
the manager's question and the eye lands there first. Charts aligned to a grid. Branch slicer at the
top, connected to both charts through Report Connections, and tested button by button.

## Common wrong answers

| What the trainee produces | What went wrong |
|---|---|
| Chart titled `Chart Title` or `Sum of Sales` | Excel's default left in place; the reader has to ask what they are looking at |
| A legend on a single-series chart | Repeats the title, costs space, adds nothing |
| Charts on the same sheet as the pivots | Not a dashboard; a dashboard is a dedicated one-screen sheet |
| A pie chart of Sales by Branch | Three values within 4 per cent of each other, so the ranking is invisible |
| Slicer connected to one chart | The failure is silent, which is what makes it worth testing every button |
