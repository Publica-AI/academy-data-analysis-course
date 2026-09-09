# Demo Guide - KPI Dashboards and Publishing
**Module 7, Topic 7.4 | Estimated duration: 45-50 minutes**

---

## What This Demo Teaches

- Designing a dashboard backwards from a named audience and their decisions, not from the fields available
- Turning a plain metric into a KPI by attaching a target
- Building four KPI cards, a ranked bar chart, and a detail table in the correct build order
- Adding a slicer and confirming it visibly shows its filtered state
- Adding a visible refresh timestamp so a failed refresh cannot go unnoticed
- Publishing to a workspace, and exporting to PDF as the fallback when no Pro licence is available

---

## Setup - Before the Demo Starts

1. `7.4_start_model.pbix` open - the completed Topic 7.3 model, measures in place, no visuals yet
2. `7.4_fallback_dashboard.pbix` open in a second window, the finished dashboard, in case a live build step fails
3. Paper and pen at each seat for the two-minute sketch before building starts
4. Confirm in advance whether the room has a Power BI Pro licence, so Part 5 is delivered accurately either way

> **Instructor note:** deliberately choose the wrong chart type once during this demo, notice it aloud, and change it. Watching a visible recovery from a wrong choice is worth more here than a perfect build.

> **Instructor note:** the shipped `7.4_start_model.pbix` carries nine measures, the state the Topic 7.3 build actually ends in. Two of them, `Late Deliveries` and `Last Refreshed`, are the ones Parts 2 and 4 below write live. If you want that live-writing moment, delete those two from the `_Measures` table before the session. If you would rather not, point at them instead and say they came out of the 7.3 build.

### Getting `7.4_start_model.pbix` ready, if not already done

