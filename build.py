#!/usr/bin/env python3
"""Build the static site from content/ into docs/ (GitHub Pages serves docs/).

No runtime services, no tracking, no JavaScript required. Needs: pip install markdown
"""
import html, os, re, shutil, datetime
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "docs")
SITE = "https://klanarongz2009-sketch.github.io/BlogPost"
REPO = "https://github.com/klanarongz2009-sketch/BlogPost"
TITLE = "BlogPost by Bogus"
TAGLINE = "Indie for indie"

NAV = [("Home", ""), ("About", "about/"), ("How I use AI", "how-i-use-ai/"),
       ("AI tools", "ai-tools/"), ("Skill library", "skills/"), ("MiniApps", "miniapps/"),
       ("Projects", "projects/"), ("Posts", "posts/"), ("Request", "request/"), ("ไทย", "th/")]

CSS = """:root{color-scheme:dark;--bg:#0d1117;--fg:#e6edf3;--mut:#9da7b3;--acc:#7cc4ff;--card:#161b22;--line:#30363d}
@media (prefers-color-scheme: light){:root.auto{color-scheme:light;--bg:#ffffff;--fg:#1f2328;--mut:#57606a;--acc:#0b63c5;--card:#f6f8fa;--line:#d0d7de}}
*{box-sizing:border-box}html{font-size:17px}body{margin:0;background:var(--bg);color:var(--fg);font:1rem/1.65 system-ui,-apple-system,"Segoe UI","Noto Sans Thai","Noto Sans",sans-serif}
a{color:var(--acc)}a:focus-visible{outline:3px solid var(--acc);outline-offset:2px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:var(--card);padding:6px 10px;z-index:9}
header,main,footer{max-width:46rem;margin:0 auto;padding:0 1rem}
header{padding-top:1.4rem;border-bottom:1px solid var(--line)}
.brand{font-size:1.35rem;font-weight:700;color:var(--fg);text-decoration:none}.tag{color:var(--mut);margin:.1rem 0 .8rem}
nav ul{list-style:none;display:flex;flex-wrap:wrap;gap:.3rem 1rem;padding:0;margin:0 0 .9rem}nav a{text-decoration:none}nav a[aria-current]{font-weight:700;text-decoration:underline}
main{padding-top:1rem;padding-bottom:2rem}h1{font-size:1.75rem;line-height:1.25}h2{font-size:1.3rem;margin-top:2rem}h3{font-size:1.08rem}
code{background:var(--card);padding:.1rem .3rem;border-radius:4px;font-size:.9em}pre{background:var(--card);padding:.8rem;border-radius:6px;overflow-x:auto;border:1px solid var(--line)}pre code{padding:0;background:none}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto}th,td{border:1px solid var(--line);padding:.35rem .55rem;text-align:left;vertical-align:top}
blockquote{margin:1rem 0;padding:.2rem 1rem;border-left:4px solid var(--acc);background:var(--card)}
.meta{color:var(--mut);font-size:.9rem}.posts{list-style:none;padding:0}.posts li{margin:.7rem 0}
footer{border-top:1px solid var(--line);padding:1rem;color:var(--mut);font-size:.9rem}"""


def parse(path):
    text = open(path, encoding="utf-8").read()
    meta = {}
    if text.startswith("---\n"):
        head, text = text[4:].split("\n---\n", 1)
        for line in head.splitlines():
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text


def md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "toc"])


def page(rel_out, title, body, lang="en", desc=""):
    depth = rel_out.count("/")
    base = "../" * depth
    cur = rel_out[:-len("index.html")]
    nav = "".join(
        f'<li><a href="{base}{href}"' + (' aria-current="page"' if href == cur else "") + f'>{name}</a></li>'
        for name, href in NAV)
    full = title if title == TITLE else f"{title} | {TITLE}"
    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc or TAGLINE + ': a blog by Bogus, an indie AI operator, for other indie makers.')}">
