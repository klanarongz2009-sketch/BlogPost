---
name: false-negative-guard
description: Use before reporting any negative result ("not found", "no results", "nothing changed", "does not exist", "none"). Re-checks with a second, different method so a failed or misdirected lookup is not reported as a confirmed negative.
---
# False negative guard

A negative result is easy to get wrong: the search errored, the page blocked bots, the query looked in the wrong place, or the data had not refreshed. This skill makes the agent prove a negative before it reports one.

## When to run

Every time a task is about to report that something is absent, empty, unchanged, or does not exist. Run it inside the task, before the report is written.

## Steps

1. **Write down the claim** in one line: what was looked for, where, and with which method.
2. **Check that the first method succeeded.** An error, a timeout, an HTTP 4xx/5xx, a login page, a rate limit, or a captcha is not an empty result. If the first method failed, the result is UNKNOWN, not NONE.
3. **Run a second method that differs in kind**, not just a retry:
   - file search by keyword -> list the directory, or search by another term, file name, or date;
   - web search -> fetch the source page directly, or check another source;
   - API returned empty -> confirm the status code and the query parameters, or check the web UI;
   - page fetch blocked -> fetch through another route or note that it is blocked.
4. **Widen once**: alternative spellings, other languages, other folders, the previous period.
5. **Decide** with exactly one status:
   - `CONFIRMED_NONE`: both methods succeeded and both found nothing.
   - `FOUND`: the second method found it. Report what was found and correct the first result.
   - `UNCONFIRMED`: a method failed or the two disagree. Say which and why.
6. **Report** the status, both methods, and their raw outcome (counts, status codes). Never write "none" for `UNCONFIRMED`.

## Output format

```
CLAIM = <what was looked for, where>
METHOD_1 = <method> -> <result, e.g. 0 matches / HTTP 200>
METHOD_2 = <method> -> <result>
STATUS = CONFIRMED_NONE | FOUND | UNCONFIRMED
NOTE = <one line, e.g. "site returned 403 to bots; not counted as broken">
```

## Rules

- Do not skip the guard because the first answer "looks obviously right".
- Do not invent a second method that is only the same call again.
- Keep the guard's own output short; it feeds the parent report.
