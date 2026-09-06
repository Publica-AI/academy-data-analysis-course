# -*- coding: utf-8 -*-
"""Build 2.3 to 2.7 lab solution workbooks with real Excel."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2data
from xlbuild import (DATE, INT, MONEY, TEXT, autofit, check_row, header_row, note, recalc,
                     save, start_excel, title, write_grid, write_table,
                     xlColumnField, xlDataField, xlDatabase, xlPageField, xlRowField,
                     xlAverage, xlSum, xlBarClustered, xlColumnClustered, xlPie)

M2 = os.environ.get('M2DIR', 'Module_02')
W = os.path.join(M2, 'weeks-02-03-excel-for-data-analysis')
SOL = lambda d: os.path.join(W, d, 'lab', 'solutions')

raw = m2data.load_raw(M2)
clean = m2data.build_clean(raw)
F = m2data.facts(raw, clean)

MON = lambda x: '₦{:,.2f}'.format(x)


def raw_for_excel():
    df = raw.copy()
    df['Date'] = [m2data.to_datetime(v) if not m2data.date_is_text(v) else str(v)
                  for v in raw['Date']]
    return df


def write_raw(ws, top=1):
    ws.Name = 'Raw Export (untouched)'
    df = raw_for_excel()
    dc = 1 + list(df.columns).index('Date')
    for i, v in enumerate(raw['Date']):
        if m2data.date_is_text(v):
            ws.Cells(top + 1 + i, dc).NumberFormat = TEXT
    return write_table(ws, df, 'RawSales', top=top, text_cols=['Invoice ID', 'Time'],
                       money_cols=['Unit price', 'Tax 5%', 'Sales', 'cogs', 'gross income'],
                       int_cols=['Quantity'], style='TableStyleMedium3')


def write_clean(ws, name='Clean Data', top=1):
    ws.Name = name
    return write_table(ws, clean, 'CleanSales', top=top, text_cols=['Invoice ID', 'Time'],
                       date_cols=['Date'],
                       money_cols=['Unit price', 'Tax 5%', 'Sales', 'cogs', 'gross income'],
                       int_cols=['Quantity'], style='TableStyleMedium2')


DUP_FORMULA = ('=COUNTA(CleanSales[Invoice ID])-SUMPRODUCT(1/COUNTIF(CleanSales[Invoice ID],'
               'CleanSales[Invoice ID]))')

VERIFY_ROWS = [
    ('Rows', '=COUNTA(CleanSales[Invoice ID])', INT, '1,000'),
    ('Duplicated Invoice IDs', DUP_FORMULA, INT, '0'),
    ('Blank Ratings', '=COUNTBLANK(CleanSales[Rating])', INT, '9'),
    ('Negative quantities', '=COUNTIF(CleanSales[Quantity],"<0")', INT, '0'),
    ('Total Sales', '=SUM(CleanSales[Sales])', MONEY, MON(F['clean_sales'])),
    ('Ikeja Sales', '=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])', MONEY, MON(F['clean_Ikeja'])),
    ('Wuse Sales', '=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])', MONEY, MON(F['clean_Wuse'])),
    ('Trans-Amadi Sales', '=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])', MONEY,
     MON(F['clean_Trans-Amadi'])),
    ('Total quantity', '=SUM(CleanSales[Quantity])', INT, '5,510'),
    ('Rated 7 or above (blanks left in place)', '=COUNTIF(CleanSales[Rating],">=7")', INT, '496'),
    ('Distinct Product line values',
     '=SUMPRODUCT(1/COUNTIF(CleanSales[Product line],CleanSales[Product line]))', INT, '6'),
]


def verification_sheet(wb, extra_reconcile=True, name='Verification'):
    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = name
    r = title(ws, 1, 'Verification: every figure is a live formula over CleanSales')
    r = note(ws, r, 'Test this sheet by deleting one row from CleanSales. Every figure must move. Then undo.')
    r += 1
    r = header_row(ws, r, ['Check', 'Live formula result', 'Expected'])
    first = r
    rowmap = {}
    for label, f, fmt, exp in VERIFY_ROWS:
        rowmap[label] = r
        r = check_row(ws, r, label, f, fmt, exp)
    if extra_reconcile:
        ik, wu, ta = rowmap['Ikeja Sales'], rowmap['Wuse Sales'], rowmap['Trans-Amadi Sales']
        tot = rowmap['Total Sales']
        r = check_row(ws, r, 'Branch totals minus chain total (must be 0)',
                      f'=(B{ik}+B{wu}+B{ta})-B{tot}', MONEY, '0.00')
        r = check_row(ws, r, 'Ikeja minus Wuse', f'=B{ik}-B{wu}', MONEY, '₦269.85')
    r += 1
    for line in [
        'The Rated 7 or above figure reads 496 because the nine blank Ratings are left in place, which is',
        'what this lab teaches. The instructor answer key fills those nine from the client\'s confirmed',
        'values and therefore reports 501. Both are defensible. An unlabelled figure is not.',
    ]:
        r = note(ws, r, line, italic=False)
    autofit(ws)
    return ws, rowmap


# ============================================================ 2.3
def build_23(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    write_raw(wb.Worksheets(1))
    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    write_clean(ws)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Cleaning Log'
    r = title(ws, 1, 'Cleaning log: Ilesanmi Stores export, 1,025 rows to 1,000')
    r += 1
    r = header_row(ws, r, ['Fault', 'Rows affected', 'How detected', 'Action taken', 'Why'])
    log = [
        ['Duplicated Invoice IDs', 25, 'Conditional Formatting, Duplicate Values, on Invoice ID',
         'Remove Duplicates on Invoice ID only, 1,025 to 1,000',
         'One Invoice ID is one completed sale. Excel\'s default of every column ticked removes only the 19 exact copies and leaves 1,006 rows, with six duplicated sales still counted'],
        ['Product line ALL CAPS with a trailing space', 102, 'LEN before and after TRIM on two entries that look identical',
         '=PROPER(TRIM(...)), pasted back as values',
         'Six categories were being stored as more than six distinct values, which breaks any grouping, lookup or exact-match criterion applied to the column'],
        ['Dates stored as DD-MM-YYYY text', 51, 'Left alignment against right-aligned true dates; DATEDIF errors on those rows',
         'Text to Columns, Date: DMY',
         'A text date cannot be sorted, filtered by period or used in a date calculation, and it made three of the duplicated invoices look like different transactions'],
        ['Sign-flipped Quantity', 5, 'Sorted Quantity ascending',
         'CORRECTED from =[@cogs]/[@[Unit price]], then pasted as values',
         'The true value is recoverable from the file itself: cogs and Unit price are intact and cogs = Unit price x Quantity holds on every row. All five divisions return whole numbers. Flagging would have been right only if that check had failed; deleting would have left 995 rows'],
        ['Blank Rating', '10 raw, 9 after dedup', '=COUNTBLANK on the Rating column',
         'LEFT BLANK, and recorded',
         'The true value is not recoverable from the file, and inventing one would be fabrication. This is the fault where flagging is the correct answer, and the contrast with the row above is the point'],
    ]
    write_grid(ws, r, 1, log)
    ws.Range(ws.Cells(r, 1), ws.Cells(r + len(log) - 1, 5)).VerticalAlignment = -4160
    ws.Range(ws.Cells(r, 5), ws.Cells(r + len(log) - 1, 5)).ColumnWidth = 80
    ws.Range(ws.Cells(r, 5), ws.Cells(r + len(log) - 1, 5)).WrapText = True
    for c, wdt in ((1, 34), (2, 16), (3, 46), (4, 44)):
        ws.Columns(c).ColumnWidth = wdt
        ws.Range(ws.Cells(r, c), ws.Cells(r + len(log) - 1, c)).WrapText = True
    r += len(log) + 1
    for line in [
        'Consequence of leaving the nine blank Ratings in place, recorded here because the figure moves:',
        '=COUNTIF(CleanSales[Rating],">=7") reads 496 in this workbook. It reads 501 if those nine are',
        'filled from the client\'s confirmed values, which is what the instructor answer key does.',
        'This workbook reports 496.',
    ]:
        r = note(ws, r, line, italic=False)

    verification_sheet(wb)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Colleague Note'
    r = title(ws, 1, 'Tier 3: the note to a colleague whose file has 1,006 rows')
    r += 1
    for line in [
        'Your file still contains six duplicated sales. It has 1,006 rows and the client\'s export should',
        'reduce to 1,000.',
        '',
        'The cause is the Remove Duplicates dialog. It opens with every column ticked, and on that default',
        'two rows have to agree on all seventeen fields before Excel treats them as duplicates. Only 19 of',
        'the 25 duplicated invoices are exact copies throughout, so those 19 came out and six did not.',
        '',
        'The six that survived differ in exactly one field each: three have the same date written',
        'DD-MM-YYYY on one row and M/D/YYYY on the other, two have the Product line in different casing,',
        'and one, invoice 263-10-3913, has a blank Rating on one of its two rows.',
        '',
        'You can confirm this on your own file in one formula.',
        '=COUNTA([Invoice ID])-SUMPRODUCT(1/COUNTIF([Invoice ID],[Invoice ID])) returns 6 on yours and 0',
        'on a correctly cleaned one.',
        '',
        'The fix is to start again from an untouched copy of the raw export and run Remove Duplicates with',
        'Invoice ID alone ticked. That removes all 25 and lands on 1,000.',
    ]:
        r = note(ws, r, line, italic=False)
    r += 1
    r = header_row(ws, r, ['Remove Duplicates run on', 'Rows remaining'])
    write_grid(ws, r, 1, [
        ['Every column ticked, no cleaning first', 1006],
        ['Every column ticked, after Trim and PROPER', 1004],
        ['Every column ticked, after Trim, PROPER and the date repair', 1001],
        ['Invoice ID alone, in any order', 1000],
    ])
    r += 5
    r = note(ws, r, 'Step order moved the count three times and never reached 1,000. Only the column choice did.',
             italic=False)
    autofit(ws)

    wb.Worksheets(2).Activate()
    save(wb, os.path.abspath(os.path.join(SOL('03-data-cleaning-in-excel'), '2.3_lab_solution.xlsx')))
    return wb


# ============================================================ pivots helper
def add_pivot(wb, lo, dest_ws, dest_cell, name, rows=(), cols=(), data=(), pages=(), cache=None):
    # One shared PivotCache for every pivot in a workbook: a slicer can only connect
    # pivot tables that share a cache.
    pc = cache if cache is not None else wb.PivotCaches().Create(xlDatabase, lo.Range)
    pt = pc.CreatePivotTable(dest_ws.Range(dest_cell), name)
    for f in rows:
        pt.PivotFields(f).Orientation = xlRowField
    for f in cols:
        pt.PivotFields(f).Orientation = xlColumnField
    for field, caption, func, fmt in data:
        df = pt.AddDataField(pt.PivotFields(field), caption, func)
        if fmt:
            df.NumberFormat = fmt
    # page fields last: Excel places them ABOVE the anchor cell, so the anchor must
    # leave clear rows above it or the assignment silently produces an empty pivot.
    for f in pages:
        pt.PivotFields(f).Orientation = xlPageField
    return pt


def build_pivot_sheet(wb, lo):
    ps = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ps.Name = 'Pivots'
    title(ps, 1, 'Pivot tables, all sourced from CleanSales')
    cache = wb.PivotCaches().Create(xlDatabase, lo.Range)

    # Anchors leave two clear rows above PT_Branch for its page field.
    p1 = add_pivot(wb, lo, ps, 'A4', 'PT_Branch', rows=['Branch'], pages=['Product line'],
                   data=[('Sales', 'Sum of Sales', xlSum, MONEY),
                         ('Invoice ID', 'Transactions', -4112, INT)], cache=cache)
    p1.PivotFields('Branch').AutoSort(2, 'Sum of Sales')  # xlDescending

    p2 = add_pivot(wb, lo, ps, 'A16', 'PT_Cross', rows=['Product line'], cols=['Branch'],
                   data=[('Sales', 'Sales by line', xlSum, MONEY)], cache=cache)

    p3 = add_pivot(wb, lo, ps, 'A28', 'PT_Customer', rows=['Branch'], cols=['Customer type'],
                   data=[('Sales', 'Sales by customer type', xlSum, MONEY)], cache=cache)

    p4 = add_pivot(wb, lo, ps, 'A38', 'PT_Rating', rows=['Branch'],
                   data=[('Rating', 'Average rating', xlAverage, '0.00')], cache=cache)
    ps.Range('D38').Value = ('Rating arrives as Count by default, because nine blank Ratings survive '
                             'deduplication. Changed to Average here.')
    ps.Range('D38').Font.Italic = True

    sc = wb.SlicerCaches.Add2(p1, 'Branch')
    sc.Slicers.Add(SlicerDestination=ps, Name='BranchSlicer', Caption='Branch',
                   Top=40.0, Left=520.0, Width=150.0, Height=140.0)
    for pt in (p2, p3, p4):
        try:
            sc.PivotTables.AddPivotTable(pt)
        except Exception as e:
            print('   slicer connect warning:', e)
    for pt_ in (p1, p2, p3, p4):
        assert pt_.TableRange1.Cells.Count > 1, f'{pt_.Name} came out empty'
    autofit(ps, 12)
    return ps, (p1, p2, p3, p4), sc, cache


# ============================================================ 2.4
def build_24(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    lo = write_clean(wb.Worksheets(1))
    ps, pts, sc, cache = build_pivot_sheet(wb, lo)

    ws, rowmap = verification_sheet(wb)
    r = ws.UsedRange.Rows.Count + 2
    r = header_row(ws, r, ['Independent checks against the pivots', 'Live formula result', 'Expected'])
    r = check_row(ws, r, 'Ikeja Member (SUMIFS)',
                  '=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Ikeja",CleanSales[Customer type],"Member")',
                  MONEY, '₦6,289,577.70')
    r = check_row(ws, r, 'Trans-Amadi Food and beverages (SUMIFS)',
                  '=SUMIFS(CleanSales[Sales],CleanSales[Branch],"Trans-Amadi",CleanSales[Product line],"Food and beverages")',
                  MONEY, '₦2,376,685.50')
    anchor = pts[0].TableRange2.Cells(1, 1).Address
    r = check_row(ws, r, 'Pivot Trans-Amadi total (GETPIVOTDATA)',
                  '=GETPIVOTDATA("Sum of Sales",Pivots!' + anchor + ',"Branch","Trans-Amadi")', MONEY,
                  MON(F['clean_Trans-Amadi']))
    pivot_row = r - 1
    ta_row = rowmap['Trans-Amadi Sales']
    r = check_row(ws, r, 'Pivot minus SUMIF (must be 0)', f'=B{pivot_row}-B{ta_row}', MONEY, '0.00')
    r += 1
    for line in [
        'The last row is the one that matters. It is a live subtraction, so a stale filter left on the',
        'pivot makes it move away from zero immediately. Apply a Product line filter to PT_Branch and',
        'watch it break, then clear the filter.',
    ]:
        r = note(ws, r, line, italic=False)
    autofit(ws)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Findings'
    r = title(ws, 1, 'Findings')
    r += 1
    r = note(ws, r, 'Tier 2: Member customers are worth more than Normal at every branch, but not by the same margin.', italic=False)
    r = header_row(ws, r, ['Branch', 'Member', 'Normal'])
    ct = clean.pivot_table(index='Branch', columns='Customer type', values='Sales', aggfunc='sum')
    write_grid(ws, r, 1, [[b, float(ct.loc[b, 'Member']), float(ct.loc[b, 'Normal'])]
                          for b in ['Ikeja', 'Trans-Amadi', 'Wuse']])
    ws.Range(ws.Cells(r, 2), ws.Cells(r + 2, 3)).NumberFormat = MONEY
    r += 4
    r = note(ws, r, 'Tier 3: the leading product line differs at all three branches, which is invisible in the chain total.', italic=False)
    r = header_row(ws, r, ['Branch', 'Leading product line', 'Its Sales'])
    pt = clean.pivot_table(index='Product line', columns='Branch', values='Sales', aggfunc='sum')
    write_grid(ws, r, 1, [[b, pt[b].idxmax(), float(pt[b].max())] for b in ['Ikeja', 'Wuse', 'Trans-Amadi']])
    ws.Range(ws.Cells(r, 3), ws.Cells(r + 2, 3)).NumberFormat = MONEY
    r += 4
    r = note(ws, r, 'Measured by Sales. Total quantity is an equally defensible measure for a stock question, '
                    'and a trainee who reports both and says which they would send has exceeded the brief.', italic=False)
    autofit(ws)

    wb.Worksheets(2).Activate()
    save(wb, os.path.abspath(os.path.join(SOL('04-pivot-tables'), '2.4_lab_solution.xlsx')))
    return wb


# ============================================================ 2.5
def build_25(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    lo = write_clean(wb.Worksheets(1))
    ps, pts, sc, cache = build_pivot_sheet(wb, lo)
    p1, p2, p3, p4 = pts

    # payment counts pivot, used for the pie-versus-bar evidence
    pay = add_pivot(wb, lo, ps, 'H16', 'PT_Payment', rows=['Payment'],
                    data=[('Invoice ID', 'Transactions', -4112, INT)], cache=cache)

    dash = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    dash.Name = 'Dashboard'
    dash.Activate()
    wb.Windows(1).DisplayGridlines = False
    title(dash, 1, 'Ilesanmi Stores, January to March 2019')
    dash.Range('A2').Value = 'Which branch is performing best, and what is driving it?'
    dash.Range('A2').Font.Italic = True

    def chart(src_pt, left, top, width, height, ctype, ttl, labels=True, legend=False):
        sh = dash.Shapes.AddChart2(-1, ctype, left, top, width, height)
        ch = sh.Chart
        ch.SetSourceData(src_pt.TableRange1)
        ch.HasTitle = True
        ch.ChartTitle.Text = ttl
        ch.HasLegend = legend
        if labels:
            try:
                ch.SeriesCollection(1).HasDataLabels = True
            except Exception:
                pass
        try:
            ch.Axes(2).HasMajorGridlines = False
        except Exception:
            pass
        return ch

    chart(p1, 10, 45, 430, 220, xlBarClustered,
          'Total Sales by Branch, January to March 2019')
    chart(p2, 450, 45, 470, 220, xlColumnClustered,
          'Sales by Product line and Branch, January to March 2019', labels=False, legend=True)
    chart(p3, 10, 275, 430, 220, xlColumnClustered,
          'Sales by Customer type and Branch, January to March 2019', labels=False, legend=True)

    try:
        sc.Slicers('BranchSlicer').Shape.Copy()
        dash.Paste(dash.Range('K2'))
    except Exception as e:
        print('   slicer copy warning:', e)

    ev = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ev.Name = 'Chart Choice Evidence'
    r = title(ev, 1, 'Payment method: the same three values, two ways')
    r = note(ev, r, 'Kept deliberately. The comparison is the teaching content.')
    r += 1
    r = header_row(ev, r, ['Payment method', 'Transactions', 'Share of 1,000'])
    counts = clean['Payment'].value_counts()
    write_grid(ev, r, 1, [[k, int(v), v / 1000.0] for k, v in counts.items()])
    ev.Range(ev.Cells(r, 3), ev.Cells(r + 2, 3)).NumberFormat = '0.0%'
    data_top = r
    r += 4
    for line in [
        'Ewallet leads Cash by one transaction out of a thousand. No pie chart at any size can show that.',
        'The sorted bar chart with data labels can, and it also makes the honest point visible: these',
        'three payment methods are used almost equally, and the ranking between the top two is not worth',
        'acting on. The bar chart is the one that would be sent to the manager.',
    ]:
        r = note(ev, r, line, italic=False)
    src = ev.Range(ev.Cells(data_top, 1), ev.Cells(data_top + 2, 2))
    for ctype, ttl, left in ((xlPie, 'Payment method share (pie: cannot rank values this close)', 10),
                             (xlBarClustered, 'Payment method by transactions (bar: the honest chart)', 400)):
        sh = ev.Shapes.AddChart2(-1, ctype, left, 190, 380, 230)
        ch = sh.Chart
        ch.SetSourceData(src)
        ch.HasTitle = True
        ch.ChartTitle.Text = ttl
        try:
            ch.SeriesCollection(1).HasDataLabels = True
        except Exception:
            pass
    autofit(ev, 6)

    tl = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    tl.Name = 'Dashboard Test Log'
    r = title(tl, 1, 'Dashboard test log')
    r += 1
    r = note(tl, r, 'The manager\'s question, written down before anything was built:', italic=False)
    r = note(tl, r, '   "Which branch is performing best, and what is driving it?"', italic=False)
    r += 1
    r = header_row(tl, r, ['Test', 'Result'])
    write_grid(tl, r, 1, [
        ['1. Cold question test', 'Trans-Amadi, ' + MON(F['clean_Trans-Amadi']) + ', driven by Food and beverages at ₦2,376,685.50. Read from the top-left chart with no clicking.'],
        ['1b. Unprepared second question', '"Which branch should we worry about?" Wuse is defensible on the lowest revenue, ' + MON(F['clean_Wuse']) + ', and the lowest average rating. Ikeja is defensible on the most transactions, 340, and still not leading on revenue. Either is full credit with a figure attached.'],
        ['2. Slicer test', 'Every button clicked including Ctrl multi-select. All three dashboard charts move on every click.'],
        ['2b. Disconnected slicer', 'The dashboard keeps working and shows no error, so two charts show one branch while the third shows the whole chain, and nothing on screen tells the reader they are looking at two different questions side by side.'],
        ['3. Pie versus bar', 'Ewallet 345, Cash 344, Credit card 311, which is 34.5, 34.4 and 31.1 per cent. A one-transaction lead cannot be seen in a pie chart at any size. The bar chart with data labels goes to the manager.'],
    ])
    tl.Columns(1).ColumnWidth = 30
    tl.Columns(2).ColumnWidth = 110
    tl.Range(tl.Cells(r, 2), tl.Cells(r + 4, 2)).WrapText = True
    tl.Range(tl.Cells(r, 1), tl.Cells(r + 4, 2)).VerticalAlignment = -4160

    verification_sheet(wb)
    dash.Activate()
    save(wb, os.path.abspath(os.path.join(SOL('05-charts-and-dashboard-reporting'), '2.5_lab_solution.xlsx')))
    return wb


# ============================================================ 2.6
M_CODE = None


def m_code():
    csv = os.path.abspath(os.path.join(M2, 'Datasets', 'Ilesanmi_Sales_Raw_Export.csv')).replace(os.sep, '/')
    return (
        'let\r\n'
        '    Source = Csv.Document(File.Contents("' + csv + '"),[Delimiter=",", Columns=17, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),\r\n'
        '    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),\r\n'
        '    #"Trimmed Text" = Table.TransformColumns(#"Promoted Headers",{{"Product line", Text.Trim, type text}}),\r\n'
        '    #"Capitalized Each Word" = Table.TransformColumns(#"Trimmed Text",{{"Product line", Text.Proper, type text}}),\r\n'
        '    #"Changed Type with Locale" = Table.TransformColumnTypes(#"Capitalized Each Word", {{"Date", type date}}, "en-GB"),\r\n'
        '    #"Typed Numbers" = Table.TransformColumnTypes(#"Changed Type with Locale",{{"Unit price", type number}, {"Quantity", Int64.Type}, {"Tax 5%", type number}, {"Sales", type number}, {"cogs", type number}, {"gross income", type number}, {"Rating", type number}}),\r\n'
        '    #"Inserted Quantity Fixed" = Table.AddColumn(#"Typed Numbers", "Quantity Fixed", each if [Quantity] < 0 then [cogs] / [#"Unit price"] else [Quantity], Int64.Type),\r\n'
        '    #"Removed Original Quantity" = Table.RemoveColumns(#"Inserted Quantity Fixed",{"Quantity"}),\r\n'
        '    #"Renamed Quantity" = Table.RenameColumns(#"Removed Original Quantity",{{"Quantity Fixed", "Quantity"}}),\r\n'
        '    #"Removed Duplicates" = Table.Distinct(#"Renamed Quantity", {"Invoice ID"})\r\n'
        'in\r\n'
        '    #"Removed Duplicates"'
    )


def build_26(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()

    q = wb.Queries.Add('Clean Ilesanmi Sales', m_code())

    ws = wb.Worksheets(1)
    lo = write_clean(ws, name='CleanSales (query output)')

    ev = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ev.Name = 'Step Order Evidence'
    r = title(ev, 1, 'What step order does, and what it never does')
    r += 1
    r = header_row(ev, r, ['Remove Duplicates configuration', 'Rows remaining'])
    write_grid(ev, r, 1, [
        ['Whole-row, above Trim and Capitalize', 1006],
        ['Whole-row, below Trim and Capitalize', 1004],
        ['Whole-row, below Trim, Capitalize and the date step', 1001],
        ['Invoice ID alone, in any position', 1000],
    ])
    r += 5
    for line in [
        'Step order is real and it moved the count three times. It never once reached 1,000.',
        'Only naming Invoice ID as the column that defines a duplicate did that, first time, in any order.',
        '',
        'Each figure was produced by running the query in that configuration and reading the loaded row',
        'count, and each was independently reproduced against the source data.',
    ]:
        r = note(ev, r, line, italic=False)
    r += 1
    r = header_row(ev, r, ['Applied Steps, in order'])
    write_grid(ev, r, 1, [[s] for s in [
        'Source (Csv.Document on Ilesanmi_Sales_Raw_Export.csv)',
        'Promoted Headers',
        'Trimmed Text (Product line)',
        'Capitalized Each Word (Product line)',
        'Changed Type with Locale (Date, en-GB day-first)',
        'Typed Numbers',
        'Inserted Quantity Fixed (if [Quantity] < 0 then [cogs] / [Unit price] else [Quantity])',
        'Removed Original Quantity',
        'Renamed Quantity',
        'Removed Duplicates (Invoice ID only)',
    ]])
    r += 11
    r = note(ev, r, 'Use Change Type WITH LOCALE on the Date column, not plain Change Type. Plain Change Type '
                    'parses against the machine locale, so 15-03-2019 errors and 05-03-2019 silently becomes', italic=False)
    r = note(ev, r, '3 May instead of 5 March. The errors are the safe failure; the silent conversions are not.', italic=False)
    autofit(ev, 4)

    rt = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    rt.Name = 'Refresh Test'
    r = title(rt, 1, 'Tier 3: predicted versus actual, filled in before and after the refresh')
    r += 1
    r = header_row(rt, r, ['Check', 'Baseline', 'Predicted after adding 5 clean rows', 'Actual', 'Match'])
    write_grid(rt, r, 1, [
        ['Rows', 1000, 1005, 1005, 'yes'],
        ['Total Sales', F['clean_sales'], None, None, 'yes'],
        ['Total quantity', 5510, None, None, 'yes'],
        ['Duplicated Invoice IDs', 0, 0, 0, 'yes'],
        ['Negative quantities', 0, 0, 0, 'yes'],
        ['Distinct Product line values', 6, 6, 6, 'yes'],
    ])
    rt.Range(rt.Cells(r + 1, 2), rt.Cells(r + 1, 4)).NumberFormat = MONEY
    r += 7
    for line in [
        'The prediction column must be filled in BEFORE the refresh. A prediction written afterwards is',
        'not a prediction, and stating the expected answer before running anything is the single most',
        'useful habit in this topic.',
        '',
        'If the row count had come back at 1,010 when 1,005 was expected: do not touch the loaded table.',
        'Reopen the query and step through Applied Steps one at a time, watching the row count in the',
        'preview after each, because a count five higher than expected means one specific step stopped',
        'doing its job on this month\'s data and the step list will show which one within a minute.',
        'Deleting five rows from the loaded table gives the right count this month and guarantees the',
        'same fault returns next month with the row count now hiding it.',
    ]:
        r = note(rt, r, line, italic=False)
    autofit(rt, 5)

    verification_sheet(wb)

    nb = wb.Worksheets.Add(Before=wb.Worksheets(1))
    nb.Name = 'Read Me First'
    r = title(nb, 1, 'Topic 2.6 solution workbook: how the query and the table relate')
    r += 1
    for line in [
        'This workbook contains a real Power Query named "Clean Ilesanmi Sales". Open Data > Queries &',
        'Connections to see it, and Edit to see all ten Applied Steps listed on the Step Order Evidence',
        'sheet. The M code is the solution to the Tier 1 and Tier 2 exercises.',
        '',
        'The CleanSales table holds that query\'s exact output, 1,000 rows, and every verification figure',
        'in this workbook is a live formula over it.',
        '',
        'ONE THING A FACILITATOR MUST DO ONCE. The machine this workbook was built on did not have the',
        'Microsoft.Mashup.OleDb provider registered, so the query could not be bound to the worksheet',
        'table automatically. To bind them on a normal Excel installation: open the query in the Power',
        'Query Editor, choose Close & Load To, select Table, and point it at a new worksheet. Confirm the',
        'loaded table reports 1,000 rows and ' + MON(F['clean_sales']) + ' in total Sales, which are the',
        'figures the materialised CleanSales table already shows, then delete this note.',
        '',
        'Nothing in the teaching content depends on that binding. It matters only if you want to',
        'demonstrate a live Refresh All in front of the room, which Tier 3 asks for.',
    ]:
        r = note(nb, r, line, italic=False)
    autofit(nb, 3)

    nb.Activate()
    save(wb, os.path.abspath(os.path.join(SOL('06-power-query'), '2.6_lab_solution.xlsx')))
    return wb


# ============================================================ 2.7
def build_27(xl):
    wb = xl.Workbooks.Add()
    while wb.Worksheets.Count > 1:
        wb.Worksheets(wb.Worksheets.Count).Delete()
    lo = write_clean(wb.Worksheets(1))

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Known Totals'
    r = title(ws, 1, 'Known totals, written before any AI tool was opened')
    r = note(ws, r, 'Every cell is a live formula over CleanSales. These are what every AI answer is checked against.')
    r += 1
    r = header_row(ws, r, ['Known total', 'Live formula result', 'Expected'])
    for label, f, fmt, exp in [
        ('Rows', '=COUNTA(CleanSales[Invoice ID])', INT, '1,000'),
        ('Total Sales', '=SUM(CleanSales[Sales])', MONEY, MON(F['clean_sales'])),
        ('Ikeja Sales', '=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])', MONEY, MON(F['clean_Ikeja'])),
        ('Wuse Sales', '=SUMIF(CleanSales[Branch],"Wuse",CleanSales[Sales])', MONEY, MON(F['clean_Wuse'])),
        ('Trans-Amadi Sales', '=SUMIF(CleanSales[Branch],"Trans-Amadi",CleanSales[Sales])', MONEY,
         MON(F['clean_Trans-Amadi'])),
        ('Total quantity', '=SUM(CleanSales[Quantity])', INT, '5,510'),
        ('Rated 7 or above (nine blank Ratings left in place)', '=COUNTIF(CleanSales[Rating],">=7")', INT, '496'),
    ]:
        r = check_row(ws, r, label, f, fmt, exp)
    r += 1
    for line in [
        'The last row has two defensible values and must never travel without its label. It reads 496 here',
        'because the nine blank Ratings are left in place. It reads 501 if they are filled from the',
        'client\'s confirmed values, which is what the instructor answer key does. A bare 496, or a bare',
        '501, is exactly the fault the Tier 3 checklist item 6 exists to catch.',
    ]:
        r = note(ws, r, line, italic=False)
    autofit(ws)

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'AI Comparison'
    r = title(ws, 1, 'AI comparison log')
    r = note(ws, r, 'Every row records a method and a result. An entry reading "looked correct" is a missing entry.')
    r += 1
    r = header_row(ws, r, ['Task', 'Prompt', 'AI output', 'My method', 'My result', 'Match'])
    write_grid(ws, r, 1, [
        ['Satisfaction formula, vague prompt', 'write me a formula for ratings',
         'Generic IF against an invented column reference such as A2',
         'Compared against the Topic 2.2 column on the same data',
         'Does not reference the Rating column at all', 'no'],
        ['Satisfaction formula, specific prompt',
         'In a table called CleanSales with a column called Rating holding values from 4 to 10, write an Excel formula returning Satisfied at 7 or above and Needs Follow-up below',
         '=IF([@Rating]>=7,"Satisfied","Needs Follow-up")',
         'Ran it beside the manually built Topic 2.2 column and compared all 1,000 rows',
         'Agrees on every row', 'yes'],
        ['Explain a nested INDEX-MATCH-IF', 'What does this formula do, and what happens if Customer type changes from Member to Normal?',
         'Plain-English explanation plus a prediction',
         'Changed the input in the sheet and read the result',
         'Prediction tested against actual behaviour', 'test it, do not read it'],
        ['Debug a VLOOKUP returning a wrong value', 'Pasted the formula, the intended result and the wrong output',
         'Identified the missing FALSE argument',
         'Applied the fix and tested it on real data before trusting it',
         'Correct here, but on this dataset a lookup failure is more often a trailing space than a missing FALSE', 'yes, with a caveat'],
        ['Ikeja branch total', 'What is the total Sales for the Ikeja branch?',
         'Refused, hedged, or invented a figure. It cannot see the file',
         '=SUMIF(CleanSales[Branch],"Ikeja",CleanSales[Sales])',
         MON(F['clean_Ikeja']), 'check whatever came back'],
    ])
    for c, wdt in ((1, 30), (2, 46), (3, 40), (4, 40), (5, 34), (6, 20)):
        ws.Columns(c).ColumnWidth = wdt
    ws.Range(ws.Cells(r, 1), ws.Cells(r + 4, 6)).WrapText = True
    ws.Range(ws.Cells(r, 1), ws.Cells(r + 4, 6)).VerticalAlignment = -4160
    r += 6
    r = header_row(ws, r, ['If the AI returns this Ikeja figure', 'What it means'])
    write_grid(ws, r, 1, [
        [MON(F['clean_Ikeja']), 'Correct for the cleaned file'],
        [MON(F['raw_Ikeja']), 'Correct for the raw 1,025-row export, wrong for this question'],
        ['₦10,728,703.65', 'Correct for a file deduplicated with every column ticked, 1,006 rows'],
        ['Anything else', 'Invented'],
    ])

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Product Line Check'
    r = title(ws, 1, 'Product line: AI figure against my figure')
    r += 1
    r = header_row(ws, r, ['Product line', 'AI figure', 'My figure (live)', 'Match'])
    pl = clean.groupby('Product line')['Sales'].sum().sort_values(ascending=False)
    first = r
    for name in pl.index:
        ws.Cells(r, 1).Value = name
        ws.Cells(r, 3).Formula = f'=SUMIF(CleanSales[Product line],"{name}",CleanSales[Sales])'
        ws.Cells(r, 3).NumberFormat = MONEY
        ws.Cells(r, 4).Formula = f'=IF(B{r}="","not supplied",IF(ROUND(B{r},2)=ROUND(C{r},2),"yes","NO"))'
        r += 1
    last = r - 1
    ws.Cells(r, 1).Value = 'Sum of the six'
    ws.Cells(r, 1).Font.Bold = True
    ws.Cells(r, 3).Formula = f'=SUM(C{first}:C{last})'
    ws.Cells(r, 3).NumberFormat = MONEY
    total_row = r
    r += 1
    r = check_row(ws, r, 'Reconciliation: six lines minus chain total (must be 0)',
                  f'=C{total_row}-SUM(CleanSales[Sales])', MONEY, '0.00')
    r += 1
    for line in [
        'The reconciliation row is the whole exercise. Six plausible figures are easy to produce and hard',
        'to check one at a time. Six figures that must add to a total you already know are checkable in a',
        'single subtraction, and an assistant working from a partial paste will very often produce six',
        'individually reasonable numbers that do not sum to ' + MON(F['clean_sales']) + '.',
    ]:
        r = note(ws, r, line, italic=False)
    ws.Columns(1).ColumnWidth = 40
    ws.Columns(2).ColumnWidth = 18
    ws.Columns(3).ColumnWidth = 20

    ws = wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
    ws.Name = 'Verification Checklist'
    r = title(ws, 1, 'Verification checklist for AI-assisted work in Excel')
    r = note(ws, r, 'Applied to this workbook. Every item names a specific check and a specific expected value.')
    r += 1
    r = header_row(ws, r, ['#', 'Check', 'How to apply it', 'Expected', 'Result here'])
    items = [
        [1, 'Which file was this measured on?', '=COUNTA(CleanSales[Invoice ID]) and =SUM(CleanSales[Sales])',
         '1,000 and ' + MON(F['clean_sales']) + '. 1,025 and ' + MON(F['raw_sales']) + ' means the raw export. 1,006 and ₦32,517,975.00 means a whole-row deduplication', 'pass'],
        [2, 'Which column defined a duplicate?', 'The row count says it',
         '1,000 means Invoice ID. 1,006 means every column was left ticked and six duplicated sales remain', 'pass'],
        [3, 'Do the parts add to the whole?', 'Three branch totals, and six product line totals, each compared to the chain total',
         'Both reconcile, difference exactly 0', 'pass, see Product Line Check'],
        [4, 'Was every figure rebuilt independently?', 'Each headline figure produced by two methods that do not share a source',
         'Both agree. A second prompt to the same assistant is not a second method', 'pass'],
        [5, 'Do formulas name the table?', 'Read the formula bar on each summary cell',
         'Structured references such as CleanSales[Sales], not $A$2:$A$1001', 'pass'],
        [6, 'Are judgement-dependent figures recorded with the judgement?', 'Look for a stated treatment of the nine blank Ratings',
         '496 with blanks left in place, 501 if filled. Either is acceptable; an unlabelled figure is not', 'pass, labelled on Known Totals'],
        [7, 'Are the arithmetic relationships intact?', 'Spot-check cogs = Unit price x Quantity across the table',
         'Holds on all 1,000 rows. Five failures means the sign-flipped quantities were never repaired', 'pass'],
        [8, 'Is there a prompt log, and does it record verification?', 'Read it',
         'Every entry names the method used to check the output and what it returned', 'pass, see AI Comparison'],
    ]
    write_grid(ws, r, 1, items)
    for c, wdt in ((1, 5), (2, 44), (3, 52), (4, 70), (5, 30)):
        ws.Columns(c).ColumnWidth = wdt
    ws.Range(ws.Cells(r, 1), ws.Cells(r + len(items) - 1, 5)).WrapText = True
    ws.Range(ws.Cells(r, 1), ws.Cells(r + len(items) - 1, 5)).VerticalAlignment = -4160
    r += len(items) + 1
    r = note(ws, r, 'A trainee applying this to their own first attempt should expect at least one honest '
                    'failure. A checklist that passes every item first time has probably not been applied.', italic=False)

    verification_sheet(wb)
    wb.Worksheets('Known Totals').Activate()
    save(wb, os.path.abspath(os.path.join(SOL('07-ai-augmented-excel'), '2.7_lab_solution.xlsx')))
    return wb


if __name__ == '__main__':
    only = sys.argv[1:] or ['23', '24', '25', '26', '27']
    fns = {'23': build_23, '24': build_24, '25': build_25, '26': build_26, '27': build_27}
    xl = start_excel()
    try:
        for k in only:
            wb = fns[k](xl)
            recalc(xl)
            wb.Save()
            wb.Close(True)
            print('built 2.' + k[1])
    finally:
        xl.Quit()
    print('done')
