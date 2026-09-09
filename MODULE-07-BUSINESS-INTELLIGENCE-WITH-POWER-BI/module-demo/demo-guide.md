# Module Demo Guide - Business Intelligence with Power BI (Week 8)
**Module 7 | Estimated duration: 70-75 minutes**

---

## The Story

SwiftRoute Logistics runs last-mile delivery across Lagos from six hubs, and promises its
business customers a ninety per cent on-time rate. Adaeze Nwosu, the operations manager,
has a folder of five CSV exports and a board meeting on Monday at which she has to say
which part of the network is breaking the promise and what she intends to do about it. She
has been told the problem is the riders. This demo builds, in one sitting, the dashboard
that tells her whether that is true.

**What this demo builds:**

- A cleaned, correctly typed delivery table loaded through Power Query, with the load
  rules written so they survive next month's file (Topic 7.1)
- A star schema whose relationships answer questions about riders, routes, customers and
  dates rather than only about deliveries (Topic 7.2)
- The measures that turn the model into numbers Adaeze can act on, each verified against
  source data before it is shown (Topic 7.3)
- A one-screen KPI dashboard, ranked, sliced, stamped with its refresh date and exported
  in the form she can actually open (Topic 7.4)
- An audit of two AI-written measures that look right and are not, using the model as the
  judge rather than the assistant's confidence (Topic 7.5)
- The sign-off conversation that turns this way of working into each trainee's own
  capstone question and dataset (Topic 7.6)

---

## Prerequisites

1. Power BI Desktop installed and signed in if a Pro licence is available. Free from the
   Microsoft Store; Windows only.
2. The five SwiftRoute files in this folder: `swiftroute_deliveries_raw.csv`,
   `swiftroute_deliveries.csv`, `riders.csv`, `routes.csv`, `routes_raw.csv`,
   `customers_business.csv` and `dates.csv`. No real personal data: every rider name,
   business name and identifier is generated, so the files are safe to upload to an AI
   tool in Part 5.
3. The topic fallbacks open in a second window, in build order:
   `7.1_fallback_loaded.pbix`, `7.2_demo_star.pbix`, `7.3_solution.pbix` and
   `7.4_fallback_dashboard.pbix`. Each lives in its topic's `demo` folder.
4. A free-tier AI assistant open in a browser tab for Part 5.
5. Blank copies of `capstone-signoff-form.md` for Part 6.

> **Instructor note:** this demo runs the whole module in seventy minutes, which means
> every part is shorter than its own topic demo. Do not try to teach Power Query, DAX and
> dashboard design properly here. The job of this session is to show the pipeline as one
> continuous piece of work, so trainees see why the topics are ordered as they are. When a
> part runs long, cut the detail and keep the join between parts.

---

## Dataset / Project Setup (before the demo starts)

1. Copy all seven CSV files to a local folder. Do not open them in Excel first, because
   Excel will silently reformat the date column and the demo's first teaching point
   depends on Power BI seeing the file as it was written.
2. Confirm the raw file's row count is 41,283 and the clean file's is 41,280. The three
   extra rows, `D-TEST01` to `D-TEST03`, have a blank CustomerID and exist to be filtered
   out in Part 1.
3. Open `routes_raw.csv` in a text editor and confirm the trailing space after `LAG-07` on
   the first data row is still present. This is the planted fault for Part 2. It survives
   copying, but not a round trip through Excel.
4. Open each fallback once, so a cold model load does not happen in front of the room.

---

## Demo Steps

### Part 1 - Loading and Cleaning, as Rules Not Edits (Topic 7.1) (12 min)

> "Adaeze has five files and no database. Before we can answer anything we have to get
> them in, and how we get them in decides whether this dashboard still works in February."

**Home, Get data, Text/CSV, point at `swiftroute_deliveries_raw.csv`, and click Transform
data rather than Load.**

> "Power BI guesses types from the first couple of hundred rows. It guesses well, and that
> is exactly the problem, because a fault in row thirty thousand is invisible at the moment
> it matters most."

**Set the types, narrating only the one that teaches: `RiderID`, `RouteID`, `CustomerID`
and `DeliveryID` to Text, `DateKey` to Date, `DeliveryFee` to Fixed decimal number.**

> "Rider fourteen plus rider twenty-two is not rider thirty-six. If arithmetic on a column
> is meaningless, the column is a label, and labels are text."

**Filter `CustomerID` to remove blanks. Watch the row count fall from 41,283 to 41,280.**

> "Read what I typed: remove rows where CustomerID is blank. That is a rule, true of any
> file with this shape. Delete rows 41,281 to 41,283 is a fact about this one file, and
> next month it will quietly delete three innocent rows instead."

**Close and Apply. Load the other four files the same way.**

---

### Part 2 - The Model Decides Which Questions Are Askable (Topic 7.2) (12 min)

