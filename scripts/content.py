"""Prose for the Northwind workshop pack: emails, Slack, the ops meeting
transcript, and the Lakeshore prospect pages. Imported by generate.py.
Everything here is fiction. Numbers that must tie out are passed in by
generate.py so the prose and the data come from one model."""

# ---------------------------------------------------------------- Gmail
# Each email: filename, subject, list of messages (sender name, sender email,
# recipients line, date line, body). Dana's address is dana@northwindhome.example.

DANA = ("Dana Whitfield", "dana@northwindhome.example")
ELENA = ("Elena Marsh", "elena@northwindhome.example")
JORDAN = ("Jordan Lee", "jordan@northwindhome.example")


def gmail_threads(m):
    """m is the model dict from generate.py (gives invoice numbers etc.)."""
    return [
        {
            "filename": "Re_ Q3 rate change - Old Port Dental.pdf",
            "subject": "Re: Q3 rate change - Old Port Dental",
            "messages": [
                (
                    "Renee Castonguay", "renee@oldportdental.example",
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Mon, Jul 27, 2026 at 3:48 PM",
                    "Hi Dana,\n\nQuick one. We are dropping the Saturday floor polish from the schedule, the hygienists said it is not needed now that the new flooring is in. Two evening visits a month is still right.\n\nWe have been at $640 a month. With the Saturday piece gone, can we move to $560 a month starting with the August visits?\n\nThanks,\nRenee\nOffice Manager, Old Port Dental",
                ),
                (
                    DANA[0], DANA[1],
                    "To: Renee Castonguay <renee@oldportdental.example>",
                    "Tue, Jul 28, 2026 at 8:05 AM",
                    "Hi Renee,\n\nYes. $560 a month effective August 1, two evening visits, no Saturday polish. I'll have Elena update the invoice so August bills at the new rate.\n\nIf the hygienists change their minds about the floors, just tell us and we'll add it back for that month.\n\nThanks so much,\nDana",
                ),
                (
                    "Renee Castonguay", "renee@oldportdental.example",
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Tue, Jul 28, 2026 at 9:12 AM",
                    "Perfect, thank you Dana. I'll let Dr. Pham know.\n\nRenee",
                ),
            ],
        },
        {
            "filename": "Re_ August arrival times - Eastern Promenade.pdf",
            "subject": "Re: August arrival times - Eastern Promenade",
            "messages": [
                (
                    "Gretchen Aldana", "galdana@easternpromcondo.example",
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Thu, Sep 3, 2026 at 11:20 AM",
                    "Dana,\n\nThree times in August the crew arrived after the window closed: August 6 (window ended 9:00, crew in at 9:40), August 13 (ended 9:00, in at 9:25) and August 27 (ended 9:00, in at 10:05). On the 27th the board president was in the lobby waiting for them.\n\nI know your standards document says a credit applies. I would rather talk about how we keep this from happening in the fall than argue about the number, but the board will ask me about both.\n\nGretchen Aldana\nProperty Manager, Eastern Promenade Condominium Association",
                ),
                (
                    DANA[0], DANA[1],
                    "To: Gretchen Aldana <galdana@easternpromcondo.example>",
                    "Fri, Sep 4, 2026 at 7:41 AM",
                    "Hi Gretchen,\n\nThat is on us, and I'm sorry. Three in one month is not what you are paying for.\n\nMarcus is moving Crew C's first stop of the day so your building is the 7:00 start, not the second stop after Stroudwater. That starts Tuesday.\n\nOn the credit: I'll make it right on the September invoice and I'll bring the exact figure to you after our ops meeting on the 18th so the board has it in writing.\n\nThanks so much,\nDana",
                ),
            ],
        },
        {
            "filename": "Start date - Munjoy Hill Senior Residence.pdf",
            "subject": "Start date - Munjoy Hill Senior Residence",
            "messages": [
                (
                    "Lorraine Beaulieu", "lbeaulieu@munjoyseniorres.example",
                    "To: Jordan Lee <jordan@northwindhome.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                    "Fri, Jul 10, 2026 at 2:16 PM",
                    "Hi Jordan,\n\nThe signed agreement went back to you Tuesday ($2,400 a month, common areas and dining room five mornings a week). Our residents' council meets on the 16th and I would love to tell them when the first crew is coming. We were hoping for the week of July 20.\n\nWho should our front desk expect, and what time?\n\nLorraine Beaulieu\nExecutive Director, Munjoy Hill Senior Residence",
                ),
            ],
        },
        {
            "filename": "Re_ Fall turnover schedule - Casco Coast Property Management.pdf",
            "subject": "Re: Fall turnover schedule - Casco Coast Property Management",
            "messages": [
                (
                    "Hal Pettengill", "hal@cascocoastpm.example",
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Mon, Sep 14, 2026 at 9:02 AM",
                    "Dana,\n\nSummer is winding down. We will drop from the weekend turnovers to weekday only after October 1. Figure 5 or 6 a month through the winter instead of the 12 to 15 you have been doing. Same per-turnover price is fine.\n\nAlso, your August invoice matched our count exactly for the first time in a while. Whatever you changed, keep doing it.\n\nHal",
                ),
                (
                    DANA[0], DANA[1],
                    "To: Hal Pettengill <hal@cascocoastpm.example>",
                    "Mon, Sep 14, 2026 at 12:30 PM",
                    "Hi Hal,\n\nThat works. Weekday turnovers only from October 1, same price per turnover. Crew B will keep your buildings.\n\nThe change was that the crew lead sends the office the unit list the same day, so the invoice comes off the job sheet instead of memory. Glad it showed.\n\nThanks so much,\nDana",
                ),
            ],
        },
        {
            "filename": "Fwd_ Renewal quote - Pine Tree Mutual Insurance.pdf",
            "subject": "Fwd: Renewal quote - Pine Tree Mutual Insurance",
            "messages": [
                (
                    ELENA[0], ELENA[1],
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Wed, Sep 23, 2026 at 4:55 PM",
                    "Dana,\n\n$5,115 for Q4, up from $4,860. The increase is the fourth van and the commercial general liability bump for the condo accounts. Invoice is attached and due October 10. I'm fine paying it unless you want to shop it.\n\nElena\n\n---------- Forwarded message ---------\nFrom: Pine Tree Mutual Insurance <billing@pinetreemutual.example>\nDate: Wed, Sep 23, 2026 at 2:10 PM\nSubject: Renewal quote - Northwind Home Services - Q4 2026\n\nAttached is invoice PTM-2026-Q4-9107 for the October 1 to December 31 term. Premium $5,115.00. Please remit by October 10, 2026.",
                ),
                (
                    DANA[0], DANA[1],
                    "To: Elena Marsh <elena@northwindhome.example>",
                    "Wed, Sep 23, 2026 at 6:02 PM",
                    "Pay it. Not worth shopping for $255 a quarter while we are adding buildings.\n\nDana",
                ),
            ],
        },
        {
            "filename": "Re_ Invoice question - Harborview Orthodontics.pdf",
            "subject": "Re: Invoice question - Harborview Orthodontics",
            "messages": [
                (
                    "Dev Mehta", "dmehta@harborviewortho.example",
                    "To: Elena Marsh <elena@northwindhome.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                    "Tue, Sep 8, 2026 at 10:44 AM",
                    "Hi Elena,\n\nThe August invoice shows $1,150, same as July. We only had you in twice in August, is that right? I want to make sure we are not paying for a third visit.\n\nDev",
                ),
                (
                    ELENA[0], ELENA[1],
                    "To: Dev Mehta <dmehta@harborviewortho.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                    "Tue, Sep 8, 2026 at 11:30 AM",
                    "Hi Dev,\n\n$1,150 is two visits at $575 each: August 4 and August 18. The flat monthly amount is right. Your agreement is two evening visits a month, so it is $1,150 whether the month has four weeks or five.\n\nElena Marsh\nNorthwind Home Services",
                ),
            ],
        },
        {
            "filename": "Re_ Window washing above the second floor - Brackett Street Lofts.pdf",
            "subject": "Re: Window washing above the second floor - Brackett Street Lofts",
            "messages": [
                (
                    "Simone Travers", "board@brackettlofts.example",
                    "To: Dana Whitfield <dana@northwindhome.example>",
                    "Wed, Aug 12, 2026 at 5:30 PM",
                    "Dana,\n\nThe board would like the exterior windows on floors three and four done before the fall. Can your crew add that to the weekly visit?\n\nSimone",
                ),
                (
                    DANA[0], DANA[1],
                    "To: Simone Travers <board@brackettlofts.example>",
                    "Thu, Aug 13, 2026 at 7:50 AM",
                    "Hi Simone,\n\nNo, and I'd rather tell you that than have a crew member on a ladder where they should not be. Our crews do not go above the second rung of a ladder outside. Floors three and four need a lift and a specialty vendor.\n\nI can send two names we have worked with, and we'll do the first and second floor glass on the regular visit at no extra charge.\n\nThanks so much,\nDana",
                ),
            ],
        },
        {
            "filename": "Re_ PO numbers on invoices - Casco Bay Janitorial Supply.pdf",
            "subject": "Re: PO numbers on invoices - Casco Bay Janitorial Supply",
            "messages": [
                (
                    ELENA[0], ELENA[1],
                    "To: orders@cascobayjanitorial.example\nCc: Dana Whitfield <dana@northwindhome.example>",
                    "Mon, Jul 20, 2026 at 9:15 AM",
                    "Hello,\n\nStarting with your next invoice, please print our PO number on every invoice you send us. Our POs look like NW-2026-### and Marcus gives one with every order. We are getting invoices by email, by mail and in the drivers' hands, and the PO is the only way I can tell them apart.\n\nThank you,\nElena Marsh\nNorthwind Home Services",
                ),
                (
                    "Casco Bay Janitorial Supply", "orders@cascobayjanitorial.example",
                    "To: Elena Marsh <elena@northwindhome.example>",
                    "Mon, Jul 20, 2026 at 1:02 PM",
                    "Elena,\n\nWill do. The PO field prints on the invoice when the order desk keys it in; I have told them to ask for it on every Northwind order.\n\nBest,\nCasco Bay Janitorial Supply",
                ),
            ],
        },
    ]


