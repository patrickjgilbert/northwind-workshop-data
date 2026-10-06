#!/usr/bin/env python3
"""Generate the Northwind workshop pack (folders 01, 02, 03 and the Lakeshore
email in 04) from ONE seeded model so every number ties out.

Run from the repo root:
    uv run --with openpyxl --with fpdf2 --with pillow python3 scripts/generate.py

Everything produced is fiction. Northwind Home Services, every customer,
vendor, person and dollar figure is invented for a training exercise.
"""
import calendar
import csv
import zlib
import os
import random
import shutil
import sys
from datetime import date, datetime, timedelta

from fpdf import FPDF
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content  # noqa: E402

SEED = 20261006
rng = random.Random(SEED)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D01 = os.path.join(ROOT, "01-invoices-inbox")
D02 = os.path.join(ROOT, "02-sources")
D03 = os.path.join(ROOT, "03-dashboard")
D04 = os.path.join(ROOT, "04-prospect")

RES, COM, HANDY = "Residential cleaning", "Commercial cleaning", "Handyman"

# 30 months, Apr 2024 -> Sep 2026
MONTHS = []
y, mo = 2024, 4
for _ in range(30):
    MONTHS.append((y, mo))
    mo += 1
    if mo == 13:
        y, mo = y + 1, 1
TTM = list(range(18, 30))   # Oct 2025 - Sep 2026
Q3 = [27, 28, 29]           # Jul, Aug, Sep 2026


def month_end(i):
    y, m = MONTHS[i]
    return date(y, m, calendar.monthrange(y, m)[1])


def month_label(i):
    return "%04d-%02d" % MONTHS[i]


def month_name(i):
    return date(MONTHS[i][0], MONTHS[i][1], 1).strftime("%B %Y")


def month_index(d):
    try:
        return MONTHS.index((d.year, d.month))
    except ValueError:
        return None


def weekday_dates(i, weekday):
    """All dates in month i that fall on weekday (0=Mon)."""
    y, m = MONTHS[i]
    out = []
    for day in range(1, calendar.monthrange(y, m)[1] + 1):
        d = date(y, m, day)
        if d.weekday() == weekday:
            out.append(d)
    return out


def money(x):
    return round(x + 1e-9, 2)


