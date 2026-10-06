# How Northwind files vendor invoices

Elena (finance) owns this process. These rules cover every file that lands in the invoice inbox. If a rule and a hunch disagree, follow the rule.

## 1. Read the file, not the filename

Open every file and read what is printed inside it. The vendor, invoice date, invoice number, PO number and total all come from the document itself. Filenames like `scan_0412.pdf` or `INV (2).pdf` tell you nothing.

Leave `README.md` and `rules.md` where they are. They are not invoices and do not go in the log.

## 2. Category folders

Every invoice goes in `<Category>/<Vendor>/`. There are 7 categories. This is the full vendor map:

| Vendor (as printed on the invoice) | Category | Folder | Vendor slug |
|---|---|---|---|
| Casco Bay Janitorial Supply | Supplies | `Supplies/Casco Bay Janitorial Supply/` | `casco-bay-janitorial-supply` |
| Pine Point Fuel Co-op | Vehicles and Fuel | `Vehicles and Fuel/Pine Point Fuel Co-op/` | `pine-point-fuel-co-op` |
| Fore River Auto & Fleet | Vehicles and Fuel | `Vehicles and Fuel/Fore River Auto & Fleet/` | `fore-river-auto-and-fleet` |
| Pine Tree Mutual Insurance | Insurance | `Insurance/Pine Tree Mutual Insurance/` | `pine-tree-mutual-insurance` |
| Tidewater Plumbing | Subcontractors | `Subcontractors/Tidewater Plumbing/` | `tidewater-plumbing` |
| Routeboard Scheduling | Software | `Software/Routeboard Scheduling/` | `routeboard-scheduling` |
| Stitchworks Uniform Co. | Uniforms and Print | `Uniforms and Print/Stitchworks Uniform Co/` | `stitchworks-uniform` |
| Old Port Print & Sign | Uniforms and Print | `Uniforms and Print/Old Port Print & Sign/` | `old-port-print-and-sign` |
| Greenline Lawn & Snow | Grounds | `Grounds/Greenline Lawn & Snow/` | `greenline-lawn-and-snow` |

The vendor folder is the vendor name as printed, with any trailing period removed (Windows does not allow a folder name that ends in a period).

A vendor that is not on this list: do not invent a category. File nothing for it and list it under "Needs a human".

## 3. Filenames

Rename every invoice:

```
YYYY-MM-DD_vendor-slug_invoice-number.pdf
```

- **Date** is the invoice date printed on the document, not the due date and not the date the file was saved.
- **Invoice number** exactly as printed, capitals and hyphens kept.
- **Vendor slug** is in the table above. For a new vendor the rules are: lowercase, spaces become hyphens, drop "Co." and "Inc.", "&" becomes "and", remove any other punctuation.

Example: Fore River Auto & Fleet invoice FRA-5602 dated August 21, 2026 becomes

```
Vehicles and Fuel/Fore River Auto & Fleet/2026-08-21_fore-river-auto-and-fleet_FRA-5602.pdf
```

## 4. ledger.csv

One row per invoice filed, in the inbox folder, sorted by date, oldest first. The columns, in this order, with this exact header row:

```
date,vendor,category,invoice_number,po_number,amount,new_path
```

- `date` as YYYY-MM-DD.
- `vendor` exactly as printed on the invoice.
- `amount` is the invoice total as a plain number with 2 decimals: `1184.60`, not `$1,184.60`.
- `po_number` blank if the invoice has none.
- `new_path` is the path from the inbox folder, for example `Supplies/Casco Bay Janitorial Supply/2026-07-09_casco-bay-janitorial-supply_CB-2198.pdf`.

Receipts, duplicates and files left in place do not get a ledger row.

## 5. Receipts

A receipt is not an invoice: a pump receipt, a register receipt, anything with no invoice number. Move receipts to `_receipts/` and name them

```
YYYY-MM-DD_store-slug_receipt.png
```

using the date printed on the receipt and the store name slugged with the same rules (for example `deering-hardware-and-supply`). Keep the original file extension.

## 6. Duplicates

Two files are duplicates when they show the same vendor and the same invoice number. Keep the one whose original filename comes first alphabetically and file it normally. Move the other one, under its original filename, to `_review/`. In MOVES.md, write "duplicate of" and the new path of the file you kept. Never delete either copy.

## 7. Files you cannot file

Blank, unreadable or undated files: leave them where they are. List each one under "Needs a human" in MOVES.md with the reason, for example "blank page, no text" or "no date anywhere in the file".

## 8. Missing PO numbers

We need a PO for anything over $500. Any invoice without a PO number still gets filed and logged the normal way, with the `po_number` column left blank. Then list it under "Needs a human" with the vendor, invoice number and amount.

## 9. MOVES.md

Write MOVES.md in the inbox folder with two parts.

First, a table with one row for every file that was in the inbox (except `README.md` and `rules.md`):

| Original file | New path | How identified |
|---|---|---|
| `casco bay july.pdf` | `Supplies/Casco Bay Janitorial Supply/2026-07-09_casco-bay-janitorial-supply_CB-2198.pdf` | Vendor, invoice number, date and total read from the PDF text |

For a duplicate, the new path is its `_review/` path and the "How identified" cell starts with "duplicate of". For a file left in place, the new path is "left in place".

Second, a section headed `## Needs a human`, one bullet per item, each with the file name and the reason.

## 10. Never delete

Move and rename only. Nothing in this folder gets deleted, including blank scans and duplicates.
