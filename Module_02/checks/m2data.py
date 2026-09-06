# -*- coding: utf-8 -*-
"""Shared data preparation for the Module 2 solution workbooks.

Produces two frames:
  raw   : the 1,025-row export exactly as issued, faults intact
  clean : the 1,000-row result of the cleaning pass the labs teach, with the nine
          blank Ratings LEFT BLANK (which is what a trainee following the lab produces,
          and why COUNTIF(Rating,">=7") reads 496 rather than the answer key's 501)
"""
import datetime as _dt
import os
import re

import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
DATA = None  # set by resolve()

COLS = ['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender', 'Product line',
        'Unit price', 'Quantity', 'Tax 5%', 'Sales', 'Date', 'Time', 'Payment',
        'cogs', 'gross margin percentage', 'gross income', 'Rating']

DDMM = re.compile(r'^(\d{2})-(\d{2})-(\d{4})$')


def resolve(module_dir):
    global DATA
    DATA = os.path.join(module_dir, 'Datasets')
    return DATA


def load_raw(module_dir):
    """The raw export, every value as it appears in the CSV. Dates stay strings."""
    p = os.path.join(module_dir, 'Datasets', 'Ilesanmi_Sales_Raw_Export.csv')
    raw = pd.read_csv(p, dtype={'Invoice ID': str, 'Date': str, 'Time': str})
    assert len(raw) == 1025, len(raw)
    assert list(raw.columns) == COLS, raw.columns
    return raw


def date_is_text(v):
    """True for the 51 DD-MM-YYYY values, which Excel leaves as left-aligned text."""
    return bool(DDMM.match(str(v)))


def to_datetime(v):
    """M/D/YYYY -> real date; DD-MM-YYYY -> real date read day-first."""
    s = str(v)
    m = DDMM.match(s)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return _dt.datetime(y, mo, d)
    mo, d, y = [int(x) for x in s.split('/')]
    return _dt.datetime(y, mo, d)


def build_clean(raw):
    """Apply the five repairs exactly as the labs teach them."""
    df = raw.copy()

    # 1. duplicates: Invoice ID only, keeping the first occurrence
    df = df.drop_duplicates(subset=['Invoice ID'], keep='first').reset_index(drop=True)

    # 2. Product line: TRIM then PROPER
    df['Product line'] = df['Product line'].str.strip().str.title()

    # 3. Dates: re-parse both formats to true dates
    df['Date'] = df['Date'].map(to_datetime)

    # 4. sign-flipped quantities: recover from cogs / Unit price
    neg = df['Quantity'] < 0
    recovered = (df.loc[neg, 'cogs'] / df.loc[neg, 'Unit price']).round(0)
    assert ((df.loc[neg, 'cogs'] / df.loc[neg, 'Unit price']) % 1 == 0).all()
    df.loc[neg, 'Quantity'] = recovered.astype(int)
    df['Quantity'] = df['Quantity'].astype(int)

    # 5. blank Ratings: LEFT BLANK, deliberately
    return df


def facts(raw, clean):
    money = lambda x: round(float(x), 2)
    f = {
        'raw_rows': len(raw),
        'clean_rows': len(clean),
        'clean_sales': money(clean['Sales'].sum()),
        'clean_qty': int(clean['Quantity'].sum()),
        'clean_cogs': money(clean['cogs'].sum()),
        'clean_tax': money(clean['Tax 5%'].sum()),
        'raw_sales': money(raw['Sales'].sum()),
        'raw_cogs': money(raw['cogs'].sum()),
        'raw_tax': money(raw['Tax 5%'].sum()),
        'raw_subtotal': money((raw['Unit price'] * raw['Quantity']).sum()),
        'blank_ratings_clean': int(clean['Rating'].isna().sum()),
        'rated7_clean_blanks_left': int((clean['Rating'] >= 7).sum()),
        'rated7_raw': int((raw['Rating'] >= 7).sum()),
        'text_dates_raw': int(raw['Date'].map(date_is_text).sum()),
        'distinct_pl_clean': int(clean['Product line'].nunique()),
        'neg_qty_clean': int((clean['Quantity'] < 0).sum()),
        'dupe_ids_clean': int(clean['Invoice ID'].duplicated().sum()),
    }
    f['raw_diff'] = money(f['raw_cogs'] - f['raw_subtotal'])
    for b in ('Ikeja', 'Wuse', 'Trans-Amadi'):
        f['clean_' + b] = money(clean.loc[clean.Branch == b, 'Sales'].sum())
        f['raw_' + b] = money(raw.loc[raw.Branch == b, 'Sales'].sum())
        f['cleanN_' + b] = int((clean.Branch == b).sum())
        f['rawN_' + b] = int((raw.Branch == b).sum())
    return f


if __name__ == '__main__':
    md = os.path.abspath(os.path.join(ROOT, '..', '..', '..', '..', '..'))
    md = os.environ.get('M2DIR', 'Module_02')
    raw = load_raw(md)
    clean = build_clean(raw)
    key = pd.read_excel(os.path.join(md, 'Datasets', 'Ilesanmi_Sales_Clean_AnswerKey.xlsx'),
                        sheet_name='Clean Data')

    print("clean rows:", len(clean))
    f = facts(raw, clean)
    for k, v in sorted(f.items()):
        print(f"  {k:28} {v}")

    # does our cleaned frame agree with the instructor answer key?
    a = clean.sort_values('Invoice ID').reset_index(drop=True)
    b = key.sort_values('Invoice ID').reset_index(drop=True)
    print("\nagreement with answer key:")
    print("  same Invoice IDs :", list(a['Invoice ID']) == list(b['Invoice ID']))
    for c in ['Sales', 'Quantity', 'cogs', 'Tax 5%', 'Unit price']:
        print(f"  {c:16} identical:", bool((a[c].round(2) == b[c].round(2)).all()))
    print("  Date identical   :", bool((pd.to_datetime(a['Date']) == pd.to_datetime(b['Date'])).all()))
    print("  Product line (case-insensitive):",
          bool((a['Product line'].str.lower() == b['Product line'].str.lower()).all()))
    print("  Rating: ours blank where key filled:",
          int(a['Rating'].isna().sum()), "blanks vs key", int(b['Rating'].isna().sum()))
    both = a['Rating'].notna()
    print("  Rating identical where both present:", bool((a.loc[both, 'Rating'] == b.loc[both, 'Rating']).all()))
