# Demo Guide - Machine Learning Concepts for Literacy
**Module 8, Topic 8.3 | Estimated duration: 35-40 minutes**

---

## What This Demo Teaches

- Explaining supervised learning as the difference between having the right answers and not
- Telling classification and regression apart by looking at what is being predicted
- Recognising clustering as the case where nobody supplies the groups
- Matching each of the three to a real SwiftRoute business question
- Stating where an analyst's job ends and a data scientist's begins, without apology
- Seeing two ways a clustering result misleads, on real data, before trusting one

---

## Setup - Before the Demo Starts

1. `swiftroute_q3_cleaned.xlsx` in this folder, carried forward from Topic 8.1
2. `customer_grouping.py` in this folder, run once before the session so the output is warm
3. `customer_groups.png` and `customer_groups.xlsx` pre-built as the fallback
4. Six business questions written on cards, three of which are in Part 2 below

> **Instructor note:** say in the first thirty seconds that nobody builds a model today and there is no coding exercise. Trainees who hear "machine learning" and expect to be assessed on building something will not listen properly until you have taken that away.

> **Instructor note:** the clustering in Part 4 is a demonstration you run, not a task they run. The outcome is that a trainee can say what clustering does and where it goes wrong, not that they can call scikit-learn.

---

## Demo Steps

### Part 1 - Supervised Means Somebody Already Knew (7 min)

> "One idea, and everything else today hangs off it. Supervised learning means you have a pile of examples where somebody already knows the right answer, and the machine learns the pattern that connects the inputs to that answer."

**Point at the cleaned deliveries table.**

> "Three thousand six hundred deliveries, and for three thousand four hundred and eighty-five of them we know how they ended: Delivered, Failed, Returned, In Transit. That column is the right answer. It is what makes this supervised."

**Ask students:** "So what makes something unsupervised?"

> "Nobody tells it the answer, because there isn't one written down. We come back to that in Part 4."

---

### Part 2 - Classification or Regression, Decided by One Question (10 min)

> "Both are supervised. The only thing that separates them is what you are predicting. Category, or number. That is the whole distinction."

**Put three real SwiftRoute questions on screen and take the room's verdict on each before giving yours.**

| Question | Which is it | Why |
|---|---|---|
| Will this delivery fail? | Classification | The answer is one of a fixed set: Delivered, Failed, Returned, In Transit |
| How many minutes will this delivery take? | Regression | The answer is a number on a scale, and 47 is meaningfully close to 45 |
| How much will we bill this customer next quarter? | Regression | A number again, in naira |

> "Here is the test that never fails you. Ask whether the answers can be meaningfully ranked or subtracted. Forty-seven minutes minus forty-five minutes is two minutes, and it means something. Delivered minus Returned is nothing at all."

**Ask students:** "Predicting which of our fourteen routes a new delivery will be assigned to. Classification or regression?"

> "Classification, and it catches people, because route codes look numeric. LAG-07 minus LAG-01 is not six of anything."

---

### Part 3 - Where Your Job Ends (6 min)

> "You have now met three of the words. Here is the sentence I want you to be able to say in an interview, without embarrassment."

> "I know what a model does, I can tell you whether a business problem is classification, regression or clustering, I can read what someone else's model outputs and tell you whether the claim is supportable, and I know when to call a data scientist. I do not build models, and that is a scope decision, not a gap."

> "That answer is stronger than a half-built model you cannot defend, and hiring managers know the difference."

**Draw the line concretely:**

| Yours | Theirs |
|---|---|
| Describing what happened, and why | Building and tuning a predictive model |
| Framing the question so it is answerable | Choosing an algorithm and validating it |
| Judging whether the output is plausible | Owning the model in production |
| Communicating it to a decision maker | Monitoring it for drift |

---

### Part 4 - Clustering, and Two Ways It Lies (12 min)

**Run `customer_grouping.py` and show the three groups it finds among 1,193 customers.**

| Group | Customers | Mean deliveries | Mean fee | Mean distance |
|---|---|---|---|---|
| Frequent customers | 419 | 4.6 | ₦3,399 | 23 km |
| Occasional, short hops | 416 | 2.2 | ₦2,458 | 15 km |
| Occasional, long hauls | 358 | 2.2 | ₦4,444 | 32 km |

> "Nobody labelled these. There is no customer type column anywhere in the file. The algorithm was handed three numbers per customer and asked to find groups, and it found those. That is unsupervised: no right answers were supplied."

> "Look at the second and third rows. Same ordering frequency, both about two point two. What separates them is distance, and therefore cost. That is a real commercial distinction that nobody at SwiftRoute wrote down."

**Now the first way it lies. Re-run without putting the columns on the same scale.**

> "Fee runs into the thousands. Delivery count runs from one to twelve. Leave them on their own scales and the distance between two customers is basically the difference in fee, so the algorithm is grouping on price alone while looking like it considered everything. Only seventy-four per cent of customers land in a matching group. Nothing warns you."

**Now the second. Ask it for five groups instead of three.**

> "Equally convincing. Different answer. The number of groups is a decision you make and have to defend, not something the data hands you. If somebody shows you a clustering result and cannot tell you why that many groups, you have not been shown a finding."

**Ask students:** "Which of the three groups should SwiftRoute discount to win more volume?"

> "That question cannot be answered by the clustering. The clustering describes. Deciding what to do about it is your job, and it needs the cost side, which is exactly where Topic 8.5 is going."

---

## Common Student Issues During This Demo

| Issue | What to say |
|-------|-------------|
| A trainee calls the route prediction regression | "Ask them what LAG-07 minus LAG-01 equals. Codes that look numeric are still categories." |
| A trainee thinks clustering found the truth | "Show them the five-group run. Same data, same method, different answer. It found a grouping, not the grouping." |
| A trainee wants to build a model in the lab | "Not this module. The outcome is that you can hold your own in the conversation and know when to call someone. Building comes later, if that is the career you choose." |
| Confusion about why scaling matters | "Put the two columns side by side on the board. Fee 2,458 against deliveries 2.2. Ask which one dominates a distance calculation." |
| A trainee treats the group labels as official | "I named those groups on the way past by reading their averages. The algorithm produced group 0, 1 and 2. Naming is interpretation, and it is yours to defend." |

---

## Up Next

Topic 8.4 - Automating Repetitive Analyst Tasks. Everything in Module 8 so far has been done once. The next topic is about the parts of your week you should never do twice by hand.
