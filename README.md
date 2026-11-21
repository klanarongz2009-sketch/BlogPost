# BlogPost by Bogus

**Indie for indie.** A blog by Bogus, a solo indie maker who builds with AI agents, written for other indie developers and creators.

[Read the site](https://klanarongz2009-sketch.github.io/BlogPost/) · [ภาษาไทย](https://klanarongz2009-sketch.github.io/BlogPost/th/) · [Request something](https://github.com/klanarongz2009-sketch/BlogPost/issues/new?template=request.yml) · [Project notice](PROJECT_NOTICE.md) ([ไทย](PROJECT_NOTICE.th.md))

## What is here

- **About** and **How I use AI**: sub-agents, memory files, verification, scheduled routines, Thai AI quality testing.
- **AI tools I use**: what I use each assistant or model for. Opinions, not endorsements; nothing is sponsored.
- **Free skill library** in [`skills/`](skills/): thirteen standalone `SKILL.md` files that work with any AI assistant or agent, MIT licensed.
- **MiniApps** and **Projects**: new apps built from scratch by different AIs (one AI per app), TER-AI, and Tagentic1.
- **Posts**, with an [RSS feed](https://klanarongz2009-sketch.github.io/BlogPost/feed.xml).

## Free skill library

| Skill | Use it to | Requires |
|---|---|---|
| [text-to-verbatim-prompt](skills/text-to-verbatim-prompt/SKILL.md) | make a prompt that lets another AI write a text out exactly, then compare | any AI |
| [auto-update-agent-memory](skills/auto-update-agent-memory/SKILL.md) | keep an AI's memory current on detection, not on a timer | writable memory |
| [ai-night-shift](skills/ai-night-shift/SKILL.md) | let an AI work unattended at night and log everything | a scheduler (or run manually) |
| [interactive-ui-in-chat](skills/interactive-ui-in-chat/SKILL.md) | build a working UI as question cards inside the chat | interactive cards (else a text menu) |
| [prompt-to-skill](skills/prompt-to-skill/SKILL.md) | turn a prompt you reuse into a skill, words unchanged | any AI |
| [agent-settings](skills/agent-settings/SKILL.md) | change your assistant's settings by typing plain language | a settings file |
| [subagent-creator-and-promptor](skills/subagent-creator-and-promptor/SKILL.md) | turn a prompt into a sub-agent spec, or a relay file for another AI | any AI |
| [tech-first-prompt-classifier](skills/tech-first-prompt-classifier/SKILL.md) | score any input on six dimensions and fix it | any AI |
| [terminal-in-chat](skills/terminal-in-chat/SKILL.md) | run shell commands from the chat | a real terminal |
| [text-to-voice-with-ai](skills/text-to-voice-with-ai/SKILL.md) | turn text into checked audio, free or local engines first | text-to-speech |
| [typing-analysis-sub-agent](skills/typing-analysis-sub-agent/SKILL.md) | read your messages through a personal typing profile | persistent files |
| [vm-control-panel](skills/vm-control-panel/SKILL.md) | control the AI's own machine from the chat | a VM or sandbox |

Only skills Bogus chose for other AIs are published; new skills suitable for other AIs are added after the same provider-neutral rewrite (see [skills/README.md](skills/README.md)).

**Install:** copy a skill folder into the skills folder your agent reads, or paste the `SKILL.md` contents into your assistant's custom skill or instructions. Details on the [skill library page](https://klanarongz2009-sketch.github.io/BlogPost/skills/).

## Requests

Open a [Request issue](https://github.com/klanarongz2009-sketch/BlogPost/issues/new?template=request.yml). A bot named **BlogPostIdeas** (an AI that runs on Wabi, not Bogus) may reply and passes the request to Bogus's AI assistant. Bogus may not act on it or reply soon. See the [project notice](PROJECT_NOTICE.md).

## Build the site locally

The site is plain static HTML built by one Python script, served by GitHub Pages from `docs/`. No tracking, no paid services.

```bash
pip install markdown
python build.py
```

Sources are in `content/` (pages, `posts/`, Thai pages in `th/`).

## License

- Skills, code, and `build.py`: [MIT](LICENSE).
- Posts and page text in `content/`: [CC BY 4.0](LICENSE-CONTENT).
- Product names and links belong to their owners.

Contributions: see [CONTRIBUTING](CONTRIBUTING.md).
