# Tier 1 Worked Solution, Topic 2.7

## What the two prompts should produce

**Vague** (`write me a formula for ratings`): something generic, typically `=IF(A2>=7,...)` with an
invented column reference, or a request for clarification. Whatever comes back cannot be correct for
this workbook, because nothing in the prompt identified the workbook.

**Specific** (naming `CleanSales`, the `Rating` column, the 4 to 10 range and the two bands):
something equivalent to

```
=IF([@Rating]>=7,"Satisfied","Needs Follow-up")
```

which must agree with the Topic 2.2 column on all 1,000 rows. The comparison is only possible because
that column already exists, which is the design of the whole topic.

## Step 4, the explanation test

Asking for an explanation is half the exercise. Asking what happens **if a specific input changes**,
and then changing it, is the half that catches a wrong explanation. A confident, fluent, wrong
explanation reads exactly like a correct one; a failed prediction does not.

## Step 5, the debugging test

A VLOOKUP without `FALSE` returns an approximate match with **no error**. The assistant will usually
identify the missing argument correctly, which is a genuine and useful speed-up.

What must be marked is the next step: applying the fix and testing it on real data. A trainee who
applies an AI fix untested has repeated the behaviour the topic exists to prevent, even when the fix
happened to be right.

Worth raising in the debrief: on this dataset a `#N/A` from a value that looks identical on screen is
more often a **trailing space** than a missing `FALSE`, because 102 Product line rows carry one. An
assistant that confidently diagnoses the missing argument may be diagnosing the wrong fault.

## Step 6, the verification test, and the trap

```
=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])   ->   ₦10,620,037.05
```

The assistant cannot see the file, so one of three things happens: it refuses, it hedges, or it
invents a figure. All three are informative and all three should be recorded.

**The trap to look out for.** If a figure comes back as **₦11,062,565.85**, it is not random.
That is the correct Ikeja total for the raw 1,025-row export, and it can arrive because the trainee
pasted raw data earlier in the conversation, or because the assistant reasoned from the wrong file.
An answer that is exactly right for a different file is the most convincing wrong answer in this
module, and it is worth spending real time on when it appears.

| Figure returned | What it means |
|---|---|
| ₦10,620,037.05 | Correct for the cleaned file |
| ₦11,062,565.85 | Correct for the raw 1,025-row export, wrong for this question |
| ₦10,728,703.65 | Correct for a file deduplicated with every column ticked, 1,006 rows |
| Anything else | Invented |

All three of those figures were verified by execution.

## Marking notes

- Both prompts kept, with both answers: the comparison is the content.
- The prediction in step 4 actually tested: the difference between reading an explanation and
  checking one.
- The AI's Ikeja answer recorded **whatever it was**, including a refusal. A trainee who only records
  the interactions that went well has not produced a prompt log.
