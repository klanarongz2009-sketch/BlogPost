# Free skill library

Thirteen standalone `SKILL.md` files that work with any AI assistant or agent (ChatGPT, Claude, Gemini, local models, Wabi, and others). MIT licensed, free, provided as is.

Install: copy a skill folder into the skills folder your agent reads, or paste the `SKILL.md` contents into your assistant's custom skill or custom instructions. Each file starts with YAML front matter (`name`, `description`) followed by plain-language instructions. Skills that need a feature (a terminal, a scheduler, memory files, interactive cards, text-to-speech) say so at the top and give a fallback or a stop message.

See the [skill library page](https://klanarongz2009-sketch.github.io/BlogPost/skills/) for what each one does.

## Maintainer notes: what goes in this library

- This folder holds only the skills Bogus has chosen for other AIs to use. Every other skill of Bogus's assistant stays private and is not published here.
- The current public set is: text-to-verbatim-prompt, auto-update-agent-memory, ai-night-shift, interactive-ui-in-chat, prompt-to-skill, agent-settings, subagent-creator-and-promptor, tech-first-prompt-classifier, terminal-in-chat, text-to-voice-with-ai, typing-analysis-sub-agent, vm-control-panel, ai-memory-continuity (merged on 2026-11-21 from its own repo, with its original README and LICENSE kept in the folder).
- New skills: when Bogus creates a new skill that is suitable for other AIs, it is added here too, after the same rewrite. A new skill is not published until Bogus confirms it belongs in the public set.
- Every published file is provider-neutral: no tool names of one assistant, no machine paths, no memory IDs, no accounts, emails, tokens, schedules, or personal information. Capability-dependent steps say what they require and what to do without it.
- After any change: update the count and the table in `content/skills.md`, `README.md`, and the home pages, rebuild with `python build.py`, and run the personal-information scan before pushing.
