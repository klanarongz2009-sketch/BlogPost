---
name: text-to-voice-with-ai
description: Use when the user provides text and wants it turned into an AI voice recording. Converts the exact text to audio with whatever text-to-speech the AI has (free or local engines first), splits long text into parts, checks non-English audio with speech recognition before sending, and delivers the audio files.
license: MIT
---
# Text to voice with AI

The user's prompt was simply: "Text to voice with AI." This skill turns text the user provides into spoken audio and delivers it as audio files in the chat.

## Requires

- **A text-to-speech capability**: a built-in voice or audio tool, a TTS API the AI is allowed to call, or a TTS engine the AI can run with shell access.
  - Prefer **free and local** options: an open-weight TTS model run locally, or a free engine. Never sign up for a paid plan, create billing, or spend money without the user's explicit request. Check each model's license (some open weights are non-commercial only) and respect the provider's terms, including age requirements.
  - If the AI has no TTS at all: say so in one line and stop. Do not pretend to produce audio.
- Optional: **speech recognition** (ASR) for the quality check below, and file output so the audio can be sent as a file.

## Source

- The text comes from the message that invokes the skill (text after the skill name), or the user's most recent message or attachment (PDF, DOCX, TXT, MD).
- If there is no text, ask for it in one line and wait.

## Steps

1. **Collect the exact text.** Keep the user's wording and language as given. Do not paraphrase, summarize, or translate unless asked.
2. **Check length.** About 150 words is about 1 minute. If the text exceeds the engine's limit, split it into sequential parts (Part 1, Part 2, ...) at sentence or paragraph boundaries. For languages without spaces between words (Thai, Japanese, Chinese), split by characters at sentence or space boundaries.
3. **Clean for speech.** Strip Markdown, code fences, bullet symbols, and emoji. Expand symbols and abbreviations only where needed for correct pronunciation. Write numbers as plain integers without thousands separators (1250, not 1,250).
4. **Route by language.** Use a voice that really speaks the text's language. A voice built for one language often cannot speak another (for example, an English-only voice reading Thai produces unintelligible audio). If the text is mostly in a language the default voice does not support, use an engine and voice for that language.
5. **Record** each part and save it as an audio file (MP3 or the engine's format) with the date and part number in the name.
6. **Quality gate** (required for any language the default voice is not verified for; recommended for all): if the AI can run speech recognition, transcribe each part, check that the detected language matches, and compute the character error rate against the cleaned text. Set thresholds (for example: language confidence at least 50 percent and character error rate under 15 percent).
   - On failure: regenerate a few times (a new seed or a different voice), then try a fallback engine with the same gate.
   - If every attempt fails: do not send that audio. Tell the user in one line which part failed and why (the measured values), and offer to retry, split the text shorter, or relax the threshold.
   - Never skip the gate for a language with a known failure history.
   - Known limit: tone-heavy tongue twisters (for example, Thai tone minimal pairs) can fail the check because speech recognition itself collapses the tones; normal prose usually passes.
   - If the AI cannot run speech recognition, say the audio was not machine-checked.
7. **Send** every part that passed as an audio file the user can play in the chat.
8. **Content rule**: do not record text that threatens, harasses, demeans, is hateful, violent, or sexual, or that impersonates a real person's voice. State the reason in one line and offer an alternative.

## Delivery

The recording(s) plus one short line in the user's language (for example "Here is the voice recording."), with the part count if split, the engine and voice used, and the gate result (for example "QA passed, CER 6%"). If a part failed the gate, send only the parts that passed and name the failed part numbers.

## Constants

No emoji. Dark mode for any UI. Copyable text in `.md` files.

## Optional run log

If the AI can write files, log each run: the full input text, the route chosen, the engine and voice, each gate attempt (language, confidence, CER, pass or fail), whether a fallback was used, every file produced, every error, and what was sent. Build any summary from the log.
