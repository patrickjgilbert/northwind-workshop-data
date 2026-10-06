# Exercise 2: what we promised vs what we invoiced

**Model: Opus 5.5.** Point Cowork at this folder. Two prompts, one after the other.

This folder is Northwind's third quarter of 2026 (July through September) as it exists across six systems, exported the way each system exports:

| File | What it is |
|---|---|
| `gmail-export/` | 8 email threads saved from Gmail as PDFs (print to PDF), named the way Gmail names them |
| `slack-export/ops-channel.txt` | the #ops channel, July 1 to September 30, about 80 lines |
| `meeting-transcript-2026-09-18-ops.txt` | Zoom transcript of the September ops meeting, about 2,500 words |
| `quickbooks-invoices-q3.csv` | every customer invoice issued July 1 to September 30 (about 130 rows). Cleaning customers get one statement per month, handyman work gets one invoice per customer per month |
| `quickbooks-bills-paid-q3.csv` | every vendor bill paid in Q3 (about 45 rows) |
| `hubspot-deals.xlsx` | the sales pipeline, 15 deals, amount is monthly |
| `jobs-export.csv` | every job from the scheduling system (Routeboard) in Q3, about 450 rows, with the invoice it was billed on (blank when it was never invoiced) |

Everything in here reconciles except six planted things, plus two that depend on how you answer Claude's questions. All of them are below.

`rules.md` is the context file for this exercise. See "The context file" below.

## Prompt 1

```
This folder holds exports from five places: our Gmail (saved as PDFs), our Slack ops channel, the transcript of our September ops meeting, our QuickBooks invoices and bills for Q3, our HubSpot deals, and the jobs export from our scheduling system. Reference rules.md and follow those rules exactly as written. Reconcile what we promised customers in Q3 2026 against what we actually invoiced them. Build northwind-q3-reconciliation.xlsx with three tabs: Summary, By Customer, and Exceptions (one row per mismatch, with the dollars at stake and the source that proves it). Then tell me in plain English the four things you would fix first, with the dollars attached. Build it in one pass and stop. Do not test it, I will open it myself.
```

## Prompt 2

```
Now make it readable without changing a single number: frozen headers, autosized columns, currency formats, conditional formatting on the Exceptions tab so anything over $1,000 is red, a dropdown on the Summary tab that filters By Customer, and in-cell sparklines of invoiced amount by month per customer. One accent color plus grey. Save it over the same file. One pass, then stop.
```

## The context file

`rules.md` is how Northwind works with data, on one page. Dana's version is two sentences: use a calculator to compute any math, do not guess; if any data is missing from an equation, or if anything is unclear, flag it before you move forward. The file turns that into rules Claude can follow: every number comes from a formula or code, every number carries its source, Q3 means July 1 to September 30, customer names match QuickBooks, what counts as a promise, and what the workbook must look like.

The prompt no longer spells out the workbook rules or the definitions. They live in `rules.md`, so they are the same every quarter and nobody has to remember to type them. "Reference rules.md and follow those rules exactly as written" tells Claude to read the file first and to let it overrule the prompt where the two disagree.

They do disagree in one place, on purpose. The prompt says "build it in one pass and stop". The rules say that if a number is missing or a source can be read two ways, stop and ask before building anything. A careful run follows the rules: it reads everything, comes back with a short list of questions, and waits. That is the behavior you want from a new hire with your books, and it is the teaching point. Answer the questions in the chat (the answers are below) and Claude builds the workbook.

## If Claude stops to ask

These are the questions a careful run is likely to ask, and the answers to give. Type the answer as written.

| Likely question | Why it is a real question | Answer to give |
|---|---|---|
| Does Munjoy Hill Senior Residence count from July, or from August? | HubSpot shows the deal Closed Won on July 8 at $2,400 a month, and Lorraine's July 10 email asks for a first visit the week of July 20. A run can defend July to September ($7,200) or August and September only ($4,800). | "Count Munjoy Hill from July: $7,200. July is the start date in the signed deal." |
| Is Pleasant Hill Veterinary a flat monthly price or per visit? | HubSpot shows $3,290 in the "Amount (monthly)" column. QuickBooks bills per visit at $760: $2,280 for August (3 visits from the August 17 start) and $3,040 for September (4 visits). If the contract is flat, September is $250 under. | "Treat Pleasant Hill Vet as flat monthly per HubSpot: $3,290 a month. August was a partial first month, leave it as invoiced. September is $250 under." |
| What do we charge for the Tanabe-Morrill deck railing? | Slack (Sep 3, 09:40) and the transcript (00:02:49) say Rafael did the job in 4 hours against a 2.5-hour quote. There is no job in `jobs-export.csv`, no invoice and no price anywhere. | "Leave Tanabe-Morrill as unpriced, flag only. Put it on Exceptions with $0 and the note 'unpriced, flag only'. Do not estimate a price." |
| Do open deals count as promises (Lakeshore, Ledgewood, Westbrook Crossing annex)? | They have dollar amounts in HubSpot. | "No. Only Closed Won deals." |
| Is the Routeboard overbilling (24 seats, 19 people, $95 a month) in scope? | The transcript at 00:05:32 raises it. | "No. Vendor bills are in scope only for duplicate payments." |
| Are the 7 cancelled jobs exceptions? | They show a price and no invoice. | "No. They are customer-side cancellations, not billed on purpose." |

With these answers a run should land on the six planted exceptions below plus two from the stop-and-ask round: Pleasant Hill Veterinary ($250) and Tanabe-Morrill (unpriced, $0). Total dollars at stake **$12,154.60**. If a run asks nothing and builds straight away, check which way it went on Munjoy Hill and Pleasant Hill; that is the conversation to have about why the rules say to stop.

## Make it a skill

