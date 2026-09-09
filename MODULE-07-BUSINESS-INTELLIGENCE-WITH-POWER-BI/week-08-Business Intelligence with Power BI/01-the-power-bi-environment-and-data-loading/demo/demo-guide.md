# Demo Guide - The Power BI Environment and Data Loading
**Module 7, Topic 7.1 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Navigating the four Power BI Desktop views (Report, Table, Model, Power Query editor) and knowing what each is for
- Choosing Transform data over Load, and explaining why
- Promoting headers and setting explicit data types, including why an ID column must be Text, not a number
- Trimming whitespace on key columns before it can silently break a relationship
- Writing a filter as a rule ("remove rows where CustomerID is blank") rather than an edit ("delete rows 41,281 to 41,283")
- Reading the Applied Steps pane as a reorderable, auditable record of every transformation

---

## Setup - Before the Demo Starts

1. Power BI Desktop installed and open, on a machine with regional settings known in advance (see instructor note below)
2. `swiftroute_deliveries_raw.csv` available locally, unopened - this is the deliberately imperfect version of the file, 41,283 rows, carrying three test rows with a blank CustomerID
3. `7.1_fallback_loaded.pbix` open in a second window or on a second machine, in case a live step fails
4. Trainees have the four other clean SwiftRoute files (`riders.csv`, `routes.csv`, `customers_business.csv`, `dates.csv`) available but not yet opened

> **Instructor note:** the raw file's row count is 41,283, not the 41,280 quoted throughout the rest of this module. The extra three rows (`D-TEST01`, `D-TEST02`, `D-TEST03`) have a blank CustomerID and exist specifically to be filtered out in Part 4 of this demo. If a trainee's row count already reads 41,280 before that step, they have opened the clean file by mistake.

### Before this demo, the first time: installing Power BI and knowing the two windows

This demo is itself the build, from nothing to a loaded, cleaned table, so there is no separate `.pbix` to construct in advance. Two things do need doing once, before the room:

1. **Install Power BI Desktop**, free, from the Microsoft Store (search "Power BI Desktop") or powerbi.microsoft.com/desktop. Windows only.
2. **Know the two-window trap before you demonstrate it.** Power BI Desktop is the main window, with three view icons down the far left edge (Report, Table, Model). The Power Query Editor is a *separate window* that opens only when Transform data is clicked - it has its own ribbon and its own taskbar entry. When you "lose" Power BI mid-demo, it is almost always this, hidden behind the other window, not a crash.

---

## Demo Steps

### Part 1 - Four Views, One File (5 min)

> "Before we load anything, I want you to know where you are. Four things, and I am going to click each one, tell you what it is for, then click away. We are not learning any of these properly yet."

Click through, in order:
- **Report view** - the default. Blank canvas, charts go here.
- **Table view** - one table at a time, as rows and columns, exactly like a spreadsheet. This is where you come back to when a number looks wrong.
- **Model view** - boxes and lines. The whole of Topic 7.2.
- **Home ribbon, Transform data** - watch the screen.

> "Separate window, not a tab. If you lose Power BI during the lab, check your taskbar before you put your hand up."

---

### Part 2 - Get Data and the Load-versus-Transform Decision (5 min)

**Home ribbon, Get data, Text/CSV. Point at `swiftroute_deliveries_raw.csv`.**

> "This shows a preview with two buttons, Load and Transform data. Load takes the file exactly as Power BI has guessed it. Power BI is quite good at guessing, and that is the problem - it infers types from the first couple of hundred rows, so a fault further down the file gets missed at the moment it matters most."

**Click Transform data.**

> "Nothing is committed yet. I am choosing Transform data not because I already know this file is dirty, but because I have not yet looked at the column types."

---

### Part 3 - Promote Headers and Set Data Types (8 min)

**In the Power Query editor, check the column headers row.**

