# -*- coding: utf-8 -*-
"""Build 2.1_lab_solution.xlsx and 2.2_lab_solution.xlsx with real Excel."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2data
from xlbuild import (MONEY, INT, TEXT, add_calc_column, autofit, check_row, header_row,
                     note, recalc, save, start_excel, title, write_grid, write_table)

M2 = os.environ.get('M2DIR', 'Module_02')
W = os.path.join(M2, 'weeks-02-03-excel-for-data-analysis')
T1 = os.path.join(W, '01-the-excel-environment-tables-and-referencing', 'lab', 'solutions')
T2 = os.path.join(W, '02-core-formulas-and-functions', 'lab', 'solutions')

raw = m2data.load_raw(M2)

TOP = 3  # header row of RawSales, leaving rows 1-2 for the tax rate


def raw_for_excel():
    """Raw frame with Date as mixed datetime / text, exactly as the export behaves."""
    df = raw.copy()
    df['Date'] = [m2data.to_datetime(v) if not m2data.date_is_text(v) else str(v)
                  for v in raw['Date']]
    return df


def text_date_rows():
    return [i for i, v in enumerate(raw['Date']) if m2data.date_is_text(v)]


def build_raw_sheet(ws, with_22=False):
    ws.Name = 'Raw Export'
    ws.Range("A1").Value = 'Tax rate'
    ws.Range("A1").Font.Bold = True
    ws.Range("B1").Value = 0.05
    ws.Range("B1").NumberFormat = '0.00%'
    ws.Range("D1").Value = 'The rate is typed once, here, and every row points at $B$1.'
    ws.Range("D1").Font.Italic = True

    df = raw_for_excel()
    date_col = 1 + list(df.columns).index('Date')  # 1-based, table starts at col 1
    for i in text_date_rows():
        ws.Cells(TOP + 1 + i, date_col).NumberFormat = TEXT

    lo = write_table(ws, df, 'RawSales', top=TOP, left=1,
                     text_cols=['Invoice ID', 'Time'],
                     money_cols=['Unit price', 'Tax 5%', 'Sales', 'cogs', 'gross income'],
                     int_cols=['Quantity'])

    add_calc_column(lo, 'Subtotal', '=[@[Unit price]]*[@Quantity]', MONEY)
    add_calc_column(lo, 'Tax Check', '=[@Subtotal]*$B$1', MONEY)
    add_calc_column(lo, 'Arithmetic Check', '=ROUND([@Subtotal],2)=ROUND([@cogs],2)')
    add_calc_column(lo, 'Check tax', '=ROUND([@cogs]*0.05,2)=ROUND([@[Tax 5%]],2)')
    add_calc_column(lo, 'Check sales', '=ROUND([@cogs]+[@[Tax 5%]],2)=ROUND([@Sales],2)')

    if with_22:
        add_calc_column(lo, 'Satisfaction', '=IF([@Rating]>=7,"Satisfied","Needs Follow-up")')
        add_calc_column(lo, 'Satisfaction Band',
                        '=IFS([@Rating]>=8,"Highly Satisfied",[@Rating]>=7,"Satisfied",TRUE,"Needs Follow-up")')
        add_calc_column(lo, 'Branch Code', '=LEFT([@[Invoice ID]],3)')
        add_calc_column(lo, 'Raw Length', '=LEN([@[Product line]])')
        add_calc_column(lo, 'Trimmed Length', '=LEN(TRIM([@[Product line]]))')
        add_calc_column(lo, 'Days Since', '=DATEDIF([@Date],TODAY(),"d")')
    ws.Range("A1").Select()
    return lo


# ----------------------------------------------------------------- 2.1
def build_21(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    build_raw_sheet(wb.Worksheets(1), with_22=False)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Checks'
    r = title(ws, 1, 'Topic 2.1 lab solution: checks')
    r = note(ws, r, 'Every figure below is a live formula over RawSales. Nothing here is typed by hand.')
    r += 1
    r = header_row(ws, r, ['Check', 'Live formula result', 'Expected'])
    rows = [
        ('Rows', '=COUNTA(RawSales[Invoice ID])', INT, '1,025'),
        ('Sum of Subtotal', '=SUM(RawSales[Subtotal])', MONEY, '₦31,307,024.00'),
        ('Sum of cogs', '=SUM(RawSales[cogs])', MONEY, '₦31,577,888.00'),
        ('Difference', '=SUM(RawSales[cogs])-SUM(RawSales[Subtotal])', MONEY, '₦270,864.00'),
        ('Sum of Tax Check', '=SUM(RawSales[Tax Check])', MONEY, '₦1,565,351.20'),
        ('Sum of Tax 5%', '=SUM(RawSales[Tax 5%])', MONEY, '₦1,578,894.40'),
        ('Tax Check gap (5% of the Subtotal gap)',
         '=SUM(RawSales[Tax 5%])-SUM(RawSales[Tax Check])', MONEY, '₦13,543.20'),
        ('Sum of Sales', '=SUM(RawSales[Sales])', MONEY, '₦33,156,782.40'),
        ('Rows failing the cogs check', '=COUNTIF(RawSales[Arithmetic Check],FALSE)', INT, '5'),
        ('Rows passing the cogs check', '=COUNTIF(RawSales[Arithmetic Check],TRUE)', INT, '1,020'),
        ('Rows passing the tax check', '=COUNTIF(RawSales[Check tax],TRUE)', INT, '1,025'),
        ('Rows passing the sales check', '=COUNTIF(RawSales[Check sales],TRUE)', INT, '1,025'),
    ]
    for label, f, fmt, exp in rows:
        r = check_row(ws, r, label, f, fmt, exp)
    r += 1
    r = note(ws, r, 'Tax Check is built on Subtotal, and Subtotal is negative on the five sign-flipped rows,', italic=False)
    r = note(ws, r, 'so its total is 13,543.20 short of Tax 5%. That is exactly 5% of the 270,864.00 Subtotal gap,', italic=False)
    r = note(ws, r, 'from exactly the same five rows. Row by row the two columns agree on 1,020 of the 1,025.', italic=False)
    r += 1
    r = note(ws, r, 'Test: delete the value in B1 on the Raw Export sheet and Sum of Tax Check must fall to zero.')
    r = note(ws, r, 'That is what proves the absolute reference is real rather than a hard-coded number.')
    autofit(ws)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Findings'
    r = title(ws, 1, 'Tier 2 and Tier 3 findings')
    r += 1
    r = note(ws, r, 'Tier 2: the five rows where Unit price x Quantity does not equal cogs.', italic=False)
    r = header_row(ws, r, ['Invoice ID', 'Branch', 'Unit price', 'Quantity', 'cogs', 'Subtotal'])
    neg = raw[raw.Quantity < 0]
    body = [[x['Invoice ID'], x['Branch'], x['Unit price'], int(x['Quantity']), x['cogs'],
             x['Unit price'] * x['Quantity']] for _, x in neg.iterrows()]
    write_grid(ws, r, 1, body)
    ws.Range(ws.Cells(r, 3), ws.Cells(r + 4, 3)).NumberFormat = MONEY
    ws.Range(ws.Cells(r, 5), ws.Cells(r + 4, 6)).NumberFormat = MONEY
    r += len(body) + 1
    r = note(ws, r, 'Shared fault: every one of the five has a negative Quantity, so the Subtotal comes out as '
                    'the negative of the correct figure while cogs stayed positive and correct.', italic=False)
    r = note(ws, r, 'The gap checks out: 2 x (9,338 + 39,546 + 13,524 + 30,456 + 42,568) = ₦270,864.00.')
    r += 1
    r = note(ws, r, 'Tier 3: how many rows satisfy each of the export\'s three arithmetic relationships.', italic=False)
    r = header_row(ws, r, ['Relationship', 'Rows where it holds', 'Rows where it fails'])
    r = check_row(ws, r, 'Sales = cogs + Tax 5%', '=COUNTIF(RawSales[Check sales],TRUE)', INT)
    ws.Cells(r - 1, 3).Formula = '=COUNTIF(RawSales[Check sales],FALSE)'
    r = check_row(ws, r, 'Tax 5% = cogs x 0.05', '=COUNTIF(RawSales[Check tax],TRUE)', INT)
    ws.Cells(r - 1, 3).Formula = '=COUNTIF(RawSales[Check tax],FALSE)'
    r = check_row(ws, r, 'cogs = Unit price x Quantity', '=COUNTIF(RawSales[Arithmetic Check],TRUE)', INT)
    ws.Cells(r - 1, 3).Formula = '=COUNTIF(RawSales[Arithmetic Check],FALSE)'
    r += 1
    r = note(ws, r, 'Conclusion: every money column is internally consistent on all 1,025 rows. The only '
                    'relationship that breaks is the one involving Quantity, on five rows, so the fault was',
             italic=False)
    r = note(ws, r, 'introduced into the Quantity column alone and no financial total is affected by it.',
             italic=False)
    autofit(ws)

    wb.Worksheets(1).Activate()
    save(wb, os.path.abspath(os.path.join(T1, '2.1_lab_solution.xlsx')))
    return wb


# ----------------------------------------------------------------- 2.2
def build_22(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    build_raw_sheet(wb.Worksheets(1), with_22=True)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Lookups'
    r = title(ws, 1, 'Three routes to the same answer')
    r = note(ws, r, 'Invoice 351-62-0822 belongs to the Wuse branch. All three lookups must agree.')
    r += 1
    ws.Range("F1").Value = '351-62-0822'
    ws.Range("F1").NumberFormat = TEXT
    ws.Range("F1").Value = '351-62-0822'
    ws.Range("E1").Value = 'Lookup value'
    ws.Range("E1").Font.Bold = True
    r = header_row(ws, r, ['Method', 'Result', 'Expected'], col=1)
    r = check_row(ws, r, 'XLOOKUP', '=XLOOKUP(F1,RawSales[Invoice ID],RawSales[Branch])', None, 'Wuse')
    r = check_row(ws, r, 'VLOOKUP with FALSE', '=VLOOKUP(F1,RawSales[#All],2,FALSE)', None, 'Wuse')
    r = check_row(ws, r, 'INDEX-MATCH', '=INDEX(RawSales[Branch],MATCH(F1,RawSales[Invoice ID],0))', None, 'Wuse')
    r = check_row(ws, r, 'VLOOKUP without FALSE', '=IFERROR(VLOOKUP(F1,RawSales[#All],2),"#N/A")', None,
                  'Approximate match, unreliable, no error raised')
    r += 1
    r = note(ws, r, 'The fourth row is the teaching point: an approximate match on unsorted text returns '
                    'whatever it lands on, with no error to warn anybody.')
    autofit(ws)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Summary'
    r = title(ws, 1, 'Summary figures: RAW FILE, 1,025 rows')
    r = note(ws, r, 'Every figure on this sheet is measured on the uncleaned export. None of them is '
                    'reportable to the client until Topic 2.3 is done.')
    r += 1
    r = header_row(ws, r, ['Measure', 'Live formula result', 'Expected'])
    first = r
    for label, f, fmt, exp in [
        ('Total Sales', '=SUM(RawSales[Sales])', MONEY, '₦33,156,782.40'),
        ('Average rating', '=AVERAGE(RawSales[Rating])', '0.00', '6.97'),
        ('Transactions', '=COUNT(RawSales[Sales])', INT, '1,025'),
        ('Rated 7 or above', '=COUNTIF(RawSales[Rating],">=7")', INT, '508'),
    ]:
        r = check_row(ws, r, label, f, fmt, exp)
    ik, wu, ta = r, r + 1, r + 2
    for label, f, fmt, exp in [
        ('Ikeja Sales', '=SUMIF(RawSales[Branch],"Ikeja",RawSales[Sales])', MONEY, '₦11,062,565.85'),
        ('Wuse Sales', '=SUMIF(RawSales[Branch],"Wuse",RawSales[Sales])', MONEY, '₦10,755,627.75'),
        ('Trans-Amadi Sales', '=SUMIF(RawSales[Branch],"Trans-Amadi",RawSales[Sales])', MONEY, '₦11,338,588.80'),
    ]:
        r = check_row(ws, r, label, f, fmt, exp)
    ikn, wun, tan = r, r + 1, r + 2
    for label, f, fmt, exp in [
        ('Ikeja transactions', '=COUNTIF(RawSales[Branch],"Ikeja")', INT, '353'),
        ('Wuse transactions', '=COUNTIF(RawSales[Branch],"Wuse")', INT, '338'),
        ('Trans-Amadi transactions', '=COUNTIF(RawSales[Branch],"Trans-Amadi")', INT, '334'),
    ]:
        r = check_row(ws, r, label, f, fmt, exp)
    r = check_row(ws, r, 'Branch Sales reconcile (must be 0)',
                  f'=(B{ik}+B{wu}+B{ta})-SUM(RawSales[Sales])', MONEY, '0.00')
    r = check_row(ws, r, 'Branch counts reconcile (must be 0)',
                  f'=(B{ikn}+B{wun}+B{tan})-COUNTA(RawSales[Invoice ID])', INT, '0')
    r += 1
    r = header_row(ws, r, ['Wuse Health and beauty', 'Live formula result', 'Expected'])
    for label, f, fmt, exp in [
        ('Transactions, exact criterion',
         '=COUNTIFS(RawSales[Branch],"Wuse",RawSales[Product line],"Health and beauty")', INT, '48'),
        ('Transactions, wildcard criterion',
         '=COUNTIFS(RawSales[Branch],"Wuse",RawSales[Product line],"Health and beauty*")', INT, '53'),
        ('Sales, wildcard criterion',
         '=SUMIFS(RawSales[Sales],RawSales[Branch],"Wuse",RawSales[Product line],"Health and beauty*")',
         MONEY, '₦1,998,066.00'),
    ]:
        r = check_row(ws, r, label, f, fmt, exp)
    r += 1
    for line in [
        'Why the two criteria differ: 102 rows in this export hold the Product line in ALL CAPS with a',
        'trailing space. Excel criteria matching is not case sensitive, so the casing costs nothing, but',
        'the trailing space makes the exact criterion miss 5 genuine Wuse Health and beauty transactions.',
        '',
        'Raw versus cleaned: the two figures that move most are the rated-7-or-above count, 508 here and',
        '501 on the cleaned file, and every branch total. 508 minus the 12 duplicated rows rated 7 or',
        'above, plus the 5 restored blank Ratings that are 7 or above, gives 501.',
    ]:
        r = note(ws, r, line, italic=False)
    autofit(ws)

    wb.Worksheets(1).Activate()
    save(wb, os.path.abspath(os.path.join(T2, '2.2_lab_solution.xlsx')))
    return wb


if __name__ == '__main__':
    xl = start_excel()
    try:
        for fn, label in ((build_21, '2.1'), (build_22, '2.2')):
            wb = fn(xl)
            recalc(xl)
            wb.Save()
            wb.Close(True)
            print('built', label)
    finally:
        xl.Quit()
    print('done')
