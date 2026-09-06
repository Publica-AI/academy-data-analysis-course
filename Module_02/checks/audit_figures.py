# -*- coding: utf-8 -*-
"""Every Naira figure appearing anywhere in Module 2 must be derivable from the datasets.

This is the strongest guard in the module: a fabricated or mistyped money figure cannot survive it,
because the allowed set is computed from the data rather than transcribed.

Run from the repository root:  python Module_02/checks/audit_figures.py
"""
import itertools
import os
import pathlib
import re
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2data

M2 = pathlib.Path(os.environ.get('M2DIR', 'Module_02'))
raw = m2data.load_raw(str(M2))
clean = m2data.build_clean(raw)

money = lambda x: '₦{:,.2f}'.format(round(float(x), 2))
allowed = {}


def allow(value, why):
    allowed.setdefault(money(value), why)


# ---- headline totals, both files
allow(clean['Sales'].sum(), 'cleaned chain Sales')
allow(raw['Sales'].sum(), 'raw chain Sales')
allow(clean['cogs'].sum(), 'cleaned cogs')
allow(raw['cogs'].sum(), 'raw cogs')
allow(clean['Tax 5%'].sum(), 'cleaned tax')
allow(raw['Tax 5%'].sum(), 'raw tax')
allow((raw['Unit price'] * raw['Quantity']).sum(), 'raw Subtotal (Unit price x Quantity)')
allow(((raw['Unit price'] * raw['Quantity']) * 0.05).sum(), 'raw Tax Check')
allow(raw['cogs'].sum() - (raw['Unit price'] * raw['Quantity']).sum(), 'Subtotal gap')
allow(raw['Tax 5%'].sum() - ((raw['Unit price'] * raw['Quantity']) * 0.05).sum(), 'Tax Check gap')
allow(raw['Sales'].mean(), 'raw average Sales')
allow(clean['Sales'].mean(), 'cleaned average Sales')

# ---- the 1,006-row whole-row deduplication
d6 = raw.drop_duplicates()
allow(d6['Sales'].sum(), '1,006-row chain Sales')
for b in ('Ikeja', 'Wuse', 'Trans-Amadi'):
    allow(d6.loc[d6.Branch == b, 'Sales'].sum(), f'1,006-row {b}')

# ---- branch, product line, customer type, payment, month, and every crossing of them
for df, tag in ((clean, 'cleaned'), (raw, 'raw')):
    for b in df['Branch'].unique():
        allow(df.loc[df.Branch == b, 'Sales'].sum(), f'{tag} {b}')
    pl = df['Product line'].str.strip().str.title()
    for v in pl.unique():
        allow(df.loc[pl == v, 'Sales'].sum(), f'{tag} product line {v}')
    for ct in df['Customer type'].unique():
        allow(df.loc[df['Customer type'] == ct, 'Sales'].sum(), f'{tag} {ct}')
    for b, v in itertools.product(df['Branch'].unique(), pl.unique()):
        allow(df.loc[(df.Branch == b) & (pl == v), 'Sales'].sum(), f'{tag} {b} x {v}')
    for b, ct in itertools.product(df['Branch'].unique(), df['Customer type'].unique()):
        allow(df.loc[(df.Branch == b) & (df['Customer type'] == ct), 'Sales'].sum(),
              f'{tag} {b} x {ct}')

# monthly, cleaned
cd = pd.to_datetime(clean['Date'])
for m in cd.dt.month.unique():
    allow(clean.loc[cd.dt.month == m, 'Sales'].sum(), f'cleaned month {m}')

# ---- branch differences, which the guides quote
cb = clean.groupby('Branch')['Sales'].sum()
rb = raw.groupby('Branch')['Sales'].sum()
for a, b in itertools.permutations(['Ikeja', 'Wuse', 'Trans-Amadi'], 2):
    allow(abs(cb[a] - cb[b]), f'cleaned {a} minus {b}')
    allow(abs(rb[a] - rb[b]), f'raw {a} minus {b}')

# ---- product line spread
pl_tot = clean.groupby(clean['Product line'].str.strip().str.title())['Sales'].sum()
allow(pl_tot.max() - pl_tot.min(), 'product line spread')

# ---- the five sign-flipped rows: unit price, cogs, and their doubles
neg = raw[raw.Quantity < 0]
for _, r in neg.iterrows():
    allow(r['Unit price'], f"unit price {r['Invoice ID']}")
    allow(r['cogs'], f"cogs {r['Invoice ID']}")
    allow(-r['Unit price'] * r['Quantity'], f"|subtotal| {r['Invoice ID']}")

# ---- the sample invoices the guides walk through
for inv in ('750-67-8428', '351-62-0822', '263-10-3913'):
    row = raw[raw['Invoice ID'] == inv].iloc[0]
    for col in ('Unit price', 'cogs', 'Tax 5%', 'Sales'):
        allow(row[col], f'{inv} {col}')

# ---- Wuse Health and beauty, exact and wildcard criteria (Topic 2.2 Tier 3)
plr = raw['Product line']
for label, mask in (
    ('exact', (plr.str.lower() == 'health and beauty') & (raw.Branch == 'Wuse')),
    ('wildcard', plr.str.lower().str.startswith('health and beauty') & (raw.Branch == 'Wuse')),
):
    allow(raw.loc[mask, 'Sales'].sum(), f'Wuse Health and beauty {label}')

# ---- the Unit price range quoted in the dataset dictionary
allow(raw['Unit price'].min(), 'minimum Unit price')
allow(raw['Unit price'].max(), 'maximum Unit price')

# ---- zero, which appears as a reconciliation target
allow(0, 'reconciliation target')

# ================================================================== scan
FIG = re.compile(r'₦\s?[\d,]+\.\d{2}')
bad, scanned = [], 0
for p in sorted(M2.rglob('*')):
    if p.suffix.lower() not in {'.md', '.csv', '.json'} or not p.is_file():
        continue
    scanned += 1
    txt = p.read_text(encoding='utf-8')
    for m in FIG.finditer(txt):
        fig = m.group(0).replace('₦ ', '₦')
        if fig not in allowed:
            line = txt[:m.start()].count('\n') + 1
            bad.append(f'{p}:{line}  {fig}')

print(f'allowed figures derived from the data: {len(allowed)}')
print(f'files scanned: {scanned}')
if bad:
    print(f'\nUNDERIVABLE FIGURES ({len(bad)}):')
    for b in sorted(set(bad)):
        print('  -', b)
    sys.exit(1)
print('EVERY NAIRA FIGURE IN MODULE 2 IS DERIVABLE FROM THE DATASETS')
