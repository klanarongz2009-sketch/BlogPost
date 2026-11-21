---
title: Five AIs, one missing space: a Thai verbatim test
date: 2026-11-21
summary: Three of five AIs rebuilt a Thai-English text exactly from a word-by-word prompt. Two dropped one space between Thai words.
---
Thai does not put spaces between words. That makes it a good stress test: can an AI copy Thai text exactly, spaces included, when it is told exactly what to write?

## The test

I took a 12-line Thai-English report (9 lines of text, 3 blank, 1,087 characters) and turned it into an English prompt with my [Text to verbatim prompt](../../skills/) skill. The prompt does not contain the text. It describes every line word by word, gives the word and character count for each line, and lists the tokens that must not change.

Five AIs got the same prompt. I scored the answers by exact character match in Python.

## Results

| AI | Exact match | Characters | Lines |
|---|---|---|---|
| Overlay.one | yes | 1,087 / 1,087 | 12 / 12 |
| Sesame (Simone) | yes | 1,087 / 1,087 | 12 / 12 |
| Qwen | yes | 1,087 / 1,087 | 12 / 12 |
| Wabi | no | 1,086 / 1,087 | 11 / 12 |
| Tagentic1 | no | 1,086 / 1,087 | 11 / 12 |

Wabi and Tagentic1 made the same single error on line 6: they joined two Thai words that the prompt listed as separate words. The prompt said line 6 has 23 words and 156 characters; both answers had 22 and 155.

Every AI got the harder-looking parts right: an em dash, straight quotes, a URL with a trailing slash, a deliberately lowercase "Ai", and the blank lines.

## Why it might happen (hypotheses)

- In normal Thai, those two words are often written together as one phrase, so a model may "fix" the spacing.
- One of the words appears elsewhere in the prompt as part of a joined compound, which may prime the model to join it again.

## Limits

One run, one text. The answers were copied from chat apps, which can also change whitespace. This shows a failure mode, not a ranking.

## What I changed

Tagentic1 is my own model, so I opened [issue #18](https://github.com/klanarongz2009-sketch/ter-ai/issues/18): keep spacing exactly as specified, check word and character counts per line after answering, and add a regression test for this exact case.

**Tip for indie makers:** if your product handles Thai (or any language without spaces), add one exact-copy test like this. It is cheap and it catches a real class of bugs.