# ---------------------------------------------------------------- Slack
# Lines in the #ops channel, Jul 1 - Sep 30 2026. Format "[YYYY-MM-DD HH:MM] Name: text".
SLACK_LINES = """[2026-07-01 07:12] Marcus: July board is up in Routeboard. Crew C has Stroudwater first then Eastern Prom, every weekday. Shout if anything looks wrong.
[2026-07-01 07:40] Marisol: looks right for A. Tanabe-Morrill moved to Thursdays starting this week, confirmed with her
[2026-07-01 08:03] Devin: B is good. Casco Coast sent 14 turnovers for the first two weeks, going to be tight
[2026-07-01 08:10] Marcus: take Nadia from A on the 2nd and 9th. Marisol can you spare her
[2026-07-01 08:12] Marisol: yes
[2026-07-02 16:48] Rafael: Brackett St water heater is beyond us, called Tidewater. they can do it the 14th
[2026-07-02 16:55] Marcus: ok. make sure Elena gets a PO to them before they start
[2026-07-06 09:30] Elena: reminder that vendor invoices go in the inbox tray or to ap@northwindhome.example, not in your van
[2026-07-07 12:14] Sofia: 5 star from Okafor on Monday's clean, she called out Marisol by name
[2026-07-08 15:02] Jordan: Munjoy Hill Senior Residence signed. $2,400/mo, five mornings a week, dining room and common areas. Sending the agreement to the shared drive
[2026-07-08 15:05] Dana: nice work
[2026-07-09 07:55] Marcus: van 2 brakes are grinding. Fore River can take it Wednesday. Crew A in van 4 that day
[2026-07-13 08:20] Tom: three cleaner interviews this week. two look good
[2026-07-14 13:31] Rafael: Tidewater finished Brackett St. tenants have hot water. invoice coming to Elena
[2026-07-15 10:02] Devin: Peaks Island ferry was late, turnovers ran to 6pm. all done
[2026-07-16 09:12] Sofia: Fore Street Bistro says the walk-in floor was skipped Tuesday. Kenji?
[2026-07-16 09:20] Kenji: it was not skipped, they had deliveries stacked on it. told the manager we'd do it Thursday
[2026-07-16 09:22] Sofia: ok I'll call them
[2026-07-20 08:45] Elena: Casco Bay is going to put our PO numbers on invoices going forward. Marcus please give them one on every order
[2026-07-20 08:50] Marcus: will do
[2026-07-22 14:10] Marisol: Pelletier wants to pause August, he's away. restarting Sept 8
[2026-07-22 14:15] Marcus: noted, I'll take him off the August board
[2026-07-27 16:30] Dana: Old Port Dental asked to drop the Saturday polish. going to say yes
[2026-07-28 08:10] Dana: told Renee $560/mo from August 1. Elena can you update the invoice
[2026-07-28 08:14] Elena: on my list
[2026-07-29 11:05] Kenji: Westbrook Crossing wants the annex quoted, 4 suites. Jordan
[2026-07-29 11:20] Jordan: on it
[2026-07-31 17:40] Marcus: good month. Casco Coast did 15 turnovers, record
[2026-08-03 07:30] Marcus: August board up. Crew C is Stroudwater 6:00 then Eastern Prom
[2026-08-04 09:15] Tom: new hires start the 5th of October, offer letters out
[2026-08-05 16:50] Rafael: Back Cove Bakery rear door closer done, also did the weatherstrip. they want shelving in dry storage next week
[2026-08-06 10:10] Kenji: late to Eastern Prom today, Stroudwater ran long. in at 9:40
[2026-08-06 10:15] Marcus: text Gretchen before the window closes next time, not after
[2026-08-06 10:16] Kenji: yeah
[2026-08-10 13:22] Sofia: Lindqvist left a 4 star, said the crew was great but arrived at the very end of the window
[2026-08-12 15:40] Rafael: Back Cove shelving done
[2026-08-13 10:02] Kenji: Eastern Prom again, in at 9:25. Stroudwater had a flooded elevator pit we had to work around
[2026-08-13 10:08] Marcus: ok. I'm going to look at flipping the order
[2026-08-14 09:12] Marisol: van 1 is shifting weird
[2026-08-14 09:20] Marcus: Fore River has it the 20th. that's the transmission service they warned us about
[2026-08-17 08:00] Devin: Pleasant Hill Vet starts today, Mondays
[2026-08-19 15:45] Marisol: Priya Natarajan on Pine St is not happy. kitchen and both baths were missed on today's clean, she sent photos. I told her we'd come back Thursday and redo them, no charge
[2026-08-19 15:50] Marcus: ok. make sure the office knows it's no charge
[2026-08-19 15:52] Marisol: told Sofia
[2026-08-19 16:01] Sofia: logged. I'll call her tonight too
[2026-08-21 14:20] Marisol: Priya re-clean done. she's happy, said thank you for coming back
[2026-08-24 08:30] Elena: Casco Bay sent the July 28 invoice again by mail. anyone know if the emailed one got paid already
[2026-08-24 08:41] Marcus: no idea. check the stack in the tray
[2026-08-26 17:10] Rafael: Back Cove stair tread fixed. that's three jobs for them this month, Elena do you want them on one invoice
[2026-08-26 17:30] Elena: yes, I'll do it with the September run
[2026-08-27 10:30] Kenji: Eastern Prom 10:05 today. board president was in the lobby. not great
[2026-08-27 10:35] Marcus: that's three this month. flipping the order starting next week, Eastern Prom is the 7:00 start
[2026-08-27 10:36] Dana: I'll call Gretchen
[2026-08-28 16:00] Devin: Longfellow St wants 4 turnovers Saturday. doable with Nadia
[2026-09-01 07:25] Marcus: September board up. Crew C: Eastern Prom 7:00, Stroudwater after
[2026-09-01 07:50] Kenji: good
[2026-09-02 11:10] Tom: Stitchworks jackets came in, 30 of them. in the back closet
[2026-09-03 09:40] Rafael: Tanabe-Morrill deck railing took 4 hours, the posts were rotted under the paint. quoted 2.5
[2026-09-03 09:45] Marcus: that's the third one like that this month
[2026-09-04 08:05] Dana: talked to Gretchen. September invoice gets a credit, we'll set the number at the ops meeting on the 18th
[2026-09-08 09:00] Marisol: Pelletier back on the board, cleaned today
[2026-09-10 14:15] Elena: September invoices go out the 30th as usual. anything that needs a credit or a change, tell me by the 25th
[2026-09-14 12:40] Dana: Casco Coast dropping to weekday turnovers after Oct 1. Devin that frees up your Saturdays
[2026-09-14 12:44] Devin: finally
[2026-09-16 15:30] Rafael: Tidewater did the Ocean Ave Pediatrics backflow. invoice to Elena
[2026-09-18 11:05] Dana: ops meeting notes are in the drive. Marcus has the action items
[2026-09-21 09:12] Jordan: Lakeshore Property Partners second call is Thursday the 24th. 48 buildings. if we get it, it's the biggest thing since Eastern Prom
[2026-09-21 09:15] Dana: send me your notes from the first call before then
[2026-09-22 10:20] Sofia: 2 star from a Spring Street Studios tenant about the restroom. not our account tenant, our account is the studio. replied and called the studio manager
[2026-09-24 14:50] Jordan: Lorraine from Munjoy Hill Senior Residence called me. asked if we are still coming. I thought that got handed off in July?
[2026-09-24 14:58] Marcus: first I'm hearing of it. nothing in Routeboard for them
[2026-09-24 15:02] Jordan: I sent the agreement to the drive on the 8th and told Dana. did nobody set up the account
[2026-09-24 15:10] Dana: call me
[2026-09-25 08:30] Marcus: Crew C hasn't missed an Eastern Prom window since the flip. Kenji thank you
[2026-09-25 08:33] Kenji: easy when you're the first stop
[2026-09-28 16:45] Elena: Q4 insurance is $5,115, Dana said pay it
[2026-09-29 09:10] Tom: October 5 start for the three new cleaners is confirmed. Marisol gets two, Devin gets one
[2026-09-30 17:20] Marcus: September board closed. 3 cancels all month, all customer side
[2026-09-30 17:25] Elena: September invoices out
""".strip("\n")


