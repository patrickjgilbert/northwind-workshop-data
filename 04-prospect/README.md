# Exercise 4: prepare for the second call (offline research)

**Model: Opus 5.5.** Point Cowork at this folder. Two prompts, one after the other. No web access needed; everything Claude should use is in the folder, and the point is that it says so when something is not.

Northwind is pitching Lakeshore Property Partners, a fictional Portland, Maine property manager with 48 buildings (60 after an acquisition closing October 1). Jordan (sales) and Dana had a first call on September 16; the second call is Thursday. This folder is what Northwind knows:

| File | What it is |
|---|---|
| `About - Lakeshore Property Partners.pdf` | their About page, saved to PDF |
| `Press release - Lakeshore acquires 12 buildings in South Portland.pdf` | their September 9 press release |
| `Job posting - Facilities Coordinator - Lakeshore Property Partners.pdf` | a job they posted August 28 |
| `Tenant reviews - Lakeshore Property Partners - RentVoice.pdf` | a tenant review page, 2.4 stars |
| `News - City fines Lakeshore building over common-area violations - Casco Bay Ledger.pdf` | a local news item, September 16 |
| `Pricing - ProClean Maine.pdf` | a competitor's public pricing page |
| `call-notes-first-call.txt` | Dana's notes from the first call |
| `Re_ follow up - Lakeshore.pdf` | the email thread after the first call, saved from Gmail |
| `northwind-company-profile.md` | the context file: who Northwind is, what it sells and how it prices, written by Northwind (see below) |

All six "web pages" carry a fake URL (`.example` domains) and a "Saved Sep 29, 2026" stamp in the header.

## Prompt 1

```
I have a second call with Lakeshore Property Partners on Thursday. This folder has everything we know about them: six pages saved from the web, one email, and my notes from the first call. Reference northwind-company-profile.md for who we are and what we sell. Write lakeshore-call-prep.md: who they are and what changed recently, what they told us on the first call and what they have walked back since, how what we offer fits what they need, the three competitors they will compare us to with one line on how each positions, the five questions I should ask, the objection I will hear first and the answer to it, and the one number I should not say out loud. Cite the filename for every claim. If something is not in the folder, say it is not there rather than filling it in.
```

## Prompt 2

```
Before you hand it to me, convene three graders: a property manager who has fired two vendors this year, the sales lead at a competing cleaning company, and a fact-checker who strikes any claim without a filename behind it. Each scores the brief 1 to 10 with their criticism. Anything under 8, rewrite using the criticism as instructions and grade again. Show me the scorecard for each round, then the final brief.
```

## The context file

`northwind-company-profile.md` is the page you would give a new salesperson on day one: who Northwind is, what it sells and at what price per building per month, how many buildings the crews can take on in a quarter, the arrival-window guarantee ($400 per missed window), what Northwind does not do, the references it can name, and how Dana sells (a 60-day pilot on one building, then expand).

Everything else in this folder is about Lakeshore. Without the profile, Claude can describe the prospect but has to guess at the seller, so "how what we offer fits what they need" comes back generic or invented. With it, the fit section can be specific and cited: weekly common areas at $120 to $260 per building per month with up to 10% off for 25 or more buildings, the monthly report with photos against Lakeshore's vendor scorecard, Eastern Promenade as the reference, and the capacity fact that 60 buildings by November 1 needs a new crew. "Reference northwind-company-profile.md for who we are and what we sell" tells Claude where the seller's facts live, so it cites them instead of making them up.

The profile does not contain Dana's floor price. If the brief names the floor, it got it from the call notes, which is correct, and it should say not to say it out loud.

## Make it a skill

When the final brief is done, paste this in the same session:

```
Wait. I might have to do this again. Turn what we just did in this session into a skill called call-prep, so next time it runs from one line. Put everything from northwind-company-profile.md inside the skill so it works in any folder. Keep it to one SKILL.md file with the steps and the rules, no scripts. Then read it back to me in five lines.
```

## What's planted

| Finding | The fact | Where |
|---|---|---|
| **Why they are buying now** | Two documents together explain it. The job posting says they are moving cleaning, grounds and snow onto portfolio-wide contracts and hiring someone to run a vendor scorecard and a monthly owner report. The news item says the city fined them $4,500 on September 11 for an unmaintained common area at a building they just took over, with a follow-up inspection October 14. Reviews and the press release back it up: common-area cleanliness is their most-mentioned complaint after maintenance speed, and the CEO's quote in the press release is about hallways and laundry rooms. | `Job posting - ...pdf`, `News - ...pdf`, `Tenant reviews - ...pdf`, `Press release - ...pdf` |
| **The budget was walked back** | On the first call Tobias Renner (Director of Operations) said "around $110K a year", twice. In the October 1 email he says the number he can defend to the owners is "closer to $80,000", with a revisit at the one-year mark. | `call-notes-first-call.txt`; `Re_ follow up - Lakeshore.pdf` |
| **The number not to say out loud** | Dana's floor is **$6,200 a month** ("do not go below $6,200/mo ... DO NOT say this number on the call"). That is $74,400 a year, under their walked-back $80,000, so there is still a deal above the floor. The planned ask was $8,500 a month (about $102K a year). | `call-notes-first-call.txt` |
| **The three competitors** | ProClean Maine (per-unit monthly pricing: $38, $52 or $71 per unit with per-building minimums and a 10% discount at 25+ buildings; Jordan's guess puts them at $5,500 to $7,500 a month), Bay State Facility Group ("big regional, corporate"), Coastal Commercial Clean ("local, cheap, we used them in 2024, didn't last"). Only ProClean has a document in the folder; the other two have one line each in the call notes and nothing else. A good brief says so. | `Pricing - ProClean Maine.pdf`; `call-notes-first-call.txt` |
| **Decision timing** | Decision by end of October, proposal wanted by September 30, management of the new buildings transitioned October 1, code follow-up inspection October 14. | `call-notes-first-call.txt`, `Press release`, `News` |
| **The first objection** | Scale. Tobias asked twice on the first call whether Northwind has done 48 buildings. The answer in the notes: Eastern Promenade, 11 buildings, 340 units, held for two and a half years. (The second call is likely to add price, given the email.) | `call-notes-first-call.txt` |
| **How we fit** (from the profile) | Weekly common areas are $120 to $260 per building per month, up to 10% off at 25 or more buildings, so the $8,500 a month ask (about $142 a building across 60) sits inside the published range. A new crew of 4 and a van covers about 60 small buildings a week, so a November 1 start depends on hiring now. Dana's usual move is a 60-day pilot on one building, which is a fair answer to both the scale objection and the walked-back budget. The arrival-window credit ($400 per missed window) and the monthly report with photos map straight onto the vendor scorecard in the job posting. | `northwind-company-profile.md`, `Job posting - ...pdf`, `call-notes-first-call.txt` |
| **What is not in the folder** | Lakeshore's current vendor's name, what Bay State or Coastal actually charge, the names of the 12 new buildings, whether the $80K is firm, and anything about Meredith Choate beyond the About page and press release. A good brief says "not in the folder" for these instead of inventing them. | |

For the grading round: the fact-checker should strike anything about Bay State Facility Group or Coastal Commercial Clean beyond the one line each in the call notes, and anything that states the $6,200 floor as if it were Lakeshore's number.
