---
name: interactive-ui-in-chat
description: Use when the user asks for an interactive UI inside the chat (a menu, quiz, settings flow, wizard, game turn). Builds it as native interactive question cards with tappable choices and text fields, not as an HTML file, and saves each new UI as a reusable skill.
license: MIT
---
# Interactive UI in chat

The user's request (paraphrased into English): "When I type a request, the system builds a UI in a window in the chat that really works." The user clarified: this does **not** mean HTML. A UI built this way should be saved as a skill automatically.

## Requires (check first)

This skill needs an AI that can render **native interactive elements in the chat**: question cards, forms, buttons, or tappable choices whose answers come back to the AI (for example a built-in "ask the user" form tool, interactive widgets, or quick-reply buttons).

- If your AI has them: continue.
- If it does not: tell the user in one line, "This AI cannot show interactive cards in the chat, so I will run the same flow as a numbered text menu." Then run every step below as plain text: each card becomes a short prompt with numbered options; the user replies with a number or text. Do not build an HTML file unless the user explicitly asks for HTML.

## Steps

1. **Read the request in full.** Everything the user typed after asking for the UI is the UI request. If nothing follows, ask (one text field) what UI to build, then continue. Work out what the UI must collect or let the user do: choices, text inputs, or a flow of several screens. Keep every requirement.
2. **Reuse first.** If a saved skill already covers this UI (same purpose), follow that skill instead of building from scratch.
3. **Map it to cards.** A short prompt line, tappable choices and/or text fields, optional fields marked optional. For a multi-step UI (menu, quiz, game turn, settings flow, wizard), show one card per step and chain them: each answer decides the next card.
4. **Show the card and wait.** Act on the answer for real (compute the result, update the state, run the chosen action with the AI's tools), then show the next card or the result.
5. **Keep state** across cards, and in a file if the flow is long or will be resumed and the AI can write files.
6. **End** when the flow reaches its end state or the user picks exit. Every multi-step card includes an exit option.
7. **Auto-save as a skill** (always, without asking): after the first card of a new UI is built, save the UI as its own skill (if the AI can save skills), so the user can reopen it. Name: 2 to 6 words describing the UI. Description: one line on what it does. The saved instructions must be self-contained: how to gather live data, the exact card prompts, fields, and choice labels, what each choice does for real, a confirmation before destructive actions, an exit option on every card, and the delivery rule. If a skill for this UI exists, update it instead of creating a duplicate. Do not save throwaway cards that only ask what UI to build. If the AI cannot save skills, offer the skill text as a `.md` file.

## Limits

Cards support text prompts, choices, and text fields only: no free layout, images, animation, or live graphics. If the request needs those, say so in one line and offer the closest card-based version.

## Constants

No emoji. The user's language by default. Copyable text (prompts, code) goes in a `.md` file, not a code block. Dark mode for any visual UI.

## Delivery

The interaction happens in the cards. At the end, send a short text (at most 3 lines) with the final result or state, the name of the skill it was saved as, and how to reopen it in this AI.

## Optional run log

If your AI can write files, log every card shown, every answer verbatim, every action, and every file or skill saved, before acting on the answer, with start and end lines. Build the final result and the saved skill from the log.
