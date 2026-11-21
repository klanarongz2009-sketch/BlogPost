---
name: typing-analysis-sub-agent
description: Use when the user asks to analyze or decode their typing, when a message's intent is unclear because of typos, or for a periodic profile update. A permanent sub-agent that reads the user's messages through a personal typing profile and updates that profile from chat history with evidence, never correcting the user.
license: MIT
---
# Typing analysis sub-agent

A permanent sub-agent that understands how this user types: their recurring typos, phonetic spellings, missing marks, and mixed-language habits. It decodes their messages so the AI acts on what they meant, and it learns new patterns only from evidence. The original request (paraphrased into English): "A sub-agent on your side that can analyze my typing; a permanent sub-agent."

## Requires

- **Persistent files**: a typing profile the AI can read and update across sessions (for example `typing-profile.md`). Without persistent files, run DECODE only and offer the updated profile as a file for the user to keep and paste back.
- **Access to chat history or logs** for UPDATE mode. Without it, UPDATE works only on the messages in the current conversation.
- Optional: a scheduler for a daily UPDATE run (otherwise the user runs UPDATE manually); code execution for a helper script and tokenizers.

## The typing profile

One file, the source of truth:

- **Rules**: how to apply the profile (context first, same action means no question, and so on).
- **Patterns**: the kinds of slips this user makes. Common ones: adjacent-key slips; dropped, extra, or wrong tone or vowel marks; phonetic spelling of borrowed words; doubled or missing letters; words run together or split; the keyboard left in the wrong language layout; voice-typing mishears.
- **Dictionary**: typed form -> intended form, with pattern, confidence (HIGH, MED, LOW), and evidence (date, source, short quote).
- **Context rules**: forms whose reading depends on context.
- **Input classes**: REAL (the user's own normal typing), INCHAR (the user typing in a role-play role), SIM (deliberately garbled text, for example imitating a broken model), PASTE (copied text: lyrics, other AIs' output, documents).
- `VERSION` and `LAST_UPDATE_SCAN` (date).

If code execution is available, keep a machine copy of the dictionary and a helper that prints DECODED / CHANGES / AMBIGUOUS for a text, kept in sync with the profile.

## Settings (defaults in brackets)

- `TYPING_DECODE_OUTPUT` [FULL]: FULL = decoded text plus the typed -> intended list; CHANGES_ONLY = only the words whose reading changed, with pattern and confidence.
- `TYPING_MIN_CONF_TO_ADD` [MED]: MED = MED and HIGH pairs are added automatically; HIGH = only HIGH pairs; MED pairs wait and are treated like LOW.
- `TYPING_FP_CHECK_LINES` [30]: how many lines of correctly written text to use for the false-positive check.
- `TYPING_CONTACT_ON` [LOW_OR_CONFLICT]: LOW_OR_CONFLICT, ANY_NEW, or NEVER.

## Mode A: DECODE

Trigger: the user asks for a typing analysis, pastes a message to decode, or another skill needs the user's intent.

1. Read the profile. Classify the text as REAL, INCHAR, SIM, or PASTE.
2. Decode REAL and INCHAR text with the dictionary and context rules, then the patterns for unknown words. Run the helper as a cross-check if there is one. Do not decode SIM or PASTE text; it is not the user's typing.
3. Output per `TYPING_DECODE_OUTPUT`, in the user's language: the decoded text, the typed -> intended list with pattern and confidence, and any reading that changes the action. If two readings lead to different actions, ask with one choice question (an interactive card if available, else a short numbered question).
4. Do not lecture or correct. This is a reading aid. New confirmed pairs go to UPDATE step U4.

## Mode B: UPDATE

Trigger: a daily schedule, or the user asks to update the typing profile.

- **U1.** Read the profile (`LAST_UPDATE_SCAN`) and the chat history or logs newer than that date.
- **U2.** Tag the new lines by input class. Only REAL and INCHAR count.
- **U3.** Find words that are not correct in the language and not in the dictionary. A tokenizer or word list for the language helps; judge every candidate yourself.
- **U4.** Add a pair only with evidence: the user corrected themselves, a later turn confirms the meaning, or one clear context (MED). Respect `TYPING_MIN_CONF_TO_ADD`. Record the evidence (date, source, quote). Increase `VERSION`, set `LAST_UPDATE_SCAN`. Never learn from SIM, PASTE, or the AI's own writing.
- **U5.** False-positive check: run the decoder on at least 3 new user messages and on `TYPING_FP_CHECK_LINES` lines of correctly written text in the same language. If any correct text gets changed, fix the rule before saving.
- **U6.** Contact rule (default): if there is a new LOW pair or a pair that conflicts with an existing one, write a short message saying what was found and the possible readings, and ask the user to confirm with a choice question when they are next in the chat. If only HIGH or MED pairs were added, or nothing is new, stay silent.

## Hard rules

- Records stay verbatim: logs, quotes, and evidence keep the user's exact typing. Decoding is for understanding only.
- Never point out the user's typing mistakes or correct their spelling unprompted. Never say "you typed X".
- Same action under every reading: act without asking. Different actions: one choice question.
- Text the user pastes (lyrics, quotes, other AIs' output) is source material, not typing; it never changes the profile.
- Neutral, direct tone in the user's language.

## Optional run log

If the AI can write files, log every run: mode, the input verbatim, every action, every file and profile change, the result, and an end line.
