---
name: text-to-verbatim-prompt
description: Use when the user wants another AI to write out a text exactly, character for character, without pasting the text to it. Turns any text into an English .md prompt that specifies the text line by line (the text itself never appears in the file), then compares the other AI's answer with the source.
license: MIT
---
# Text to verbatim prompt

Flow: the user gives any text -> you analyze it -> you write an English prompt file -> the user pastes that file into a **new chat** of a destination AI -> the destination AI writes out the user's text -> the user pastes the answer back to you -> you compare it with the source.

The destination AI must produce the user's text. It must never rewrite it.

## Two hard rules

1. The prompt file never contains the source text: no block of it, no whole lines of it, no heading or marker for it.
2. The prompt file never contains the words "ORIGINAL TEXT" (any capitalization).

## Works with

Any AI assistant. Running small scripts (Python) is strongly recommended for counting and checking; if your AI cannot run code, count with extreme care and tell the user the counts were not machine-checked.

## Settings (ask once, or use the defaults)

- `MINOR_FIX = NONE` (default): a "No adjustments of any kind" section; the destination keeps every spelling, capitalization, hyphen, quote style, and space the specification gives. `ALLOW`: an "Allowed minor adjustments" section that permits spacing or punctuation slips only, never wording.
- `SAFE_FRAMING = ON` (default): do not use the words "verbatim", "reproduce", or "reproducer" in the prompt; frame it truthfully as writing out a user's text from a specification for a comparison check. `OFF`: say plainly that the output will be compared character by character. Never invent authorship either way.
- `SOURCE_NOTES = FULL` (default): a "Notes on the source" section with counts and the spots that tempt a change (by line number, general words, single short tokens only). `COUNTS_ONLY` or `OFF`.
- `SELF_CHECK = ON` (default): keep the Self-check section. `OFF`: leave it out.

The raw save, the count, the verification, and the compare never depend on settings.

## Make the prompt

1. **Get the text** exactly as the user sent it. If there is none, ask for it once. Save it at once to a private file (for example `verbatim-raw-<date>-<time>.txt`); this file is the only source of truth. Never retype or rebuild the source with code (no loops, lists, or escaped-unicode rebuilds). Do not change a single character.
2. **Count by script first**: a script reads the raw file and prints total, non-empty, and blank lines; total characters; whether there is a trailing newline; and for every line its length in characters, its word count (split on whitespace), and its sentences with word counts. Also count characters a destination AI may change: straight and curly quotes, em dashes, ellipses, doubled hyphens, braces, non-ASCII characters, emoji. Every number in the prompt comes from this output.
3. **Analyze the text**: languages, structure, tone, technical tokens (commands, flags, paths, file names, sample values, handles, proper nouns), and anything a destination AI would be tempted to "improve": typos, slang, mixed languages, repeated letters, odd punctuation, inconsistent capitalization, footers. List likely typos; never fix them.
4. **Write the prompt**, all in English, as one `.md` file. Sections in this order:
   - **Context and task**: what the text is in general words (topic, line count, language); that the text is not in the file; that the file specifies every line; that the user will compare the output with their text.
   - **Notation**: text between backticks is exact, character for character (the backticks are not part of the text). Described wording means the plainest English carrying exactly that meaning, in the given order, with exactly the stated word count, using the words named, no synonyms. A "word" is anything separated by spaces.
   - **Hard rule**: no rewriting, no additions, no commentary, titles, or Markdown. Commands and code-like lines stay plain lines (no code fences, no backticks, no indentation). Sample values stay as they are.
   - **Minor adjustments** section per `MINOR_FIX`.
   - **Line-by-line specification**: one entry per line, `Line N (W words, C characters): ...`; blank lines as `Line N: blank.` Long lines are split into sentences with their own word counts. Exact backtick tokens are allowed only for technical tokens, single words or spellings that must not change, punctuation, and short fixed phrases of at most 4 to 5 words. Runs without spaces (Thai, Japanese, Chinese) are given as pieces to join: `piece1` + `piece2`, and the specification states where a space separates two words. Natural-language wording is described by meaning, naming its key words separately, never quoted as a run.
   - **Notes on the source** per `SOURCE_NOTES`.
   - **Output format**: only the N lines of text, nothing before or after, no code fence (unless the source had one), no line numbers.
   - **Self-check** per `SELF_CHECK`: check the output against the specification line by line (line count, blank lines, word count and character count per line, backtick tokens exact, straight quotes, final newline as in the source); any difference means redo that line.
5. **Verify before sending**, and fix and re-verify on any failure:
   - A case-insensitive search for "original text" in the file returns 0.
   - Leak check: a script normalizes words (lowercase, strip surrounding quotes, backticks, and punctuation) and confirms that no source line longer than 15 characters appears in the file and no run of 6 consecutive source words appears in the file. Any hit: rewrite that spot by meaning and check again.
   - Spec check: a script parses every `Line N (W words, C characters)` and `Line N: blank` entry and compares it with the raw file; sentence word counts and every number in the Notes are re-checked against the step 2 output. Mismatches must be 0.
   - With `SAFE_FRAMING = ON`, "verbatim", "reproduce", and "reproducer" do not appear.
   - Never ask the user to count or check numbers.
6. **Deliver** the `.md` file (a new file name each run). Tell the user what the prompt enforces and the main counts, to paste the file content only into a **new chat** of the destination AI, and to paste the destination AI's answer back to you for the comparison.

## Compare

When the user pastes the destination AI's answer, save it exactly to a second file, then compare the two files with a script using exact matching (for example Python `difflib` with `autojunk=False`). Report: IDENTICAL or DIFFERENT, characters and lines in both, lines matching at the same position, a similarity ratio, and each differing line with its number, the source, the returned text, and the kind of change (wording, punctuation, quote style, spacing, missing or extra line).

If the same spots keep failing, the next fix is a more precise specification for those lines (more exact tokens, a tighter description), never putting the source text or the words "ORIGINAL TEXT" into the prompt.

## Rules

- One run = one text = one `.md` file. A new text later is a new run and a new file.
- Do not run the prompt on another AI yourself unless the user asks.
- The raw save, the count, the verification, and the compare are never skipped, even for a one-line text.
