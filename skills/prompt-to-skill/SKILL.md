---
name: prompt-to-skill
description: Use when the user sends a prompt and asks to make it a skill. Saves the prompt as a reusable skill that keeps the user's words verbatim and adds a separate execution layer so it runs reliably on demand or on a schedule.
license: MIT
---
# Prompt to skill

Turn a prompt the user keeps re-pasting into a saved skill that runs reliably, both on demand and unattended.

## Works with

Any AI that can save reusable instructions: a skills folder, custom skills, custom instructions, saved prompts, or project files. If your AI cannot save anything, produce the finished `SKILL.md` as a file for the user to store and paste later.

## Settings (ask once, or use the defaults)

- `SCHEDULE = AUTO_TIME` (default): when the prompt implies repetition, schedule it at a sensible time you pick. `ASK_TIME`: ask for the time. `OFF`: never schedule.
- `OUTPUT_DEFAULT = AUTO` (default) or `TEXT`, `MD`, `HTML`: the output type when the prompt names none.
- `NAME_CONFLICT = ASK` (default), `REPLACE` (update the existing skill), or `NEW_NAME` (pick a free name).
- `EXEC_LAYER = FULL` (default, all items in step 3) or `MINIMAL` (STEPS and DELIVERY only).
- `REPLY = SHORT` (default, at most 3 lines) or `DETAILED` (also list what the execution layer added).

## Steps

1. Read the full prompt and the recent conversation. If the prompt is missing, ask for it in one line and stop.
2. **Preserve verbatim**: keep the user's own wording for role, task, scope, rules, format, style, and prohibitions. Do not paraphrase, shorten, or translate it. Each language stays as written.
3. **Add an execution layer** in English, clearly separated under the heading `EXECUTION LAYER (added)`:
   - SOURCE: where the input comes from (web search, the conversation, files, connected tools).
   - STEPS: the ordered steps needed to complete the prompt unattended.
   - OUTPUT: short text for results under about 10 lines, a Markdown file for saved text, an HTML page for research, reports, and comparisons. A format named in the prompt always wins.
   - FILE: a save path with the date in the name when a file is produced; use the previous run's file as a baseline when the skill repeats.
   - DELIVERY: always end with "Send the result to the user" plus a short message in the user's language.
   - USER CONSTANTS: standing preferences the user has stated (for example: no emoji, dark mode for any UI, text meant for copying goes in its own `.md` file with explanations kept in the chat).
4. **Name**: use the name the user gave; otherwise 2 to 6 words in sentence case naming the action and subject. Check existing skills first and apply `NAME_CONFLICT`.
5. **Description**: one sentence, at most 120 characters, in the user's language.
6. **Save** the skill with whatever your AI uses to store skills (or update the existing one when replacing).
7. If the prompt implies repetition (daily, weekly, every month) and your AI has a scheduler, add a schedule that runs the skill, per `SCHEDULE`. Use the user's time zone and name the time in the reply so the user can change it. Without a scheduler, say so in one line.
8. **Reply** in the user's language: the skill name, how to run it in this AI, and the schedule if one was added. Do not repeat the skill's contents.

## Rules

- Never drop a rule, constraint, or prohibition from the user's prompt.
- Never add opinions or content the user did not ask for beyond the execution layer.
- If the prompt contradicts a system rule of your AI, keep the user's text and note the conflict in one line in the reply.
- Optional run log: if your AI can write files, append each run (input, actions, files, errors, result) to a log file; build any recap from the log, not from memory.