> "Nine columns: DeliveryID, DateKey, RiderID, RouteID, CustomerID, PromisedMinutes, ActualMinutes, DeliveryFee, Status. If these had come in as Column1, Column2, the header row was not promoted - Home, Use First Row as Headers fixes it."

**Set each column's type, narrating the choice for each:**

- `DateKey` to **Date**
- `RiderID`, `RouteID`, `CustomerID`, `DeliveryID` to **Text**
- `PromisedMinutes`, `ActualMinutes` to **Whole Number**
- `DeliveryFee` to **Fixed decimal number**
- `Status` to **Text**

> "RiderID to Text, not Whole Number. Here is the test: does arithmetic on this column mean anything? Rider fourteen plus rider twenty-two is not rider thirty-six. Type it as a number and Power BI will auto-sum it the moment it lands in a visual, and leading zeros disappear silently."

**Ask students:** "What would happen to a rider ID of `007` if this column were typed as a number instead of text?"

> "It becomes `7`. If your other table kept it as text, that relationship now fails on every rider whose ID had a leading zero, and nothing tells you why."

---

### Part 4 - Trim Whitespace and Filter as a Rule, Not an Edit (10 min)

**Select `RiderID` and `RouteID`. Transform, Format, Trim.**

> "A trailing space is invisible on screen and fatal to a relationship, because `R-014` with a space and `R-014` without one are different strings as far as the computer is concerned. Nothing turns red. The join just produces blanks."

**Home, Reduce Rows, Remove Rows, Remove Blank Rows - then, more precisely, use a filter on CustomerID:**

Filter `CustomerID` to remove blanks.

> "Watch what I typed as the condition: remove rows where CustomerID is blank. That is a rule. It is true of any file with this shape. Compare that with 'delete rows 41,281 to 41,283', which is a fact about this one file and will not fail next month, it will just quietly delete three different, innocent rows."

**Check the row count in the status bar: should now read 41,280.**

> "Three rows gone, and the count matches exactly what we expect."

---

### Part 5 - Read the Applied Steps Pane (5 min)

**Point at the right-hand pane.**

> "Source. Promoted Headers. Changed Type. Trimmed Text. Filtered Rows. Every single thing we just did is recorded, in order, with a name. I can click any one of these and see the table exactly as it stood at that moment."

**Demonstrate the deliberate mistake:** drag the Filtered Rows step to a position above Changed Type, show it behaving oddly, then drag it back.

> "That is why the steps being reorderable matters. I got the order wrong just now, and it cost me one drag to fix, not a rebuild."

**Home, Close & Apply.**

---

## Final State of the Query

At the end of this demo, `swiftroute_deliveries` should show:

| Check | Expected value |
|---|---|
| Row count | 41,280 |
| Column count | 9 |
| RiderID, RouteID, CustomerID, DeliveryID type | Text (ABC icon) |
| DateKey type | Date |
| DeliveryFee type | Fixed decimal number |
| Applied Steps | Source, Promoted Headers, Changed Type, Trimmed Text, Filtered Rows |

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Row count reads 41,283, not 41,280 | "That means the blank-CustomerID filter in Part 4 either wasn't applied, or was applied to the wrong column. Check the Applied Steps pane for a Filtered Rows step." |
| RiderID still shows a number icon after setting the type | "A later step may have reverted it. Click through the Applied Steps pane from the top and find where the type changes back." |
| Row count reads 41,280 from the very start of the demo | "You have opened the clean file, not the raw one. Close it and re-open `swiftroute_deliveries_raw.csv` specifically." |
| Trim did nothing visible | "Trim is invisible by design, it only removes leading and trailing spaces, which do not show on screen anyway. Confirm it ran by checking the Applied Steps pane for a Trimmed Text step, not by looking at the data." |

---

## Up Next

Topic 7.2 - Data Modelling and Relationships. You now have five loaded, cleaned tables sitting next to each other with nothing connecting them, and in the next topic you will find out exactly what goes wrong when somebody joins them the obvious way instead of the right way.