# ---------------------------------------------------------------- Transcript
def transcript(m):
    """Zoom-style transcript of the Sep 18 2026 ops meeting. m gives numbers."""
    ep_credit = m["ep_credit"]          # 1200
    ep_q3 = m["ep_q3_invoiced"]         # computed
    handy_h_start = m["handy_hours_start"]
    handy_h_now = m["handy_hours_now"]
    q3_round = int(-(-m["q3_total"] // 10000) * 10000)        # rounded up to the next $10,000 ("a little under")
    ep_q3_round = int(round(ep_q3 / 5000.0) * 5000)           # nearest $5,000 ("about")
    lines = [
        ("00:00:04", "Dana Whitfield", "Okay, I think we have everyone. Marcus, Elena, Jordan, Sofia, Tom. Rafael is joining from the van. This is the September ops meeting, and I want to get through four things: the August arrival problem at Eastern Promenade, the handyman hours, hiring, and Lakeshore. Elena has a billing item at the end."),
        ("00:00:31", "Marcus Reyes", "Rafael says he can hear us, his camera is off."),
        ("00:00:35", "Rafael Ortiz", "I'm here. Parked."),
        ("00:00:38", "Dana Whitfield", "Good. Let's start with Eastern Promenade because Gretchen is waiting on me. In August, Crew C arrived after the window closed three times. August 6, August 13, August 27. She sent me the times. On the 27th the board president was standing in the lobby."),
        ("00:01:02", "Marcus Reyes", "All three were the same cause. Stroudwater was the first stop and it kept running long. The elevator pit flooded on the 13th. On the 27th it was a delivery blocking the loading dock. We flipped the order on September 1. Eastern Prom is the 7:00 start now and Stroudwater is second."),
        ("00:01:25", "Dana Whitfield", "And since the flip?"),
        ("00:01:27", "Marcus Reyes", "Zero misses. Two and a half weeks. Kenji has been in the building by 6:55 every day."),
        ("00:01:34", "Dana Whitfield", "Okay. That's the fix. Now the credit. Our service standards say a missed window gets a credit, and for a commercial account it totals on the monthly statement. The standard residential number is $45 an hour of labor. That is not the right number for a building that pays us what Eastern Promenade pays us."),
        ("00:01:58", "Elena Marsh", "What did you tell Gretchen?"),
        ("00:02:01", "Dana Whitfield", "I told her I'd make it right on the September invoice and bring the number here first. Here is the number. $400 per missed window, three windows, $1,200 total, as a credit line on the September invoice. That is roughly a third of one week of service. The board sees it in writing, it's done, and we move on."),
        ("00:02:24", "Jordan Lee", "I'd rather do that than have it come up in the contract conversation in January. $1,200 against what they pay us a year is nothing."),
        ("00:02:33", "Elena Marsh", "Fine with me. I need it by the 25th to get it on the September run. The September invoice goes out on the 30th."),
        ("00:02:41", "Dana Whitfield", "You have it now. $1,200 credit, Eastern Promenade, September invoice. Marcus, put it in the action items. Elena owns it."),
        ("00:02:49", "Marcus Reyes", "Got it."),
        ("00:02:51", "Sofia Alvarez", "Do you want me to send Gretchen anything, or is that you?"),
        ("00:02:55", "Dana Whitfield", "That's me. I'll email her today with the number and the schedule change. You take the board president if he calls."),
        ("00:03:03", "Sofia Alvarez", "Okay."),
        ("00:03:06", "Dana Whitfield", "Second thing. Handyman hours. Rafael, you're on."),
        ("00:03:11", "Rafael Ortiz", "So the thing Marcus flagged in Slack. We quote a job at two, two and a half hours and it takes four. The deck railing at Tanabe-Morrill, the posts were rotted under the paint. The Brackett Street laundry room door, the frame was out of square. Three of those in September already."),
        ("00:03:33", "Dana Whitfield", "Elena, what does it look like in the numbers?"),
        ("00:03:36", "Elena Marsh", f"When we started tracking it in the spring of 2024 a handyman job averaged about {handy_h_start} crew hours. The last three months it is about {handy_h_now}. The price per job has not moved. We are still quoting $385 to $640 depending on the job, same list as two years ago. So the margin on that line has been walking down for a long time and nobody was looking at it because the total revenue on the line kept growing."),
        ("00:04:05", "Dana Whitfield", "So we're doing more jobs and making less on each one."),
        ("00:04:08", "Elena Marsh", "Yes. And it's not a Rafael problem. The jobs are harder. Half of them now come from the commercial accounts, and a door in a 1920s condo building is not a door in a ranch house in Deering."),
        ("00:04:22", "Rafael Ortiz", "I've been saying that."),
        ("00:04:24", "Dana Whitfield", "You have. Okay. Two things. One, Rafael, from October 1, every handyman quote over two hours gets a site visit before we quote, not a phone estimate. Two, Elena, build me the price list with the hours we actually spend, not the hours we quoted in 2024, and we'll reprice in January with the commercial contracts."),
        ("00:04:48", "Elena Marsh", "I can have that for the October meeting."),
        ("00:04:51", "Dana Whitfield", "Good. Tom, hiring."),
        ("00:04:54", "Tom Kowalski", "Three cleaners start October 5. Two go to Marisol on Crew A, one to Devin on Crew B. Offer letters are signed. Uniforms came in from Stitchworks, they're in the back closet. I still need one more for Crew C by November if Jordan closes anything."),
        ("00:05:12", "Marcus Reyes", "On that. If Lakeshore happens we need a whole crew, not one person. Sixty buildings weekly is four people and a van, minimum. I'd want them hired by the middle of October to be ready for November 1."),
        ("00:05:26", "Tom Kowalski", "Then I need to know by October 1 whether to post. I can get four in three weeks if I start now. I cannot get four in one week."),
        ("00:05:35", "Dana Whitfield", "Post it on October 1 either way. If Lakeshore doesn't close we are still short on Crew C and we have the annex at Westbrook Crossing and the Marginal Way expansion in the pipeline. Worst case we hire two instead of four."),
        ("00:05:49", "Tom Kowalski", "Okay. Posting goes up October 1."),
        ("00:05:52", "Elena Marsh", "One more thing on people. Routeboard is billing us for 24 seats. We have 19 people on it. I asked Marcus to look at who the other five are."),
        ("00:06:01", "Marcus Reyes", "Three are people who left. One is a test account from when we set it up. One I can't identify. I'll clean it up this week. That's $95 a month we've been paying for nothing."),
        ("00:06:12", "Dana Whitfield", "Do it today. Elena, that's a good catch. Tom, when someone leaves, the checklist includes taking them off Routeboard. Add it."),
        ("00:06:21", "Tom Kowalski", "Added."),
        ("00:06:23", "Jordan Lee", "Which brings us to Lakeshore."),
        ("00:05:14", "Dana Whitfield", "Go."),
        ("00:05:16", "Jordan Lee", "Lakeshore Property Partners. Property manager in Portland, 48 buildings, and they just bought 12 more in South Portland, which was in the paper. They fired their cleaning vendor in June. The ops director is Tobias Renner. I had the first call with him on the 16th, Dana you were on for the last fifteen minutes. He said the budget is around $110,000 a year, decision by the end of October, and they're talking to three vendors including us."),
        ("00:05:48", "Dana Whitfield", "Who are the other two?"),
        ("00:05:50", "Jordan Lee", "ProClean Maine, which has a per-unit price on their website. And he mentioned Bay State Facility Group, which is the big regional one, and Coastal Commercial Clean. So three, and us. He asked twice whether we have done anything at 48 buildings. I said Eastern Promenade is 11 buildings and 340 units and we've held it for two and a half years."),
        ("00:06:14", "Dana Whitfield", "That's the right answer. What's the second call?"),
        ("00:06:17", "Jordan Lee", "Thursday the 24th. He wants a proposal in hand by the end of the month."),
        ("00:06:21", "Dana Whitfield", "Okay. I'll be on it. Here is what I want everyone to understand about Lakeshore. If we win it, it is the biggest account since Eastern Promenade, and it means we have two customers that together are more than half of the company. Elena, what is Eastern Promenade as a share of us right now?"),
        ("00:06:42", "Elena Marsh", "Trailing twelve months, Eastern Promenade is about 31 percent of revenue. Lakeshore at $110,000 would be another four percent, so it's not the same thing. But it would be our second biggest commercial account on day one."),
        ("00:06:58", "Dana Whitfield", "Right. So I want to win it, and I don't want to win it at a price that loses money. Jordan, before Thursday, I want a floor from Elena. The number below which we say no. And nobody says that number on the call."),
        ("00:07:12", "Jordan Lee", "Understood."),
        ("00:07:14", "Elena Marsh", "I'll have it to you both tomorrow. It'll be a monthly number."),
        ("00:07:18", "Jordan Lee", "Can I say one more thing about how we pitch it? What Tobias kept coming back to was reporting. He's hiring a coordinator whose whole job is a vendor scorecard. Nobody else is going to lead with that. ProClean leads with price per unit. The big regional leads with being big. If we walk in with a sample monthly report, with photos, using Eastern Promenade as the example, that's the thing he can hand to his owners."),
        ("00:07:44", "Dana Whitfield", "Yes. Build the sample from a real month at Eastern Promenade, with Gretchen's permission, with the three missed windows in it. Don't hide them. Show the credit, show the fix, show September with zero misses. That is the report. A vendor who tells you when they missed is the one you keep."),
        ("00:08:03", "Jordan Lee", "I like that. I'll ask Gretchen tomorrow."),
        ("00:08:06", "Sofia Alvarez", "If it helps, I can pull the tenant reviews for Lakeshore. The complaints are public. Slow maintenance, dirty hallways, laundry rooms. If the proposal answers those by name, it reads like we did the homework."),
        ("00:08:18", "Dana Whitfield", "Do that. Send it to Jordan by Monday."),
        ("00:08:21", "Dana Whitfield", "Good. Marcus, anything on the vans?"),
        ("00:07:21", "Marcus Reyes", "Van 1 transmission service is done, that was $2,247 at Fore River. Van 2 brakes were done in July. Van 3 goes in for inspection. We're fine through the winter. The snow contract with Greenline renews November 1, and I want to add the two new condo accounts to it."),
        ("00:07:40", "Dana Whitfield", "Do it. Elena, get a PO to Greenline for the renewal so we are not chasing it in December."),
        ("00:07:46", "Elena Marsh", "Okay. That's a good segue to my item."),
        ("00:07:49", "Dana Whitfield", "Go ahead."),
        ("00:07:51", "Elena Marsh", "Vendor invoices. I have a tray with about thirty things in it from this quarter. Some came by email, some by mail, some came out of a van. Casco Bay sent at least one invoice twice, once by email and once on paper, and I am not sure whether I paid it twice. Tidewater's August invoice has no PO on it at all. Fuel co-op statements come as photos of the pump receipt. I spend a day a month on this."),
        ("00:08:22", "Dana Whitfield", "What do you need?"),
        ("00:08:24", "Elena Marsh", "Two things. One, every vendor gets told: PO number on the invoice or it does not get paid. I started with Casco Bay in July. Two, I want to stop accepting paper. Everything to ap@northwindhome.example."),
        ("00:08:38", "Marcus Reyes", "The subs won't all do that. Tidewater is one guy and a truck."),
        ("00:08:42", "Elena Marsh", "Then he hands it to Rafael and Rafael takes a photo and emails it. The point is one inbox."),
        ("00:08:48", "Dana Whitfield", "Agreed. One inbox, PO on everything, and Elena, if you think you paid Casco Bay twice, find out this week and get the credit. Marcus, the PO rule goes in the vendor letter. Sofia, anything on reviews?"),
        ("00:09:03", "Sofia Alvarez", "Quiet month. One two-star from a tenant at Spring Street Studios about a restroom, which is not our scope, the studio manager knows. The Priya Natarajan re-clean in August went well, she left a five-star after. That's the one where Marisol missed the kitchen and baths and went back Thursday at no charge."),
        ("00:09:24", "Dana Whitfield", "Good. That is exactly how I want those handled. Own it, go back, no charge, no argument."),
        ("00:09:31", "Sofia Alvarez", "The review follow-up log is current. Nothing older than two days."),
        ("00:09:35", "Marcus Reyes", "Two scheduling things before you wrap. Casco Coast goes to weekday-only turnovers after October 1, Hal emailed Dana. That's five or six a month instead of twelve to fifteen. Devin gets his Saturdays back, and I'm going to use Crew B on Saturdays for the fall deep cleans we've been turning away."),
        ("00:09:52", "Dana Whitfield", "Good. What's the second?"),
        ("00:09:54", "Marcus Reyes", "Peaks Island winds down after Columbus Day. The ferry schedule changes and Bev only has two or three units going in the winter. Same as last year. I'll pull Nadia back to Crew A full time in October."),
        ("00:10:05", "Dana Whitfield", "Fine. Elena, where did the quarter land? Rough."),
        ("00:10:08", "Elena Marsh", f"Rough, with September not out yet: a little under ${q3_round:,} invoiced for the quarter, which is the best quarter we've had. Eastern Promenade is about ${ep_q3_round:,} of that. Commercial overall is roughly four out of every five dollars now. Residential is flat, which is fine, that's not where we are investing. Handyman revenue is up and the margin on it is down, which is the conversation we just had."),
        ("00:10:34", "Dana Whitfield", "And collections?"),
        ("00:10:36", "Elena Marsh", "Two August invoices are past due, Fore Street Bistro and the Castellano statement. Both small. I'll call them this week. Everything else from July and August is paid."),
        ("00:10:45", "Dana Whitfield", "Okay. Last thing from me. Q3 closes in twelve days. Elena, when the September invoices go out on the 30th, I want the quarter in one place. What we invoiced, by customer. What the crews actually did, from Routeboard. And anything we promised somebody that is not on an invoice, because I am sure there is some of that and I would rather find it than have a customer find it."),
        ("00:10:02", "Elena Marsh", "That is going to take me a week."),
        ("00:10:05", "Dana Whitfield", "Then it takes a week. Marcus, action items."),
        ("00:10:09", "Marcus Reyes", f"One. Elena, ${ep_credit:,} credit on the Eastern Promenade September invoice, by the 25th. Two. Dana emails Gretchen today with the number and the schedule change. Three. Rafael, site visit before any handyman quote over two hours, from October 1. Four. Elena, handyman price list with real hours, for the October meeting. Five. Elena, floor number for Lakeshore to Dana and Jordan by tomorrow. Six. Greenline PO for the snow renewal. Seven. Vendor letter, PO on every invoice, one inbox. Eight. Elena checks whether Casco Bay was paid twice. Nine. Q3 reconciliation after the 30th."),
        ("00:10:52", "Dana Whitfield", "That's it. Thanks everyone. Rafael, drive safe."),
        ("00:10:56", "Rafael Ortiz", "Thanks."),
    ]
    header = (
        "Northwind Home Services - Ops meeting\n"
        "Recorded via Zoom - Sep 18, 2026 10:00 AM Eastern\n"
        "Participants: Dana Whitfield, Marcus Reyes, Elena Marsh, Jordan Lee, Sofia Alvarez, Tom Kowalski, Rafael Ortiz\n"
        "Transcript generated automatically. Speaker labels may contain errors.\n\n"
    )
    # timestamps are derived from word counts (about 2.6 words a second) so inserted lines stay in order
    out, secs = [], 4
    for _t, who, text in lines:
        out.append("%02d:%02d:%02d %s: %s" % (secs // 3600, (secs % 3600) // 60, secs % 60, who, text))
        secs += max(2, int(round(len(text.split()) / 2.6)))
    body = "\n\n".join(out)
    return header + body + "\n"


# ---------------------------------------------------------------- Note to self
NOTE_TO_SELF = """ask Elena if the fuel co-op statement is monthly or per fill, the pump receipts are in my phone
Greenline snow contract auto renews, call them before it does and add Baxter Woods and Brackett St
Routeboard is charging 24 seats. we have 19 people on it. who are the other 5
Pine Tree needs the updated vehicle list before the Q4 premium is final, van 4 is not on it
the plumber's invoice for Brackett St has no PO on it, Marcus said he gave him one verbally
"""


# ---------------------------------------------------------------- Prospect pages (exercise 4)
PROSPECT_PAGES = [
    {
        "filename": "About - Lakeshore Property Partners.pdf",
        "url": "https://lakeshorepartners.example/about",
        "saved": "Saved Sep 29, 2026, 8:14 AM",
        "title": "About Lakeshore Property Partners",
        "blocks": [
            ("h1", "Managing the places people call home"),
            ("p", "Lakeshore Property Partners manages 48 residential buildings across Portland, Westbrook and Scarborough, Maine: 1,140 apartments, from six-unit Victorians on the West End to a 96-unit building in Bayside. We have managed property in Greater Portland since 2011."),
            ("h2", "What we do"),
            ("p", "We handle leasing, rent collection, maintenance, vendor management and owner reporting for private owners and small investment groups. Owners get a monthly statement, a quarterly building walk with photos and a single point of contact."),
            ("h2", "Leadership"),
            ("p", "Meredith Choate, Founder and Chief Executive. Meredith started Lakeshore with two buildings on Brackett Street and has grown it building by building."),
            ("p", "Tobias Renner, Director of Operations. Tobias joined in 2024 from a regional facilities company and runs maintenance, vendors and the field team."),
            ("p", "Anita Fournier, Director of Leasing."),
            ("h2", "By the numbers"),
            ("ul", ["48 buildings under management", "1,140 apartments", "Average tenant stay: 3.1 years", "Field team of 9 maintenance technicians", "Owner retention: 94 percent since 2019"]),
            ("h2", "Our standard"),
            ("p", "Every building we manage should look cared for from the sidewalk to the top floor. Common areas are the first thing a tenant sees and the first thing an owner asks about. We are investing in that standard in 2026 and 2027."),
            ("small", "Lakeshore Property Partners, 210 Fore Street, Suite 4, Portland, ME 04101. (207) 555-0148. info@lakeshorepartners.example"),
        ],
    },
    {
        "filename": "Press release - Lakeshore acquires 12 buildings in South Portland.pdf",
        "url": "https://lakeshorepartners.example/news/south-portland-acquisition",
        "saved": "Saved Sep 29, 2026, 8:17 AM",
        "title": "Lakeshore Property Partners adds 12 South Portland buildings",
        "blocks": [
            ("small", "FOR IMMEDIATE RELEASE - September 9, 2026"),
            ("h1", "Lakeshore Property Partners takes over management of 12 South Portland buildings"),
            ("p", "PORTLAND, Maine - Lakeshore Property Partners announced today that it has been selected to manage a portfolio of 12 residential buildings in South Portland, bringing its total to 60 buildings and approximately 1,420 apartments across Greater Portland. The buildings, previously managed by the owner directly, include 280 apartments along Ocean Street, Broadway and Cottage Road."),
            ("p", "\"These are good buildings that have not had consistent attention,\" said Meredith Choate, Founder and Chief Executive of Lakeshore. \"Our first ninety days are about the basics: the hallways, the entries, the laundry rooms, the grounds. Tenants notice that before anything else.\""),
            ("p", "Tobias Renner, Director of Operations, said the company is consolidating its vendor relationships as it grows. \"We are moving from a building-by-building approach to portfolio contracts for cleaning, grounds and snow, with reporting that an owner can read in five minutes. We expect to have those contracts in place for the fourth quarter.\""),
            ("p", "Lakeshore will add two maintenance technicians and a facilities coordinator to support the new buildings. Management transitions on October 1, 2026."),
            ("p", "About Lakeshore Property Partners: Founded in 2011, Lakeshore manages residential buildings for private owners and investment groups in Greater Portland, Maine. lakeshorepartners.example"),
            ("small", "Media contact: Anita Fournier, afournier@lakeshorepartners.example, (207) 555-0148"),
        ],
    },
    {
        "filename": "Job posting - Facilities Coordinator - Lakeshore Property Partners.pdf",
        "url": "https://lakeshorepartners.example/careers/facilities-coordinator",
        "saved": "Saved Sep 29, 2026, 8:21 AM",
        "title": "Facilities Coordinator - Lakeshore Property Partners",
        "blocks": [
            ("h1", "Facilities Coordinator"),
            ("small", "Portland, ME - Full time - Posted August 28, 2026 - Reports to the Director of Operations"),
            ("h2", "About the role"),
            ("p", "Lakeshore is growing from 48 to 60 buildings this fall and we are moving our cleaning, grounds and snow vendors onto portfolio-wide contracts. The Facilities Coordinator is the person who makes those contracts work day to day: scheduling, inspections, vendor scorecards and the monthly report our owners read."),
            ("h2", "What you will do"),
            ("ul", [
                "Own the vendor calendar for cleaning, grounds and snow across all buildings",
                "Walk 15 to 20 buildings a week and log common-area condition with photos",
                "Build and maintain a vendor scorecard: on-time arrival, missed visits, tenant complaints, resolution time",
                "Produce the monthly owner report on common-area condition and vendor performance",
                "Track tenant maintenance requests from intake to close and report response times weekly",
                "Hold vendors to the service levels in their contracts and escalate when they miss",
            ]),
            ("h2", "What we are looking for"),
            ("ul", [
                "Two or more years in property management, facilities or field operations",
                "Comfortable with spreadsheets; you will be building the first version of our reporting",
                "A driver's license and a willingness to be in buildings, not at a desk",
                "Someone who notices a burned-out hallway bulb and does something about it",
            ]),
            ("h2", "Why now"),
            ("p", "Our tenants have told us, clearly, that maintenance response and common-area cleanliness are where we need to improve. This role exists to fix that."),
            ("p", "Salary $58,000 to $66,000 plus benefits. To apply, email careers@lakeshorepartners.example with a short note about a time you held a vendor accountable."),
        ],
    },
    {
        "filename": "Tenant reviews - Lakeshore Property Partners - RentVoice.pdf",
        "url": "https://rentvoice.example/management/lakeshore-property-partners-portland-me",
        "saved": "Saved Sep 29, 2026, 8:26 AM",
        "title": "Lakeshore Property Partners reviews - RentVoice",
        "blocks": [
            ("h1", "Lakeshore Property Partners"),
            ("small", "Property management - Portland, ME - 2.4 out of 5 (87 reviews)"),
            ("h2", "Recent reviews"),
            ("review", ("2 stars", "Sept 12, 2026", "West End", "Put in a request for the hallway light on the 2nd floor on Aug 3. Fixed Aug 29. The hallway carpet has not been vacuumed in weeks. Rent is on time every month, I would like the same from them.")),
            ("review", ("1 star", "Aug 30, 2026", "Bayside", "Laundry room has been dirty for a month. Lint everywhere, trash overflowing. I emailed twice. The leasing office is nice but nothing happens after the email.")),
            ("review", ("4 stars", "Aug 22, 2026", "Scarborough", "Apartment itself is great and the leasing team was easy to work with. Taking a star off for the entryway, which is always muddy and nobody seems to clean it.")),
            ("review", ("2 stars", "Aug 14, 2026", "Westbrook", "Maintenance takes forever. Three weeks for a dripping faucet. Common areas are hit or miss depending on which cleaning company is doing it that month, there have been at least three.")),
            ("review", ("3 stars", "Jul 31, 2026", "Munjoy Hill", "Rent is fair for the area. The building could be cleaner. Stairwell smelled like trash for most of July.")),
            ("review", ("1 star", "Jul 19, 2026", "Bayside", "Submitted a maintenance request for the front door lock on July 2. Still broken. Anyone can walk in.")),
            ("review", ("5 stars", "Jul 6, 2026", "Deering", "New management took over our building in the spring and it is noticeably better. Hallways painted, new mats, cleaned weekly. Hope it lasts.")),
            ("review", ("2 stars", "Jun 28, 2026", "West End", "They are responsive when you call Anita directly. Through the portal, nothing. Common area cleaning seems to have stopped entirely in June.")),
            ("h2", "Summary of 87 reviews"),
            ("ul", ["Most mentioned, negative: maintenance response time (41 reviews), common-area cleanliness (33 reviews)", "Most mentioned, positive: leasing staff (29 reviews), rent fairness (18 reviews)"]),
        ],
    },
    {
        "filename": "News - City fines Lakeshore building over common-area violations - Casco Bay Ledger.pdf",
        "url": "https://cascobayledger.example/2026/09/16/south-portland-code-violation-ocean-street",
        "saved": "Saved Sep 29, 2026, 8:31 AM",
        "title": "South Portland fines property manager $4,500 over common-area violations - Casco Bay Ledger",
        "blocks": [
            ("small", "Casco Bay Ledger - Local - September 16, 2026"),
            ("h1", "South Portland fines property manager $4,500 over common-area violations at Ocean Street building"),
            ("p", "SOUTH PORTLAND - The city's code enforcement office has fined Lakeshore Property Partners $4,500 for violations at a 24-unit apartment building on Ocean Street, following tenant complaints about the condition of the building's common areas."),
            ("p", "According to the notice of violation dated September 11, inspectors found accumulated trash in the rear stairwell, a non-functioning hallway light on two floors, and a laundry room that \"had not been cleaned in a manner consistent with the city's property maintenance ordinance.\" The building is one of 12 that Lakeshore took over management of this month; the violations were cited after the transition date."),
            ("p", "Tobias Renner, Lakeshore's Director of Operations, said in a statement that the company inherited the conditions and has already addressed the lighting. \"We took on these buildings because they needed attention, and we are giving it to them. The common areas will be on a weekly cleaning schedule with a contracted vendor by the end of October.\""),
            ("p", "A tenant who asked not to be named said the stairwell had been in that condition \"since at least July,\" before Lakeshore's involvement."),
            ("p", "The fine is due within 30 days. A follow-up inspection is scheduled for October 14."),
            ("small", "Reporting by the Casco Bay Ledger local desk. This is a fictional news item created for a training exercise."),
        ],
    },
    {
        "filename": "Pricing - ProClean Maine.pdf",
        "url": "https://procleanmaine.example/pricing",
        "saved": "Saved Sep 29, 2026, 8:36 AM",
        "title": "Pricing - ProClean Maine",
        "blocks": [
            ("h1", "Simple per-unit pricing for multifamily common areas"),
            ("p", "ProClean Maine cleans common areas for apartment buildings and condominium associations from Kittery to Augusta. One price per unit per month, no surprises."),
            ("h2", "Plans"),
            ("table", [
                ["Plan", "Visits", "Price per unit per month", "Minimum per building"],
                ["Essential", "Weekly", "$38", "$900"],
                ["Standard", "Twice weekly", "$52", "$1,200"],
                ["Premium", "3x weekly + monthly deep clean", "$71", "$1,600"],
            ]),
            ("h2", "What is included"),
            ("ul", ["Entries, hallways, stairwells, laundry rooms, elevators, mailroom", "Trash room sweep and sanitize", "Exterior entry sweep", "Photo log after every visit, emailed to the manager", "Quarterly condition report"]),
            ("h2", "Portfolio discounts"),
            ("ul", ["10 to 24 buildings: 5 percent", "25 or more buildings: 10 percent", "Snow and grounds available through our partner network"]),
            ("p", "Pricing shown is for buildings of 6 to 100 units within 20 miles of Portland. Request a quote for larger buildings or other areas."),
            ("small", "ProClean Maine - (207) 555-0191 - quotes@procleanmaine.example - Fully insured - Serving Maine since 2015"),
        ],
    },
]

CALL_NOTES = """Lakeshore Property Partners - first call - Wed Sep 16 2026, 2:00 pm
Jordan on the whole call, Dana for the last 15 min
Them: Tobias Renner (Dir of Ops), Anita Fournier joined late (Leasing)

What they said
- 48 buildings now, 60 on Oct 1 with the South Portland ones. about 1,400 units after that
- fired their cleaning vendor in June. "building by building, nobody owned it". three different companies in the last 18 months
- common area complaints are the #1 tenant issue after maintenance speed. Anita said owners are asking about it
- they want ONE vendor for common areas across the portfolio, weekly minimum, some buildings twice weekly
- want reporting: on-time, missed visits, photos, a monthly summary the owners can read. Tobias is hiring a coordinator to run a vendor scorecard
- budget: Tobias said "around $110K a year" for cleaning. said it twice
- decision by end of October. wants proposals by Sep 30
- three vendors in the running plus us: ProClean Maine (per unit pricing, he has their sheet), Bay State Facility Group (big regional, "corporate"), Coastal Commercial Clean (local, "cheap, we used them in 2024, didn't last")
- asked twice if we've done 48 buildings. Jordan: Eastern Prom is 11 buildings / 340 units, 2.5 years. He wrote it down
- Tobias: "the owners don't care about cleaning until they get a fine or a one star"

Our side
- Dana: do not go below $6,200/mo. that's the floor Elena gave us, below that we lose money on the drive time alone. DO NOT say this number on the call
- our ask: $8,500/mo weekly common areas all 60 buildings, photo log every visit, monthly report. that's ~$102K/yr, under their $110K
- Jordan thinks ProClean comes in around $5,500 to $7,500/mo on their sheet depending on the plan
- Dana wants to lead with the reporting and the Eastern Prom reference, not price
- next call: Thu Sep 24. Tobias said Meredith (CEO) may join

To do
- Jordan: send Eastern Prom reference (ask Gretchen first)
- Elena: confirm the floor
- Dana: proposal draft by Sep 28
"""


def prospect_email():
    return {
        "filename": "Re_ follow up - Lakeshore.pdf",
        "subject": "Re: follow up - Lakeshore",
        "messages": [
            (
                JORDAN[0], JORDAN[1],
                "To: Tobias Renner <trenner@lakeshorepartners.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                "Fri, Sep 25, 2026 at 9:10 AM",
                "Hi Tobias,\n\nThanks for yesterday. Confirming what we heard: weekly common areas across all 60 buildings from November 1, a photo log after every visit, and a monthly report in a form the owners can read. Proposal to you by the 30th.\n\nOne question: is the $110,000 figure for cleaning only, or does it include grounds and snow?\n\nJordan Lee\nNorthwind Home Services",
            ),
            (
                "Tobias Renner", "trenner@lakeshorepartners.example",
                "To: Jordan Lee <jordan@northwindhome.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                "Thu, Oct 1, 2026 at 4:47 PM",
                "Jordan,\n\nCleaning only. But I need to be straight with you after the South Portland closing and the fine down there: the number I can defend to the owners this year is closer to $80,000, not $110,000. We would revisit at the one-year mark if the reporting does what you say it will.\n\nIf that changes your proposal, send the version that works at that number. We are still deciding by the end of the month.\n\nTobias",
            ),
            (
                JORDAN[0], JORDAN[1],
                "To: Tobias Renner <trenner@lakeshorepartners.example>\nCc: Dana Whitfield <dana@northwindhome.example>",
                "Fri, Oct 2, 2026 at 8:02 AM",
                "Understood, thank you for telling us. We'll come back to you with options early next week.\n\nJordan",
            ),
        ],
    }
