---
title: Free skill library
summary: Eight free, standalone SKILL.md files for indie makers who work with AI agents. MIT licensed.
---
# Free skill library

These are skills I use every day, rewritten as standalone files with nothing private in them. Each is one `SKILL.md` file: a name, a one-line description, and plain instructions an agent follows. They are free under the [MIT license](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/LICENSE) and provided as is, without warranty.

They are written for solo makers: no paid service is needed, and most need only an agent that can read files and, for some, run shell commands or fetch web pages.

| Skill | What it does |
|---|---|
| [text-to-verbatim-prompt](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/text-to-verbatim-prompt/SKILL.md) | Turns any text into an English prompt that lets another AI rebuild the text exactly, without the text itself appearing in the prompt. Includes a compare step. |
| [tech-first-prompt-classifier](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/tech-first-prompt-classifier/SKILL.md) | Scores any input on six dimensions as KEY = VALUE lines, then rewrites it to fix the weak points. |
| [false-negative-guard](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/false-negative-guard/SKILL.md) | Before an agent reports "not found" or "none", re-checks with a second, different method. |
| [fact-checker](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/fact-checker/SKILL.md) | Checks claims against real sources before they go into published work or to another AI. |
| [prompt-to-skill](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/prompt-to-skill/SKILL.md) | Turns a prompt you keep re-pasting into a saved skill, keeping your words verbatim. |
| [md-sub-agent](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/md-sub-agent/SKILL.md) | A Markdown specialist: writes, converts, fixes, and organizes `.md` files. |
| [task-watchdog](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/task-watchdog/SKILL.md) | Watches long-running agent tasks and checks finished ones against the real files. Reports only when something is wrong. |
| [link-page-monitor](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/link-page-monitor/SKILL.md) | Checks a link-in-bio page (such as Linktree) for changed, broken, or redirected links, against a saved baseline. |

## Install

The files follow the common `SKILL.md` layout (YAML front matter with `name` and `description`, then instructions), so they work with agents that load skills from a folder, and as plain instructions anywhere else.

1. Download the folder of the skill you want from the [skills directory](https://github.com/klanarongz2009-sketch/BlogPost/tree/main/skills), or clone the repo:

   ```bash
   git clone https://github.com/klanarongz2009-sketch/BlogPost.git
   ```

2. Copy the skill folder (for example `skills/false-negative-guard/`) into the skills folder your agent reads. For agents that keep skills per project, that is usually a `skills/` folder in the project.
3. If your assistant has no skill folder, open the `SKILL.md` and paste its contents into the assistant's custom skill, custom instructions, or a new chat.
4. Ask the agent to use it by name, or let it pick the skill when the description matches.

## Adapting (tips)

- Keep the description line specific; agents use it to decide when to load the skill.
- Replace example paths with your own. None of the files need an API key.
- If you improve one, a pull request is welcome; see [CONTRIBUTING](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/CONTRIBUTING.md).
