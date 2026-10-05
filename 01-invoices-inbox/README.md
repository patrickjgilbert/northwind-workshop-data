# Exercise 1: the vendor invoice inbox

**Model: Sonnet 5.5.** Point Cowork at this folder and paste the prompt below.

This folder is Northwind's vendor invoice inbox for the third quarter of 2026, the way Elena (finance) actually receives it: scanned PDFs with camera and scanner names, email attachments called `INV (2).pdf`, two photos of receipts, a note Dana left in the tray, and one scan that came through blank. About 30 files from nine vendors.

The point of the exercise is that Claude has to open every file and read what is inside it. Nothing here can be identified from its filename alone, and a few files are meant to be flagged rather than filed.

## The prompt

```
This folder is our vendor invoice inbox and it is a mess. Read every file. Group them by vendor, rename each one YYYY-MM-DD_vendor_invoice-number.pdf using the date and number printed inside the document, not the filename, and move it into a folder for that vendor. Write ledger.csv with one row per invoice: date, vendor, invoice number, amount, PO number if there is one, and the new filename. Write MOVES.md listing every file, what you did with it, and how you identified it. If a file is unreadable, empty, or you are not sure what it is, leave it where it is and flag it in MOVES.md. Do not guess. Do not delete anything.
```

## What's planted

Check Claude's `MOVES.md` and `ledger.csv` against this list.

| Finding | The fact | Where |
|---|---|---|
| Duplicate invoice | Casco Bay Janitorial Supply invoice **CB-2211**, dated July 28, 2026, **$1,184.60**, is in the folder twice: `INV (2).pdf` and `scan_0417.pdf` are byte-for-byte identical. A good answer files one and flags the other as a duplicate, not two ledger rows. | both files |
| Invoice with no PO | Tidewater Plumbing invoice **TP-0893**, August 14, 2026, **$3,250.00** (emergency sewer line repair at Westbrook Crossing). Every other invoice in the folder carries a PO number; this one has none. | `plumber invoice.pdf` |
| Unreadable file | `scan_0421.pdf` is a blank page. It contains no text at all. It should be left in place and flagged, not named. | `scan_0421.pdf` |
| Undated file | `note to self.txt` is a real note from Dana (five reminders about vendors) with no date anywhere in it. It is not an invoice and cannot be dated. Flag it. | `note to self.txt` |
| Receipts, not invoices | `IMG_4502.png` (Pine Point Fuel Co-op pump receipt, Aug 9, 2026, $86.40) and `receipt.png` (Deering Hardware & Supply, Sep 14, 2026, $47.92) are readable images of receipts. A good answer reads them, says what they are, and either files them as receipts or flags that they are not invoices. They have no invoice numbers. | the two PNGs |

The other 25 invoice PDFs are clean and should all end up renamed and filed. The full set, by vendor:

| Vendor | Invoices (number, date, amount) |
|---|---|
| Casco Bay Janitorial Supply | CB-2198 (Jul 9, $842.15), CB-2211 (Jul 28, $1,184.60, twice), CB-2240 (Aug 18, $963.40), CB-2267 (Sep 8, $1,027.90), CB-2291 (Sep 29, $778.25) |
| Pine Point Fuel Co-op | PPF-77102 (Jul 31, $1,412.88), PPF-77388 (Aug 31, $1,566.02), PPF-77651 (Sep 30, $1,338.47) |
| Fore River Auto & Fleet | FRA-5531 (Jul 15, $612.40), FRA-5602 (Aug 21, $2,247.19), FRA-5640 (Sep 12, $389.00) |
| Pine Tree Mutual Insurance | PTM-2026-Q3-8841 (Jul 1, $4,860.00), PTM-2026-Q4-9107 (Sep 25, $5,115.00) |
| Tidewater Plumbing | TP-0871 (Jul 22, $1,480.00), TP-0893 (Aug 14, $3,250.00, no PO), TP-0912 (Sep 16, $925.00) |
| Stitchworks Uniform Co. | SW-3310 (Jul 11, $1,096.50), SW-3377 (Sep 3, $448.00) |
| Routeboard Scheduling | RB-204411 (Jul 1, $456.00), RB-209872 (Aug 1, $456.00), RB-215306 (Sep 1, $456.00) |
| Old Port Print & Sign | OPP-1188 (Jul 18, $312.75), OPP-1243 (Sep 10, $684.00) |
| Greenline Lawn & Snow | GL-2026-0712 (Jul 31, $2,150.00), GL-2026-0804 (Aug 31, $2,150.00), GL-2026-0909 (Sep 30, $2,380.00) |

26 invoice PDFs, 25 unique invoices, total of the unique set $38,581.51. Every nameable PDF has the vendor, invoice number, date, amount, PO and "Bill To: Northwind Home Services" as extractable text (checked with `pdftotext` by `scripts/qa_check.py`).

## Things to watch for in Claude's answer

- Did it read the receipts (images) or skip them?
- Did it create two ledger rows for CB-2211, or one row and a flag?
- Did it try to name `scan_0421.pdf` from the filename pattern, or leave it alone?
- Did it keep the originals and copy, or move? Either is fine as long as nothing was deleted.
- The PO numbers in the ledger are what exercise 2 would use to match these bills to `quickbooks-bills-paid-q3.csv`, where CB-2211 shows up paid twice.