# ----------------------------------------------------------------- customers
# cadence: weekly | twice-monthly | biweekly | turnover
# rate: per visit (per turnover for turnover accounts)
CUSTOMERS = [
    # Commercial cleaning (crew C = commercial crew, B does turnovers)
    dict(id="C-2001", name="Eastern Promenade Condominium Association", type="commercial", segment="Condo association",
         cadence="weekly", rate=None, weekday=0, crew="C", start=date(2024, 4, 1), neighborhood="East End",
         contact="Gretchen Aldana, Property Manager", notes="11 buildings, 340 units. Common areas five days a week, turnovers, grounds via sub. Monthly invoice.", handy=True),
    dict(id="C-2002", name="Stroudwater Commons Condominium Trust", type="commercial", segment="Condo association",
         cadence="weekly", rate=4900, weekday=0, crew="C", start=date(2024, 4, 1), neighborhood="Stroudwater",
         contact="Phil Nadeau, Trustee", notes="Four buildings, daily common areas. Monthly invoice.", handy=True),
    dict(id="C-2003", name="Westbrook Crossing Professional Park", type="commercial", segment="Office",
         cadence="weekly", rate=6900, weekday=0, crew="C", start=date(2024, 9, 2), neighborhood="Westbrook",
         contact="Carla Jimenez, Facilities", notes="Nightly, five nights, three buildings. Annex quote pending.", handy=False),
    dict(id="C-2004", name="Bramhall Square Offices", type="commercial", segment="Office",
         cadence="weekly", rate=4300, weekday=1, crew="C", start=date(2024, 4, 1), neighborhood="West End",
         contact="Ted Vasquez, Building Manager", notes="Nightly, five nights. Alarm code on file.", handy=False),
    dict(id="C-2005", name="Baxter Woods Condominium Association", type="commercial", segment="Condo association",
         cadence="weekly", rate=3800, weekday=2, crew="C", start=date(2025, 1, 6), neighborhood="Deering",
         contact="Joan Whitcomb, Board Treasurer", notes="Three buildings, common areas three days a week.", handy=True),
    dict(id="C-2006", name="Marginal Way Medical Suites", type="commercial", segment="Medical office",
         cadence="weekly", rate=3100, weekday=1, crew="C", start=date(2026, 1, 5), neighborhood="Bayside",
         contact="Ravi Sundaram, Practice Administrator", notes="Evenings, five nights. Suite 300 expansion in HubSpot.", handy=False),
    dict(id="C-2007", name="Brackett Street Lofts Owners Association", type="commercial", segment="Condo association",
         cadence="weekly", rate=2700, weekday=3, crew="C", start=date(2024, 4, 1), neighborhood="West End",
         contact="Simone Travers, Board", notes="1920s building, common laundry. No exterior window work above floor two.", handy=True),
    dict(id="C-2008", name="Tidal Flats Coworking", type="commercial", segment="Office",
         cadence="weekly", rate=2400, weekday=4, crew="C", start=date(2025, 3, 3), neighborhood="Bayside",
         contact="Mei Lin Chau, Community Manager", notes="Nightly, five nights.", handy=True),
    dict(id="C-2009", name="Ocean Avenue Pediatrics", type="commercial", segment="Medical office",
         cadence="weekly", rate=890, weekday=2, crew="A", start=date(2024, 6, 3), neighborhood="North Deering",
         contact="Dr. Helen Okoro", notes="Evenings after 6. Use their wipes on exam tables.", handy=True),
    dict(id="C-2010", name="Pleasant Hill Veterinary", type="commercial", segment="Medical office",
         cadence="weekly", rate=760, weekday=0, crew="B", start=date(2026, 8, 17), neighborhood="Scarborough",
         contact="Dr. Sam Pelkey", notes="Mondays. Closed won in HubSpot Aug 4 2026.", handy=False),
    dict(id="C-2011", name="The Wharf House Restaurant", type="commercial", segment="Restaurant",
         cadence="weekly", rate=720, weekday=0, crew="A", start=date(2024, 4, 1), neighborhood="Old Port",
         contact="Nico Barros, GM", notes="Monday mornings before 10.", handy=False),
    dict(id="C-2012", name="Fore Street Bistro", type="commercial", segment="Restaurant",
         cadence="weekly", rate=640, weekday=1, crew="C", start=date(2024, 11, 4), neighborhood="Old Port",
         contact="Amara Diallo, Owner", notes="Tuesday mornings. Walk-in floor is in scope.", handy=False),
    dict(id="C-2013", name="Deering Oaks Dental Arts", type="commercial", segment="Dental",
         cadence="weekly", rate=480, weekday=3, crew="A", start=date(2024, 4, 1), neighborhood="Deering",
         contact="Marta Kowal, Office Manager", notes="Thursday evenings.", handy=False),
    dict(id="C-2014", name="Back Cove Bakery", type="commercial", segment="Restaurant",
         cadence="weekly", rate=420, weekday=2, crew="A", start=date(2025, 5, 7), neighborhood="Back Cove",
         contact="Luis Ferreira, Owner", notes="Wednesday afternoons after close. Handyman work as needed.", handy=True),
    dict(id="C-2015", name="Old Port Dental", type="commercial", segment="Dental",
         cadence="twice-monthly", rate=320, weekday=3, crew="A", start=date(2024, 4, 1), neighborhood="Old Port",
         contact="Renee Castonguay, Office Manager", notes="Two evening visits a month, $640 flat. Saturday polish dropped Aug 2026.", handy=False),
    dict(id="C-2016", name="Harborview Orthodontics", type="commercial", segment="Dental",
         cadence="twice-monthly", rate=575, weekday=1, crew="A", start=date(2024, 8, 6), neighborhood="South Portland",
         contact="Dev Mehta, Practice Manager", notes="Two evening visits a month, $1,150 flat.", handy=False),
    dict(id="C-2017", name="Spring Street Studios", type="commercial", segment="Office",
         cadence="twice-monthly", rate=280, weekday=4, crew="B", start=date(2025, 2, 7), neighborhood="West End",
         contact="Jess Quimby, Studio Manager", notes="Studio common area only, not the tenant restrooms.", handy=False),
    dict(id="C-2018", name="Riverton Family Chiropractic", type="commercial", segment="Medical office",
         cadence="twice-monthly", rate=240, weekday=2, crew="A", start=date(2026, 7, 1), neighborhood="Riverton",
         contact="Dr. Ben Lachance", notes="Closed won in HubSpot Jun 20 2026, started July.", handy=False),
    dict(id="C-2019", name="Casco Coast Property Management", type="commercial", segment="Property manager (turnovers)",
         cadence="turnover", rate=295, weekday=None, crew="B", start=date(2024, 4, 1), neighborhood="Various",
         contact="Hal Pettengill", notes="Six rental buildings. Per-turnover pricing, heavy in summer. Weekday only from Oct 2026.", handy=False,
         base=12.0, season=[0.5, 0.5, 0.55, 0.7, 1.0, 1.15, 1.25, 1.2, 1.0, 0.7, 0.55, 0.5], override={27: 15, 28: 14, 29: 11}),
    dict(id="C-2020", name="Longfellow Street Rentals", type="commercial", segment="Property manager (turnovers)",
         cadence="turnover", rate=275, weekday=None, crew="B", start=date(2024, 4, 1), neighborhood="West End",
         contact="Dale Marchetti", notes="Per-turnover pricing.", handy=False,
         base=7.0, season=[0.5, 0.5, 0.6, 0.75, 1.0, 1.2, 1.3, 1.25, 1.0, 0.7, 0.5, 0.45], override={}),
    dict(id="C-2021", name="Peaks Island Rentals", type="commercial", segment="Property manager (turnovers)",
         cadence="turnover", rate=330, weekday=None, crew="B", start=date(2024, 5, 1), neighborhood="Peaks Island",
         contact="Bev Tolman", notes="Seasonal, ferry schedule. Almost nothing December to March.", handy=False,
         base=6.0, season=[0.15, 0.1, 0.2, 0.5, 1.0, 1.4, 1.6, 1.5, 1.0, 0.5, 0.2, 0.15], override={}),
    # Former commercial customers (history only)
    dict(id="C-2022", name="Park Street Yoga Loft", type="commercial", segment="Office",
         cadence="twice-monthly", rate=190, weekday=2, crew="B", start=date(2024, 4, 1), end=date(2025, 8, 31), neighborhood="West End",
         contact="Ines Baptiste", notes="Ended Aug 2025, studio closed.", handy=False),
    dict(id="C-2023", name="Deering Center Family Dental", type="commercial", segment="Dental",
         cadence="weekly", rate=410, weekday=4, crew="A", start=date(2024, 4, 1), end=date(2026, 2, 28), neighborhood="Deering",
         contact="Pat Gorham", notes="Ended Feb 2026, moved to in-house.", handy=False),
    # Residential (weekly / biweekly, monthly statement)
    dict(id="R-3001", name="Priya Natarajan", type="residential", segment="Residential",
         cadence="weekly", rate=260, weekday=2, crew="A", start=date(2024, 4, 1), neighborhood="Pine Street", contact="", notes="Wednesdays. Re-clean Aug 21 2026 after missed kitchen and baths.", handy=True),
    dict(id="R-3002", name="Caleb Thibodeau", type="residential", segment="Residential",
         cadence="biweekly", rate=240, weekday=0, crew="A", start=date(2024, 4, 1), neighborhood="Deering", contact="", notes="", handy=True),
    dict(id="R-3003", name="Marguerite Okafor", type="residential", segment="Residential",
         cadence="weekly", rate=300, weekday=0, crew="A", start=date(2024, 4, 1), neighborhood="West End", contact="", notes="Mondays. Prefers Marisol.", handy=True),
    dict(id="R-3004", name="Ruth Hendricks", type="residential", segment="Residential",
         cadence="biweekly", rate=320, weekday=1, crew="B", start=date(2024, 4, 1), neighborhood="Cape Elizabeth", contact="", notes="", handy=True),
    dict(id="R-3005", name="Owen Castellano", type="residential", segment="Residential",
         cadence="biweekly", rate=220, weekday=3, crew="B", start=date(2024, 10, 3), neighborhood="North Deering", contact="", notes="", handy=True),
    dict(id="R-3006", name="Beatrix Lindqvist", type="residential", segment="Residential",
         cadence="weekly", rate=340, weekday=4, crew="A", start=date(2024, 4, 1), neighborhood="Falmouth Foreside", contact="", notes="Fridays.", handy=True),
    dict(id="R-3007", name="Samuel Agyemang", type="residential", segment="Residential",
         cadence="biweekly", rate=250, weekday=2, crew="B", start=date(2025, 2, 5), neighborhood="Rosemont", contact="", notes="", handy=True),
    dict(id="R-3008", name="Noor Haddad", type="residential", segment="Residential",
         cadence="biweekly", rate=280, weekday=4, crew="B", start=date(2024, 4, 1), neighborhood="Munjoy Hill", contact="", notes="", handy=True),
    dict(id="R-3009", name="Theo Bergstrom", type="residential", segment="Residential",
         cadence="weekly", rate=275, weekday=1, crew="A", start=date(2025, 6, 3), neighborhood="Oakdale", contact="", notes="Tuesdays.", handy=True),
    dict(id="R-3010", name="Imani Washington-Reyes", type="residential", segment="Residential",
         cadence="biweekly", rate=295, weekday=0, crew="B", start=date(2024, 4, 1), neighborhood="South Portland", contact="", notes="", handy=True),
    dict(id="R-3011", name="Walter Pelletier", type="residential", segment="Residential",
         cadence="biweekly", rate=230, weekday=1, crew="A", start=date(2024, 4, 1), neighborhood="Deering", contact="", notes="Paused August 2026, restarted Sep 8.", handy=True,
         pause=(date(2026, 8, 1), date(2026, 9, 7))),
    dict(id="R-3012", name="Yuki Tanabe-Morrill", type="residential", segment="Residential",
         cadence="weekly", rate=310, weekday=3, crew="A", start=date(2024, 4, 1), neighborhood="Stroudwater", contact="", notes="Moved to Thursdays July 2026.", handy=True),
    dict(id="R-3013", name="Hollis Brannigan", type="residential", segment="Residential",
         cadence="weekly", rate=265, weekday=3, crew="B", start=date(2024, 4, 1), end=date(2025, 12, 31), neighborhood="East End", contact="", notes="Moved away Dec 2025.", handy=True),
]
CUST = {c["id"]: c for c in CUSTOMERS}
for c in CUSTOMERS:
    c.setdefault("end", None)
    c["line"] = COM if c["type"] == "commercial" else RES

EP = "C-2001"
EP_RATE_PRE_2026_FACTOR = 0.78
EP_CREDIT = 1200
OLD_PORT = "C-2015"
BACK_COVE = "C-2014"
PRIYA = "R-3001"


def active(c, d):
    if d < c["start"]:
        return False
    if c["end"] and d > c["end"]:
        return False
    p = c.get("pause")
    if p and p[0] <= d <= p[1]:
        return False
    return True


# ----------------------------------------------------------------- jobs
HANDY_PRICES = [495, 520, 450, 560, 420, 610, 385, 640]   # ordered in balanced pairs so partial cycles keep the mean flat
HANDY_DESC = [
    "Replace door closer", "Rehang interior door", "Patch and paint hallway wall", "Replace bathroom exhaust fan",
    "Install grab bars", "Repair deck boards", "Replace light fixtures (2)", "Caulk and reseal tub surround",
    "Replace kitchen faucet", "Repair loose stair tread", "Mount shelving", "Replace mailbox unit",
    "Weatherstrip exterior door", "Replace storm door", "Repair fence section", "Install closet system",
    "Replace garbage disposal", "Fix sticking windows (3)", "Replace entry lockset", "Repair drywall, laundry room",
]


def handy_hours_target(i):
    return 2.1 + (3.4 - 2.1) * i / 29.0