> "SwiftRoute employs sixty-eight riders. Watch what happens when I count them from a
> single flat table."

**Open `7.2_demo_flat.pbix`, drop `RiderName` on a Card, set it to Count. It reads 41,280.**

Pause. Say nothing for three seconds.

> "No error, no warning, nothing red. The file loaded, the visual built, and the answer is
> nonsense. Fatima Abubakar, rider R-014, is in that table six hundred and seventeen times,
> because she made six hundred and seventeen deliveries. Counting her name counts
> deliveries, not riders."

**Switch to the star file, Model view. Draw the four relationships from riders, routes,
customers_business and dates onto swiftroute_deliveries. Mark dates as the date table.**

> "One row per thing that happened in the middle, one row per thing that exists around the
> outside. Read the cardinality every time: one to many, with the one on the dimension. If
> it ever says many to many, stop, because your dimension has duplicate keys."

**Swap in `routes_raw.csv` and show the relationship failing silently.**

> "LAG-07 and LAG-07 with a trailing space look identical to you and are different strings
> to Power BI. The fix is upstream in Power Query, Transform, Format, Trim. Never by hand
> in the source file."

**Ask students:** "The relationship built without an error and produced blanks. Which is
more dangerous, an error or a blank?"

> "The blank, every time. An error stops you. A blank lets you present."

---

### Part 3 - Measures, and Proving Them (Topic 7.3) (12 min)

**In `7.3_solution.pbix`, write the four that carry the dashboard:**

```dax
Total Deliveries = COUNTROWS ( swiftroute_deliveries )
Total Revenue    = SUM ( swiftroute_deliveries[DeliveryFee] )
On-Time Deliveries = CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "On time" )
On-Time Rate     = DIVIDE ( [On-Time Deliveries], [Total Deliveries] )
```

**Confirm at the total level: 41,280 deliveries, ₦247,680,000 revenue, 82.0 per cent on
time.**

> "Eighty-two against a promise of ninety. That is the whole reason this dashboard exists."

> "DIVIDE, not a slash. Filter to a rider who joined last week with no deliveries and the
> denominator is zero. A slash gives you an error on Adaeze's screen. DIVIDE gives you a
> blank, which is the honest answer."

**Reconcile: switch to Table view, filter Status to On time, read 33,850 rows.**

> "A number from a completely different surface agreeing with the measure. That is what
> verification looks like, and it takes ten seconds."

---

### Part 4 - The Dashboard, and the Answer It Gives (Topic 7.4) (16 min)

**Open `7.4_start_model.pbix`. Sketch on paper first: four cards along the top, ranked
chart on the left, detail table on the right.**

**Build the four cards: On-Time Rate 82.0%, Total Deliveries 41,280, Total Revenue
₦247,680,000, Late Deliveries 7,430. Put a 90 per cent target on the rate.**

> "Eighty-two per cent is a metric. Eighty-two per cent against ninety is a KPI, and now it
> demands a decision."

**Build the ranked bar chart: `routes[RouteID]` on the axis, On-Time Rate as the value,
`routes[RouteName]` in Tooltips, sorted descending, with an SLA reference line at 90 per
cent.**

> "RouteID on the axis, not RouteName. SwiftRoute runs two different routes called Apapa to
> Ikeja. Group by the name and they merge into one bar at sixty-nine point nine per cent,
> and the worst route in the business disappears into an average. The ID is unique, so the
> ID goes on the axis."

**LAG-07 lands at the bottom at 61.4 per cent.**

**Now the part that answers Adaeze's question. Add a Hub slicer, click through all six
hubs, and read the rate each time.**

| Hub | Deliveries | On-time rate |
|---|---|---|
| Ikorodu | 6,683 | 81.5% |
| Ikeja | 7,370 | 81.5% |
| Apapa | 7,218 | 81.6% |
| Surulere | 6,647 | 82.4% |
| Lekki | 6,800 | 82.5% |
| Yaba | 6,562 | 82.6% |

> "Six hubs, and barely one percentage point between the best and the worst. Whatever is
> breaking the promise, it is not a hub, and it is not a rider, because the riders sit in
> the same narrow band. Adaeze was told it was the riders. It is not."

**Swap the slicer field to `routes[ZoneTier]` and read it again.**

| Zone tier | Deliveries | On-time rate |
|---|---|---|
| Long | 13,806 | 77.8% |
| Medium | 13,272 | 83.5% |
| Short | 14,202 | 84.6% |

> "Nearly seven points between short and long runs, and LAG-07, the worst route in the
> business, is an eighteen point four kilometre run. The finding is not who is driving. It
> is how far. That changes what Adaeze does on Monday: she reprices or reschedules the long
> routes, she does not retrain the riders."

**Add the refresh stamp and export to PDF.**

```dax
Last Refreshed = "Data as at " & FORMAT ( MAX ( dates[DateKey] ), "dd MMM yyyy" )
```