<link rel="alternate" type="application/rss+xml" title="{TITLE}" href="{base}feed.xml">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header>
<a class="brand" href="{base}">{TITLE}</a>
<p class="tag">{TAGLINE}. Notes from a solo indie maker who builds with AI agents, for other indie makers.</p>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</header>
<main id="main">
{body}
</main>
<footer>
<p>{TAGLINE}. Posts: <a href="{REPO}/blob/main/LICENSE-CONTENT">CC BY 4.0</a>. Skills and code: <a href="{REPO}/blob/main/LICENSE">MIT</a>, free and provided as is.
<a href="{REPO}/blob/main/PROJECT_NOTICE.md">Project notice</a> (<a href="{REPO}/blob/main/PROJECT_NOTICE.th.md">ไทย</a>): replies can be slow and the site may pause. Opinions are personal; nothing here is sponsored.
<a href="{base}feed.xml">RSS</a> · <a href="{REPO}">Source</a></p>
</footer>
</body>
</html>
"""
    path = os.path.join(OUT, rel_out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(doc)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    # posts
    posts = []
    pdir = os.path.join(SRC, "posts")
    for fn in sorted(os.listdir(pdir)):
        if not fn.endswith(".md"):
            continue
        meta, text = parse(os.path.join(pdir, fn))
        slug = fn[:-3]
        meta["slug"] = slug
        body = f'<article><h1>{html.escape(meta["title"])}</h1><p class="meta">{meta["date"]}</p>{md(text)}</article>'
        page(f"posts/{slug}/index.html", meta["title"], body, desc=meta.get("summary", ""))
        meta["html"] = md(text)
        posts.append(meta)
    posts.sort(key=lambda m: m["date"], reverse=True)

    def plist(base):
        return '<ul class="posts">' + "".join(
            f'<li><a href="{base}posts/{p["slug"]}/">{html.escape(p["title"])}</a> <span class="meta">{p["date"]}</span><br>{html.escape(p.get("summary", ""))}</li>'
            for p in posts) + "</ul>"

    # pages
    for fn in sorted(os.listdir(SRC)):
        p = os.path.join(SRC, fn)
        if fn.endswith(".md"):
            meta, text = parse(p)
            name = fn[:-3]
            out = "index.html" if name == "index" else f"{name}/index.html"
            body = md(text).replace("<p>{{POSTS}}</p>", plist("" if name == "index" else "../"))
            page(out, meta.get("title", TITLE), body, desc=meta.get("summary", ""))
    # Thai pages
    tdir = os.path.join(SRC, "th")
    for fn in sorted(os.listdir(tdir)):
        meta, text = parse(os.path.join(tdir, fn))
        name = fn[:-3]
        out = "th/index.html" if name == "index" else f"th/{name}/index.html"
        page(out, meta.get("title", TITLE), md(text), lang="th", desc=meta.get("summary", ""))

    posts_body = "<h1>Posts</h1>" + plist("../")
    page("posts/index.html", "Posts", posts_body)

    # RSS
    items = "".join(f"""<item><title>{html.escape(p['title'])}</title><link>{SITE}/posts/{p['slug']}/</link><guid>{SITE}/posts/{p['slug']}/</guid><pubDate>{datetime.datetime.strptime(p['date'], '%Y-%m-%d').strftime('%a, %d %b %Y 00:00:00 +0700')}</pubDate><description>{html.escape(p.get('summary', ''))}</description></item>""" for p in posts)
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>{TITLE}</title><link>{SITE}/</link><description>{TAGLINE}: notes from a solo indie maker who builds with AI agents.</description><language>en</language>{items}</channel></rss>
"""
    open(os.path.join(OUT, "feed.xml"), "w", encoding="utf-8").write(rss)

    # skills: copy raw SKILL.md files so they can be downloaded from the site too
    shutil.copytree(os.path.join(ROOT, "skills"), os.path.join(OUT, "skills-raw"))
    print("built", sum(len(f) for _, _, f in os.walk(OUT)), "files")


if __name__ == "__main__":
    main()