When the workbook is done, paste this in the same session:

```
Wait. I might have to do this again. Turn what we just did in this session into a skill called quarterly-reconciliation, so next time it runs from one line. Put everything from rules.md inside the skill so it works in any folder. Keep it to one SKILL.md file with the steps and the rules, no scripts. Then read it back to me in five lines.
```

## What's planted

Six exceptions. Every one is provable from a named file and line. Total dollars at stake: **$11,904.60** (customer side $10,720.00, vendor side $1,184.60). With the stop-and-ask answers above, Pleasant Hill Veterinary ($250.00) and Tanabe-Morrill (unpriced, flag only) are added, for **$12,154.60**.

| # | Exception | Dollars | Proof |
|---|---|---|---|
| 1 | **Eastern Promenade credit promised, never applied.** Dana commits to a $1,200 credit ($400 per missed arrival window, three windows in August) on the September invoice. The September invoice carries no credit. | $1,200.00 | `meeting-transcript-2026-09-18-ops.txt`, Dana at 00:01:39 ("$400 per missed window, three windows, $1,200 total") and the action items at the end; `gmail-export/Re_ August arrival times - Eastern Promenade.pdf` lists the three dates. `quickbooks-invoices-q3.csv` row **INV-2089** (Sep 30, Eastern Promenade, Commercial cleaning) is the full amount with no credit line. Slack Aug 6, 13, 27 corroborate the misses. |
| 2 | **Old Port Dental rate cut agreed, never billed.** Dana agrees in writing to drop the monthly rate from $640 to $560 effective August 1. QuickBooks shows $640 for August and $640 for September. | $160.00 ($80 x 2) | `gmail-export/Re_ Q3 rate change - Old Port Dental.pdf`, Dana's reply Jul 28; `quickbooks-invoices-q3.csv` rows **INV-2066** (Aug) and **INV-2108** (Sep), both $640.00. Slack Jul 28 ("Elena can you update the invoice" / "on my list"). |
| 3 | **Munjoy Hill Senior Residence: closed-won, never started.** HubSpot shows the deal Closed Won on July 8 at $2,400 a month. There are no jobs for them in `jobs-export.csv` and no invoices in QuickBooks. Three months of a signed contract. | $7,200.00 | `hubspot-deals.xlsx`, row 2 (Munjoy Hill Senior Residence, Closed Won, $2,400, 2026-07-08, Jordan Lee); `gmail-export/Start date - Munjoy Hill Senior Residence.pdf` (Jul 10, never answered); Slack Sep 24 ("nothing in Routeboard for them"). Absence in `jobs-export.csv` and `quickbooks-invoices-q3.csv`. |
| 4 | **Back Cove Bakery handyman work, completed, never invoiced.** Three jobs in August, status Completed, invoice_no blank. No handyman invoice for Back Cove Bakery exists in QuickBooks. | $1,975.00 | `jobs-export.csv` rows **J-13508** (Aug 5, $725), **J-13538** (Aug 12, $650), **J-13605** (Aug 26, $600). Slack Aug 26 (Rafael: "three jobs for them this month, Elena do you want them on one invoice" / "I'll do it with the September run"). |
| 5 | **Casco Bay Janitorial invoice CB-2211 paid twice.** $1,184.60 on August 6 and again on August 20. This is the same duplicate PDF from exercise 1. | $1,184.60 | `quickbooks-bills-paid-q3.csv` rows **BILL-10223** (2026-08-06) and **BILL-10230** (2026-08-20), both invoice_number CB-2211. Slack Aug 24 (Elena: "Casco Bay sent the July 28 invoice again by mail"); transcript at 00:09:56 (Elena: "I am not sure whether I paid it twice"). |
| 6 | **Priya Natarajan's free re-clean was invoiced.** A crew lead promises a re-clean at no charge after a missed kitchen and baths. QuickBooks invoiced it at $185. | $185.00 | `slack-export/ops-channel.txt` Aug 19 15:45 (Marisol: "I told her we'd come back Thursday and redo them, no charge") and Aug 19 15:50 (Marcus: "make sure the office knows it's no charge"); `quickbooks-invoices-q3.csv` row **INV-2047** (Aug 21, Priya Natarajan, Re-clean, $185.00, Open); `jobs-export.csv` has the re-clean job at $0.00 linked to INV-2047. |

A reasonable "four things to fix first" by dollars: Munjoy Hill ($7,200), Back Cove ($1,975), Eastern Promenade ($1,200), Casco Bay double payment ($1,184.60). Old Port and Priya are small in dollars but are the ones a customer will notice.

## What should reconcile cleanly

- Every invoice in QuickBooks equals the sum of the jobs that carry its invoice number, except the Priya re-clean (job priced $0.00, invoice $185.00).
- Cancelled jobs (7 in the quarter, all customer-side) show a price but no invoice. They are not exceptions.
- Monthly contract customers (Old Port Dental, Harborview Orthodontics, Spring Street Studios, Riverton Family Chiropractic) bill a flat amount for two visits a month, so their invoice is the same whether the month has four weeks or five. The Harborview email thread is a customer asking exactly that.
- The other two closed-won deals in Q3 (Riverton Family Chiropractic, Pleasant Hill Veterinary) do have jobs and invoices.
- Walter Pelletier paused August and restarted September 8 (Slack Jul 22 and Sep 8). No August statement is correct.
- Casco Coast Property Management's turnover counts (15 in July, 14 in August, 11 in September) match Slack and the Hal Pettengill email.

## Row counts

`quickbooks-invoices-q3.csv` 129 rows, `jobs-export.csv` 455 rows, `quickbooks-bills-paid-q3.csv` 45 rows, `hubspot-deals.xlsx` 15 deals. Q3 invoiced total $733,675.00.
