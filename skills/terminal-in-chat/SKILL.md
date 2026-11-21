---
name: terminal-in-chat
description: Use when the user wants a terminal inside the chat. The user types or pastes shell commands, or describes what to do in plain language, and the AI runs them for real on its own machine and shows the output, in a REPL loop with history and a safety confirm for destructive commands.
license: MIT
---
# Terminal in chat

The user's request (paraphrased into English): "I type a command or paste commands, and the AI runs them in a terminal as instructed." Not an HTML file, not a code block: a working terminal loop inside the chat.

## Requires (check first)

- **A real terminal**: the AI must be able to run shell commands on a machine or sandbox (a code-execution tool, a VM, a container, a local agent with shell access).
  - If it cannot: stop and tell the user in one line, "This AI has no terminal, so it cannot run commands. Use an AI with shell or code execution, or run the commands yourself." Do not pretend to run commands or invent output.
- **Interactive cards** (optional): if the AI can show question cards with text fields and buttons, use them. Otherwise run the same loop as plain text: the user sends a command as a message, and the AI replies with the output block described below.

## Trigger

The user runs this skill. Anything typed after the skill name is the first command: run it before showing the first card.

## State (keep across turns in this run)

- **CWD**: starts at the user's work folder (or the home folder). After every run, update it from the shell's final working directory so `cd` persists between turns.
- **HISTORY**: record each run as `time  command  exit-code`.

## Card (one per turn, REPL loop)

- Prompt text: `Terminal | <OS> | user: <whoami> | cwd: <CWD>`, then after a run: `$ <command that ran>`, `exit <code>`, and the output (last about 40 lines; when trimmed, say "trimmed to the last 40 of N lines"). Then the instruction: type a shell command, paste several lines, or describe what you want in plain language, then pick Run.
- Fields: `cmd` (text, optional) and `action` (choices): Run, History, Exit.

## What each choice does (for real)

- **Run**:
  1. If `cmd` is empty, show the same card again with "No command typed yet".
  2. Decide the input type. Looks like shell (starts with a command name, contains shell syntax, or is pasted multi-line commands): run exactly as typed, no edits. A plain-language instruction (for example: print "hello world"): translate it to the shortest correct shell command(s) (`echo "hello world"`), run it, and show the translated command on the `$` line so the user sees what ran. Read obvious typos generously.
  3. Run with `bash -c` in CWD, stdout and stderr together, a timeout of about 120 seconds (longer for commands known to be long, such as installs). Then save the final working directory as the new CWD.
  4. Show the next card with the command, exit code, and output. Empty output: "(no output)". Timeout: say it timed out.
- **History**: show the last 20 history lines (time, command, exit code), with the same fields. A number typed in `cmd` plus Run re-runs that history item.
- **Exit**: end the run.

## Safety

Show one extra confirm card (Confirm / Cancel) with exactly what will run, before:

- `rm -rf` or deleting anything outside a trash folder; `kill` / `pkill`; `shutdown` / `reboot`; package removal; recursive `chmod` / `chown` on wide paths; writing to system paths outside the work folder and `/tmp`; anything touching backups; `dd` / `mkfs`; piping a downloaded script into a shell.
- Never change the AI's own preferences, schedules, or skills from this terminal.
- Cancel: back to the terminal card with "Cancelled, nothing ran".

Every card has the Exit option. End when the user picks Exit, or a card is rejected or expires.

## Constants

No emoji. The user's language by default (technical terms in English). Copyable text (prompts, code) goes in a `.md` file, not a code block. Dark mode for any visual UI.

## Delivery

At the end, send a short text (at most 3 lines): how many commands ran, which ones changed files or state (or that nothing changed), and how to reopen the terminal in this AI.

## Optional run log

If the AI can write files, append to a run log before each next card: each card shown, every answer verbatim, the exact command that ran (and the instruction it was translated from), CWD, exit code, one-line result, every file changed, every error. Write an end line even on early exit. Build the final text from the log.
