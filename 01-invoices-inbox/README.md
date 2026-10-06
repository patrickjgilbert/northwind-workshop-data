# Exercise 1: the vendor invoice inbox

**Model: Sonnet 5.5.** Point Cowork at this folder and paste the prompt below.

This folder is Northwind's vendor invoice inbox for the third quarter of 2026, the way Elena (finance) actually receives it: scanned PDFs with camera and scanner names, email attachments called `INV (2).pdf`, two photos of receipts, a note Dana left in the tray, and one scan that came through blank. 31 files from nine vendors, plus `rules.md`.

The point of the exercise is that Claude has to open every file and read what is inside it. Nothing here can be identified from its filename alone, and a few files are meant to be flagged rather than filed.

## The prompt

```
This folder is our vendor invoice inbox and it is a mess. Reference rules.md and follow those rules exactly as written. Read every file, then sort, rename and log each one the way the rules say. Write ledger.csv and MOVES.md as the rules describe. Do not delete anything.
```

## The context file

`rules.md` is Elena's filing procedure, written down: the 7 category folders and which vendor goes in which, the exact filename pattern, the ledger columns in order, where receipts and duplicates go, and what to do with a file nobody can read or an invoice with no PO.

The prompt is short on purpose. It says what to do (sort, rename, log) and hands every decision about how to `rules.md`. "Reference rules.md and follow those rules exactly as written" does two jobs: it tells Claude to read the file before it starts, and it tells Claude the rules win over its own judgment. Without that line Claude invents its own folder scheme, its own filename style and its own ledger columns, and every run looks different. With it, every run looks like Elena did it.

Try it both ways if you have time. A run without `rules.md` gives you vendor folders and a reasonable ledger. A run with it gives you category folders, a `_receipts/` folder, a `_review/` folder and a "Needs a human" list. Same model, same files, different result, because of one page of context.

## Make it a skill

When the run is done, paste this in the same session:

```
Wait. I might have to do this again. Turn what we just did in this session into a skill called invoice-inbox, so next time it runs from one line. Put everything from rules.md inside the skill so it works in any folder. Keep it to one SKILL.md file with the steps and the rules, no scripts. Then read it back to me in five lines.
```

## What's planted

Check Claude's folders, `MOVES.md` and `ledger.csv` against this list.

| Finding | The fact | Where | What the rules say to do |
|---|---|---|---|
| Duplicate invoice | Casco Bay Janitorial Supply invoice **CB-2211**, dated July 28, 2026, **$1,184.60**, is in the folder twice: `INV (2).pdf` and `scan_0417.pdf` are byte-for-byte identical. | both files | Keep `INV (2).pdf` (first alphabetically) and file it. Move `scan_0417.pdf` to `_review/` and write "duplicate of Supplies/Casco Bay Janitorial Supply/2026-07-28_casco-bay-janitorial-supply_CB-2211.pdf" in MOVES.md. One ledger row, not two. |
| Invoice with no PO | Tidewater Plumbing invoice **TP-0893**, August 14, 2026, **$3,250.00** (emergency sewer line repair at Westbrook Crossing). Every other invoice in the folder carries a PO number; this one has none. | `plumber invoice.pdf` | File it in `Subcontractors/Tidewater Plumbing/`, ledger row with a blank PO, and list it under "Needs a human". |
| Unreadable file | `scan_0421.pdf` is a blank page. It contains no text at all. | `scan_0421.pdf` | Leave it in place, list it under "Needs a human". |
| Undated file | `note to self.txt` is a real note from Dana (five reminders about vendors) with no date anywhere in it. It is not an invoice and cannot be dated. | `note to self.txt` | Leave it in place, list it under "Needs a human". |
| Receipts, not invoices | `IMG_4502.png` (Pine Point Fuel Co-op pump receipt, Aug 9, 2026, $86.40) and `receipt.png` (Deering Hardware & Supply, Sep 14, 2026, $47.92) are readable images of receipts with no invoice numbers. | the two PNGs | Move to `_receipts/2026-08-09_pine-point-fuel-co-op_receipt.png` and `_receipts/2026-09-14_deering-hardware-and-supply_receipt.png`. No ledger row. |

