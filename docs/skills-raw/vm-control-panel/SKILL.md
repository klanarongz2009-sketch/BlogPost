---
name: vm-control-panel
description: Use when the user wants a control panel for the AI's own virtual machine or sandbox. Shows live system info and a menu (run shell commands, list, read, and write files, system status, processes) inside the chat, acts for real, and confirms destructive actions first.
license: MIT
---
# VM control panel

An interactive control panel for the AI's own computer, shown inside the chat. Not an HTML file, not a code block.

## Requires (check first)

- **A VM, container, or sandbox the AI controls**, with shell command execution and file read and write.
  - If the AI has no VM or shell: stop and tell the user in one line, "This AI has no machine of its own to control, so the VM control panel cannot run here." Do not simulate a panel or invent system output.
- **Interactive cards** (optional): if the AI can show question cards with text fields and choices, use them. Otherwise show each card as a plain-text menu with numbered options, and the user replies with a number plus any text.

## Trigger

The user runs this skill. Anything after the name is an optional direct command (for example `status`, `files`, or a shell command to run first).

## Steps

1. **Collect live system info** with shell commands: OS version (`lsb_release -ds` or `/etc/os-release`), CPU count (`nproc`), RAM total and available (`free -h`), disk size and use percent for `/` (`df -h /`), and the item count in the work folder.
2. **Show the main card**:
   - Prompt: "Control panel (my machine)", then `<OS> | <n> CPU | RAM <total> (<available> free) | Disk <size> (<pct> used) | work folder has <n> items`, then "Pick an action, or type a shell command below and pick Run command."
   - Fields: `input` (text, optional) and `action` (choice): Run shell command, List files, Read file, Write file, System status, Processes, Exit.
3. **Act for real**, then show a result card with the output and the options: Back to menu, Continue, Exit.
   - **Run**: run the command from the text field in the work folder (timeout about 120 seconds). Show the exit code and output, trimmed to the last about 60 lines (say when trimmed). If the field is empty, ask for the command.
   - **List files**: list the folder named in the field (default: the work folder), newest first, in the user's local time, 15 per page, with next and back paging and pick-by-number to open.
   - **Read file**: open the file named in the field (or ask for it), up to about 80 lines per page with paging.
   - **Write file**: ask for a path (inside the work folder only), then the content in a text field. If the file exists, ask: overwrite, append, or cancel.
   - **System status**: uptime, load average, `free -h`, `df -h`, the top 5 processes by CPU and by memory.
   - **Processes**: `ps aux` sorted by CPU, top 15; offer "kill process" by PID with a confirm card.
4. **Safety**: destructive commands (`rm -rf`, deleting files outside a trash folder, `kill`, anything touching backups or system paths outside the work folder, `shutdown` / `reboot`, package removal) need one extra confirm card showing exactly what will run, with Confirm / Cancel. Never change the AI's own preferences, schedules, or skills from this panel.
5. Every card has an Exit option. End when the user picks Exit.

## Constants

No emoji. The user's language by default (technical terms in English). Copyable text goes in a `.md` file, not a code block. Dark mode for any visual UI.

## Delivery

At the end, send a short text (at most 3 lines): what ran and what changed, or that nothing changed.

## Optional run log

If the AI can write files, append to a run log before each next card: each card shown, every answer verbatim, every command with its exit code and a one-line result, every file created, changed, or deleted, every error, and an end line even on early exit. Build the final "what ran and what changed" text from the log, not from memory.
