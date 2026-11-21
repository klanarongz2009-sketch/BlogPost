---
title: Projects
summary: TER-AI, Tagentic1, the Telegram bot, and Klasster music.
---
# Projects

## TER-AI

[TER-AI](https://github.com/klanarongz2009-sketch/ter-ai) is my offline-first Thai AI toolkit (MIT). From its README: typo-tolerant intent routing, local chat and vision, speech synthesis, SVG graphics, and music creation. The intent router is 1.1 MB, runs on CPU, has no runtime dependencies, and works offline: give it one Thai or Thai-English message and it returns one of 15 intents. Try the [web demo](https://klanarongz2009-sketch.github.io/ter-ai/).

TER-AI is an indie project and may pause or close with little warning. Its [project notice](https://github.com/klanarongz2009-sketch/ter-ai/blob/main/PROJECT_NOTICE.md) says why.

## Tagentic1

Tagentic1 is a local thinking-and-agentic model setup inside the TER-AI project: short visible reasoning steps, tool use, and four memory files (`User.md`, `Systemprompt.md`, `Memory.md`, `Systemskill.md`). It is a work in progress. My own test found it drops a space between Thai words in exact-copy tasks ([issue #18](https://github.com/klanarongz2009-sketch/ter-ai/issues/18)).

## Telegram bot @Terai_F0_bot

[@Terai_F0_bot](https://t.me/Terai_F0_bot) is the Telegram bot for Tagentic1. Bot system messages are in English; the AI replies in the language it writes in. Anyone can suggest knowledge with `/add`. Suggestions go to a queue and are checked against sources before they are added to the shared knowledge file. Public users cannot read private files or run commands. The bot can stop at any time.

## AI memory continuity

[ai-memory-continuity](https://github.com/klanarongz2009-sketch/ai-memory-continuity): a provider-neutral agent skill for persistent memory across AI sessions (MIT).

## Music as Klasster

I make AI-assisted music as **Klasster**.

- [Klasster on Treblo](https://treblo.com/artist/dgjuyyu209026). Treblo sometimes blocks automated checks with HTTP 403; the page works in a normal browser.
- [Top song: idc](https://treblo.com/song/f5055d23-5bbe-4a65-9702-434e847e06bd) on Treblo.
- [My AI music on ElevenMusic](https://elevenmusic.io/artists/klanarong-487021)
- [AI music playlist on YouTube (7 videos)](https://youtube.com/playlist?list=PLiVKEuzl8bijQXHEZSml5VsaP64m78VCM)
- [Tech Deep Dive EP.6: Treblo/Sonauto](https://youtube.com/watch?v=UTCHLpRn7Ks) on YouTube