def cleaning_hours(c, price):
    if c["line"] == RES:
        return round(price / 85.0 * 4) / 4
    return round(price / 70.0 * 4) / 4


def direct_cost(line, hours, price):
    if line == RES:
        return money(hours * 34 + price * 0.05)
    if line == COM:
        return money(hours * 31 + price * 0.04)
    return money(hours * 58 + price * 0.12)


def gen_jobs(ep_rate):
    """Return list of job dicts for all 30 months."""
    jobs = []

    def add(c, d, line, price, hours, desc, status="Completed", flag=None, crew=None):
        jobs.append(dict(cust=c["id"], date=d, line=line, price=money(price), hours=hours, desc=desc,
                         status=status, flag=flag, crew=crew or c["crew"]))

    for c in CUSTOMERS:
        if c["cadence"] == "turnover":
            continue
        for i in range(30):
            if c["cadence"] in ("weekly", "biweekly"):
                dates = weekday_dates(i, c["weekday"])
                if c["cadence"] == "biweekly":
                    dates = [d for d in dates if (d.isocalendar()[1] % 2) == (int(c["id"][-1]) % 2)]
            else:  # twice-monthly: first and third occurrence
                wd = weekday_dates(i, c["weekday"])
                dates = [wd[0], wd[2]]
            for d in dates:
                if not active(c, d):
                    continue
                if c["id"] == EP:
                    rate = ep_rate if i >= 21 else round(ep_rate * EP_RATE_PRE_2026_FACTOR)
                else:
                    rate = c["rate"]
                if c["type"] == "commercial":
                    desc = {"weekly": "Weekly service", "twice-monthly": "Evening visit"}[c["cadence"]]
                    if c["id"] == EP:
                        desc = "Weekly common-area service, 11 buildings (5 days)"
                else:
                    desc = "Recurring clean"
                add(c, d, c["line"], rate, cleaning_hours(c, rate), desc)

    # turnovers
    for c in CUSTOMERS:
        if c["cadence"] != "turnover":
            continue
        for i in range(30):
            y, m = MONTHS[i]
            n = c["override"].get(i)
            if n is None:
                n = max(0, int(round(c["base"] * c["season"][m - 1] + rng.uniform(-1.2, 1.2))))
            days = sorted(rng.sample(range(1, calendar.monthrange(y, m)[1] + 1), min(n, 28)))
            for day in days:
                d = date(y, m, day)
                if not active(c, d):
                    continue
                price = c["rate"] + rng.choice([0, 0, 0, 40, 85])
                add(c, d, COM, price, cleaning_hours(c, price), "Rental turnover")

    # handyman
    pool = [c for c in CUSTOMERS if c["handy"]]
    for i in range(30):
        y, m = MONTHS[i]
        n = int(round(10 + 5 * i / 29.0 + rng.uniform(-1.5, 1.5)))
        target = handy_hours_target(i)
        k = 0
        for _ in range(n):
            c = rng.choice(pool)
            d = date(y, m, rng.randint(1, calendar.monthrange(y, m)[1]))
            if not active(c, d):
                continue
            if c["id"] == BACK_COVE and i in Q3:
                continue  # Back Cove's Q3 handyman work is planted below
            price = HANDY_PRICES[k % len(HANDY_PRICES)]  # cycled so price per job stays flat
            hours = round(target * rng.uniform(0.82, 1.18) * 4) / 4
            add(c, d, HANDY, price, hours, rng.choice(HANDY_DESC), crew="H")
            k += 1

    # planted: Back Cove Bakery, three completed handyman jobs in Aug 2026, never invoiced
    for d, price, desc, hours in [
        (date(2026, 8, 5), 725, "Replace rear door closer and weatherstrip", 3.5),
        (date(2026, 8, 12), 650, "Mount shelving in dry storage", 3.0),
        (date(2026, 8, 26), 600, "Repair loose stair tread, rear entry", 2.75),
    ]:
        add(CUST[BACK_COVE], d, HANDY, price, hours, desc, flag="unbilled", crew="H")

    # planted: Priya Natarajan re-clean Aug 21 2026, promised free in Slack, invoiced $185
    add(CUST[PRIYA], date(2026, 8, 21), RES, 0, 2.5, "Re-clean: kitchen and baths (no charge per crew lead)", flag="reclean")

    # a few customer-side cancellations in Q3 (price shown, nothing billed)
    for d, cid in [(date(2026, 7, 13), "R-3002"), (date(2026, 7, 29), "R-3005"), (date(2026, 8, 11), "R-3009"),
                   (date(2026, 8, 24), "R-3007"), (date(2026, 9, 9), "R-3004"), (date(2026, 9, 22), "R-3010"), (date(2026, 9, 29), "R-3008")]:
        c = CUST[cid]
        add(c, d, RES, c["rate"], 0, "Recurring clean", status="Cancelled")

    jobs.sort(key=lambda j: (j["date"], j["cust"], j["line"]))
    for k, j in enumerate(jobs, start=1):
        j["id"] = "J-%05d" % (10000 + k)
    return jobs


# ----------------------------------------------------------------- invoices
def gen_invoices(jobs):
    """One invoice per customer-month-line (cleaning statements and handyman
    statements), dated the last day of the month. Planted deviations applied."""
    groups = {}
    for j in jobs:
        if j["status"] != "Completed":
            continue
        if j["flag"] == "unbilled":
            continue
        i = month_index(j["date"])
        if j["flag"] == "reclean":
            groups.setdefault(("reclean", j["cust"], i, j["line"]), []).append(j)
            continue
        groups.setdefault((j["cust"], i, j["line"]), []).append(j)

    invoices = []
    for key, js in groups.items():
        if key[0] == "reclean":
            _, cid, i, line = key
            inv = dict(cust=cid, date=js[0]["date"], line=line, amount=185.00,
                       desc="Re-clean: kitchen and baths (8/21)", status="Open", jobs=js)
            invoices.append(inv)
            continue
        cid, i, line = key
        c = CUST[cid]
        amount = money(sum(j["price"] for j in js))
        n = len(js)
        if line == HANDY:
            desc = "Handyman services - %s (%d job%s)" % (month_name(i), n, "" if n == 1 else "s")
        elif c["cadence"] == "turnover":
            desc = "Rental turnovers - %s (%d units)" % (month_name(i), n)
        elif c["cadence"] == "twice-monthly":
            desc = "Monthly service - %s (2 evening visits)" % month_name(i)
        elif c["type"] == "commercial":
            desc = "Weekly service - %s (%d visits)" % (month_name(i), n)
        else:
            desc = "Monthly cleaning statement - %s (%d visits)" % (month_name(i), n)
        # status
        if i == 29:
            status = "Open"
        elif i == 28 and cid in ("C-2012", "R-3005"):
            status = "Overdue"
        else:
            status = "Paid"
        invoices.append(dict(cust=cid, date=month_end(i), line=line, amount=amount, desc=desc, status=status, jobs=js))

    invoices.sort(key=lambda v: (v["date"], v["cust"], v["line"]))
    for k, v in enumerate(invoices, start=1):
        v["no"] = "INV-%d" % (1000 + k)
        for j in v["jobs"]:
            j["invoice_no"] = v["no"]
    return invoices


def calibrate_ep_rate(trial_rate):
    """Pick EP's 2026 weekly rate so EP is 31.0% of trailing-12-month revenue."""
    jobs = gen_jobs(trial_rate)
    inv = gen_invoices(jobs)
    other = sum(v["amount"] for v in inv if v["cust"] != EP and month_index(v["date"]) in TTM)
    ep_handy = sum(v["amount"] for v in inv if v["cust"] == EP and v["line"] == HANDY and month_index(v["date"]) in TTM)
    target = other * 0.31 / 0.69 - ep_handy
    weeks_2026 = sum(len([d for d in weekday_dates(i, 0)]) for i in TTM if i >= 21)
    weeks_2025 = sum(len([d for d in weekday_dates(i, 0)]) for i in TTM if i < 21)
    rate = target / (weeks_2026 + EP_RATE_PRE_2026_FACTOR * weeks_2025)
    return int(round(rate))


