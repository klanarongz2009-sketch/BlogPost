---
title: Why my READMEs put English first and Thai in its own file
date: 2026-11-21
summary: Many Thai repos open with Thai and put English at the bottom, or leave it out. I do the reverse: English README first, Thai as a separate full file. Here is why.
---
A pattern I often see in repos made by Thai developers: the README opens in Thai, and English comes at the bottom, or not at all. This is my own observation, not a survey. Here is one real example, and then why I do it the other way.

Thai version of this post: [ภาษาไทย](../../th/english-first/)

## One example: Kreycin

[Kreycin](https://github.com/Kreycin) is a Thai maker who publishes AI animation and tool kits. The work is good, and the kits are clearly written for a Thai audience. That is why I picked it as an example, not to criticize it. I read the README of every repo on the account on 2026-11-21:

- **Thai first, English section at the bottom:** [pdoom-mv-kit](https://github.com/Kreycin/pdoom-mv-kit) (the `## English` heading starts around line 91 of 110), [pdoom-3d-kit](https://github.com/Kreycin/pdoom-3d-kit) (line 83 of 99), and [Auto-Prompt-Image-Extension-Gemini-](https://github.com/Kreycin/Auto-Prompt-Image-Extension-Gemini-) (English copy starts at line 51).
- **Mostly Thai, no English section:** [Auto-Caption](https://github.com/Kreycin/Auto-Caption). The section headings are Thai and the steps are in Thai.
- **Thai and English on the same line:** [thai-docs-to-excel](https://github.com/Kreycin/thai-docs-to-excel), with headings like "ติดตั้งและใช้งาน / Install and run".
- **English first, Thai at the bottom:** [scope](https://github.com/Kreycin/scope), a Claude Code plugin.
- **English:** [ton-sea](https://github.com/Kreycin/ton-sea). Only the title has Thai in it.

I left out two frontend repos that still have the default framework README, and one with no README.md.

So even on one account, it is mixed. Three of seven READMEs put Thai first with English at the bottom, and one is mostly Thai. The two that put English first are the most general tools: a Claude Code plugin and a code-only animated film.

## Why I put English first

- **The first screen decides.** Someone who lands on a repo reads the top and leaves if it is not in a language they read. On GitHub, the people who might use, star, or fix a dev tool mostly read English. If the top is Thai, most of them never scroll to the English part.
- **Search and AI agents read the top too.** GitHub search, link previews, and AI coding agents that are pointed at a repo all start at the top of README.md. An English summary there makes the repo easier to find and easier for an agent to use correctly.
- **My public work is meant for anyone.** I publish in English, and keep Thai for personal or local work. A dev tool, a skill, or a model like Tagentic1 has no reason to be limited to readers of one language.

## Why Thai goes in its own file

- **Each language stays complete.** A Thai section at the bottom of an English README tends to fall behind: the English gets updated and the Thai part does not. With `README.md` and `README.th.md` as two full files, I can check that they match. In [ter-ai](https://github.com/klanarongz2009-sketch/ter-ai) the project notice is also split this way, as `PROJECT_NOTICE.md` and `PROJECT_NOTICE.th.md`.
- **Nobody has to scroll past a language they cannot read.** English readers get English from the first line. Thai readers click one link at the top and get Thai from the first line.
- **It is Thai, not a translation squeezed into a corner.** A separate file gives the Thai text the same room and the same structure as the English one.

## When Thai first makes sense (opinion)

If the audience is Thai, Thai first is the right call. Kreycin's kits come with Thai YouTube videos and are written for people who watch them, so Thai first fits. My rule is simple: write the first screen for the people you most want to reach. For my public dev work, that is everyone, so it is English first, with one clear link to a full Thai version.