Every other invoice PDF is clean and should end up renamed and filed. The full set, by category and vendor:

| Category | Vendor | Invoices (number, date, amount) |
|---|---|---|
| Supplies | Casco Bay Janitorial Supply | CB-2198 (Jul 9, $842.15), CB-2211 (Jul 28, $1,184.60, twice), CB-2240 (Aug 18, $963.40), CB-2267 (Sep 8, $1,027.90), CB-2291 (Sep 29, $778.25) |
| Vehicles and Fuel | Pine Point Fuel Co-op | PPF-77102 (Jul 31, $1,412.88), PPF-77388 (Aug 31, $1,566.02), PPF-77651 (Sep 30, $1,338.47) |
| Vehicles and Fuel | Fore River Auto & Fleet | FRA-5531 (Jul 15, $612.40), FRA-5602 (Aug 21, $2,247.19), FRA-5640 (Sep 12, $389.00) |
| Insurance | Pine Tree Mutual Insurance | PTM-2026-Q3-8841 (Jul 1, $4,860.00), PTM-2026-Q4-9107 (Sep 25, $5,115.00) |
| Subcontractors | Tidewater Plumbing | TP-0871 (Jul 22, $1,480.00), TP-0893 (Aug 14, $3,250.00, no PO), TP-0912 (Sep 16, $925.00) |
| Software | Routeboard Scheduling | RB-204411 (Jul 1, $456.00), RB-209872 (Aug 1, $456.00), RB-215306 (Sep 1, $456.00) |
| Uniforms and Print | Stitchworks Uniform Co. | SW-3310 (Jul 11, $1,096.50), SW-3377 (Sep 3, $448.00) |
| Uniforms and Print | Old Port Print & Sign | OPP-1188 (Jul 18, $312.75), OPP-1243 (Sep 10, $684.00) |
| Grounds | Greenline Lawn & Snow | GL-2026-0712 (Jul 31, $2,150.00), GL-2026-0804 (Aug 31, $2,150.00), GL-2026-0909 (Sep 30, $2,380.00) |

28 PDFs in all: 27 invoice PDFs (26 unique invoices plus the duplicate) and the blank scan. `ledger.csv` should have 26 rows totaling $38,581.51. Every nameable PDF has the vendor, invoice number, date, amount, PO and "Bill To: Northwind Home Services" as extractable text (checked with `pdftotext` by `scripts/qa_check.py`).

What a correct run leaves behind:

```
Supplies/Casco Bay Janitorial Supply/                5 invoices
Vehicles and Fuel/Pine Point Fuel Co-op/             3
Vehicles and Fuel/Fore River Auto & Fleet/           3
Insurance/Pine Tree Mutual Insurance/                2
Subcontractors/Tidewater Plumbing/                   3
Software/Routeboard Scheduling/                      3
Uniforms and Print/Stitchworks Uniform Co/           2
Uniforms and Print/Old Port Print & Sign/            2
Grounds/Greenline Lawn & Snow/                       3
_receipts/                                           2 receipts
_review/scan_0417.pdf                                the duplicate
scan_0421.pdf, note to self.txt                      left in place
ledger.csv, MOVES.md, README.md, rules.md
```

"Needs a human" in MOVES.md should list exactly three items: `scan_0421.pdf` (blank), `note to self.txt` (no date, not an invoice) and TP-0893 (no PO, $3,250.00).

## Things to watch for in Claude's answer

- Did it read the receipts (images) or skip them?
- Did it create two ledger rows for CB-2211, or one row and a `_review/` copy?
- Did it try to name `scan_0421.pdf` from the filename pattern, or leave it alone?
- Did it use the vendor slugs from `rules.md` (`fore-river-auto-and-fleet`, `stitchworks-uniform`) or make up its own?
- Did it put `$` signs or commas in the amount column? The rules say plain numbers.
- The PO numbers in the ledger are what exercise 2 would use to match these bills to `quickbooks-bills-paid-q3.csv`, where CB-2211 shows up paid twice.
