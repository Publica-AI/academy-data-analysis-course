# Demo Guide - AI-Assisted Coding
**Module 5, Topic 5.4 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Write a strong prompt that gives an AI assistant the context it needs to generate correct pandas code
- Ask an AI assistant to explain a piece of code, then verify that explanation independently
- Debug an AI-generated error by pasting the full error message and code back to the assistant
- Catch an AI-generated result that runs without error but is logically wrong
- Explain a piece of AI-assisted code line by line, without help, before it is considered ready to submit

---

## Setup - Before the Demo Starts

1. Continuing in the same notebook as Topics 5.1-5.3, with `df` carrying `Profit_check`, `Sales_Tier` and `Margin_%` already built and verified.
2. An AI assistant (Claude, ChatGPT or Gemini) open in a separate browser tab, ready to receive live prompts.
3. Trainees have completed Topic 5.3: filtering, sorting, grouping, aggregating and calculated columns, including the `Margin_%` column this demo builds on directly.

> **Instructor note:** the AI responses shown in this guide are realistic examples of what an assistant is likely to produce, verified to be accurate outputs when the code is actually run. They are not a guaranteed verbatim transcript, the exact wording an AI gives you live will differ each time you run it. Prompt the assistant live rather than reading these boxes aloud, then compare what comes back against the pattern shown here.

---

## Demo Steps

### Part 1 - Writing a Strong Prompt (8 min)

> "We already have Margin_% sitting in df from last topic. Let's ask an AI assistant to take it one step further, and give it enough to work with the first time."

**Prompt:**

> "I have a pandas DataFrame called df with a column Margin_% that is already calculated as Profit divided by Sales times 100. Write code to show the average Margin_% for each Region, sorted from highest to lowest."

**A representative AI answer:**

```python
df.groupby("Region")["Margin_%"].mean().sort_values(ascending=False)
```

> "Before running anything, check it: does it use real column names, Region and Margin_%, yes. Does the logic match the question, group then average then sort, yes. Now let's run it."

Output:
```text
Region
North Central    15.0
North West       15.0
South West       15.0
Name: Margin_%, dtype: float64
```

> "Every region again at exactly 15.0%, which is exactly what we already found by hand last topic. A strong prompt, dataset structure, column names, the exact question, got this right on the first attempt."

### Part 2 - Ask AI to Explain the Code (6 min)

> "Let's ask the same assistant to explain what it just gave us, as if we'd never seen it before."

**Prompt:**

> "Explain this pandas code line by line, as if I am a beginner data analyst."

**A representative explanation:**

> "groupby('Region') groups every row by its Region value. ['Margin_%'].mean() then calculates the average Margin_% within each group. sort_values(ascending=False) puts the highest average margin first."

> "That explanation is AI output too, so it still needs checking, not trusting outright. Does it match what we already know this code does? Yes. That agreement is the verification, not the confidence of the explanation itself."

### Part 3 - Debugging with AI Assistance (9 min)

> "Now Optimum's manager wants transactions sorted by Cost, highest first. Watch what happens when an AI assistant reaches for a method that used to exist."

```python
df.sort("Cost", ascending=False)
```

Output:
```text
AttributeError: 'DataFrame' object has no attribute 'sort'
```

**Prompt sent back to the AI:**

> "I'm getting this error: AttributeError: 'DataFrame' object has no attribute 'sort'. Here's my code: df.sort(\"Cost\", ascending=False). I'm trying to sort my DataFrame by Cost, highest first. What's wrong?"

**AI's correction:**

> "sort() was removed from pandas years ago. Use sort_values() instead: df.sort_values(\"Cost\", ascending=False)."

```python
df.sort_values("Cost", ascending=False)[["Branch", "Product", "Cost"]].head(3)
```

Output:
```text
Branch         Product   Cost
 Lagos       Rice 50kg 174250
  Kano       Rice 50kg 151300
  Kano Beverages Crate 141950
```

> "Fixed and verified, Lagos's big Rice 50kg order carries the highest cost this month. Notice what made this fixable: the full error message and the exact code were both pasted back. 'It doesn't work' alone would have given the assistant nothing to diagnose."

### Part 4 - Catching a Silent AI Mistake (8 min)

> "Now the dangerous kind. Let's ask for the overall average margin across every transaction, not by region this time."

**Prompt:**

> "What is the average profit margin across all transactions in df?"

**A representative, plausible, wrong AI answer:**

```python
avg_margin = df["Margin_%"].sum()
print(avg_margin)
```

Output:
```text
300.0
```

> "No error, no traceback, this ran perfectly, and it is wrong. We already know from Part 1 that every region sits at 15.0%, so the overall figure has to be 15.0% too, not 300%. sum() added every row's margin instead of averaging them. This is the checklist question from earlier in this module doing exactly its job: does the output make sense?"

```python
avg_margin = df["Margin_%"].mean()
print(avg_margin)
```

Output:
```text
15.0
```

> "Fixed, and it matches what we already knew before we ever asked the question. That's what verification looks like in practice, not a feeling, a number we could predict in advance."

### Part 5 - Explain It Back: Before You Submit (7 min)

> "One rule closes this topic, and it applies to every line built this session, not just the last one: if you cannot explain the code, you cannot submit the code."

**Ask students:** "Pick any one line from today's notebook, Part 1 through Part 4. Could you explain it to the person next to you right now, without looking it up?"

> "Pair up. One of you explains a line out loud, the other asks a question about anything that isn't clear, then swap to a different line. Any line neither of you can explain gets investigated before it goes anywhere near a submission, no matter how correct the number looked."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| Trainee accepts an AI explanation without checking it against the actual code or output | "An explanation is a draft, not a verdict. Ask them: does this match what you already expected the code to do? If they don't know, that's the real gap, not the explanation itself." |
| Trainee reports "it doesn't work" instead of pasting the error and code back to the AI | "Show them Part 3 again: the fix only happened because the full error message and the exact code were both given to the assistant. Vague reports get vague answers." |
| Trainee assumes code that ran without an error must be correct | "Point back to Part 4. Nothing in Python stops sum() from running when mean() was needed. Running without an error only proves the syntax was valid, nothing about the logic." |

---

## Up Next

This is the last topic in Module 5. Trainees carry this same verified, AI-checked notebook into Module 6, Data Storytelling and Visualisation, where the numbers built here become charts and a written insight narrative.
