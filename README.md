# Built Young Skills

Agent skills for teen entrepreneurship education, built and used by [Built Young](https://builtyoung.org).

A skill is a folder of instructions and reference material that an AI assistant loads when it's relevant. These package knowledge that's expensive to reassemble — competition rubrics, real precedent, the specific questions that unstick a teenager staring at a blank page.

## Skills

### `challenge_startup_coach`

Coaches a student from a blank page to a competition-ready venture.

Built on every finalist project from the 2026 Diamond Challenge (83 teams) and Conrad Challenge (33), all 22 Blue Ocean 2026 winners, and the 14 Conrad 2025 award winners — **152 teams, 62 of which won something** — plus the published judging rubrics of four competitions.

It handles three jobs:

- **Finding an idea** — three extraction methods that start from something the student already has, rather than open brainstorming. Plus 152 discussion prompts, each tied to a specific project.
- **Evaluating an idea** — scores against six patterns derived from what actually separated finalists from everyone else, with named comparables so a critique lands concretely.
- **Matching to a competition** — the four tracks reward genuinely different things. Includes full rules, deadlines, team limits, and the rules that cause forfeits.

Ships with `backplan.py`, which walks backwards from a deadline to a working schedule and flags the January collision that catches Ontario students every year.

```
challenge_startup_coach/
├── SKILL.md                        the routing logic and core method
├── references/
│   ├── finalist-library.md         152 projects by theme, with proof metrics
│   ├── winning-patterns.md         six patterns + the evidence behind each
│   ├── competitions.md             rules, rubrics, deadlines, disqualifiers
│   └── idea-finding.md             three methods + 152 discussion prompts
├── scripts/
│   └── backplan.py                 deadline → working schedule
└── evals/
    └── evals.json                  test cases
```

## Using a skill

**Claude Code** — clone into your skills directory:

```bash
git clone https://github.com/YOUR-ORG/builtyoung-skills.git
cp -r builtyoung-skills/challenge_startup_coach ~/.claude/skills/
```

**Claude.ai / Claude Desktop** — package it and upload:

```bash
cd builtyoung-skills
zip -r challenge_startup_coach.skill challenge_startup_coach/
```

**Any assistant** — the reference files are plain Markdown and readable on their own. `finalist-library.md` works as a standalone lookup; `idea-finding.md` works as a workshop guide with no AI involved at all.

## On the data

Compiled from official sources in September 2026:

- [Diamond Challenge finalists](https://diamondchallenge.org/finalists/) and [competition rules](https://diamondchallenge.org/competition/)
- [Conrad Challenge 2026 finalists](https://conrad.spacecenter.org/2026-innovation-summit-finalists/) and [2025 winners](https://conrad.spacecenter.org/2025-winners/)
- [Blue Ocean 2025–26 winners](https://blueoceancompetition.org/2025-2026-winners/)
- [DECA competitive events](https://www.deca.org/compete) and the DECA Guide

**Deadlines shift every cycle.** The dates here are for 2026–27 and are marked as such throughout, but verify against the official site before a student plans around one.

Two known limits, flagged in the skill itself so nobody mistakes absence for completeness:

- **DECA publishes no winning projects** — it protects students' intellectual property, and many take their judged plans to real investors. The rubric is the only available map.
- **Conrad's 2025 record is winners only** — there's no public archive of finalists who didn't place.

## Contributing

Corrections to competition rules and deadlines are especially welcome — these change annually and a stale date is worse than no date. Open an issue or a PR.

If you add a finalist project, include the source. The skill's value depends on every claim being traceable, and an invented metric would undermine the whole thing.

## License

MIT. See [LICENSE](LICENSE).

The competition data is factual information compiled from public sources; the descriptions and discussion prompts are original writing.
