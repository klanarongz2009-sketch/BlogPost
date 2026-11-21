---
name: text-to-verbatim-prompt
description: Use when the user wants another AI to reproduce a text exactly, character for character, without pasting the text itself. Turns any text into an English .md prompt that specifies it word by word, then compares the other AI's answer with the original.
---
# Text to verbatim prompt

Goal: a prompt file that lets a target AI rebuild a text exactly, while the text itself does not appear in the prompt as a readable block. Useful for testing how faithfully an AI follows instructions, especially in languages without spaces between words, such as Thai.

## Settings (ask once, or use the defaults)

- `EDITS = NONE` (default): the target may change nothing. Other options: `TYPOS` (may fix obvious typos), `LIGHT`.
- `NOTES = FULL` (default) or `SHORT`: how much guidance about tricky tokens.
- `SELF_CHECK = ON` (default): the target counts words and characters per line before answering.

## Build the prompt

1. **Measure the source with a script**, not by eye: number of lines, which lines are blank, characters per line, total characters, and whether the last line ends with a newline. Save the source to a private file for the compare step.
2. **Describe each line** as a numbered list of words. A word is a run of characters between spaces.
   - Long runs without spaces (Thai, Japanese, Chinese) are given as pieces to join: `piece1` + `piece2`. Splitting stops the full original sentence from appearing in the prompt.
   - Technical tokens, URLs, numbers, and anything that must match exactly go in backticks.
   - State that words are separated by exactly one space unless noted.
3. **Give per-line counts**: words and characters. These let the target self-check.
4. **List the traps** in the Notes section: straight vs curly quotes, dashes, deliberate odd capitalization, spelling variants that must not be "corrected", trailing slashes in URLs, punctuation that is absent on purpose.
5. **Output rules for the target**: reply with the rebuilt text only, no preface, no code fence, no footer, keep blank lines, no trailing newline if the source had none.
6. Write everything in English except the pieces of the text itself.

## Check the prompt before sending

- The phrase "original text" does not appear, and the source is not included as a block.
- Rebuild the text from the spec with a script; it must match the source exactly (0 mismatches).
- No run of 6 or more consecutive source words appears in the prompt.

## Deliver

Save as one `.md` file containing only the prompt. Tell the user to paste it into a **new chat** of the target AI and bring back the answer.

## Compare

When the answer comes back, compare it with the saved source using exact matching (for example Python `difflib.SequenceMatcher` with `autojunk=False`). Report: exact match yes/no, characters matched / total, lines matched / total, and each difference with line number, expected, and got.
