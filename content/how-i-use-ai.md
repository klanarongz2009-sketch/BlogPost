---
title: How I use AI
summary: Sub-agents, memory, verification, scheduled routines, and Thai AI testing in a solo workflow.
---
# How I use AI

I work alone, so I treat AI agents as the team. My main assistant is Sesame, and I run most of this through its custom skills, a Linux VM it can use, and schedules. The patterns below work with other agent platforms too.

## 1. Sub-agents with one job each

Instead of one assistant that does everything, I give narrow jobs to sub-agents, each defined by a skill file. Some examples from my own setup:

- **Task watchdog**: watches long-running tasks and checks finished ones against the real files.
- **Fact checker**: verifies claims against real sources before they go into public work or to another AI.
- **False negative guard**: re-checks every "not found" result with a second method before it is reported.
- **Release coordinator**: reserves version numbers so two tasks do not release the same version.
- **GET IDEAS** and **Teemate**: answer GitHub Issues and Discussions on my TER-AI repository while I am away. They are bots, and they say so.

A coordinator sub-agent can also run child sub-agents. My license audit for TER-AI uses one coordinator and three child auditors, and the coordinator merges and verifies their results.

## 2. Memory that survives sessions

Agents forget between sessions unless memory is a file. I keep a numbered memory file with tags such as FACT, RULE, and IDEA, a changelog, and a backup before every edit. A separate routine updates memory when I state a new rule, and checks for conflicts with old entries before writing.

When I move to another assistant, I export a **portable memory snapshot**: reliable facts only, short third-person bullets, inferences labeled as uncertain, and nothing sensitive. Some assistants have small memory limits (one I use holds 100 entries), so the snapshot has to fit.

## 3. Verification by default

The most useful habit I have: never accept an AI's claim that work is done or that something does not exist without a check. In practice:

- After a push, read it back from GitHub. After a deploy, request the live URL.
- A "not found" must survive a second search method.
- Reports separate verified facts, hypotheses, and unknowns.

## 4. Scheduled routines

Agents can work while I sleep or am away. My routines include a daily link check for my link page, a daily summary email, a weekly AI news review, an "AI night shift" that prepares work and logs everything, and a memory update routine. Free credits run out sometimes and tasks pause; the routines log where they stopped so they can resume.

One rule I learned the hard way: a delayed run is dated by the day it actually ran, not the day it was scheduled. Otherwise date-based tasks silently skip.

## 5. Testing Thai AI quality

Thai is my first language, and AI still gets it wrong in specific ways: pronunciation, transliteration, transcription, and word spacing (Thai does not put spaces between words). I test this directly.

Example: on 2026-11-21 I ran a **verbatim text-return benchmark**. Five AIs got the same English prompt that described a 12-line Thai-English text word by word, and had to rebuild it exactly. Scoring was exact character match with Python.

| AI | Characters matched | Lines matched |
|---|---|---|
| Overlay.one | 1,087 / 1,087 | 12 / 12 |
| Sesame (Simone) | 1,087 / 1,087 | 12 / 12 |
| Qwen | 1,087 / 1,087 | 12 / 12 |
| Wabi | 1,086 / 1,087 | 11 / 12 |
| Tagentic1 (my model) | 1,086 / 1,087 | 11 / 12 |

The two misses were the same: one dropped space between two Thai words, even though the prompt gave the word count for that line. It was one run with one text, so it shows a failure mode, not a ranking. I opened [an issue](https://github.com/klanarongz2009-sketch/ter-ai/issues/18) for my own model. The prompt was made with the [Text to verbatim prompt](../skills/) skill.

## What I would tell another indie maker

My opinion, from my own use:

- Write the rules down once, as a skill or memory file, instead of re-explaining them to every AI.
- Make the agent prove its work. It costs a few extra tool calls and saves hours.
- Keep copyable prompts in Markdown files, one file per paste target.