1. If `7.3_solution.pbix` does not exist yet, build it first (see the 7.3 demo guide's Setup and Demo Steps).
2. Open `7.3_solution.pbix`. **File → Save as → `7.4_start_model.pbix`.** The measures are already in place and no visuals exist yet, which is the correct starting point for this demo.

### Building `7.4_fallback_dashboard.pbix` in advance

A built and checked copy of this file already sits in this folder. Opened in Power BI Desktop it reads On-Time Rate 82.0%, Total Deliveries 41280, Total Revenue ₦247,680,000, Late Deliveries 7430, a refresh stamp of "Data as at 31 Dec 2025", the ranked route chart on RouteID, the rider table and the Hub slicer. Two cosmetic touches are left to whoever presents it: the thousands separator on Total Deliveries and Late Deliveries, which comes from the measure's format string in the model, and the chart title, which still reads the Power BI default rather than a finding.

If you would rather build your own, or need to rebuild it, this is the sequence, following Part 2 to Part 4 of this demo:

1. **Canvas.** Format your report page (paint roller icon) → Canvas settings → Type **16:9** → Canvas background colour **#F7FAFA**.
2. **Four cards**, one per measure (On-Time Rate, Total Deliveries, Total Revenue, Late Deliveries), formatted with a white background, 8px rounded corners, a subtle bottom shadow, callout value in `#0A1A23`, and the category label turned off in favour of a plain text title in `#64748B`. Align and distribute them evenly (Format tab → Align → Align top, then Distribute horizontally).
3. **On-Time Rate as a KPI visual**, Value = On-Time Rate, Trend axis = `dates[MonthName]`, target set to 90%.
4. **Ranked bar chart**: horizontal bars, Y-axis `routes[RouteID]`, X-axis On-Time Rate, `routes[RouteName]` in Tooltips, sorted by On-Time Rate descending so LAG-07 falls to the bottom. Use RouteID and not RouteName, because two routes share the name Apapa to Ikeja and grouping by name merges LAG-07 into a single 69.9% bar that hides the real worst performer. Bar colour `#387F7F`, data labels on, title stating the finding rather than naming the fields. Add a constant reference line via the Analytics pane at value 0.9, colour `#A8322D`, dashed, labelled SLA 90%. Optionally colour bars below 70% red using a field-based rule (Format → Bars → Colour → fx → Rules).
5. **Hub slicer**, Tile style, white background with an 8px border, placed top right.
6. **Rider detail table**: RiderName, Total Deliveries, On-Time Rate, horizontal gridlines only, header background `#F4F7F7`.
7. **Refresh stamp card** using the `Last Refreshed` measure, bottom of the canvas.
8. **File → Save as → `7.4_fallback_dashboard.pbix`.**

---

## Demo Steps

### Part 1 - Sketch Before Building (5 min)

**On paper, sketch Adaeze's layout: title and filters across the top, four KPI cards in a row, a ranked chart on the left, a detail table on the right.**

> "Two minutes on paper saves forty minutes in Power BI. Readers scan a screen from the top left, the same way they read a page, so the most important number goes where the eye lands first."

---

### Part 2 - Four KPI Cards (10 min)

**Add four Card visuals in a row: On-Time Rate, Total Deliveries, Total Revenue, Late Deliveries (a new quick measure: `CALCULATE([Total Deliveries], swiftroute_deliveries[Status]="Late")`).**

> "Cards first, because the headline answers should exist before we spend time on a chart nobody needed yet."

**Confirm the four values: On-Time Rate 82.0%, Total Deliveries 41,280, Total Revenue ₦247,680,000, Late Deliveries 7,430.**

**On the On-Time Rate card, add a target line or switch to the KPI visual, set the target to 90%.**

> "Eighty-two percent on its own is a metric. Eighty-two percent against a ninety percent target is a KPI - eight points below promise, and now it demands a decision."

---

### Part 3 - The Ranked Route Chart (10 min)

**Add a horizontal bar chart: `routes[RouteID]` on the axis, On-Time Rate as the value. Drag `routes[RouteName]` into the Tooltips well so the reader can still see the plain-English name on hover.**

*(Deliberately build this first as a vertical column chart, notice aloud that the long route codes are unreadable, then switch to horizontal.)*

> "That was the wrong choice, and I want you to see me notice it and fix it rather than pretend I got it right first time."

> "Notice which field I put on the axis. RouteID, not RouteName. SwiftRoute runs two different routes called Apapa to Ikeja, LAG-07 and APA-01, on different distances. Put the name on the axis and Power BI silently merges them into one bar, and the worst route in the business disappears into an average. The ID is unique, so the ID goes on the axis and the name rides along in the tooltip."

**Sort by On-Time Rate, descending.**

> "Descending, not ascending. On a horizontal bar chart Power BI puts the first sorted value at the top, so descending puts the best route at the top and walks the reader down to the worst. Sort it the other way and LAG-07 appears at the top, which reads as a chart about the leader rather than a chart about the problem."

> "LAG-07 lands at the bottom, sixty-one point four percent, exactly where it sat in Topic 7.2. Sorting deliberately is what makes the worst performer visible without anyone having to hunt for it."

**Add a constant reference line at 90% via the Analytics pane, labelled SLA 90%.**

---

### Part 4 - Slicer and Refresh Stamp (10 min)

**Add a Hub slicer. Set its style to Tiles.**

> "Click Apapa. Watch both the chart and a rider detail table respond." Add a simple rider detail table (RiderName, Total Deliveries, On-Time Rate) if not already present.

> "One rule, not optional: every slicer must visibly show what it is currently filtered to. A dashboard filtered to one hub with no visible sign of which hub is a dashboard that gets misread."

**Add a measure and a card for the refresh stamp:**

```dax
Last Refreshed = "Data as at " & FORMAT ( MAX ( dates[DateKey] ), "dd MMM yyyy" )
```

> "A failed refresh is invisible by default - the dashboard keeps showing old data with total confidence. This one card is the cheapest professional insurance in the whole topic."

---

### Part 5 - Publish, or Export (5 min)

*(Deliver whichever half of this section is actually true for the room.)*

**If Pro licence available:** demonstrate File, Publish, select a workspace, then open the published report in a browser and show the link.

> "Adaeze opens this herself, at this link, without needing Power BI Desktop or your file."

**If no Pro licence:** demonstrate Publish reaching only "My workspace," then demonstrate File, Export, PDF.

> "I am not going to pretend to a live share-link demo I cannot actually perform. What I can show you is the real deliverable for this room: export to PDF. It will not refresh itself, but it is honest and it is exactly what you will submit."

---

## Final State of the Dashboard

| Element | Expected content |
|---|---|
| Four KPI cards | On-Time Rate 82.0% (target 90%), Total Deliveries 41,280, Total Revenue ₦247,680,000, Late Deliveries 7,430 |
| Ranked route chart | Axis on RouteID, 24 bars, sorted descending, IKJ-02 top at 94.2%, LAG-07 bottom at 61.4%, SLA line at 90% |
| Slicer | Hub, tile style, visibly shows current selection |
| Detail table | RiderName, Total Deliveries, On-Time Rate |
| Refresh stamp | Visible Last Refreshed card |

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| The route chart shows routes in alphabetical order, not ranked | "Check the visual's sort setting via the ellipsis menu - it must be set to sort by On-Time Rate, not by RouteID." |
| The route chart shows 22 bars instead of 24, and the worst bar reads 69.9% rather than 61.4% | "RouteName has been used on the axis instead of RouteID. Two pairs of routes share a name, so two bars have merged and LAG-07's 61.4% has been averaged away. Swap the axis field to RouteID and put RouteName in Tooltips." |
| Clicking the Hub slicer does not change the rider table | "Confirm the relationship between riders and swiftroute_deliveries is active and its cross-filter direction is Single, from Topic 7.2." |
| The refresh stamp shows a date far in the past | "That is actually correct behaviour if the underlying data has not been refreshed - it is the measure doing its job. Refresh the model and the card should update." |
| Publish button is greyed out or fails silently | "Confirm sign-in status in the top right of Power BI Desktop, and confirm whether this account has a Pro licence before assuming it is a bug." |

---

## Up Next

Topic 7.5 - AI-Augmented BI. Everything built in this module so far, you wrote and verified yourself. In the next topic, an AI assistant hands you four DAX measures, two of which are wrong, and the job changes from writing to judging.
