# -*- coding: utf-8 -*-
"""Verify Module 2 by execution: every figure, every MCQ structural rule, every prose rule.

Run from inside Module_02/.  Exits non-zero on any failure.
"""
import csv
import json
import pathlib
import re
import sys

import pandas as pd

fails, passes = [], [0]


def check(label, cond, detail=""):
    if cond:
        passes[0] += 1
    else:
        fails.append(f"{label}: {detail}")


RAW = 'Datasets/Ilesanmi_Sales_Raw_Export.csv'
KEY = 'Datasets/Ilesanmi_Sales_Clean_AnswerKey.xlsx'
raw = pd.read_csv(RAW)
clean = pd.read_excel(KEY, sheet_name='Clean Data')

# ---------------------------------------------------------------- 1. figures
money = lambda x: f"₦{x:,.2f}"
num = lambda x: f"{x:,}"

facts = {}
cb = clean.groupby('Branch')['Sales'].sum()
rb = raw.groupby('Branch')['Sales'].sum()
facts['Ikeja clean'] = money(cb['Ikeja'])
facts['Wuse clean'] = money(cb['Wuse'])
facts['Trans-Amadi clean'] = money(cb['Trans-Amadi'])
facts['chain clean'] = money(clean['Sales'].sum())
facts['Ikeja raw'] = money(rb['Ikeja'])
facts['Wuse raw'] = money(rb['Wuse'])
facts['Trans-Amadi raw'] = money(rb['Trans-Amadi'])
facts['chain raw'] = money(raw['Sales'].sum())
pl = clean.groupby('Product line')['Sales'].sum()
for k in pl.index:
    facts[f'PL {k}'] = money(pl[k])
facts['TA x Food and beverages'] = money(
    clean[(clean.Branch == 'Trans-Amadi') & (clean['Product line'] == 'Food and beverages')]['Sales'].sum())
facts['rows raw'] = len(raw)
facts['rows clean'] = len(clean)
facts['rows all-col dedup'] = len(raw.drop_duplicates())
facts['dup invoice ids'] = int(raw['Invoice ID'].duplicated().sum())
facts['rated>=7 clean'] = int((clean.Rating >= 7).sum())
facts['rated>=7 raw'] = int((raw.Rating >= 7).sum())
facts['avg rating clean'] = round(clean.Rating.mean(), 2)
facts['total quantity'] = int(clean.Quantity.sum())
pay = clean['Payment'].value_counts()
facts['payment'] = dict(pay)
ct = clean['Customer type'].value_counts()
facts['customer type'] = dict(ct)
facts['branch counts'] = dict(clean['Branch'].value_counts())

