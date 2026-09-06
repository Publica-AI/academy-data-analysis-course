# -*- coding: utf-8 -*-
"""Excel COM helpers shared by the Module 2 solution-workbook builders."""
import datetime as dt
import math
import os

import win32com.client as w32

# Excel enums
xlSrcRange, xlYes = 1, 1
xlDatabase = 1
xlRowField, xlColumnField, xlPageField, xlDataField = 1, 2, 3, 4
xlSum, xlAverage, xlCount = -4157, -4106, -4112
xlOpenXMLWorkbook = 51
xlBarClustered, xlColumnClustered, xlPie = 57, 51, 5
xlCalculationAutomatic, xlCalculationManual = -4105, -4135

MONEY = '"₦"#,##0.00'
INT = '#,##0'
DATE = 'dd/mm/yyyy'
TEXT = '@'
RATE = '0.00%'


def start_excel():
    xl = w32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = False
    xl.DisplayAlerts = False
    xl.ScreenUpdating = False
    return xl


def set_manual(xl):
    """Only settable once a workbook is open."""
    try:
        xl.Calculation = xlCalculationManual
    except Exception:
        pass


def clean_val(v):
    """pandas value -> something COM will accept."""
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    if isinstance(v, (dt.datetime, dt.date)):
        return dt.datetime(v.year, v.month, v.day)
    if hasattr(v, 'item'):
        try:
            v = v.item()
        except Exception:
            pass
    if isinstance(v, float) and math.isnan(v):
        return None
    if isinstance(v, str) and v[:1] in ('=', '+', '@'):
        # Excel would parse this as a formula. A leading apostrophe forces text and is
        # not part of the stored value.
        return "'" + v
    return v


def write_grid(ws, top, left, rows):
    """Write a list of lists starting at (top,left). Blank-safe.

    Excel's array-assignment path rejects strings longer than 255 characters, so any
    block containing one is written cell by cell instead.
    """
    if not rows:
        return
    h, w = len(rows), max(len(r) for r in rows)
    block = [[clean_val(r[i]) if i < len(r) else None for i in range(w)] for r in rows]
    long_text = any(isinstance(v, str) and len(v) > 255 for row in block for v in row)
    if not long_text:
        ws.Range(ws.Cells(top, left), ws.Cells(top + h - 1, left + w - 1)).Value = block
        return
    for i, row in enumerate(block):
        for j, v in enumerate(row):
            if v is not None:
                ws.Cells(top + i, left + j).Value = v


def write_table(ws, df, name, top=1, left=1, text_cols=(), date_cols=(), money_cols=(),
                int_cols=(), style="TableStyleMedium2"):
    """Write a DataFrame as a real structured table (ListObject) and return it."""
    ncols = len(df.columns)
    nrows = len(df)
    # pre-set number formats on the columns that must not be coerced
    for cname in text_cols:
        c = left + list(df.columns).index(cname)
        ws.Range(ws.Cells(top + 1, c), ws.Cells(top + nrows, c)).NumberFormat = TEXT

    write_grid(ws, top, left, [list(df.columns)])
    body = df.values.tolist()
    # chunk the body so a single COM call never gets enormous
    CH = 500
    for i in range(0, nrows, CH):
        write_grid(ws, top + 1 + i, left, body[i:i + CH])

    rng = ws.Range(ws.Cells(top, left), ws.Cells(top + nrows, left + ncols - 1))
    lo = ws.ListObjects.Add(xlSrcRange, rng, None, xlYes)
    lo.Name = name
    lo.TableStyle = style

    for cname, fmt in ([(c, DATE) for c in date_cols] + [(c, MONEY) for c in money_cols]
                       + [(c, INT) for c in int_cols]):
        if cname in list(df.columns):
            lo.ListColumns(cname).DataBodyRange.NumberFormat = fmt
    return lo


def add_calc_column(lo, header, formula, fmt=None):
    """Append a calculated column to a ListObject and fill it."""
    lc = lo.ListColumns.Add()
    lc.Name = header
    lc.DataBodyRange.Formula = formula
    if fmt:
        lc.DataBodyRange.NumberFormat = fmt
    return lc


def title(ws, row, text, size=13):
    c = ws.Cells(row, 1)
    c.Value = text
    c.Font.Bold = True
    c.Font.Size = size
    return row + 1


def note(ws, row, text, col=1, italic=True):
    c = ws.Cells(row, col)
    c.Value = clean_val(text)
    c.Font.Italic = italic
    return row + 1


def check_row(ws, row, label, formula, fmt=None, expected=None, label_col=1):
    """label | live formula | expected. Returns the next row."""
    ws.Cells(row, label_col).Value = clean_val(label)
    cell = ws.Cells(row, label_col + 1)
    cell.Formula = formula
    if fmt:
        cell.NumberFormat = fmt
    if expected is not None:
        exp_cell = ws.Cells(row, label_col + 2)
        exp_cell.NumberFormat = TEXT
        exp_cell.Value = str(expected)
    return row + 1


def header_row(ws, row, headers, col=1, bold=True):
    write_grid(ws, row, col, [headers])
    rng = ws.Range(ws.Cells(row, col), ws.Cells(row, col + len(headers) - 1))
    rng.Font.Bold = bold
    rng.Interior.Color = 0xEFEFEF
    return row + 1


def autofit(ws, last_col=24):
    try:
        ws.Range(ws.Columns(1), ws.Columns(last_col)).AutoFit()
    except Exception:
        pass


def wrap_block(ws, row, lines, col=1, width=110):
    """Write a paragraph as one line per row, so it stays readable without merged cells."""
    for ln in lines:
        ws.Cells(row, col).Value = ln
        row += 1
    return row


def save(wb, path):
    if os.path.exists(path):
        os.remove(path)
    wb.SaveAs(path, FileFormat=xlOpenXMLWorkbook)


def recalc(xl):
    try:
        xl.Calculation = xlCalculationAutomatic
    except Exception:
        pass
    xl.CalculateFullRebuild()
