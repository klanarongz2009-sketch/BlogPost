---
name: agent-settings
description: Use when the user wants to view or change how their AI assistant behaves. The user types any settings change in plain language (several in one message, typos allowed); the AI maps it to a settings file and applies it, including advanced and power-user settings, storage cleanup on detection, and factory reset.
license: MIT
---
# Agent settings

A settings layer for whatever AI assistant or agent runs this skill. It started as the settings panel for one assistant and is written here for any AI with equivalent features.

The user's original requests (paraphrased into English):

- Settings for the agent side of the assistant, saved as a skill.
- Menus the assistant's own settings page does not have (for example adding memory, hidden or advanced settings).
- Technical settings a non-technical person could not do.
- A "reset all settings" (factory reset), even if it takes a long time.
- Storage control (clear caches, deletion suggestions, keep the disk from filling), browser settings, role-swap settings, and a very large set of fine-grained settings so the user can control the agent freely.
- An "Auto next steps" switch: exactly one next step the AI itself can do, never a list, and none when the work is finished unless necessary.
- A setting for how reasoning is shown: short, detailed (default), or off, written in the chat as talking to the user.
- More notification settings and an "export user profile" for any AI: one generic export with no AI names, no destination presets, and no size budget.
- Change from picking settings one by one to typing anything and applying it automatically, and run automatically when something is detected (for example, unnecessary files detected -> clean storage).

## Requires

- **Persistent storage** for a settings file (for example `agent-settings.json` or `.md` in the AI's workspace or project files), read at the start of each session. Without it, keep the settings in the conversation and offer the file for the user to save and paste back.
- Optional, per feature: file system and shell access (storage cleanup), a scheduler (schedule-related settings), a memory store (memory menu), interactive cards (card fallback mode).

Only offer settings the AI can really honor. Every key needs a real effect or a stated consumer; never pad the catalog with settings that do nothing.

## The settings catalog

Keep one settings file with categories, and for each key: name, current value, allowed values or range, default, a one-line description, and what reads it. Suggested categories:

- **Language and tone**: reply language, technical terms language, tone (neutral, formal, warm), emoji on or off, name tags in replies.
- **Reasoning display** `REASONING_DISPLAY`: SHORT, DETAILED (default), or OFF; shown in the chat as talking to the user.
- **Auto next steps** `AUTO_NEXT_STEPS`: ON or OFF. When ON, after a task the AI does (or offers) exactly one next step that it or another AI can carry out; never a list, never a chore for a human, never in casual or emotional talk, and none when the work is finished unless necessary.
- **Memory**: add, edit, view, or export memory entries (if the AI has memory).
- **Notifications**: what triggers a message to the user (on change only, always, never), quiet hours, digest or immediate.
- **Storage**: warn level (disk percent), backup keep count, trash retention days, cache size threshold, large-file threshold.
- **Auto-detect**: enabled, action (AUTO_CLEAN or SUGGEST_ONLY), notify (ON_CHANGE, ALWAYS, NEVER), recent-file protection window.
- **Browser** (if the AI drives a browser): default start page, cookie and sign-in behavior, what to decline on sites.
- **Role swap** and other skill-specific settings, as the user's skills need them.
- **Export profile**: one generic export of what the AI knows about the user, for any AI, with full content and evidence. No AI names, no destination presets, no token budget, no trimming for size.
- **Input mode**: FREE_TEXT (default) or CARDS; auto-apply ON (default) or OFF.

Some keys are locked (for example the model, when the platform does not let the AI change it: show it read-only).

## Free text first

1. **Entry**: the user's message is the input. Any language, typos, and several settings in one message are valid (for example: "turn off auto next steps, keep trash 3 days, reply in English").
2. **Parse** each clause into a candidate key and value, or an action. Search the catalog by name, description, and allowed values. The AI is the judge. If unclear, pick the closest key and say which one was chosen; ask once only when two readings would change different things and neither is clearly closer.
3. **Apply** directly. Reversible changes (any catalog key, memory add or edit, moving files to trash, cache cleanup, restore) run with no confirmation. With auto-apply OFF, show the plan and apply after the user agrees.
4. **Actions by typing**: every menu stays reachable by name or by what it does: view settings, clear cache, show storage, restore a trash batch, export memory, export profile, factory reset, and so on. "Cards" opens a card-based menu once, if the AI can render cards.
5. **Confirm only irreversible or high-risk actions**, once each, never per item: factory reset, permanent deletion outside the trash.
6. **Refuse** (one-line reason, change nothing): locked keys, anything the AI cannot really do.
7. **Result**: one short text with `KEY: old -> new` lines, "interpreted as KEY" lines, "not understood" lines, "refused: KEY (reason)" lines, and action results (space freed, items trashed).

## Auto-detect (runs on detection, never on a clock)

If the AI has file system and shell access:

- **Detect**: regenerable caches over the threshold (package manager caches, build caches, `__pycache__`), old temp files, partial downloads, temp leftovers (`*.part`, `*.tmp`, `*.crdownload`), backups beyond the keep count, trash older than retention, disk over the warn level.
- **Act** (AUTO_CLEAN): delete regenerable caches and partial downloads; move scratch files, temp leftovers, and old backups to a dated trash batch that can be restored; purge old trash batches that hold no work files. Duplicates of code or documents, large files, and old media are suggest-only. SUGGEST_ONLY mode reports and changes nothing.
- **Never touch**: the settings file, memory, logs, tools, model files and model caches, protected paths, anything a running process is using, and work files modified recently.
- **Hooks**: run detection after a task that created large files, whenever a command reports low disk or out-of-memory, and at the start of every settings run. Report per the notify setting.

## Factory reset

One confirmation (the user types RESET). Back up the settings file first, restore every key to its default, keep logs and memory unless the user names them, then report what changed and where the backup is. It may take a while.

## Constants

No emoji; the user's language by default; copyable text in a `.md` file, not a code block; dark mode for any visual UI.

## Optional run log

If the AI can write files, log every settings session: the typed message verbatim, one parse line per clause, every command and result, every file touched, errors, and an end line with what changed. Never log passwords or secrets. Build the "what changed" summary from the log.
