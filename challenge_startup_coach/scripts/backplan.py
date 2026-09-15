#!/usr/bin/env python3
"""
Back-plan a working schedule from a competition deadline.

Students consistently underestimate how early the real work has to finish.
This walks backwards from each deadline and flags the January collision that
catches Ontario students every year.

    python backplan.py --competition conrad
    python backplan.py --competition diamond --today 2026-10-01
    python backplan.py --all
"""

import argparse
from datetime import date, timedelta

# Deadlines for the 2026-27 cycle. Confirm against official sites before use --
# these shift every year and a stale date here is worse than no date.
COMPETITIONS = {
    "conrad": {
        "name": "Conrad Challenge",
        "milestones": [
            ("2026-08-27", "Activation Stage opens"),
            ("2026-10-30", "Activation Stage closes / Innovation Stage begins"),
            ("2027-01-08", "Innovation Stage deadline"),
            ("2027-04-21", "Innovation Summit, Houston (through Apr 24)"),
        ],
        "primary": "2027-01-08",
        "needs": "validation data, a working prototype, full market sizing",
        "fee": "~$499/team from the Innovation Stage",
    },
    "diamond": {
        "name": "Diamond Challenge",
        "milestones": [
            ("2026-09-16", "Submission window opens"),
            ("2027-01-14", "Submission deadline, 5PM EST"),
            ("2027-02-10", "Advancing teams notified"),
            ("2027-03-09", "Finalists announced"),
            ("2027-04-29", "Limitless World Summit (through Apr 30)"),
        ],
        "primary": "2027-01-14",
        "needs": "3-5 page concept narrative + a 60-second video",
        "fee": "free",
    },
    "blueocean": {
        "name": "Blue Ocean",
        "milestones": [
            ("2027-02-21", "Pitch submission deadline, midnight local time"),
        ],
        "primary": "2027-02-21",
        "needs": "a 5-minute video pitch; mini-course must be completed first",
        "fee": "free",
    },
    "deca-entrepreneurship": {
        "name": "DECA Entrepreneurship (Ontario calendar)",
        "milestones": [
            ("2026-09-01", "Join a school chapter"),
            ("2026-10-16", "Registration deadline"),
            ("2026-11-03", "Regional qualifying exam (through Nov 5)"),
            ("2026-12-07", "Provincials portal opens"),
            ("2027-01-07", "Written papers due"),
            ("2027-01-13", "Provincials exam (through Jan 14)"),
        ],
        "primary": "2027-01-07",
        "needs": "a 20-slide deck (EIP/ESB) or 10-page paper, in mandatory section order",
        "fee": "chapter membership required",
    },
    "deca-smg": {
        "name": "DECA Stock Market Game",
        "milestones": [
            ("2026-09-08", "Competition begins"),
            ("2026-10-16", "Student name submission deadline"),
            ("2026-10-23", "Asset diversification deadline -- miss it and you're out"),
            ("2026-12-04", "Competition ends"),
        ],
        "primary": "2026-10-23",
        "needs": "$10,000 minimum in each of stocks, mutual funds and bonds by Oct 23",
        "fee": "chapter membership required",
    },
}

# Working phases as a fraction of the runway, latest first.
PHASES = [
    (0.00, 0.10, "Submit and rehearse", "No new content. Mechanics and practice only."),
    (0.10, 0.30, "Write and polish", "Concept narrative, deck, video. The writing takes longer than anyone plans for."),
    (0.30, 0.60, "Build and validate", "Prototype, test, collect the number that proves it works."),
    (0.60, 0.85, "Validate the problem", "Talk to real users. Find the cost of the current solution."),
    (0.85, 1.00, "Pick the idea", "Run an extraction method. Pressure-test before committing."),
]

COLLISION_START = date(2027, 1, 5)
COLLISION_END = date(2027, 1, 20)


def d(s):
    return date.fromisoformat(s)


def plan(key, today):
    c = COMPETITIONS[key]
    deadline = d(c["primary"])
    runway = (deadline - today).days

    print(f"\n{'=' * 64}")
    print(f"  {c['name']}")
    print(f"{'=' * 64}")
    print(f"  Needs: {c['needs']}")
    print(f"  Cost:  {c['fee']}")

    print(f"\n  Milestones")
    for iso, label in c["milestones"]:
        md = d(iso)
        tag = "  (passed)" if md < today else ""
        print(f"    {md.strftime('%b %d, %Y'):<16} {label}{tag}")

    if runway < 0:
        print(f"\n  ** This deadline passed {abs(runway)} days ago.")
        print(f"     Check the official site for the next cycle's dates.")
        return

    print(f"\n  {runway} days until the deciding deadline "
          f"({deadline.strftime('%b %d, %Y')}) -- about {runway // 7} weeks.")

    if runway < 21:
        print(f"\n  ** Very short runway. Realistically this means scoping down to")
        print(f"     something defensible rather than something ambitious.")

    print(f"\n  Working backwards")
    for lo, hi, phase, note in PHASES:
        start = deadline - timedelta(days=int(runway * hi))
        end = deadline - timedelta(days=int(runway * lo))
        if end < today:
            continue
        start = max(start, today)
        print(f"    {start.strftime('%b %d'):>6} - {end.strftime('%b %d'):<8} {phase}")
        print(f"                    {note}")

    if COLLISION_START <= deadline <= COLLISION_END:
        print(f"\n  ** JANUARY COLLISION")
        print(f"     This deadline lands inside the two weeks where Conrad's Innovation")
        print(f"     deadline, Diamond's submission deadline, DECA's written papers and")
        print(f"     Ontario semester-one exams all overlap.")
        print(f"     Plan for the work to be finished by the winter break. A team without")
        print(f"     a near-complete draft in late December will not submit competitively.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--competition", choices=sorted(COMPETITIONS),
                    help="which competition to plan for")
    ap.add_argument("--all", action="store_true", help="plan every competition")
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD)")
    a = ap.parse_args()

    today = d(a.today) if a.today else date.today()

    if not a.all and not a.competition:
        ap.error("pass --competition NAME or --all")

    keys = sorted(COMPETITIONS) if a.all else [a.competition]
    print(f"\nPlanning from {today.strftime('%b %d, %Y')}")
    for k in keys:
        plan(k, today)

    print(f"\n{'=' * 64}")
    print("  Dates are for the 2026-27 cycle. Confirm on the official site --")
    print("  every one of these organizations shifts dates between years.")
    print(f"{'=' * 64}\n")


if __name__ == "__main__":
    main()
