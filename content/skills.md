---
title: Free skill library
summary: Thirteen free, standalone SKILL.md files that work with any AI assistant or agent. MIT licensed.
---
# Free skill library

These are skills I use every day, rewritten so that any AI can run them: ChatGPT, Claude, Gemini, local models, Wabi, or any agent that reads instructions. Each is one `SKILL.md` file: a name, a one-line description, and plain instructions. Nothing in them is tied to one provider: where a step needs a feature (a terminal, a scheduler, memory files, interactive cards, text-to-speech), the file says so and gives a fallback or a clear stop message. They are free under the [MIT license](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/LICENSE) and provided as is, without warranty.

No paid service is needed for any of them.

| Skill | What it does | Requires |
|---|---|---|
| [text-to-verbatim-prompt](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/text-to-verbatim-prompt/SKILL.md) | Turns any text into an English prompt that lets another AI write the text out exactly, without the text itself appearing in the prompt. Includes a compare step. | Any AI; running scripts recommended for counting |
| [auto-update-agent-memory](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/auto-update-agent-memory/SKILL.md) | Adds, updates, and removes memory entries (rules, preferences, thoughts, ideas, facts) on its own whenever a change is detected, never on a timer. | Persistent memory the AI can write; else outputs the memory file |
| [ai-night-shift](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/ai-night-shift/SKILL.md) | An unattended late-night session: the AI picks useful work for your projects, does it within hard limits, logs everything, and reports in the morning. | A scheduler; else run it manually |
| [interactive-ui-in-chat](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/interactive-ui-in-chat/SKILL.md) | Builds a working UI inside the chat as interactive question cards (menus, quizzes, wizards), not an HTML file, and saves each one as a skill. | Interactive cards in the chat; else a numbered text menu |
| [prompt-to-skill](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/prompt-to-skill/SKILL.md) | Turns a prompt you keep re-pasting into a saved skill, keeping your words verbatim and adding a separate execution layer. | A place to save skills or instructions; else outputs the file |
| [agent-settings](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/agent-settings/SKILL.md) | A settings layer for your assistant: type any change in plain language and it is applied, with storage cleanup on detection and a factory reset. | A persistent settings file; some features need shell access |
| [subagent-creator-and-promptor](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/subagent-creator-and-promptor/SKILL.md) | Turns a prompt into a sub-agent spec and runs it, or builds one relay file for another AI with a source-routing rule; also exports your profile for any AI. | Any AI |
| [tech-first-prompt-classifier](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/tech-first-prompt-classifier/SKILL.md) | Scores any input on six dimensions as KEY = VALUE lines, lists the issues, and returns a fixed version. | Any AI |
| [terminal-in-chat](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/terminal-in-chat/SKILL.md) | A terminal in the chat: type or paste commands, or describe the task in plain language, and the AI runs it for real and shows the output. | A real terminal (shell execution); stops if there is none |
| [text-to-voice-with-ai](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/text-to-voice-with-ai/SKILL.md) | Turns your exact text into audio with whatever text-to-speech the AI has, free or local engines first, with a speech-recognition check before sending. | A text-to-speech capability |
| [typing-analysis-sub-agent](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/typing-analysis-sub-agent/SKILL.md) | Reads your messages through a personal typing profile so the AI acts on what you meant, and learns new typo patterns only from evidence. | Persistent files; chat history for updates |
| [vm-control-panel](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/vm-control-panel/SKILL.md) | A control panel for the AI's own machine: system info, shell commands, files, status, and processes, with a confirm step for destructive actions. | A VM, container, or sandbox the AI controls; stops if there is none |
| [ai-memory-continuity](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/skills/ai-memory-continuity/SKILL.md) | Before personalized or follow-up work, finds the relevant long-term context in your `USER.md` and `MEMORY.md` files or a connected memory tool, prefers current statements over old notes, and never claims a read that did not happen. | Any AI; memory files or a memory tool for recall |

## Install

The files follow the common `SKILL.md` layout (YAML front matter with `name` and `description`, then instructions), so they work with agents that load skills from a folder, and as plain instructions anywhere else.

1. Download the folder of the skill you want from the [skills directory](https://github.com/klanarongz2009-sketch/BlogPost/tree/main/skills), or clone the repo:

   ```bash
   git clone https://github.com/klanarongz2009-sketch/BlogPost.git
   ```

2. Copy the skill folder (for example `skills/prompt-to-skill/`) into the skills folder your agent reads. For agents that keep skills per project, that is usually a `skills/` folder in the project.
3. If your assistant has no skill folder, open the `SKILL.md` and paste its contents into the assistant's custom skill, custom instructions, project instructions, or a new chat.
4. Ask the AI to use it by name, or let it pick the skill when the description matches.

## Adapting (tips)

- Keep the description line specific; agents use it to decide when to load the skill.
- Each file starts with what it needs. If your AI lacks a feature, the skill tells it to fall back or to stop with a clear message instead of pretending.
- Replace example file names with your own. None of the files need an API key.
- If you improve one, a pull request is welcome; see [CONTRIBUTING](https://github.com/klanarongz2009-sketch/BlogPost/blob/main/CONTRIBUTING.md).