# ----------------------------------------------------------------- PDF helpers
class PDF(FPDF):
    pass


def new_pdf():
    pdf = PDF(format="letter")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_creation_date(datetime(2026, 10, 5, 9, 14, 0))
    pdf.set_margins(18, 18, 18)
    pdf.add_page()
    return pdf


def write_gmail_pdf(path, thread):
    pdf = new_pdf()
    pdf.set_font("Helvetica", size=8)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 5, "10/5/26, 9:14 AM")
    pdf.set_xy(18, 18)
    pdf.cell(0, 5, "Gmail - " + thread["subject"], align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(28, 8, "M  Gmail")
    pdf.set_font("Helvetica", size=9)
    pdf.cell(0, 8, "Dana Whitfield <dana@northwindhome.example>", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_draw_color(200, 200, 200)
    pdf.line(18, pdf.get_y(), 198, pdf.get_y())
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, thread["subject"], new_x="LMARGIN", new_y="NEXT")
    n = len(thread["messages"])
    pdf.set_font("Helvetica", size=9)
    pdf.set_text_color(90, 90, 90)
    pdf.cell(0, 6, "%d message%s" % (n, "" if n == 1 else "s"), new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0)
    for (name, email, to_line, when, body) in thread["messages"]:
        pdf.ln(2)
        pdf.line(18, pdf.get_y(), 198, pdf.get_y())
        pdf.ln(3)
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(120, 6, "%s <%s>" % (name, email))
        pdf.set_font("Helvetica", size=9)
        pdf.cell(0, 6, when, align="R", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(90, 90, 90)
        pdf.multi_cell(0, 5, to_line, new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(2)
        pdf.set_font("Helvetica", size=10)
        pdf.multi_cell(0, 5.2, body, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)
    pdf.set_font("Helvetica", size=7)
    pdf.set_text_color(90, 90, 90)
    ident = zlib.crc32(thread["subject"].encode()) * 7919 % 10**12
    pdf.cell(0, 5, "https://mail.google.com/mail/u/0/?ik=4a1f%d&view=pt&search=all&permthid=thread-f:18%012d" % (ident % 9973, ident))
    pdf.cell(0, 5, "1/1", align="R")
    pdf.output(path)


VENDORS = {
    "Casco Bay Janitorial Supply": dict(addr="88 Warren Avenue, Portland, ME 04103", phone="(207) 555-0122", email="orders@cascobayjanitorial.example", terms="Net 30"),
    "Pine Point Fuel Co-op": dict(addr="14 Pine Point Road, Scarborough, ME 04074", phone="(207) 555-0137", email="billing@pinepointfuel.example", terms="Due on receipt"),
    "Fore River Auto & Fleet": dict(addr="301 Riverside Street, Portland, ME 04103", phone="(207) 555-0160", email="service@foreriverauto.example", terms="Net 15"),
    "Pine Tree Mutual Insurance": dict(addr="PO Box 9120, Lewiston, ME 04243", phone="(800) 555-0175", email="billing@pinetreemutual.example", terms="Due by date shown"),
    "Tidewater Plumbing": dict(addr="6 Mussey Street, South Portland, ME 04106", phone="(207) 555-0109", email="tidewaterplumbing@example.net", terms="Net 15"),
    "Stitchworks Uniform Co.": dict(addr="520 Main Street, Westbrook, ME 04092", phone="(207) 555-0184", email="orders@stitchworksuniform.example", terms="Net 30"),
    "Routeboard Scheduling": dict(addr="1200 Market Street, Suite 800, Philadelphia, PA 19107", phone="(888) 555-0142", email="billing@routeboard.example", terms="Auto-pay, card on file"),
    "Old Port Print & Sign": dict(addr="45 Exchange Street, Portland, ME 04101", phone="(207) 555-0166", email="jobs@oldportprint.example", terms="Net 30"),
    "Greenline Lawn & Snow": dict(addr="77 Spurwink Avenue, Cape Elizabeth, ME 04107", phone="(207) 555-0151", email="office@greenlinelawnsnow.example", terms="Net 30"),
}

# (vendor, number, date, total, po, filename, lines[(desc, qty, unit)])
INBOX_INVOICES = [
    ("Casco Bay Janitorial Supply", "CB-2198", date(2026, 7, 9), 842.15, "NW-2026-133", "casco bay july.pdf",
     [("Neutral floor cleaner, 5 gal", 4, 46.50), ("Microfiber cloths, case of 200", 3, 58.00), ("Nitrile gloves, L, case", 5, 41.20), ("Can liners 33 gal, case", 4, 61.15), ("Fuel surcharge", 1, 4.95)]),
    ("Casco Bay Janitorial Supply", "CB-2211", date(2026, 7, 28), 1184.60, "NW-2026-141", "INV (2).pdf",
     [("Disinfectant concentrate, 1 gal", 12, 28.40), ("Paper towels, case", 10, 39.90), ("Toilet tissue, 2-ply, case", 8, 44.75), ("Mop heads, looped, dozen", 3, 36.30), ("Spray bottles, 32 oz, case", 2, 23.00), ("Fuel surcharge", 1, 4.95)]),
    ("Casco Bay Janitorial Supply", "CB-2240", date(2026, 8, 18), 963.40, "NW-2026-152", "scan_0412.pdf",
     [("Glass cleaner, 1 gal", 8, 19.80), ("Can liners 55 gal, case", 6, 72.50), ("Floor finish, 5 gal", 2, 118.00), ("Scrub pads, case", 4, 24.95), ("Fuel surcharge", 1, 4.95)]),
    ("Casco Bay Janitorial Supply", "CB-2267", date(2026, 9, 8), 1027.90, "NW-2026-160", "Document.pdf",
     [("Disinfectant concentrate, 1 gal", 10, 28.40), ("Paper towels, case", 8, 39.90), ("Nitrile gloves, M, case", 6, 41.20), ("Neutral floor cleaner, 5 gal", 3, 46.50), ("Fuel surcharge", 1, 4.95)]),
    ("Casco Bay Janitorial Supply", "CB-2291", date(2026, 9, 29), 778.25, "NW-2026-171", "INV (3).pdf",
     [("Toilet tissue, 2-ply, case", 7, 44.75), ("Microfiber cloths, case of 200", 4, 58.00), ("Hand soap, foaming, case", 5, 45.30), ("Fuel surcharge", 1, 4.95)]),
    ("Pine Point Fuel Co-op", "PPF-77102", date(2026, 7, 31), 1412.88, "NW-2026-FUEL", "fuel july.pdf",
     [("Unleaded, member rate, July (gal)", 412.0, 3.429)]),
    ("Pine Point Fuel Co-op", "PPF-77388", date(2026, 8, 31), 1566.02, "NW-2026-FUEL", "IMG_4471.pdf",
     [("Unleaded, member rate, August (gal)", 451.0, 3.472)]),
    ("Pine Point Fuel Co-op", "PPF-77651", date(2026, 9, 30), 1338.47, "NW-2026-FUEL", "scan_0419.pdf",
     [("Unleaded, member rate, September (gal)", 394.0, 3.397)]),
    ("Fore River Auto & Fleet", "FRA-5531", date(2026, 7, 15), 612.40, "NW-2026-136", "invoice (1).pdf",
     [("Van 2: front brake pads and rotors", 1, 418.00), ("Labor, 1.8 hr", 1.8, 98.00), ("Shop supplies", 1, 18.00)]),
    ("Fore River Auto & Fleet", "FRA-5602", date(2026, 8, 21), 2247.19, "NW-2026-154", "scan_0413.pdf",
     [("Van 1: transmission service, fluid and filter", 1, 612.19), ("Van 1: valve body replacement", 1, 1145.00), ("Labor, 5.0 hr", 5.0, 98.00)]),
    ("Fore River Auto & Fleet", "FRA-5640", date(2026, 9, 12), 389.00, "NW-2026-162", "Document (1).pdf",
     [("Van 3: state inspection", 1, 18.50), ("Van 3: oil and filter, synthetic", 1, 112.50), ("Van 3: wiper blades, pair", 1, 42.00), ("Labor, 2.2 hr", 2.2, 98.00)]),
    ("Pine Tree Mutual Insurance", "PTM-2026-Q3-8841", date(2026, 7, 1), 4860.00, "NW-2026-INS", "insurance q3.pdf",
     [("Commercial general liability, Q3 2026", 1, 2340.00), ("Commercial auto, 3 vehicles, Q3 2026", 1, 1860.00), ("Janitorial bond, Q3 2026", 1, 660.00)]),
    ("Pine Tree Mutual Insurance", "PTM-2026-Q4-9107", date(2026, 9, 25), 5115.00, "NW-2026-INS", "attachment.pdf",
     [("Commercial general liability, Q4 2026", 1, 2475.00), ("Commercial auto, 4 vehicles, Q4 2026", 1, 1980.00), ("Janitorial bond, Q4 2026", 1, 660.00)]),
    ("Tidewater Plumbing", "TP-0871", date(2026, 7, 22), 1480.00, "NW-2026-139", "tidewater.pdf",
     [("Water heater, 50 gal, Brackett Street Lofts common laundry", 1, 980.00), ("Labor, 4 hr", 4, 110.00), ("Permit and disposal", 1, 60.00)]),
    ("Tidewater Plumbing", "TP-0893", date(2026, 8, 14), 3250.00, None, "plumber invoice.pdf",
     [("Emergency sewer line repair, Westbrook Crossing Bldg B", 1, 2150.00), ("Labor, 8 hr, after hours", 8, 125.00), ("Camera inspection", 1, 100.00)]),
    ("Tidewater Plumbing", "TP-0912", date(2026, 9, 16), 925.00, "NW-2026-163", "scan_0420.pdf",
     [("Backflow preventer, Ocean Avenue Pediatrics", 1, 595.00), ("Labor, 3 hr", 3, 110.00)]),
    ("Stitchworks Uniform Co.", "SW-3310", date(2026, 7, 11), 1096.50, "NW-2026-134", "invoice_final_FINAL.pdf",
     [("Crew polo, embroidered, navy", 30, 32.50), ("Name tags, magnetic", 30, 4.05)]),
    ("Stitchworks Uniform Co.", "SW-3377", date(2026, 9, 3), 448.00, "NW-2026-158", "Invoice.pdf",
     [("Fleece jacket, embroidered", 8, 56.00)]),
    ("Routeboard Scheduling", "RB-204411", date(2026, 7, 1), 456.00, "NW-2026-SW1", "routeboard july.pdf",
     [("Routeboard Team plan, July 2026, 24 seats", 24, 19.00)]),
    ("Routeboard Scheduling", "RB-209872", date(2026, 8, 1), 456.00, "NW-2026-SW1", "untitled.pdf",
     [("Routeboard Team plan, August 2026, 24 seats", 24, 19.00)]),
    ("Routeboard Scheduling", "RB-215306", date(2026, 9, 1), 456.00, "NW-2026-SW1", "scan_0415.pdf",
     [("Routeboard Team plan, September 2026, 24 seats", 24, 19.00)]),
    ("Old Port Print & Sign", "OPP-1188", date(2026, 7, 18), 312.75, "NW-2026-137", "print shop.pdf",
     [("Door hangers, 4x9, full color", 1500, 0.1885), ("Setup", 1, 30.00)]),
    ("Old Port Print & Sign", "OPP-1243", date(2026, 9, 10), 684.00, "NW-2026-161", "INV (1).pdf",
     [("Van door decals, 24 in, pair", 2, 292.00), ("Installation", 2, 50.00)]),
    ("Greenline Lawn & Snow", "GL-2026-0712", date(2026, 7, 31), 2150.00, "NW-2026-144", "greenline.pdf",
     [("Grounds maintenance, July, Eastern Promenade (11 bldgs)", 1, 1650.00), ("Grounds maintenance, July, Baxter Woods", 1, 500.00)]),
    ("Greenline Lawn & Snow", "GL-2026-0804", date(2026, 8, 31), 2150.00, "NW-2026-153", "scan_0418.pdf",
     [("Grounds maintenance, August, Eastern Promenade (11 bldgs)", 1, 1650.00), ("Grounds maintenance, August, Baxter Woods", 1, 500.00)]),
    ("Greenline Lawn & Snow", "GL-2026-0909", date(2026, 9, 30), 2380.00, "NW-2026-170", "scan_0416.pdf",
     [("Grounds maintenance, September, Eastern Promenade (11 bldgs)", 1, 1650.00), ("Grounds maintenance, September, Baxter Woods", 1, 500.00), ("Fall cleanup, both sites", 1, 230.00)]),
]
DUPLICATE_FILE = ("INV (2).pdf", "scan_0417.pdf")   # same CB-2211 twice
BLANK_SCAN = "scan_0421.pdf"


def write_invoice_pdf(path, vendor, number, d, total, po, lines):
    v = VENDORS[vendor]
    pdf = new_pdf()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 10, vendor, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=9)
    pdf.cell(0, 5, v["addr"], new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, "%s  |  %s" % (v["phone"], v["email"]), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 10, "INVOICE", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", size=10)
    due = d + timedelta(days=30 if "30" in v["terms"] else 15)
    rows = [("Invoice Number:", number), ("Invoice Date:", d.strftime("%B %d, %Y")), ("Due Date:", due.strftime("%B %d, %Y"))]
    if po:
        rows.append(("PO Number:", po))
    rows.append(("Terms:", v["terms"]))
    for k, val in rows:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(38, 6, k)
        pdf.set_font("Helvetica", size=10)
        pdf.cell(0, 6, val, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "Bill To:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=10)
    pdf.multi_cell(0, 5.5, "Northwind Home Services\nAttn: Accounts Payable\n412 Forest Avenue, Suite 2\nPortland, ME 04101", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_fill_color(235, 235, 235)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(104, 7, "Description", fill=True)
    pdf.cell(22, 7, "Qty", fill=True, align="R")
    pdf.cell(26, 7, "Unit", fill=True, align="R")
    pdf.cell(28, 7, "Amount", fill=True, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=10)
    running = 0.0
    for k, (desc, qty, unit) in enumerate(lines):
        amt = money(qty * unit)
        if k == len(lines) - 1:
            amt = money(total - running)   # absorb rounding so lines sum to the total
        running = money(running + amt)
        qty_s = ("%g" % qty) if isinstance(qty, (int, float)) else str(qty)
        pdf.cell(104, 7, desc)
        pdf.cell(22, 7, qty_s, align="R")
        pdf.cell(26, 7, "$%s" % ("{:,.2f}".format(unit) if unit >= 1 else "{:,.4f}".format(unit)), align="R")
        pdf.cell(28, 7, "${:,.2f}".format(amt), align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(152, 8, "Total Due", align="R")
    pdf.cell(28, 8, "${:,.2f}".format(total), align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.multi_cell(0, 5, "Please include the invoice number with your payment. Remit to %s, %s. Thank you for your business." % (vendor, v["addr"]), new_x="LMARGIN", new_y="NEXT")
    pdf.output(path)


def write_receipt_png(path, vendor, addr, d, items, total, footer):
    W, H = 420, 120 + 28 * (len(items) + 10)
    img = Image.new("RGB", (W, H), (252, 250, 245))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 17)
        bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 19)
    except OSError:
        font = ImageFont.load_default(size=17)
        bold = ImageFont.load_default(size=19)
    y = 22
    for line in [vendor, addr]:
        w = draw.textlength(line, font=bold if line == vendor else font)
        draw.text(((W - w) / 2, y), line, fill=(30, 30, 30), font=bold if line == vendor else font)
        y += 28
    y += 6
    draw.text((24, y), d.strftime("%m/%d/%Y  %I:%M %p"), fill=(30, 30, 30), font=font)
    y += 36
    draw.text((24, y), "-" * 32, fill=(30, 30, 30), font=font)
    y += 28
    for desc, amt in items:
        draw.text((24, y), desc[:22].ljust(22), fill=(30, 30, 30), font=font)
        if amt:
            draw.text((300, y), "%8.2f" % amt, fill=(30, 30, 30), font=font)
        y += 28
    draw.text((24, y), "-" * 32, fill=(30, 30, 30), font=font)
    y += 30
    draw.text((24, y), "TOTAL", fill=(30, 30, 30), font=bold)
    draw.text((290, y), "$%8.2f" % total, fill=(30, 30, 30), font=bold)
    y += 40
    for line in footer:
        draw.text((24, y), line, fill=(30, 30, 30), font=font)
        y += 26
    img.save(path, optimize=True)


# ----------------------------------------------------------------- prospect pages
def write_webpage_pdf(path, page):
    pdf = new_pdf()
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Helvetica", size=8)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(120, 6, page["url"], fill=True)
    pdf.cell(60, 6, page["saved"], fill=True, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 5, page["title"], new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)
    pdf.set_text_color(0, 0, 0)
    for kind, val in page["blocks"]:
        if kind == "h1":
            pdf.set_font("Helvetica", "B", 17)
            pdf.multi_cell(0, 8, val, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif kind == "h2":
            pdf.ln(2)
            pdf.set_font("Helvetica", "B", 12)
            pdf.multi_cell(0, 7, val, new_x="LMARGIN", new_y="NEXT")
        elif kind == "p":
            pdf.set_font("Helvetica", size=10)
            pdf.multi_cell(0, 5.4, val, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif kind == "small":
            pdf.set_font("Helvetica", "I", 8)
            pdf.set_text_color(90, 90, 90)
            pdf.multi_cell(0, 4.5, val, new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(2)
        elif kind == "ul":
            pdf.set_font("Helvetica", size=10)
            for item in val:
                pdf.set_x(24)
                pdf.multi_cell(0, 5.4, "-  " + item, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif kind == "review":
            stars, when, where, text = val
            pdf.set_font("Helvetica", "B", 10)
            pdf.cell(0, 6, "%s  -  %s  -  %s" % (stars, when, where), new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", size=10)
            pdf.multi_cell(0, 5.4, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif kind == "table":
            widths = [34, 62, 44, 40]
            for r, row in enumerate(val):
                pdf.set_font("Helvetica", "B" if r == 0 else "", 10)
                for w, cell in zip(widths, row):
                    pdf.cell(w, 7, cell, border=1)
                pdf.ln(7)
            pdf.ln(3)
    pdf.output(path)


# ----------------------------------------------------------------- xlsx helpers
def new_wb():
    wb = Workbook()
    wb.properties.creator = "Northwind"
    wb.properties.lastModifiedBy = "Northwind"
    wb.properties.title = ""
    return wb


def style_header(ws):
    for cell in ws[1]:
        cell.font = Font(bold=True)
        cell.fill = PatternFill("solid", fgColor="E7E6E6")
        cell.alignment = Alignment(vertical="center")
    ws.freeze_panes = "A2"


def autosize(ws, maxw=48):
    for col in ws.columns:
        width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
        ws.column_dimensions[get_column_letter(col[0].column)].width = min(maxw, max(10, width + 2))


# ----------------------------------------------------------------- main
# Hand-written files the generator must never delete: the folder READMEs and
# the context files each exercise prompt tells Claude to reference.
KEEP = {"README.md", "rules.md", "brand-guidelines.md", "northwind-company-profile.md"}


def clean_dir(d):
    if os.path.isdir(d):
        for name in os.listdir(d):
            if name in KEEP:
                continue
            p = os.path.join(d, name)
            if os.path.isdir(p):
                shutil.rmtree(p)
            else:
                os.remove(p)
    os.makedirs(d, exist_ok=True)


def main():
    global rng
    print("Northwind workshop pack generator (seed %d)" % SEED)

    # --- model
    rng = random.Random(SEED)
    ep_rate = calibrate_ep_rate(16000)
    rng = random.Random(SEED)
    jobs = gen_jobs(ep_rate)
    invoices = gen_invoices(jobs)

    ttm_total = sum(v["amount"] for v in invoices if month_index(v["date"]) in TTM)
    ep_ttm = sum(v["amount"] for v in invoices if v["cust"] == EP and month_index(v["date"]) in TTM)
    print("  Eastern Promenade weekly rate 2026: $%s  (pre-2026: $%s)" % (f"{ep_rate:,}", f"{round(ep_rate*EP_RATE_PRE_2026_FACTOR):,}"))
    print("  PLANTED  trailing-12 revenue: $%s; Eastern Promenade share: %.1f%% ($%s)" % (f"{ttm_total:,.2f}", 100 * ep_ttm / ttm_total, f"{ep_ttm:,.2f}"))

    # --- 02: jobs export (Q3 only)
    clean_dir(D02)
    os.makedirs(os.path.join(D02, "gmail-export"))
    os.makedirs(os.path.join(D02, "slack-export"))
    q3_jobs = [j for j in jobs if month_index(j["date"]) in Q3]
    with open(os.path.join(D02, "jobs-export.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["job_id", "date", "customer", "service_line", "crew", "hours", "price", "status", "invoice_no"])
        for j in q3_jobs:
            w.writerow([j["id"], j["date"].isoformat(), CUST[j["cust"]]["name"], j["line"], "Crew " + j["crew"],
                        "%.2f" % j["hours"], "%.2f" % j["price"], j["status"], j.get("invoice_no", "")])
    print("  jobs-export.csv: %d rows (Q3 2026)" % len(q3_jobs))

    # --- 02: QuickBooks invoices (Q3 only)
    q3_inv = [v for v in invoices if month_index(v["date"]) in Q3]
    with open(os.path.join(D02, "quickbooks-invoices-q3.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["invoice_no", "date", "customer", "service_line", "description", "amount", "status"])
        for v in q3_inv:
            w.writerow([v["no"], v["date"].isoformat(), CUST[v["cust"]]["name"], v["line"], v["desc"], "%.2f" % v["amount"], v["status"]])
    print("  quickbooks-invoices-q3.csv: %d rows, $%s invoiced" % (len(q3_inv), f"{sum(v['amount'] for v in q3_inv):,.2f}"))

    # planted prints
    op = [v for v in q3_inv if v["cust"] == OLD_PORT]
    print("  PLANTED  Old Port Dental invoiced: " + ", ".join("%s $%.2f" % (v["date"].strftime("%b"), v["amount"]) for v in op)
          + "  (rate cut to $560 from Aug 1 per email -> $160.00 over)")
    bc = [j for j in q3_jobs if j["cust"] == BACK_COVE and j["line"] == HANDY]
    print("  PLANTED  Back Cove Bakery handyman jobs Aug, no invoice: %s = $%.2f" % (", ".join(j["id"] for j in bc), sum(j["price"] for j in bc)))
    pr = [v for v in q3_inv if v["cust"] == PRIYA and v["amount"] == 185.0]
    print("  PLANTED  Priya Natarajan re-clean invoiced: %s $%.2f (Slack says no charge)" % (pr[0]["no"], pr[0]["amount"]))
    ep_sep = [v for v in q3_inv if v["cust"] == EP and v["line"] == COM and v["date"].month == 9][0]
    print("  PLANTED  Eastern Promenade $%d credit promised in transcript; September invoice %s is $%s with no credit" % (EP_CREDIT, ep_sep["no"], f"{ep_sep['amount']:,.2f}"))
    print("  PLANTED  Munjoy Hill Senior Residence: HubSpot closed won Jul 8 at $2,400/mo; 0 jobs, 0 invoices -> $7,200.00")
    print("  PLANTED  Casco Bay CB-2211 $1,184.60 paid twice in quickbooks-bills-paid-q3.csv")

    # --- 02: bills paid
    bills = []
    paid = {  # invoice number -> paid date for inbox invoices paid in Q3
        "CB-2198": date(2026, 7, 24), "CB-2240": date(2026, 9, 2), "CB-2267": date(2026, 9, 24),
        "PPF-77102": date(2026, 8, 12), "PPF-77388": date(2026, 9, 11),
        "FRA-5531": date(2026, 7, 30), "FRA-5602": date(2026, 9, 4), "FRA-5640": date(2026, 9, 25),
        "PTM-2026-Q3-8841": date(2026, 7, 8), "TP-0871": date(2026, 8, 7), "TP-0893": date(2026, 8, 28),
        "SW-3310": date(2026, 7, 29), "RB-204411": date(2026, 7, 3), "RB-209872": date(2026, 8, 4), "RB-215306": date(2026, 9, 2),
        "OPP-1188": date(2026, 8, 4), "GL-2026-0712": date(2026, 8, 14), "GL-2026-0804": date(2026, 9, 15),
    }
    for (vendor, number, d, total, po, fn, lines) in INBOX_INVOICES:
        if number in paid:
            bills.append((vendor, number, paid[number], total))
    bills.append(("Casco Bay Janitorial Supply", "CB-2211", date(2026, 8, 6), 1184.60))
    bills.append(("Casco Bay Janitorial Supply", "CB-2211", date(2026, 8, 20), 1184.60))
    # June bills paid in July
    bills += [("Casco Bay Janitorial Supply", "CB-2176", date(2026, 7, 10), 901.35), ("Pine Point Fuel Co-op", "PPF-76820", date(2026, 7, 14), 1288.60),
              ("Fore River Auto & Fleet", "FRA-5498", date(2026, 7, 2), 274.50), ("Greenline Lawn & Snow", "GL-2026-0615", date(2026, 7, 17), 2150.00),
              ("Tidewater Plumbing", "TP-0855", date(2026, 7, 9), 640.00), ("Stitchworks Uniform Co.", "SW-3298", date(2026, 7, 21), 212.00),
              ("Old Port Print & Sign", "OPP-1150", date(2026, 7, 6), 148.00)]
    # recurring overhead
    for i, (y, m) in enumerate([(2026, 7), (2026, 8), (2026, 9)]):
        bills += [("Forest Avenue Holdings LLC", "RENT-2026-%02d" % m, date(y, m, 1), 3400.00),
                  ("Downeast Telecom", "DT-%d%02d-4471" % (y, m), date(y, m, 12), 318.40),
                  ("Casco Utilities Cooperative", "CUC-%d%02d-0092" % (y, m), date(y, m, 18), [412.77, 455.10, 398.62][i]),
                  ("Ledgerline Bookkeeping", "LB-%d-%02d" % (y, m), date(y, m, 5), 850.00),
                  ("Bayside Waste & Recycling", "BWR-%d%02d" % (y, m), date(y, m, 22), 265.00),
                  ("Harbor Light Payroll Services", "HLP-%d%02d" % (y, m), date(y, m, 15), 189.00)]
    bills.sort(key=lambda b: (b[2], b[0]))
    with open(os.path.join(D02, "quickbooks-bills-paid-q3.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["bill_no", "vendor", "invoice_number", "paid_date", "amount"])
        for k, (vendor, number, d, total) in enumerate(bills, start=1):
            w.writerow(["BILL-%d" % (10200 + k), vendor, number, d.isoformat(), "%.2f" % total])
    print("  quickbooks-bills-paid-q3.csv: %d rows" % len(bills))

    # --- 02: HubSpot deals
    deals = [
        ("Munjoy Hill Senior Residence - common areas", "Munjoy Hill Senior Residence", "Closed Won", 2400, date(2026, 7, 8), "Jordan Lee", date(2026, 5, 19)),
        ("Riverton Family Chiropractic - evening service", "Riverton Family Chiropractic", "Closed Won", 480, date(2026, 6, 20), "Jordan Lee", date(2026, 5, 4)),
        ("Pleasant Hill Veterinary - weekly", "Pleasant Hill Veterinary", "Closed Won", 3290, date(2026, 8, 4), "Jordan Lee", date(2026, 6, 30)),
        ("Lakeshore Property Partners - portfolio common areas", "Lakeshore Property Partners", "Proposal Sent", 8500, date(2026, 10, 31), "Jordan Lee", date(2026, 9, 10)),
        ("Marginal Way Medical Suites - Suite 300 expansion", "Marginal Way Medical Suites", "Negotiation", 1100, date(2026, 10, 15), "Jordan Lee", date(2026, 8, 20)),
        ("Westbrook Crossing - annex (4 suites)", "Westbrook Crossing Professional Park", "Negotiation", 1850, date(2026, 10, 9), "Jordan Lee", date(2026, 7, 29)),
        ("Cumberland Avenue Lofts - common areas", "Cumberland Avenue Lofts", "Closed Lost", 1900, date(2026, 8, 22), "Jordan Lee", date(2026, 6, 11)),
        ("Forest Avenue Dental Associates", "Forest Avenue Dental Associates", "Qualified", 720, date(2026, 11, 14), "Dana Whitfield", date(2026, 9, 2)),
        ("Saltbox Taproom - weekly", "Saltbox Taproom", "Discovery", 1450, date(2026, 11, 30), "Jordan Lee", date(2026, 9, 22)),
        ("Ledgewood Office Park - nightly", "Ledgewood Office Park", "Proposal Sent", 5600, date(2026, 10, 24), "Jordan Lee", date(2026, 8, 12)),
        ("Portside Yoga Collective", "Portside Yoga Collective", "Closed Lost", 540, date(2026, 7, 30), "Jordan Lee", date(2026, 6, 2)),
        ("North Deering Family Practice", "North Deering Family Practice", "Qualified", 960, date(2026, 12, 5), "Dana Whitfield", date(2026, 9, 15)),
        ("Rosemont Market Hall - nightly", "Rosemont Market Hall", "Discovery", 2100, date(2026, 12, 19), "Jordan Lee", date(2026, 9, 28)),
        ("Deering Center Daycare", "Deering Center Daycare", "Closed Lost", 830, date(2026, 9, 12), "Dana Whitfield", date(2026, 7, 21)),
        ("Sawyer Street Condominium Trust - common areas", "Sawyer Street Condominium Trust", "Proposal Sent", 2300, date(2026, 11, 7), "Jordan Lee", date(2026, 8, 25)),
    ]
    wb = new_wb()
    ws = wb.active
    ws.title = "Deals"
    ws.append(["Deal Name", "Company", "Deal Stage", "Amount (monthly)", "Close Date", "Deal Owner", "Pipeline", "Create Date"])
    for (name, company, stage, amt, close, owner, created) in deals:
        ws.append([name, company, stage, amt, close, owner, "Sales Pipeline", created])
    for row in ws.iter_rows(min_row=2):
        row[3].number_format = '"$"#,##0'
        row[4].number_format = "yyyy-mm-dd"
        row[7].number_format = "yyyy-mm-dd"
    style_header(ws)
    autosize(ws)
    wb.save(os.path.join(D02, "hubspot-deals.xlsx"))
    print("  hubspot-deals.xlsx: %d deals" % len(deals))

    # --- 02: prose
    model = dict(ep_credit=EP_CREDIT, ep_q3_invoiced=sum(v["amount"] for v in q3_inv if v["cust"] == EP),
                 q3_total=sum(v["amount"] for v in q3_inv),
                 handy_hours_start=2.1, handy_hours_now=3.4)
    with open(os.path.join(D02, "slack-export", "ops-channel.txt"), "w") as f:
        f.write(content.SLACK_LINES + "\n")
    tr = content.transcript(model)
    with open(os.path.join(D02, "meeting-transcript-2026-09-18-ops.txt"), "w") as f:
        f.write(tr)
    print("  transcript: %d words; slack: %d lines" % (len(tr.split()), content.SLACK_LINES.count("\n") + 1))
    for thread in content.gmail_threads(model):
        write_gmail_pdf(os.path.join(D02, "gmail-export", thread["filename"]), thread)
    print("  gmail-export: %d PDFs" % len(content.gmail_threads(model)))

    # --- 03: dashboard
    clean_dir(D03)
    agg = {}
    for v in invoices:
        i = month_index(v["date"])
        k = (i, v["cust"], v["line"])
        a = agg.setdefault(k, dict(revenue=0.0, cost=0.0, hours=0.0, jobs=0))
        a["revenue"] = money(a["revenue"] + v["amount"])
    for j in jobs:
        if j["status"] != "Completed":
            continue
        i = month_index(j["date"])
        k = (i, j["cust"], j["line"])
        a = agg.setdefault(k, dict(revenue=0.0, cost=0.0, hours=0.0, jobs=0))
        a["cost"] = money(a["cost"] + direct_cost(j["line"], j["hours"], j["price"]))
        a["hours"] += j["hours"]
        a["jobs"] += 1
    rows = []
    for (i, cid, line) in sorted(agg, key=lambda k: (k[0], k[1], k[2])):
        a = agg[(i, cid, line)]
        rows.append([month_end(i), month_label(i), cid, CUST[cid]["name"], line, a["revenue"], a["cost"], round(a["hours"], 2), a["jobs"]])
    header = ["month_end", "month", "customer_id", "customer", "service_line", "revenue", "direct_cost", "crew_hours", "jobs"]
    with open(os.path.join(D03, "revenue_30mo.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow([r[0].isoformat()] + r[1:5] + ["%.2f" % r[5], "%.2f" % r[6], "%.2f" % r[7], r[8]])
    wb = new_wb()
    ws = wb.active
    ws.title = "Monthly"
    ws.append(header)
    for r in rows:
        ws.append(r)
    for row in ws.iter_rows(min_row=2):
        row[0].number_format = "yyyy-mm-dd"
        row[5].number_format = '#,##0.00'
        row[6].number_format = '#,##0.00'
        row[7].number_format = '0.00'
    style_header(ws)
    autosize(ws)
    ws2 = wb.create_sheet("Customers")
    ws2.append(["customer_id", "customer", "type", "segment", "neighborhood", "cadence", "first_month", "last_month", "contact", "notes"])
    for c in CUSTOMERS:
        months = [k[0] for k in agg if k[1] == c["id"]]
        ws2.append([c["id"], c["name"], c["type"], c["segment"], c["neighborhood"], c["cadence"],
                    month_label(min(months)) if months else "", month_label(max(months)) if months else "",
                    c["contact"], c["notes"]])
    style_header(ws2)
    autosize(ws2)
    ws3 = wb.create_sheet("Notes")
    notes = [
        "Northwind Home Services - revenue by customer and service line, April 2024 to September 2026 (30 months).",
        "Practice file. The company, every customer and every number is fictional.",
        "",
        "Monthly sheet, one row per customer x month x service line:",
        "  month_end    last day of the month, stored as a real date",
        "  month        the same month as text, yyyy-mm (if EOMONTH or a date function returns 0 on this column, it is because this is text, use month_end)",
        "  revenue      invoiced revenue from QuickBooks, by invoice date",
        "  direct_cost  crew labor plus supplies or materials for the jobs done that month",
        "  crew_hours   hours logged by the crews in the scheduling system for that month",
        "  jobs         completed jobs that month",
        "",
        "Revenue for July, August and September 2026 equals the QuickBooks invoices in 02-sources/quickbooks-invoices-q3.csv, by customer and month.",
        "A row with crew hours and no revenue is work that was done but not invoiced that month.",
        "Gross margin = (revenue - direct_cost) / revenue. Overhead (office, vans, insurance, software) is not in direct_cost.",
    ]
    for n in notes:
        ws3.append([n])
    ws3.column_dimensions["A"].width = 140
    wb.save(os.path.join(D03, "northwind-revenue-30mo.xlsx"))
    print("  northwind-revenue-30mo.xlsx + revenue_30mo.csv: %d rows" % len(rows))

    # planted dashboard prints
    hm = {}
    for (i, cid, line), a in agg.items():
        if line == HANDY:
            h = hm.setdefault(i, dict(hours=0.0, jobs=0, rev=0.0, cost=0.0))
            h["hours"] += a["hours"]; h["jobs"] += a["jobs"]; h["rev"] += a["revenue"]; h["cost"] += a["cost"]
    first3 = [hm[i] for i in range(0, 3)]
    last3 = [hm[i] for i in range(27, 30)]
    hpj0 = sum(h["hours"] for h in first3) / sum(h["jobs"] for h in first3)
    hpj1 = sum(h["hours"] for h in last3) / sum(h["jobs"] for h in last3)
    ppj0 = sum(h["rev"] for h in first3) / sum(h["jobs"] for h in first3)
    ppj1 = sum(h["rev"] for h in last3) / sum(h["jobs"] for h in last3)
    gm0 = 1 - sum(h["cost"] for h in first3) / sum(h["rev"] for h in first3)
    gm1 = 1 - sum(h["cost"] for h in last3) / sum(h["rev"] for h in last3)
    print("  PLANTED  handyman hours/job: %.2f (Apr-Jun 2024) -> %.2f (Jul-Sep 2026); price/job $%.0f -> $%.0f; gross margin %.0f%% -> %.0f%%" % (hpj0, hpj1, ppj0, ppj1, 100 * gm0, 100 * gm1))
    turn = {}
    for (i, cid, line), a in agg.items():
        if CUST[cid]["cadence"] == "turnover":
            turn[MONTHS[i][1]] = turn.get(MONTHS[i][1], 0) + a["revenue"]
    print("  PLANTED  seasonality, turnover revenue by calendar month (all years): Jan $%s  Jul $%s  (summer peak)" % (f"{turn[1]:,.0f}", f"{turn[7]:,.0f}"))

    # --- 01: invoice inbox
    clean_dir(D01)
    for (vendor, number, d, total, po, fn, lines) in INBOX_INVOICES:
        write_invoice_pdf(os.path.join(D01, fn), vendor, number, d, total, po, lines)
    shutil.copyfile(os.path.join(D01, DUPLICATE_FILE[0]), os.path.join(D01, DUPLICATE_FILE[1]))
    blank = new_pdf()
    blank.output(os.path.join(D01, BLANK_SCAN))
    with open(os.path.join(D01, "note to self.txt"), "w") as f:
        f.write(content.NOTE_TO_SELF)
    write_receipt_png(os.path.join(D01, "IMG_4502.png"), "PINE POINT FUEL CO-OP", "14 Pine Point Rd, Scarborough ME",
                      datetime(2026, 8, 9, 7, 42), [("Pump 3  Unleaded", 0.0), ("24.902 gal @ 3.469", 86.40)], 86.40,
                      ["Member: NW HOME SVCS", "Vehicle: VAN 2", "Paid: Fleet card ****4471", "Thank you"])
    write_receipt_png(os.path.join(D01, "receipt.png"), "DEERING HARDWARE & SUPPLY", "1012 Forest Ave, Portland ME",
                      datetime(2026, 9, 14, 15, 18), [("Door closer, comm.", 38.99), ("Weatherstrip 17ft", 6.49), ("Tax", 2.44)], 47.92,
                      ["Paid: Visa ****2210", "Return within 30 days", "Thank you for shopping local"])
    n = len([f for f in os.listdir(D01) if f not in KEEP])
    print("  01-invoices-inbox: %d files (%d invoice PDFs incl. 1 duplicate, 1 blank scan, 2 receipts, 1 note)" % (n, len(INBOX_INVOICES) + 1))
    print("  PLANTED  duplicate: CB-2211 $1,184.60 as '%s' and '%s' (identical bytes)" % DUPLICATE_FILE)
    print("  PLANTED  no PO: Tidewater Plumbing TP-0893 $3,250.00 ('plumber invoice.pdf')")
    print("  PLANTED  unreadable: %s (blank page); undated: 'note to self.txt'" % BLANK_SCAN)

    # --- 04: prospect (pages + call notes + email)
    os.makedirs(D04, exist_ok=True)
    for page in content.PROSPECT_PAGES:
        write_webpage_pdf(os.path.join(D04, page["filename"]), page)
    with open(os.path.join(D04, "call-notes-first-call.txt"), "w") as f:
        f.write(content.CALL_NOTES)
    write_gmail_pdf(os.path.join(D04, content.prospect_email()["filename"]), content.prospect_email())
    print("  04-prospect: %d web-page PDFs, call notes, 1 email PDF" % len(content.PROSPECT_PAGES))
    print("  PLANTED  Lakeshore: budget $110K/yr on the call -> 'closer to $80,000' in the Oct 1 email; floor $6,200/mo in call notes (do not say it)")
    print("done")


if __name__ == "__main__":
    main()
