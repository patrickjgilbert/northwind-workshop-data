# Exercise 3: the revenue dashboard

**Model: Opus 5.5.** Point Cowork at this folder. Two prompts, one after the other. The first one builds a dashboard with no brand guidance and is meant to look generic. The second one rebuilds it from `brand-guidelines.md`.

`northwind-revenue-30mo.xlsx` is 30 months of Northwind's revenue, April 2024 through September 2026, by customer and service line (Residential cleaning, Commercial cleaning, Handyman), with direct cost, crew hours and job counts. `revenue_30mo.csv` is the same Monthly sheet as a CSV. Three sheets:

| Sheet | What it holds |
|---|---|
| Monthly | one row per customer x month x service line: `month_end` (a real date), `month` (text, yyyy-mm), `customer_id`, `customer`, `service_line`, `revenue`, `direct_cost`, `crew_hours`, `jobs`. About 1,100 rows. |
| Customers | the 36 customers, type, segment, neighborhood, cadence, first and last month, contact, notes |
| Notes | column definitions and the two sentences below about dates and the tie-out |

Revenue is invoiced revenue by invoice month. **July, August and September 2026 equal the Q3 QuickBooks invoices in `02-sources/quickbooks-invoices-q3.csv` to the cent, by customer and by month.** `scripts/qa_check.py` asserts that.

## Prompt 1 (the generic version, on purpose)

```
northwind-revenue-30mo.xlsx is 30 months of revenue by customer and service line, with crew hours and direct cost. Build one self-contained HTML dashboard, northwind-dashboard.html, that I can open offline: a KPI row (trailing-12-month revenue, gross margin, active customers, revenue per crew hour), revenue and margin trend by month, customer concentration with any customer over 25% flagged, and service-line mix over time. Compute everything from the data; do not hardcode numbers. Put a short note at the top naming the two trends leadership should worry about. Build it in one pass and stop. Do not screenshot or test it, I will open it myself.
```

This prompt says nothing about how the dashboard should look, so Claude falls back on the average of every dashboard it has seen: a system font, a blue or purple accent, rounded cards with soft shadows, a donut chart, a legend under every chart, and section titles like "Revenue Overview". The numbers will be right. It will look like every other AI dashboard. That is the point of running it first.

## Prompt 2 (the brand pass)

```
Now reference brand-guidelines.md and follow those guidelines exactly as written. Rebuild the dashboard so it looks like Northwind made it. Do not change a single number. Save it as northwind-dashboard-branded.html. One pass, then stop. Do not screenshot or test it.
```

Open the two files side by side. Same data, same numbers, and the second one should be unmistakably Northwind's.

## The context file

`brand-guidelines.md` is the one-pager a designer would hand over: 8 named colors with hex codes and a role for each, three fonts with sizes and fallbacks, layout rules (12-column grid, 1px borders, no shadows, corners no rounder than 4px), chart rules (one accent color, direct labels, no pie or donut charts, the flagged item in Buoy Orange), number formats ($2.78M, 51.8%) and a headline voice that states the finding as a sentence.

It only comes in on the second pass. "Reference brand-guidelines.md and follow those guidelines exactly as written" tells Claude to read the file before it touches the HTML and to treat every line as a rule, not a suggestion. Vague words like "make it look professional" get you the generic version again. Specific words (hex codes, font names, "no donut charts", "headlines state the finding") are vocabulary Claude can act on. The file is that vocabulary, written down once.

What to look for in the branded version: Fraunces headlines that read as sentences ("Eastern Promenade is 31.0% of revenue"), numbers in IBM Plex Mono, Sea Glass as the only data color, Eastern Promenade's bar in Buoy Orange as the one flag, horizontal bars instead of a donut for concentration, square-cornered cards with a thin border and no shadow, and a NORTHWIND wordmark with a compass glyph.

## Make it a skill

When the branded dashboard is done, paste this in the same session:

```
Wait. I might have to do this again. Turn what we just did in this session into a skill called monthly-dashboard, so next time it runs from one line. Put everything from brand-guidelines.md inside the skill so it works in any folder. Keep it to one SKILL.md file with the steps and the rules, no scripts. Then read it back to me in five lines.
```

## What's planted

| Finding | The fact | How to check |
|---|---|---|
| **Customer concentration** | Eastern Promenade Condominium Association is **31.0% of trailing-12-month revenue** (October 2025 through September 2026). It is the only customer over 25%; the next largest (Westbrook Crossing Professional Park) is about 13%. Its share grew: it was a smaller share in 2024 and 2025 and stepped up in January 2026. | Sum `revenue` for 2025-10 to 2026-09, by customer. Total is about $2.78M; Eastern Promenade is about $862K. |
| **Handyman margin walking down** | Crew hours per handyman job rise from about **2.2 (spring 2024) to about 3.4 (summer 2026)** while price per job stays roughly flat around $500. Handyman gross margin falls from about 63% to about 45%. Handyman revenue is still growing, which is why nobody noticed. The September ops transcript in `02-sources` has Elena saying the same thing. | Filter `service_line` = Handyman: `crew_hours / jobs` and `(revenue - direct_cost) / revenue` by month. |
| **Summer seasonality** | Rental turnovers (Casco Coast Property Management, Longfellow Street Rentals, Peaks Island Rentals) peak June through August and nearly stop in winter. July turnover revenue is about 4.5x January. Everything else is flat month to month, so total revenue has a visible summer bump. | Those three customers by calendar month. |
| **Dates as text** (teaching point) | Column A `month_end` is a real date. Column B `month` is the same month as text ("2026-09"). `EOMONTH`, `YEAR`, `MONTH` and date math on column B return 0 or errors; on column A they work. A dashboard that groups by column B as a label is fine; one that tries to do date math on it is not. | Try `=EOMONTH(B2,0)` vs `=EOMONTH(A2,0)`. |
| **Work with no revenue** | Back Cove Bakery, August 2026, Handyman: 3 jobs, 9.25 crew hours, $0 revenue. That is the unbilled work from exercise 2 showing up as cost with no revenue. It is the only row in the file with jobs and no revenue. | Filter `revenue` = 0 and `jobs` > 0. |

Two trends leadership should worry about, for checking Claude's note at the top: concentration (one customer at 31%, and the Lakeshore deal in `02-sources/hubspot-deals.xlsx` would add a second large one) and the handyman margin.

Expected KPI ballparks for the trailing 12 months: revenue about $2.78M, gross margin about 52%, 33 customers with revenue in September 2026 (36 in the file, three of them former), revenue per crew hour about $72. Claude's exact figures depend on how it defines "active" and whether it includes $0-revenue rows, and that is a fair thing to ask it to state.
