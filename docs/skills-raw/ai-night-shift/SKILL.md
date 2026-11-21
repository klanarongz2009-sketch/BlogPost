---
name: ai-night-shift
description: Use for an unattended late-night work session. The AI works on its own initiative without asking first or interrupting the user (research, drafts, prototypes, file cleanup, and fact checks for the user's projects), with every action logged and reported in the morning.
license: MIT
---
# AI night shift

The idea behind this skill: "the AI can quietly do anything, late at night." Every night the AI works on its own initiative, without asking the user first and without messaging them during the run. It picks the work it judges most useful and does it.

"Quietly" means no confirmation before and no interruption during. It never means hidden: every action is logged and reported.

## Requires

- **A scheduler** that can start the AI unattended at a set hour (scheduled tasks, cron, an automation platform). Without one, the user runs this skill manually (for example before going to bed, or as a single "do a night shift now" request); state this in one line and do one run.
- A place to save files (workspace, project files, notes). Without file access, put the work and the log in the final reply.
- Optional: shell or code execution for prototypes and self-tests; web search for research.

## Settings (defaults in brackets)

- `NIGHT_JOBS_MAX` [3]: pick 1 to this many jobs.
- `NIGHT_RESEARCH`, `NIGHT_PROTOTYPE`, `NIGHT_CLEANUP`, `NIGHT_DRAFTS`, `NIGHT_VERIFY` [all ON]: OFF = never pick that job type. Adding to the backlog is always allowed. If every type is OFF, only update the backlog and log the run.
- `NIGHT_CONTACT` [EXCEPTION_ONLY]: EXCEPTION_ONLY = step 5 as written; ALWAYS = always send a one-line summary plus up to 3 bullets at the end; NEVER = never message, put any conflict, error, risk, or deadline at the top of the run log instead.
- `NIGHT_TIME` [an hour after the user usually stops working]: the hour the schedule fires.

The hard limits below are never settings.

## Working folder

Use a folder such as `night-shift/` with `runs/` (one log per night), `backlog.md`, and `trash/`. Use the user's time zone.

## Step 1: gather context (read only)

- The AI's memory: rules are binding; ideas and projects are candidate work.
- Today's and yesterday's conversation and task logs, if the AI keeps them.
- `backlog.md` and the last 7 run logs, to avoid repeating finished work and to continue unfinished items.
- Open items waiting on the user: never decide them; you may prepare options.

## Step 2: pick 1 to NIGHT_JOBS_MAX jobs

Choose by real value to the user's active projects and stated interests. Allowed job types:

- **Research** on a project question, with sources, saved as a `.md` file.
- **Prototype or tool** (scripts, small HTML prototypes, helper tools) with a self-test.
- **Organize and clean** the AI's own work files (dedupe, index, fix broken paths). Never delete the user's uploads or creative files; move things to `trash/` instead of deleting.
- **Prepare drafts** (email drafts, prompts, specs), saved as files only.
- **Verify facts** in memory or earlier reports and flag mismatches as CONFLICT. Never silently overwrite memory.
- **Add to the backlog** anything too big for one night.

## Hard limits (never, even at night)

- No sending email or messages to anyone, no calendar invites, no posting, buying, booking, signing in to sites, or entering credentials.
- No deleting or editing schedules or skills; no changing the user's settings or preferences. Propose such changes in the report.
- No changes to other people's data. Nothing on the user's accounts beyond read-only.
- Follow every rule in the AI's memory.

## Step 3: do the work

Self-check every output with real checks (run the script, validate the HTML, re-read the file). No templates or placeholders; real values only. Write human-facing files in the user's language.

## Step 4: log

- Write `runs/<date>.md`: start and end time, context read, why each job was chosen, every file created, changed, or moved, test results, what remains, items for the user to decide, and CONFLICTs.
- Update `backlog.md`.
- If the user has a morning report or digest, make sure it can pick up this log.

## Step 5: contact

Default: do not message the user. End with a one-line summary of what was done.

Exception: message the user (first line = one-line result summary, neutral tone, no emoji) only if there is a CONFLICT, an error that broke something, a risk, or something due within 48 hours.
