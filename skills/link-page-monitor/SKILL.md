---
name: link-page-monitor
description: Use on a schedule or on request to check a link-in-bio page (such as Linktree) for links that were added, removed, renamed, broken, or redirected to a home page, compared with a saved baseline. Reports changes in plain language.
---
# Link page monitor

Link-in-bio pages break quietly: a game gets deleted, a profile redirects to a home page, a share link expires. This skill checks the page and every link on it.

## Inputs

- `PAGE_URL`: the public page, for example `https://linktr.ee/<your-handle>`.
- A folder for baselines, for example `link-monitor/`.

## Steps

1. **Fetch the page.** Link pages often block plain scripts (HTTP 403, 406, 429). Try in order and record which worked:
   1. a normal request with browser-like headers;
   2. a browser tool, if the agent has one;
   3. a free reader service that fetches the page from its own IP.
   If every route fails, report `FETCH_ERROR` and stop. Never report "no change" when the page was not read.
2. **Extract links**: title, URL, whether it is enabled, and its group or collection. Many pages embed this as JSON in the HTML (for Linktree, the `__NEXT_DATA__` script).
3. **Compare with the last baseline**, ignoring a single trailing `/` and tracking parameters:
   - `ADDED`, `REMOVED`, `RENAMED` (same URL, new title), `URL_CHANGED` (same title, new URL).
4. **Check each link**: follow redirects, record the final URL and status.
   - 200 -> OK;
   - 404 or 410 -> `BROKEN`;
   - final URL is just the site's home page while the link pointed deeper -> `REDIRECT_HOME` (the item was probably removed);
   - 403 or 429 -> `BLOCKED` (often bot protection; not counted as broken, re-check next run);
   - timeout or 5xx -> `ERROR`, re-check once.
5. **Save a new baseline** with the date, only after a successful fetch.
6. **Report**: a one-line summary first (for example "21 links, no changes, 18 OK, 3 blocked"), then each change or problem with title, URL, and status.

## Rules

- A link that was `BLOCKED` in one run and OK in the next is not broken.
- Before saying a link is broken, check it a second way (see the false-negative-guard skill).
- Read-only: the monitor never edits the link page.
