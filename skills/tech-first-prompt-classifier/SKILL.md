---
name: tech-first-prompt-classifier
description: Use when the user asks to analyze, grade, or improve a prompt, message, AI answer, image, or file. Scores it on six dimensions as KEY = VALUE lines, explains the weakest points, and returns a fixed version.
---
# Tech-first prompt classifier

A fast, repeatable rubric for any input, with a technical bias: clarity and checkability come first.

## The six dimensions (0 to 10 each)

1. `CLARITY`: is the goal stated in one reading?
2. `SPECIFICITY`: are inputs, constraints, format, and length given?
3. `CONTEXT`: does it carry what the reader needs (audience, background, prior decisions)?
4. `VERIFIABILITY`: can the result be checked (criteria, tests, sources, examples)?
5. `TECH_DEPTH`: are technical terms, versions, and tools exact and correct?
6. `RISK`: privacy leaks, unsafe actions, false claims, ambiguity that could cause harm. Higher score = lower risk.

## Steps

1. Identify the input type: `PROMPT`, `MESSAGE`, `AI_ANSWER`, `IMAGE`, `FILE`, `OTHER`.
2. Score each dimension with a one-line reason tied to a specific part of the input.
3. Compute `TOTAL` = sum (0 to 60) and `GRADE`: A (52+), B (42 to 51), C (30 to 41), D (below 30).
4. List the top three fixes, most impactful first.
5. Produce the fixed version. Keep the author's intent, language, and voice. For an AI answer, the fix is a corrected answer; for an image or file, the fix is a list of concrete edits.

## Output format

```
TYPE = PROMPT
CLARITY = 7 | goal is clear but buried in paragraph 2
SPECIFICITY = 4 | no output format or length
CONTEXT = 6 | audience missing
VERIFIABILITY = 3 | no success criteria
TECH_DEPTH = 8 | versions given
RISK = 9 | no private data
TOTAL = 37
GRADE = C
FIX_1 = add an output format
FIX_2 = add success criteria
FIX_3 = state the audience
```

Then the fixed version.

## Rules

- Score what is there, not what the author probably meant.
- Do not reward length. A short, exact prompt can score 60.
- If a claim in the input is checkable and doubtful, flag it under `VERIFIABILITY` instead of accepting it.