> "A failed refresh is invisible by default. The dashboard keeps showing old numbers with
> total confidence. This one card is the cheapest professional insurance in the module."

---

### Part 5 - Handing the Same Job to an AI Assistant (Topic 7.5) (12 min)

*(The AI part comes here, after everything above was built by hand, deliberately.)*

**In the assistant, prompt blind: "Write a DAX measure for on-time rate." Paste the answer
in, put it on a card with no filters, then filter to LAG-07.**

> "You already know LAG-07 is sixty-one point four. Read what the card says now."

**Now show the two planted faults side by side:**

```dax
Measure B: On-Time Rate = DIVIDE ( [On-Time Deliveries], 41280 )
Measure C: Late Rate    = DIVIDE (
    CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "Late" ),
    CALCULATE ( [Total Deliveries], swiftroute_deliveries[Status] = "Late" ) )
```

**Build B live. At the total it reads 82.0 per cent, because 41,280 genuinely is the grand
total. Filter to LAG-07 and it collapses to 5.1 per cent against the true 61.4.**

> "The denominator is a number, not a measure, so it never moves when the numerator does.
> This is exactly why you check more than one filter state, never just the total."

**Build C live. It returns one hundred per cent in every context.**

> "Late divided by late. The formatting is perfect and the number is meaningless."

**Re-prompt properly, with the schema, the grain, the actual Status values and the
constraint that the measure must respond correctly to any filter.**

> "Same assistant, same question, completely different answer, because this time it could
> see the model. The skill being assessed in this module is not prompting. It is judging."

---

### Part 6 - From SwiftRoute to Your Own Question (Topic 7.6) (8 min)

**Read a weak idea aloud: "Analysis of Nigerian fintech transaction data."**

> "Run the test silently. Could a named person act differently depending on the answer?
> Hands up if you can picture that person."

*(Few or no hands.)*

> "That is a topic, not a question. Watch me fix it. For a fraud analyst at a Nigerian
> fintech, how does the failed-transaction rate vary by bank and time of day, and where
> should manual review be focused?"

**Point back at the dashboard on screen.**

> "Everything we built today answers one question for one named person, and it changed what
> she does on Monday. That is the standard your capstone is held to. Four criteria on the
> form: real, sufficient, no personal data, and a genuine question. All four, or not yet."

**Hand out `capstone-signoff-form.md`. Collect it before anyone leaves.**

---

## Demo Wrap-Up

| Capability | Topic it came from | What it shows |
|---|---|---|
| Query that reloads next month without editing | 7.1 | Filters written as rules, types set explicitly, 41,280 rows every time |
| Rider and route counts that are actually rider and route counts | 7.2 | A star schema, four one-to-many relationships, dates marked |
| Numbers that survive a filter | 7.3 | Measures with DIVIDE and CALCULATE, reconciled against Table view |
| A one-screen answer with a target, a ranking and a refresh stamp | 7.4 | Four KPI cards, ranked chart on RouteID, Hub slicer, SLA line |
| A wrong AI measure caught before it reached the board | 7.5 | Measures B and C audited against source data, not accepted on sight |
| Each trainee's own question, judged against the same standard | 7.6 | A completed sign-off form with four criteria answered |

> "Adaeze walked in believing her riders were the problem. She leaves with a dashboard
> showing that her six hubs are within one point of each other, that long routes run nearly
> seven points worse than short ones, and that her worst route is an eighteen kilometre
> run. That is what a BI analyst is paid for: not the chart, the change of mind."

---

## Common Student Issues During the Module Demo

| Issue | What to say |
|-------|-------------|
| Row count reads 41,283 instead of 41,280 after Part 1 | "The blank-CustomerID filter was not applied, or was applied to the wrong column. Check the Applied Steps pane for a Filtered Rows step." |
| The rider count still reads a delivery-sized number after Part 2 | "You are still looking at the flat file in the other window. Confirm the title bar says the star schema file." |
| The routes relationship refuses to build, or builds with blanks | "Trim has to be applied to the key column in both tables, not just one. Check RouteID in routes and in swiftroute_deliveries." |
| On-Time Rate returns blank at the total level | "Status has no rows matching exactly 'On time'. Check the casing and spacing in the CALCULATE condition." |
| The ranked chart shows 22 bars and the worst reads 69.9% | "RouteName is on the axis instead of RouteID. Two pairs of routes share a name, so two bars merged and LAG-07's 61.4% was averaged away." |
| A trainee concludes from the flat hub table that nothing is wrong | "Flat is the finding, not the absence of one. It rules out the hub as the cause, which is why the next slicer matters." |
| Deliveries Previous Month is blank for every month | "The dates table is not marked as a date table. Table tools, Mark as date table, DateKey." |
| A trainee wants to submit a sign-off form with the dataset field as 'TBD' | "That is a blank field, not an honest source entry. Write 'no dataset chosen yet, considering X and Y' instead." |