# expected values asserted against the data itself
check("Ikeja clean", facts['Ikeja clean'] == "₦10,620,037.05", facts['Ikeja clean'])
check("Wuse clean", facts['Wuse clean'] == "₦10,619,767.20", facts['Wuse clean'])
check("Trans-Amadi clean", facts['Trans-Amadi clean'] == "₦11,056,870.65", facts['Trans-Amadi clean'])
check("chain clean", facts['chain clean'] == "₦32,296,674.90", facts['chain clean'])
check("Ikeja raw", facts['Ikeja raw'] == "₦11,062,565.85", facts['Ikeja raw'])
check("Wuse raw", facts['Wuse raw'] == "₦10,755,627.75", facts['Wuse raw'])
check("Trans-Amadi raw", facts['Trans-Amadi raw'] == "₦11,338,588.80", facts['Trans-Amadi raw'])
check("chain raw", facts['chain raw'] == "₦33,156,782.40", facts['chain raw'])
check("PL Food and beverages", facts['PL Food and beverages'] == "₦5,614,484.40", facts['PL Food and beverages'])
check("PL Sports and travel", facts['PL Sports and travel'] == "₦5,512,282.65", facts['PL Sports and travel'])
check("PL Electronic accessories", facts['PL Electronic accessories'] == "₦5,433,753.15", facts['PL Electronic accessories'])
check("PL Fashion accessories", facts['PL Fashion accessories'] == "₦5,430,589.50", facts['PL Fashion accessories'])
check("PL Home and lifestyle", facts['PL Home and lifestyle'] == "₦5,386,191.30", facts['PL Home and lifestyle'])
check("PL Health and beauty", facts['PL Health and beauty'] == "₦4,919,373.90", facts['PL Health and beauty'])
check("TA x F&B", facts['TA x Food and beverages'] == "₦2,376,685.50", facts['TA x Food and beverages'])
check("rows raw", facts['rows raw'] == 1025, facts['rows raw'])
check("rows clean", facts['rows clean'] == 1000, facts['rows clean'])
check("all-column dedup leaves 1006", facts['rows all-col dedup'] == 1006, facts['rows all-col dedup'])
check("25 duplicated invoice ids", facts['dup invoice ids'] == 25, facts['dup invoice ids'])
check("invoice-id dedup leaves 1000", len(raw.drop_duplicates(subset=['Invoice ID'])) == 1000)
check("rated>=7 clean", facts['rated>=7 clean'] == 501, facts['rated>=7 clean'])
check("rated>=7 raw", facts['rated>=7 raw'] == 508, facts['rated>=7 raw'])
check("avg rating", facts['avg rating clean'] == 6.97, facts['avg rating clean'])
check("total quantity", facts['total quantity'] == 5510, facts['total quantity'])
check("payment counts", dict(pay) == {'Ewallet': 345, 'Cash': 344, 'Credit card': 311}, dict(pay))
check("customer type", dict(ct) == {'Member': 565, 'Normal': 435}, dict(ct))
check("Trans-Amadi txn count 328", facts['branch counts']['Trans-Amadi'] == 328, facts['branch counts'])

# the 19 exact vs 6 disguised split
dupids = raw['Invoice ID'][raw['Invoice ID'].duplicated()].unique()
exact = sum(1 for i in dupids if len(raw[raw['Invoice ID'] == i].drop_duplicates()) == 1)
check("19 exact full-row copies", exact == 19, exact)
check("6 disguised copies", len(dupids) - exact == 6, len(dupids) - exact)
diff_fields = {}
for i in dupids:
    sub = raw[raw['Invoice ID'] == i]
    cols = [c for c in raw.columns if sub[c].astype(str).nunique() > 1]
    if cols:
        diff_fields[i] = cols
check("3 differ by Date", sum(1 for v in diff_fields.values() if v == ['Date']) == 3, diff_fields)
check("2 differ by Product line", sum(1 for v in diff_fields.values() if v == ['Product line']) == 2, diff_fields)
check("263-10-3913 differs by Rating", diff_fields.get('263-10-3913') == ['Rating'], diff_fields.get('263-10-3913'))

# injected fault counts
plr = raw['Product line']
check("102 ALL CAPS + trailing space", int(((plr != plr.str.strip()) & (plr.str.strip() == plr.str.strip().str.upper())).sum()) == 102)
check("51 DD-MM-YYYY dates", int(raw['Date'].astype(str).str.match(r'^\d{2}-\d{2}-\d{4}$').sum()) == 51)
check("10 blank Ratings in raw", int(raw.Rating.isna().sum()) == 10)
check("0 blank Ratings in key", int(clean.Rating.isna().sum()) == 0)

# the five sign-flipped quantities recover exactly
neg = raw[raw.Quantity < 0]
check("5 negative quantities", len(neg) == 5, len(neg))
expected_neg = {'875-31-8302': (9338.0, 9338.0, 1), '200-40-6154': (6591.0, 39546.0, 6),
                '134-75-2619': (1932.0, 13524.0, 7), '827-26-2100': (3384.0, 30456.0, 9),
                '499-27-7781': (5321.0, 42568.0, 8)}
