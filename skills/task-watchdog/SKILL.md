---
name: task-watchdog
description: Use on a schedule (for example every two hours) to watch an agent's background tasks. Flags tasks that run too long, look stuck, or approach their budget, and checks finished tasks' claims against the real files. Reports only when something needs attention.
---
# Task watchdog

When many agent tasks run in the background, some stall and some report success that did not happen. The watchdog catches both, and stays quiet otherwise.

## Inputs

- How to list tasks and their status in your agent platform.
- Thresholds (defaults): `MAX_RUNTIME = 2h`, `NO_PROGRESS = 45m`, `BUDGET_WARN = 80%`.
- A state file to remember what was already flagged, for example `watchdog/state.json`.

## Each run

1. **List running tasks.** For each, read start time, last activity, and budget used if available.
   - runtime over `MAX_RUNTIME` -> `LONG`;
   - no activity for `NO_PROGRESS` -> `STUCK`;
   - budget over `BUDGET_WARN` -> `BUDGET`;
   - waiting on the user (an approval, a login) -> `WAITING`, with what it waits for.
2. **Check tasks finished since the last run.** For each claim in the result ("file written", "pushed", "sent", "tests passed"), verify one concrete piece of evidence: the file exists and is not empty, the commit is on the remote, the message is in Sent, the test log shows the numbers. Mismatch -> `CLAIM_MISMATCH`.
3. **Spot duplicates**: two tasks doing the same job (for example two copies of one routine). Flag `DUPLICATE` and suggest which one to keep (the one with the most recent good report).
4. **Compare with the state file.** Report only new flags or flags whose state changed. Clear flags that are resolved.
5. **Save the state file** and append one line to a log.

## Report (only when there is a new flag)

One line per flag: task name, flag, the evidence (times, numbers), and the suggested action. If nothing is new, send nothing.

## Rules

- Read-only: the watchdog never cancels, resumes, or edits tasks itself. It suggests.
- A failed status lookup is `UNKNOWN`, not "fine".
- Keep the report short enough to read on a phone notification.
