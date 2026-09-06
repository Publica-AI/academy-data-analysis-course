# -*- coding: utf-8 -*-
"""Test the seven Module 2 solution workbooks by opening them in Excel, forcing a full
recalculation, and asserting every live figure against values recomputed from the datasets.

Nothing here trusts a cached value: Excel recalculates from scratch before anything is read.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import m2data
from xlbuild import start_excel

M2 = os.environ.get('M2DIR', 'Module_02')
W = os.path.join(M2, 'weeks-02-03-excel-for-data-analysis')

raw = m2data.load_raw(M2)
clean = m2data.build_clean(raw)
F = m2data.facts(raw, clean)

fails, passed = [], [0]


def check(wbname, label, actual, expected, tol=0.005):
    ok = False
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        ok = abs(float(actual) - float(expected)) <= tol
    else:
        ok = str(actual).strip() == str(expected).strip()
    if ok:
        passed[0] += 1
    else:
        fails.append(f"{wbname} | {label}: got {actual!r}, expected {expected!r}")


def find_row(ws, label, col=1, maxrow=80):
    for r in range(1, maxrow + 1):
        v = ws.Cells(r, col).Value
        if v is not None and str(v).strip() == label:
            return r
    return None


def val(ws, label, col=2, maxrow=80):
    r = find_row(ws, label, maxrow=maxrow)
    return ws.Cells(r, col).Value if r else None


PATHS = {
    '2.1': os.path.join(W, '01-the-excel-environment-tables-and-referencing', 'lab', 'solutions', '2.1_lab_solution.xlsx'),
    '2.2': os.path.join(W, '02-core-formulas-and-functions', 'lab', 'solutions', '2.2_lab_solution.xlsx'),
    '2.3': os.path.join(W, '03-data-cleaning-in-excel', 'lab', 'solutions', '2.3_lab_solution.xlsx'),
    '2.4': os.path.join(W, '04-pivot-tables', 'lab', 'solutions', '2.4_lab_solution.xlsx'),
    '2.5': os.path.join(W, '05-charts-and-dashboard-reporting', 'lab', 'solutions', '2.5_lab_solution.xlsx'),
    '2.6': os.path.join(W, '06-power-query', 'lab', 'solutions', '2.6_lab_solution.xlsx'),
    '2.7': os.path.join(W, '07-ai-augmented-excel', 'lab', 'solutions', '2.7_lab_solution.xlsx'),
}

RAW_SUBTOTAL_TAX = round(((raw['Unit price'] * raw['Quantity']) * 0.05).sum(), 2)


def verify_common(name, wb, sheet='Verification'):
    ws = wb.Worksheets(sheet)
    check(name, 'Rows', val(ws, 'Rows'), 1000)
    check(name, 'Duplicated Invoice IDs', val(ws, 'Duplicated Invoice IDs'), 0)
    check(name, 'Blank Ratings', val(ws, 'Blank Ratings'), 9)
    check(name, 'Negative quantities', val(ws, 'Negative quantities'), 0)
    check(name, 'Total Sales', val(ws, 'Total Sales'), F['clean_sales'])
    check(name, 'Ikeja Sales', val(ws, 'Ikeja Sales'), F['clean_Ikeja'])
    check(name, 'Wuse Sales', val(ws, 'Wuse Sales'), F['clean_Wuse'])
    check(name, 'Trans-Amadi Sales', val(ws, 'Trans-Amadi Sales'), F['clean_Trans-Amadi'])
    check(name, 'Total quantity', val(ws, 'Total quantity'), 5510)
    check(name, 'Rated 7+ (blanks left)', val(ws, 'Rated 7 or above (blanks left in place)'), 496)
    check(name, 'Distinct Product line values', val(ws, 'Distinct Product line values'), 6)
    check(name, 'Branch reconcile = 0', val(ws, 'Branch totals minus chain total (must be 0)'), 0)
    check(name, 'Ikeja minus Wuse', val(ws, 'Ikeja minus Wuse'), 269.85)


def table_rows(wb, tname):
    for ws in wb.Worksheets:
        for lo in ws.ListObjects:
            if lo.Name == tname:
                return lo.ListRows.Count
    return None


def run():
    xl = start_excel()
    try:
        # ---------------------------------------------------------- 2.1
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.1']))
        xl.CalculateFullRebuild()
        n = '2.1'
        check(n, 'RawSales rows', table_rows(wb, 'RawSales'), 1025)
        ws = wb.Worksheets('Checks')
        check(n, 'Rows', val(ws, 'Rows'), 1025)
        check(n, 'Sum of Subtotal', val(ws, 'Sum of Subtotal'), F['raw_subtotal'])
        check(n, 'Sum of cogs', val(ws, 'Sum of cogs'), F['raw_cogs'])
        check(n, 'Difference', val(ws, 'Difference'), F['raw_diff'])
        check(n, 'Sum of Tax Check', val(ws, 'Sum of Tax Check'), RAW_SUBTOTAL_TAX)
        check(n, 'Sum of Tax 5%', val(ws, 'Sum of Tax 5%'), F['raw_tax'])
        check(n, 'Tax Check gap', val(ws, 'Tax Check gap (5% of the Subtotal gap)'),
              round(F['raw_tax'] - RAW_SUBTOTAL_TAX, 2))
        check(n, 'gap is 5% of subtotal gap', round(F['raw_tax'] - RAW_SUBTOTAL_TAX, 2),
              round(0.05 * F['raw_diff'], 2))
        check(n, 'Sum of Sales', val(ws, 'Sum of Sales'), F['raw_sales'])
        check(n, 'cogs check fails', val(ws, 'Rows failing the cogs check'), 5)
        check(n, 'cogs check passes', val(ws, 'Rows passing the cogs check'), 1020)
        check(n, 'tax check passes', val(ws, 'Rows passing the tax check'), 1025)
        check(n, 'sales check passes', val(ws, 'Rows passing the sales check'), 1025)
        # the B1 test the notes promise
        rs = wb.Worksheets('Raw Export')
        keep = rs.Range('B1').Value
        rs.Range('B1').ClearContents()
        xl.CalculateFullRebuild()
        check(n, 'clearing B1 sends Tax Check to zero', val(ws, 'Sum of Tax Check'), 0)
        rs.Range('B1').Value = keep
        xl.CalculateFullRebuild()
        check(n, 'restoring B1 restores Tax Check', val(ws, 'Sum of Tax Check'), RAW_SUBTOTAL_TAX)
        wb.Close(False)

        # ---------------------------------------------------------- 2.2
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.2']))
        xl.CalculateFullRebuild()
        n = '2.2'
        check(n, 'RawSales rows', table_rows(wb, 'RawSales'), 1025)
        ws = wb.Worksheets('Lookups')
        for label in ('XLOOKUP', 'VLOOKUP with FALSE', 'INDEX-MATCH'):
            check(n, label, val(ws, label), 'Wuse')
        ws = wb.Worksheets('Summary')
        check(n, 'Total Sales', val(ws, 'Total Sales'), F['raw_sales'])
        check(n, 'Average rating', round(float(val(ws, 'Average rating')), 2), 6.97)
        check(n, 'Transactions', val(ws, 'Transactions'), 1025)
        check(n, 'Rated 7 or above', val(ws, 'Rated 7 or above'), 508)
        check(n, 'Ikeja Sales', val(ws, 'Ikeja Sales'), F['raw_Ikeja'])
        check(n, 'Wuse Sales', val(ws, 'Wuse Sales'), F['raw_Wuse'])
        check(n, 'Trans-Amadi Sales', val(ws, 'Trans-Amadi Sales'), F['raw_Trans-Amadi'])
        check(n, 'Ikeja transactions', val(ws, 'Ikeja transactions'), F['rawN_Ikeja'])
        check(n, 'Wuse transactions', val(ws, 'Wuse transactions'), F['rawN_Wuse'])
        check(n, 'Trans-Amadi transactions', val(ws, 'Trans-Amadi transactions'), F['rawN_Trans-Amadi'])
        check(n, 'Branch Sales reconcile', val(ws, 'Branch Sales reconcile (must be 0)'), 0)
        check(n, 'Branch counts reconcile', val(ws, 'Branch counts reconcile (must be 0)'), 0)
        check(n, 'H&B exact', val(ws, 'Transactions, exact criterion'), 48)
        check(n, 'H&B wildcard', val(ws, 'Transactions, wildcard criterion'), 53)
        check(n, 'H&B wildcard Sales', val(ws, 'Sales, wildcard criterion'), 1998066.00)
        wb.Close(False)

        # ---------------------------------------------------------- 2.3
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.3']))
        xl.CalculateFullRebuild()
        n = '2.3'
        check(n, 'RawSales rows', table_rows(wb, 'RawSales'), 1025)
        check(n, 'CleanSales rows', table_rows(wb, 'CleanSales'), 1000)
        check(n, 'sheets', [s.Name for s in wb.Worksheets],
              ['Raw Export (untouched)', 'Clean Data', 'Cleaning Log', 'Verification', 'Colleague Note'])
        verify_common(n, wb)
        wb.Close(False)

        # ---------------------------------------------------------- 2.4
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.4']))
        xl.CalculateFullRebuild()
        n = '2.4'
        check(n, 'CleanSales rows', table_rows(wb, 'CleanSales'), 1000)
        verify_common(n, wb)
        ps = wb.Worksheets('Pivots')
        check(n, 'pivot count', ps.PivotTables().Count, 4)
        pt = ps.PivotTables('PT_Branch')
        for b in ('Ikeja', 'Wuse', 'Trans-Amadi'):
            check(n, f'pivot {b}', pt.GetPivotData('Sum of Sales', 'Branch', b).Value, F['clean_' + b])
        ws = wb.Worksheets('Verification')
        check(n, 'Ikeja Member SUMIFS', val(ws, 'Ikeja Member (SUMIFS)', maxrow=40), 6289577.70)
        check(n, 'TA F&B SUMIFS', val(ws, 'Trans-Amadi Food and beverages (SUMIFS)', maxrow=40), 2376685.50)
        check(n, 'GETPIVOTDATA', val(ws, 'Pivot Trans-Amadi total (GETPIVOTDATA)', maxrow=40),
              F['clean_Trans-Amadi'])
        check(n, 'pivot minus SUMIF = 0', val(ws, 'Pivot minus SUMIF (must be 0)', maxrow=40), 0)
        # the slicer must reach every pivot
        sc = wb.SlicerCaches(1)
        check(n, 'slicer connects all 4 pivots', sc.PivotTables.Count, 4)
        # a stale filter must break the reconciliation, exactly as the notes promise
        pf = pt.PivotFields('Product line')
        pf.CurrentPage = 'Food and beverages'
        xl.CalculateFullRebuild()
        stale = val(ws, 'Pivot minus SUMIF (must be 0)', maxrow=40)
        check(n, 'stale filter breaks the reconciliation', abs(float(stale)) > 1.0, True)
        check(n, 'filtered pivot shows the TA x F&B figure',
              val(ws, 'Pivot Trans-Amadi total (GETPIVOTDATA)', maxrow=40), 2376685.50)
        pf.CurrentPage = '(All)'
        xl.CalculateFullRebuild()
        check(n, 'clearing the filter restores the reconciliation',
              val(ws, 'Pivot minus SUMIF (must be 0)', maxrow=40), 0)
        wb.Close(False)

        # ---------------------------------------------------------- 2.5
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.5']))
        xl.CalculateFullRebuild()
        n = '2.5'
        verify_common(n, wb)
        dash = wb.Worksheets('Dashboard')
        charts = [s for s in dash.Shapes if s.Type == 3]
        check(n, 'dashboard chart count', len(charts), 3)
        for sh in charts:
            t = sh.Chart.ChartTitle.Text if sh.Chart.HasTitle else ''
            check(n, f'chart titled ({t[:38]})', t not in ('', 'Chart Title', 'Sum of Sales'), True)
        ev = wb.Worksheets('Chart Choice Evidence')
        check(n, 'evidence chart count', len([s for s in ev.Shapes if s.Type == 3]), 2)
        counts = clean['Payment'].value_counts()
        for i, k in enumerate(counts.index):
            check(n, f'payment {k}', ev.Cells(5 + i, 2).Value, int(counts[k]))
        check(n, 'gridlines hidden', wb.Windows(1).DisplayGridlines, False)
        sc5 = wb.SlicerCaches(1)
        sheets_with_slicers = sorted({sc5.Slicers(i + 1).Parent.Name for i in range(sc5.Slicers.Count)})
        check(n, 'a Branch slicer sits on the Dashboard', 'Dashboard' in sheets_with_slicers, True)
        check(n, 'slicer still drives every pivot', sc5.PivotTables.Count >= 4, True)
        wb.Close(False)

        # ---------------------------------------------------------- 2.6
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.6']))
        xl.CalculateFullRebuild()
        n = '2.6'
        check(n, 'CleanSales rows', table_rows(wb, 'CleanSales'), 1000)
        check(n, 'query count', wb.Queries.Count, 1)
        q = wb.Queries(1)
        check(n, 'query name', q.Name, 'Clean Ilesanmi Sales')
        f = q.Formula
        for step in ('Trimmed Text', 'Capitalized Each Word', 'Changed Type with Locale',
                     'Inserted Quantity Fixed', 'Removed Duplicates'):
            check(n, f'M step present: {step}', step in f, True)
        check(n, 'dedups on Invoice ID only', 'Table.Distinct(#"Renamed Quantity", {"Invoice ID"})' in f, True)
        verify_common(n, wb)
        ev = wb.Worksheets('Step Order Evidence')
        for i, expect in enumerate([1006, 1004, 1001, 1000]):
            check(n, f'step order row {i+1}', ev.Cells(4 + i, 2).Value, expect)
        wb.Close(False)

        # ---------------------------------------------------------- 2.7
        wb = xl.Workbooks.Open(os.path.abspath(PATHS['2.7']))
        xl.CalculateFullRebuild()
        n = '2.7'
        verify_common(n, wb)
        ws = wb.Worksheets('Known Totals')
        check(n, 'Rows', val(ws, 'Rows'), 1000)
        check(n, 'Total Sales', val(ws, 'Total Sales'), F['clean_sales'])
        check(n, 'Ikeja Sales', val(ws, 'Ikeja Sales'), F['clean_Ikeja'])
        check(n, 'Wuse Sales', val(ws, 'Wuse Sales'), F['clean_Wuse'])
        check(n, 'Trans-Amadi Sales', val(ws, 'Trans-Amadi Sales'), F['clean_Trans-Amadi'])
        check(n, 'Total quantity', val(ws, 'Total quantity'), 5510)
        check(n, 'Rated 7+ labelled', val(ws, 'Rated 7 or above (nine blank Ratings left in place)'), 496)
        pc = wb.Worksheets('Product Line Check')
        pl = clean.groupby('Product line')['Sales'].sum().sort_values(ascending=False)
        for i, (name_, v) in enumerate(pl.items()):
            check(n, f'product line {name_}', pc.Cells(4 + i, 3).Value, round(float(v), 2))
        check(n, 'six lines minus chain total = 0',
              val(pc, 'Reconciliation: six lines minus chain total (must be 0)', maxrow=30), 0)
        wb.Close(False)

    finally:
        xl.Quit()

    print(f"checks passed: {passed[0]}")
    if fails:
        print(f"\nFAILURES ({len(fails)}):")
        for f_ in fails:
            print("  -", f_)
        sys.exit(1)
    print("ALL WORKBOOK CHECKS PASSED")


if __name__ == '__main__':
    run()
