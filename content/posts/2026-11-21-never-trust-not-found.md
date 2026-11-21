---
title: Never trust "not found" from an agent
date: 2026-11-21
summary: Why I run a second check on every negative result, and the free skill that does it.
---
An agent that says "done" can be checked: open the file, run the test. An agent that says "not found" is harder. Nothing appears, so nothing looks wrong.

In my own logs I found reports that said "no information found" without any second check. Some negatives are real. Some come from a search that errored, a page that blocked bots, or a query that looked in the wrong place. A tool that fails is not a tool that returned nothing.

## The rule

Before an agent reports a negative ("no results", "nothing changed", "does not exist"), it re-checks with a **different method**:

- searched by keyword? also list the folder, or search by a different term;
- a web page returned nothing? fetch it another way, or check another source;
- an API returned empty? confirm the request actually succeeded.

Only when both methods agree does the report say "confirmed none". If they disagree, the report says so.

## Example

My link-page monitor once got HTTP 403 from three music links. A naive report would call them broken. The second check pointed to the site blocking automated requests, not to broken pages, so the report said "unconfirmed" instead of "broken". In a later check the same links returned 200.

## Take it

The [false-negative-guard](../../skills/) skill is free (MIT). Drop it into your agent's skills folder. Pair it with [fact-checker](../../skills/) for positive claims.
