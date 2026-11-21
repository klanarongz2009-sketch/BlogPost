# BlogPost by Bogus

**Indie for indie.** A blog by Bogus, a solo indie maker who builds with AI agents, written for other indie developers and creators.

[Read the site](https://klanarongz2009-sketch.github.io/BlogPost/) · [ภาษาไทย](https://klanarongz2009-sketch.github.io/BlogPost/th/) · [Request something](https://github.com/klanarongz2009-sketch/BlogPost/issues/new?template=request.yml) · [Project notice](PROJECT_NOTICE.md) ([ไทย](PROJECT_NOTICE.th.md))

## What is here

- **About** and **How I use AI**: sub-agents, memory files, verification, scheduled routines, Thai AI quality testing.
- **AI tools I use**: what I use each assistant or model for. Opinions, not endorsements; nothing is sponsored.
- **Free skill library** in [`skills/`](skills/): eight standalone `SKILL.md` files for AI agents, MIT licensed.
- **MiniApps** and **Projects**: games and apps built on AI platforms, TER-AI, Tagentic1, and Klasster music.
- **Posts**, with an [RSS feed](https://klanarongz2009-sketch.github.io/BlogPost/feed.xml).

## Free skill library

| Skill | Use it to |
|---|---|
| [text-to-verbatim-prompt](skills/text-to-verbatim-prompt/SKILL.md) | make a prompt that lets another AI rebuild a text exactly, then compare |
| [tech-first-prompt-classifier](skills/tech-first-prompt-classifier/SKILL.md) | score any input on six dimensions and fix it |
| [false-negative-guard](skills/false-negative-guard/SKILL.md) | re-check every "not found" with a second method |
| [fact-checker](skills/fact-checker/SKILL.md) | verify claims against primary sources before publishing |
| [prompt-to-skill](skills/prompt-to-skill/SKILL.md) | turn a prompt you reuse into a skill, words unchanged |
| [md-sub-agent](skills/md-sub-agent/SKILL.md) | write, convert, and fix Markdown files |
| [task-watchdog](skills/task-watchdog/SKILL.md) | catch stuck agent tasks and false "done" claims |
| [link-page-monitor](skills/link-page-monitor/SKILL.md) | watch a link-in-bio page for broken or changed links |

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
