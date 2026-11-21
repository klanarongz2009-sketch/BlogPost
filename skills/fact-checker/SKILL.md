---
name: fact-checker
description: Use before a claim goes into published work, a public post, a README, or a prompt for another AI. Verifies each factual claim against a real primary source and labels it verified, corrected, unverified, or removed, with the source link.
---
# Fact checker

Check facts before they spread. Once a wrong claim is in a README or in another AI's context, it gets repeated.

## Input

A draft (text, a list of claims, or a file path) and, if known, where it will be used.

## Steps

1. **Extract claims.** List each checkable statement: names, numbers, dates, versions, prices, links, quotes, "X supports Y", "X is free". Skip opinions, but make sure they are worded as opinions.
2. **Pick the primary source** for each claim: the project's own repo or docs, the official site, the release page, the original paper, the store listing. Prefer the newest dated source. Use aggregators and blogs only to find the primary source.
3. **Check each claim** by actually opening the source. A search snippet is not enough.
4. **Label** each claim:
   - `VERIFIED` with the source URL;
   - `CORRECTED` with the right value and the source URL;
   - `UNVERIFIED` when no primary source could be read (say what you tried);
   - `REMOVE` when the source contradicts it and there is no corrected form worth keeping.
5. **Check links.** Every URL in the draft must load (status 200 after redirects). A 403 from a site that blocks bots is noted, not dropped.
6. **Return** the corrected draft plus the claim table.

## Output

| # | Claim | Status | Source | Note |
|---|---|---|---|---|

Then the corrected text.

## Rules

- Never upgrade a guess to a fact. "Probably" stays "probably".
- Performance claims ("fastest", "best", "X% better") need a reproducible source, or they are removed.
- Do not add facts that were not in the draft unless the user asked.
- If a negative is part of the check ("no such release exists"), run a second method before saying so.
