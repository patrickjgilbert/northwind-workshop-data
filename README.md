# Northwind workshop data: practice files for Claude Cowork

Practice files for the "Claude Cowork for Beginners" workshop. One fictional company, four exercises. Every file in this repository is synthetic: the company, the people, the customers, the vendors, the emails, the dollar figures. Any resemblance to a real business or person is a coincidence. The whole pack is released under CC0 (public domain), so use it however you like.

## The company

Northwind Home Services is a residential cleaning and handyman business in Portland, Maine, run by an owner named Dana Whitfield. Over the last two years Dana added a light-commercial cleaning line (condo associations, dental and medical offices, restaurants, property managers), and that line now brings in most of the roughly $2.8 million the company invoices a year. In the exercises, you play Dana.

## How to get the files

1. Click the green **Code** button near the top of this page.

   ![Code button](docs/img/01-code-button.png)

2. Choose **Download ZIP**.

   ![Download ZIP](docs/img/02-download-zip.png)

3. Unzip it (double-click on a Mac; right-click and choose Extract All on Windows) and drag the folder to your Desktop.

   ![Folder on the Desktop](docs/img/03-desktop-folder.png)

**Windows note:** the folder unzips as `northwind-workshop-data-main`, not `northwind-workshop-data`. That is normal. Open that folder when Cowork asks you to pick one.

## The four exercises

Each folder has its own README with the exact prompt to paste and a "What's planted" section so you can check Claude's answer against the truth.

| Folder | Exercise | Model | What you will get |
|---|---|---|---|
| `01-invoices-inbox/` | Clean up a messy vendor invoice inbox: read every file, rename, sort into vendor folders, build a ledger | Sonnet 5.5 | Renamed files in vendor folders, `ledger.csv`, `MOVES.md` |
| `02-sources/` | Reconcile what Northwind promised customers in Q3 2026 against what it invoiced, across Gmail, Slack, a meeting transcript, QuickBooks, HubSpot and the scheduling export | Opus 5.5 | `northwind-q3-reconciliation.xlsx` with formulas, then a formatted version |
| `03-dashboard/` | Turn 30 months of revenue by customer and service line into an offline HTML dashboard | Opus 5.5 | `northwind-dashboard.html` |
| `04-prospect/` | Prepare for a second sales call using only the pages, email and notes in the folder | Opus 5.5 | `lakeshore-call-prep.md`, graded and revised |

Do them in order if you can. Exercise 3 reads the reconciliation file from exercise 2 if it is there, and exercise 2 pays off the duplicate invoice you will meet in exercise 1.

## Use your own files instead

Nothing here depends on this company. If you have a real inbox of vendor invoices, a real set of exports, a real revenue spreadsheet or a real prospect, point Cowork at that folder and paste the same prompt. The prompts are written so the folder, not the prompt, carries the specifics. Start with a copy of your files, not the originals, and keep the "do not delete anything" and "one pass, then stop" lines; they are what make the first run safe to watch.

## How to regenerate

Folders `01`, `02` and `03` (and the one email in `04`) are produced by a single seeded script from one model, so the numbers tie out across folders. The web-page PDFs and call notes in `04` are also written by the script from text in `scripts/content.py`. To rebuild everything:

```bash
uv run --with openpyxl --with fpdf2 --with pillow python3 scripts/generate.py
uv run --with openpyxl --with fpdf2 --with pillow python3 scripts/qa_check.py
```

`generate.py` prints every planted number as it runs. `qa_check.py` asserts every planted fact and every tie-out (and that every invoice PDF extracts cleanly with `pdftotext`, which it needs installed) and exits non-zero if anything is off. The README files are written by hand.

## License

CC0 1.0 Universal. See `LICENSE`. No attribution required.
