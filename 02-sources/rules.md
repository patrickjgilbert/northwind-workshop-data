# How Northwind works with data

These rules apply to any analysis, reconciliation or report built from Northwind's files. Dana's version: use a calculator to compute any math, do not guess. If any data is missing from an equation, or if anything is unclear, flag it before you move forward.

## 1. Math

- Do every calculation with spreadsheet formulas or code. Never do arithmetic in your head and never estimate.
- Do not guess. If a number is not in the files, you do not have it.

## 2. Sources

- Every number in the output must trace to a file and a row or line. Put the source next to the number: the filename plus the invoice number, job ID, bill number, row number, Slack date and time, or transcript timestamp.
- Use customer names exactly as spelled in `quickbooks-invoices-q3.csv`. Slack and email use short names ("Eastern Prom", "Pleasant Hill Vet"); map them to the QuickBooks name.

## 3. When something is missing or unclear, stop and ask

- If a number you need for a calculation is missing, or a source can be read two ways, stop before you build anything.
- List your questions. For each one, name the files involved and the readings you are choosing between.
- Wait for answers. Do not pick a reading yourself and footnote it.

## 4. Definitions

- **Q3** means July 1 to September 30, 2026, both days included.
- **A promise** is anything Dana or a crew lead committed to a customer in writing (email or Slack) or out loud in the recorded ops meeting. The crew leads are Marisol (Crew A), Devin (Crew B), Kenji (Crew C) and Rafael (handyman). A signed agreement, shown as Closed Won in HubSpot, is a promise too.
- **A promised credit or price change is owed** even if it was never issued.
- **Vendor bills** (`quickbooks-bills-paid-q3.csv`) are in scope only to catch duplicate payments: the same vendor invoice number paid more than once. Nothing else about vendor spend belongs in the reconciliation.

## 5. The workbook

- Real formulas, not pasted values. Summary totals are formulas that point at the By Customer and Exceptions tabs.
- Summary shows revenue invoiced, jobs completed, promised but not invoiced, and invoiced but not promised.
- By Customer has one row per customer with Q3 jobs, invoices or a signed deal.
- Exceptions has one row per exception. Columns: customer or vendor, what was promised, what was invoiced or paid, dollars at stake, source.
- Dollars at stake is a number, not text. `1200`, not "about $1.2K".
