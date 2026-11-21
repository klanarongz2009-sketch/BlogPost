---
name: prompt-to-skill
description: Use when the user sends a prompt they want to reuse, or says "make this a skill". Converts the prompt into a saved, reusable skill while keeping the user's own words verbatim.
---
# Prompt to skill

If you paste the same prompt again and again, it should be a skill.

## Steps

1. **Take the prompt exactly as given.** Do not paraphrase, shorten, translate, or "improve" the user's wording. Keep line breaks, spelling, and language.
2. **Pick a name**: short, lowercase, hyphenated, describing the job (`weekly-news-digest`, not `my-prompt-3`).
3. **Write the description line**: when should an agent load this? One sentence that starts with "Use when..." and names the trigger words or situation.
4. **Build the file**:

   ```
   ---
   name: <name>
   description: <description>
   ---
   # <Title>

   ## Instructions (verbatim from the user)

   <the prompt, unchanged>

   ## Inputs
   <only if the prompt has blanks the user fills each time; list them>
   ```

5. **Do not add steps** the user did not write. If something is unclear (an input, an output format), ask the user once, and add their answer as a separate "Notes" section, marked as added.
6. **Save** the file as `skills/<name>/SKILL.md` (or in the assistant's skill store) and confirm the name and how to run it.
7. **Check**: compare the instructions section with the original prompt character by character. They must match.

## Rules

- If the same skill already exists, update it instead of making a duplicate.
- Strip secrets (tokens, passwords, personal emails) and tell the user you removed them.
