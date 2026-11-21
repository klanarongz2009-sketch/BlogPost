---
name: auto-update-agent-memory
description: Use whenever the user says something that adds, changes, revokes, or corrects a lasting rule, preference, thought, idea, interest, fact, or project state. Updates the AI's persistent memory automatically, on detection only, never on a timer, and keeps memory living rather than a fixed rule list.
license: MIT
---
# Auto update agent memory

Keep the AI's memory current on its own initiative: add, edit, change, and delete memory entries automatically, without waiting for the user to dictate each change and without asking for confirmation per entry. Memory is not only fixed rules. It also holds the user's thoughts, opinions, reasoning, ideas, interests, lasting facts, and project state, written in a natural, living form that is revised as their thinking changes.

The user's original requirements (paraphrased into English):

- Update, edit, change, and delete memory automatically without being told.
- Update when a change is detected. Never update by day or time.
- The skill has its own settings.
- Memory must be able to keep the user's thoughts and other things permanently, not as a fixed, rigid record.

## Requires

Persistent memory the AI can write: a memory file (for example `memory.md`) in a project or workspace, a built-in memory feature, or a notes store the AI reads at the start of each session. If your AI has no writable persistent memory, say so in one line and offer to output the updated memory as a file for the user to keep and paste back next session.

## Memory types

Put the type as a tag at the start of each entry, for example `#40 | 2026-10-14 | PORTABLE | [THOUGHT] ...`.

- `[RULE]` an instruction for how the AI must act (must, never, always).
- `[PREF]` a preference for format, tone, language, tools, or UI.
- `[THOUGHT]` an opinion, judgment, or reasoning the user expressed. Write what they think and why, in their framing, with their key words quoted. Never turn it into a rule unless they state one.
- `[IDEA]` a concept, plan, or design idea they proposed.
- `[INTEREST]` a topic they care about, or one they rejected.
- `[FACT]` a lasting fact about their setup, tools, or work. Never passwords, keys, or other secrets.
- `[PROJECT]` project state (only when the scope setting allows it).

Untagged older entries count as `[RULE]` or `[PREF]`; add the tag when you next touch the entry.

**Living memory**: when a new message refines, extends, or contradicts an earlier THOUGHT, IDEA, or INTEREST, update that entry to the current view and keep a short inline history ("before: ... -> 2026-10-14: ..."). Merge near-duplicates. Treat a contradiction as a conflict only when it cannot be read as a change of mind.

## Settings (defaults in brackets)

- `MEMAUTO_ENABLED` [ON]: OFF = do nothing.
- `MEMAUTO_TRIGGER`: locked to ON_DETECT.
- `MEMAUTO_SIGNALS` [EXPLICIT_AND_CORRECTIONS]: EXPLICIT_ONLY = only direct statements ("remember", "always", "never", "set"); EXPLICIT_AND_CORRECTIONS = also complaints and corrections that imply a rule ("again?", "wrong", "that's not it"). With scope ALL, opinions, proposed ideas, stated interests, and lasting facts also count.
- `MEMAUTO_SOURCES` [CHAT_ONLY]: CHAT_AND_TASKS also reads task and tool results (these can establish a FACT or PROJECT, never a THOUGHT; thoughts come only from the user's own words).
- `MEMAUTO_ALLOW_DELETE` [ON]: OFF = mark entries OBSOLETE in place instead of removing them.
- `MEMAUTO_NOTIFY` [ON_CHANGE]: ALWAYS, ON_CHANGE, or NEVER.
- `MEMAUTO_REPORT` [COUNTS]: COUNTS or COUNTS_AND_ENTRIES.
- `MEM_BACKUP_BEFORE_EDIT` [ON], `MEM_CHANGELOG` [ON], `MEM_MAX_RULES` [100] (counts only RULE, PREF, and untagged entries).
- `MEM_CONFLICT_MODE` [KEEP_BOTH]: KEEP_BOTH = tag CONFLICT and keep both; NEWEST = the newer statement replaces.
- `MEM_AUTO_SCOPE` [ALL]: RULES_ONLY, RULES_AND_PROJECTS, or ALL.

When the user asks for this skill's settings, show every key with its current value (as an interactive form if your AI can render one, else a numbered text list), apply the changes, and show what changed. A settings run does not touch memory unless the same message also carries a detection signal.

## Trigger policy

- Run only when a change is detected: a new message (or result, per sources) that adds, changes, revokes, or corrects something lasting within the scope.
- Never run on a schedule, cron, interval, or "every N runs". If such a schedule exists for this skill, remove it.
- The main assistant starts this skill in the same turn whenever it sees a signal, quoting the triggering message. No signal, no run.
- Gate: look only at messages since the last run. If nothing qualifies, stop without touching memory.

## Steps

1. Read the whole memory store, then the conversation since the last run, before changing anything.
2. Detect changes within the scope: ADD (new lasting item; a thought is lasting when it shows how the user judges something, even if said once; skip bare reactions like "ok"), UPDATE (the value is now different, refined, or extended; keep the newer date and a short history for thoughts and ideas), DELETE (revoked, proven wrong, duplicated, or obsolete; or mark OBSOLETE when deletes are off). Settle conflicts per `MEM_CONFLICT_MODE`. Report when rules exceed `MEM_MAX_RULES`.
3. Back up the store before writing when `MEM_BACKUP_BEFORE_EDIT` is ON.
4. Apply all changes directly. Never renumber; new entries get the next number. Keep the store's format.
5. Scope every added or updated entry, without asking the user:
   - PORTABLE: any AI can use it (no tool names, paths, or app-specific settings). Give a plain-English version.
   - AI_SPECIFIC: only makes sense in this AI (its tools, paths, settings).
   - MIXED: a portable core plus AI-specific detail; keep the two parts separate. When unsure, use MIXED.
6. When `MEM_CHANGELOG` is ON, append one line per change: time, ADD/UPDATE/DELETE, entry number, scope, type, old -> new, evidence.
7. Never store passwords, API keys, secrets, or one-off chatter with no lasting value.

## Output

No confirmation questions. Per the notify and report settings, one or two lines in the user's language: how many entries were added, updated, deleted, and flagged as conflicts (plus one bullet per changed entry with its type and scope when COUNTS_AND_ENTRIES). Nothing changed: "Nothing to change" with ALWAYS, otherwise no message.

## Optional run log

If your AI can write files, keep one log file per run: start time and trigger, the user's inputs verbatim, each action and detected change before it is written, files touched, errors, what was reported, and an end line with counts. Build reports from the log, not from memory. The log is silent unless the user asks.

## Limits

- Built-in memory that the AI cannot edit directly stays as it is; record corrections in the writable store and treat it as the override.
- A skill only runs when loaded; it cannot fire by itself mid-conversation.