for inv, (up, cogs, trueq) in expected_neg.items():
    r = neg[neg['Invoice ID'] == inv]
    check(f"neg {inv}", len(r) == 1 and float(r['Unit price'].iloc[0]) == up
          and float(r['cogs'].iloc[0]) == cogs and cogs / up == trueq, r.to_dict('records'))

# the 508 -> 501 arithmetic
ded = raw.drop_duplicates(subset=['Invoice ID'], keep='first')
removed = raw[~raw.index.isin(ded.index)]
check("12 removed dup rows rated >=7", int((removed.Rating >= 7).sum()) == 12, int((removed.Rating >= 7).sum()))
check("508 - 12 + 5 = 501", 508 - int((removed.Rating >= 7).sum()) + 5 == 501)

# step-order counts quoted in the Power Query guides
cl = raw.copy()
cl['Product line'] = cl['Product line'].str.strip().str.title()
check("clean casing then all-col dedup = 1004", len(cl.drop_duplicates()) == 1004, len(cl.drop_duplicates()))
cl2 = cl.copy()
cl2['Date'] = pd.to_datetime(cl2['Date'], format='mixed', errors='coerce')
mask = raw['Date'].astype(str).str.match(r'^\d{2}-\d{2}-\d{4}$')
cl2.loc[mask, 'Date'] = pd.to_datetime(raw.loc[mask, 'Date'], format='%d-%m-%Y')
check("plus dates then all-col dedup = 1001", len(cl2.drop_duplicates()) == 1001, len(cl2.drop_duplicates()))
check("invoice-id dedup after cleaning still 1000", len(cl.drop_duplicates(subset=['Invoice ID'])) == 1000)

# sample invoices quoted in the guides
s1 = raw[raw['Invoice ID'] == '750-67-8428'].iloc[0]
check("750-67-8428", (s1.Branch, s1['Product line'], float(s1['Unit price']), int(s1.Quantity),
                      float(s1.cogs), float(s1['Tax 5%']), float(s1.Sales), float(s1.Rating), s1.Date)
      == ('Ikeja', 'Health and beauty', 7469.0, 7, 52283.0, 2614.15, 54897.15, 9.1, '1/5/2019'), s1.to_dict())
s2 = raw[raw['Invoice ID'] == '351-62-0822'].iloc[0]
check("351-62-0822 is Wuse", (s2.Branch, s2['Product line'], float(s2['Unit price']), int(s2.Quantity), float(s2.Sales))
      == ('Wuse', 'Fashion accessories', 1448.0, 4, 6081.6), s2.to_dict())

# product line spread quoted in the charts items
top, bot = pl.max(), pl.min()
check("PL spread ~12 per cent of the top", 11.5 <= 100 * (top - bot) / top <= 12.9, 100 * (top - bot) / top)

# date coverage
d = pd.to_datetime(clean['Date'])
check("Jan to Mar 2019", (d.min().year, d.min().month, d.max().year, d.max().month) == (2019, 1, 2019, 3),
      (str(d.min()), str(d.max())))

# ---------------------------------------------------------------- 2. MCQ bank
bank = json.loads(pathlib.Path('MCQ/module-02-mcq.json').read_text(encoding='utf-8'))
check("every item has an explanation", all(i.get('explanation', '').strip() for i in bank))
check("every item has all fields", all(set(i) == {'title', 'description', 'type', 'question', 'options',
                                                  'answer', 'difficulty', 'explanation'} for i in bank))
