# Module 2 dataset: Ilesanmi Stores point-of-sale export

## Scenario

Ilesanmi Retail Limited, trading as **Ilesanmi Stores**, is a fictional three-branch Nigerian
supermarket chain. Origin Analytics, a Lagos consultancy, has been engaged to turn the chain's
monthly point-of-sale export into a reporting workbook the regional manager can trust.

| Branch | City |
|---|---|
| Ikeja | Lagos |
| Wuse | Abuja |
| Trans-Amadi | Port Harcourt |

All monetary values are in Naira (₦). The export covers 1 January to 30 March 2019.
No real person, business or transaction is represented in this file.

## Files

| File | Rows | Role |
|---|---|---|
| `Ilesanmi_Sales_Raw_Export.csv` | 1,025 | The export exactly as the POS system produces it. Issued to trainees. |
| `Ilesanmi_Sales_Raw_Export.xlsx` | 1,025 | The same file as a workbook, every fault preserved. Issued to trainees. |
| `Ilesanmi_Sales_Clean_AnswerKey.xlsx` | 1,000 | Cleaned, formatted, with a Verification sheet of live formulas. **Instructor copy, never issued.** |

The raw file ships in both formats deliberately: CSV is what a POS system actually produces,
and the programme's content standard requires XLSX distribution for Excel modules.

## Column dictionary

| Column | Type | Notes |
|---|---|---|
| Invoice ID | Text | `NNN-NN-NNNN`. One per completed sale. This is the column that defines a duplicate. |
| Branch | Text | Ikeja, Wuse or Trans-Amadi. |
| City | Text | Lagos, Abuja or Port Harcourt. One city per branch. |
| Customer type | Text | Member or Normal. |
| Gender | Text | Female or Male. |
| Product line | Text | Six categories. **Carries an injected fault, see below.** |
| Unit price | Number | ₦1,008.00 to ₦9,996.00. |
| Quantity | Integer | 1 to 10. **Carries an injected fault, see below.** |
| Tax 5% | Number | 5% of cogs. |
| Sales | Number | cogs + Tax 5%. |
| Date | Text | **Carries an injected fault, see below.** |
| Time | Text | `h:mm:ss AM/PM`, 10:00 to 20:59. |
| Payment | Text | Cash, Credit card or Ewallet. |
| cogs | Number | Unit price × Quantity. |
| gross margin percentage | Number | Constant 4.761904762 across every row. |
| gross income | Number | Equal to Tax 5% in this dataset. |
| Rating | Number | 4.0 to 10.0. **Carries an injected fault, see below.** |

Arithmetic holds exactly to two decimal places on every row:
`cogs = Unit price × Quantity`, `Tax 5% = cogs × 0.05`, `Sales = cogs + Tax 5%`.

## Injected faults, and the expected outcome of repairing them

Every fault below was injected deliberately and is reproducible from the answer key.

| Fault | Count | How to detect it | Correct repair |
|---|---|---|---|
| Duplicated Invoice IDs | 25 | Conditional Formatting on Invoice ID | Remove Duplicates **on Invoice ID only** |
| Product line in ALL CAPS with a trailing space | 102 | `LEN` before and after `TRIM` | `=PROPER(TRIM(...))`, then paste values |
| Dates written `DD-MM-YYYY` instead of `M/D/YYYY` | 51 | Left-aligned in the cell; date formulas fail | Text to Columns, Date: DMY |
| Blank Rating | 10 (9 survive deduplication) | `=COUNTBLANK` | Leave, flag, or fill only if confirmed |
| Sign-flipped Quantity | 5 | Sort Quantity ascending | `cogs ÷ Unit price` recovers the true value |

Of the 25 duplicated Invoice IDs, **19 are exact copies in every column**. The remaining 6 differ
in exactly one field: three by date format, two by Product line casing, and one
(`263-10-3913`) by a blank Rating on one of the two rows.

**The Remove Duplicates trap.** Excel's Remove Duplicates dialog opens with every column ticked.
Left on that default it removes only the 19 exact copies and leaves **1,006** rows, with six
duplicated sales still in the file. Ticking Invoice ID alone removes all 25 and leaves **1,000**.
Both runs are the tool behaving correctly; only one answers the client's question.

The five sign-flipped quantities are **correctable, not merely flaggable**: `cogs` and
`Unit price` are both intact on those rows, so the true quantity is recoverable from the file
itself. This is why the answer key holds 1,000 rows and not 995.

## Expected outputs after a correct cleaning pass

| Check | Expected |
|---|---|
| Rows | 1,000 |
| Duplicated Invoice IDs | 0 |
| Chain total Sales | ₦32,296,674.90 |
| Ikeja | ₦10,620,037.05 |
| Wuse | ₦10,619,767.20 |
| Trans-Amadi | ₦11,056,870.65 |
| Transactions rated 7 or above | 501 |
| Average rating | 6.97 |
| Total quantity | 5,510 |

Raw-file figures, for the Topic 2.2 comparison, are ₦11,062,565.85 (Ikeja),
₦10,755,627.75 (Wuse), ₦11,338,588.80 (Trans-Amadi), ₦33,156,782.40 (chain), 508 rated 7 or above.

## Provenance and licence

Adapted from the public "Supermarket Sales" dataset on Kaggle (originally a three-branch retail
chain in Myanmar), re-scenarioed to a Nigerian context. Branch and city labels were replaced,
monetary values were rescaled by a constant factor of 100 to give plausible Naira amounts, and
the faults listed above were injected by script. Row counts, distributions and all internal
arithmetic relationships are unchanged from the source. The source dataset carries no personal
data, and none was introduced.