for n, i in enumerate(bank, 1):
    if i['type'] == 'multiple choice':
        opts = i['options'].split('|')
        check(f"item {n} has 4 options", len(opts) == 4, opts)
        check(f"item {n} answer in options", i['answer'] in opts, i['answer'])
        check(f"item {n} options unique", len(set(opts)) == 4, opts)
    elif i['type'] == 'True or False':
        check(f"item {n} TF options", i['options'] == 'True|False', i['options'])
        check(f"item {n} TF answer", i['answer'] in ('True', 'False'), i['answer'])
    elif i['type'] == 'short answer':
        check(f"item {n} SA has no options", i['options'] == '', i['options'])
        check(f"item {n} SA has an answer", bool(i['answer'].strip()))
    else:
        check(f"item {n} type", False, i['type'])
    blob = (i['question'] + i['options'] + i['answer']).lower()
    for banned in ('all of the above', 'none of the above'):
        check(f"item {n} no '{banned}'", banned not in blob)

# every figure quoted anywhere in the bank must be one this script recomputed
allowed_money = {facts[k] for k in facts if isinstance(facts[k], str) and facts[k].startswith('₦')}
# figures recomputed above but not stored in `facts`: the sign-flipped rows' unit prices and cogs,
# and the Ikeja-minus-Wuse gap quoted in the pivot-table item.
for _inv, (_up, _cogs, _q) in expected_neg.items():
    allowed_money |= {money(_up), money(_cogs)}
allowed_money.add(money(cb['Ikeja'] - cb['Wuse']))
quoted = set()
for i in bank:
    for f in (i['question'], i['options'], i['answer'], i['explanation']):
        quoted |= set(re.findall(r'₦[\d,]+\.\d{2}', f))
check("every naira figure in the bank is a recomputed one", quoted <= allowed_money, quoted - allowed_money)

# CSV mirrors JSON exactly
with open('MCQ/module-02-mcq.csv', encoding='utf-8') as fh:
    rows = list(csv.DictReader(fh))
check("csv row count matches json", len(rows) == len(bank), (len(rows), len(bank)))
check("csv content matches json", all(dict(r) == b for r, b in zip(rows, bank)))
check("csv header", list(rows[0]) == ['title', 'description', 'type', 'question', 'options', 'answer',
                                      'difficulty', 'explanation'], list(rows[0]))

# ---------------------------------------------------------------- 3. prose
US = re.compile(r'\b(analyz\w*|organiz\w*|colou?rize\w*|summariz\w*|standardiz\w*|labeled|modeling|'
                r'behavior\w*|centered|optimiz\w*|recogniz\w*|favorit\w*|catalog|visualiz\w*)\b', re.I)
ALLOWED_US = {'PivotTable Analyze'}  # Excel ribbon tab name, correct as a UI label
OLD = re.compile(r'\b(Alex|Cairo|Giza|Yangon|Mandalay|Naypyitaw)\b')
OLDFIG = re.compile(r'106,200\.37|110,568\.71|56,144\.84|55,122\.83|106,197\.67')
OLDFILE = re.compile(r'supermarket_sales_dirty|SuperMarket_Analysis')

for p in sorted(pathlib.Path('.').rglob('*')):
    if p.suffix.lower() not in {'.md', '.csv', '.json'} or not p.is_file():
        continue
    t = p.read_text(encoding='utf-8')
    check(f"{p} no em dash", '—' not in t)
    check(f"{p} no old branch names", not OLD.search(t), OLD.findall(t)[:5])
    check(f"{p} no old figures", not OLDFIG.search(t), OLDFIG.findall(t)[:5])
    check(f"{p} no old file names", not OLDFILE.search(t), OLDFILE.findall(t)[:5])
    hits = [m.group(0) for m in US.finditer(t)
            if not any(a in t[max(0, m.start() - 12):m.end() + 4] for a in ALLOWED_US)]
    check(f"{p} British English", not hits, hits[:5])
    for m in re.finditer(r'trainee can[^.\n]*', t):
        check(f"{p} outcome verb", not re.search(r'\b(understand|know)\b', m.group(0), re.I), m.group(0)[:70])

# ---------------------------------------------------------------- report
print(f"checks passed: {passes[0]}")
if fails:
    print(f"\nFAILURES ({len(fails)}):")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")
