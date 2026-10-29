"""Build index.html from REPORT.md (5W cards, report stylesheet).
The page chrome (title, h1, facts, footer) comes from front matter, and the sections render
in source order.

    python tools/build_report.py [--check] [REPORT.md]

--check parses and validates without writing (the merge step uses it).

REPORT.md layout:
    --- front matter: title, h1, edition, subject, updated, facts (list), footer, status (optional banner)
    # Heading (not rendered), then the lede paragraph
    ## Current state {#state}     named sections above "## Index" render above the index
    ## Index                      | ID | Severity | Title | Status |, then ---
    ## N1. Card title
    **High. Why: confirmed.**
    - **Who:** ...                Who/What/When/Where/Why form the 5W list; any other
    - **Impact:** ...             "- **Field:**" (Impact, Mitigation, Status, Suggested fix...) goes below it.
    - **Update, 26 Oct (run):** ... any field starting "Update" is a dated note at the card's end.
    A card may also be (or end with) plain paragraphs and "- " lists after a blank line, in source order.
    ---
    ## What worked {#worked}      named sections below the cards render below them
    ## Changelog                  bullets, newest first
Inline markup: `code`, **bold**, [text](https://...), {{Fixed}} = status pill.
"""
import html, os, re, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from reportlib import CARD, SEVLINE, FIELD, read, chunks, heading, table_rows

args = [a for a in sys.argv[1:] if not a.startswith("--")]
CHECK = "--check" in sys.argv
SRC = args[0] if args else os.path.join(ROOT, "REPORT.md")
fm, md = read(SRC)
css = open(os.path.join(ROOT, "templates", "report.css"), encoding="utf-8").read()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
         '&family=IBM+Plex+Sans+Condensed:wght@500;600;700&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">')

SEV = {"critical": "crit", "high": "high", "medium": "med", "low": "low"}
W5 = ("Who", "What", "When", "Where", "Why")


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\{\{([^}]+)\}\}", r'<span class="status">\1</span>', t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"(https://[^\s<)]+)", lambda m: m.group(1) if 'href="' in t else '<a href="%s">%s</a>' % (m.group(1), m.group(1)), t)
    return t


def md_block(text):
    """Small markdown -> HTML for the named sections: ### headings, paragraphs (*...* = note),
    '- ' bullets with '  - ' sub-bullets, '1. ' numbered items with '   - ' sub-bullets, and tables."""
    out, lines, i = [], text.strip("\n").splitlines(), 0
    item = re.compile(r"^(- |\d+\. )")
    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == "---":
            i += 1
        elif l.startswith("### "):
            out.append("  <h3>%s</h3>" % inline(l[4:].strip()))
            i += 1
        elif l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.match(r"^:?-+:?$", c) for c in cells):
                    rows.append(cells)
                i += 1
            h = '  <div class="table-scroll"><table><thead><tr>%s</tr></thead><tbody>' % "".join("<th>%s</th>" % inline(c) for c in rows[0])
            h += "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in rows[1:])
            out.append(h + "</tbody></table></div>")
        elif item.match(l):
            tag = "ol" if l[0].isdigit() else "ul"
            items = []  # [text, [sub-bullets], [continuation paragraphs]]
            while i < len(lines) and (item.match(lines[i]) or lines[i].startswith("  ") or
                                      (not lines[i].strip() and i + 1 < len(lines) and lines[i + 1].startswith("  "))):
                x = lines[i]
                if item.match(x):
                    items.append([item.sub("", x), [], []])
                elif x.strip().startswith("- "):
                    items[-1][1].append(x.strip()[2:])
                elif x.strip():
                    items[-1][2].append(x.strip())
                i += 1
            h = ['  <%s class="plain">' % tag]
            for t, subs, cont in items:
                li = inline(t)
                if subs:
                    li += '<ul class="plain">%s</ul>' % "".join("<li>%s</li>" % inline(x) for x in subs)
                if cont:
                    li += "<p>%s</p>" % inline(" ".join(cont))
                h.append("    <li>%s</li>" % li)
            out.append("\n".join(h) + "\n  </%s>" % tag)
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(- |\d+\. |### |\|)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            t = " ".join(para)
            if t.startswith("*") and t.endswith("*") and not t.startswith("**"):
                out.append('  <p class="note">%s</p>' % inline(t[1:-1]))
            else:
                out.append("  <p>%s</p>" % inline(t))
    return "\n".join(out)


def field_html(v, subs, tail=""):
    h = inline(v) if v.strip() else ""
    if subs:
        h += '<ul class="plain">%s</ul>' % "".join("<li>%s</li>" % inline(x) for x in subs)
    if tail.strip():
        h += " " + inline(tail.strip())
    return h


def card(cid, title, body):
    body = "\n".join(l for l in body.splitlines() if l.strip() != "---")
    sevm = SEVLINE.search(body)
    sev = sevm.group(1) if sevm else "Medium"
    why = re.search(r"Why: (.+?)\.?\s*$", sevm.group(2)) if sevm else None
    conf = "Why: " + why.group(1) if why else ""
    after = body[sevm.end():] if sevm else body
    fields, extra, notes, blocks = [], [], [], []  # field: [key, text, sub-bullets, text after them]; block: ["p", text] or ["ul", items]
    cur, gap = None, True
    for line in after.splitlines():
        m = FIELD.match(line)
        if m:
            cur = [m.group(1), m.group(2), [], ""]
            (fields if cur[0] in W5 else notes if cur[0].startswith("Update") else extra).append(cur)
        elif not line.strip():
            cur, gap = None, True
            continue
        elif cur and line.startswith("  - "):
            cur[2].append(line.strip()[2:])
        elif cur and line.strip().startswith("|"):
            cur[1] += "\n" + line.strip()
        elif cur and cur[2]:
            cur[3] += " " + line.strip()
        elif cur:
            cur[1] += " " + line.strip()
        elif line.startswith("- "):
            if gap or not blocks or blocks[-1][0] != "ul":
                blocks.append(["ul", []])
            blocks[-1][1].append(line[2:].strip())
        elif blocks and blocks[-1][0] == "p" and not gap:
            blocks[-1][1] += " " + line.strip()
        else:
            blocks.append(["p", line.strip()])
        gap = False
    s = SEV[sev.lower()]
    h = ['  <article class="record %s" id="%s">' % (s, cid.lower()),
         '    <div class="rec-head"><span class="rec-id">%s</span><h3>%s</h3><span class="sev %s">%s</span><span class="conf">%s</span><a class="back" href="#index">↑ index</a></div>'
         % (cid, inline(title.strip()), s, sev, html.escape(conf))]
    if fields:
        h.append('    <dl class="w5">')
        h += ["      <dt>%s</dt><dd>%s</dd>" % (html.escape(k), field_html(v, subs, tail)) for k, v, subs, tail in fields]
        h.append("    </dl>")
    for kind, x in blocks:
        h.append("    <p>%s</p>" % inline(x) if kind == "p" else
                 '    <ul class="plain">%s</ul>' % "".join("<li>%s</li>" % inline(i) for i in x))
    if extra:
        h.append('    <div class="extra">')
        for k, v, subs, tail in extra:
            if "\n|" in v:  # a markdown table inside a field
                txt, _, tbl = v.partition("\n|")
                inner = ("<p>%s</p>" % inline(txt) if txt.strip() else "") + md_block("|" + tbl)
            else:
                inner = "<p>%s</p>" % field_html(v, subs, tail)
            h.append("      <div><h4>%s</h4>%s</div>" % (html.escape(k), inner))
        h.append("    </div>")
    # "- **Update, 26 Oct (recovery run):** ..." fields: dated notes at the end of the card
    h += ['    <div class="update"><p><b>%s:</b> %s</p></div>' % (inline(k), field_html(v, subs, tail)) for k, v, subs, tail in notes]
    h.append("  </article>")
    return sev, "\n".join(h)


def named(chunk):
    title, attrs = heading(chunk)
    sid = attrs.get("id") or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    cls = ' class="%s"' % attrs["class"] if attrs.get("class") else ""
    return '<section id="%s"%s>\n  <h2>%s</h2>\n%s\n</section>' % (sid, cls, inline(title), md_block(chunk.split("\n", 1)[1]))


# walk the chunks in source order
parts = chunks(md)
intro = [l.strip() for l in parts[0].splitlines() if l.strip() and not l.startswith("# ")]
above, below, cards, card_sev, idx_rows, log_html = [], [], [], {}, [], ""
seen_index = False
for c in parts[1:]:
    m = CARD.match(c.split("\n", 1)[0])
    title, _ = heading(c)
    if m:
        sev, h = card(m.group(1), m.group(2) or "", c.split("\n", 1)[1] if "\n" in c else "")
        card_sev[m.group(1)] = sev
        cards.append(h)
    elif title == "Index":
        seen_index = True
        idx_rows = [r for r in table_rows(c) if re.match(r"[A-Z]\d+$", r[0])]
    elif title == "Changelog":
        items = [l.strip()[2:] for l in c.splitlines() if l.strip().startswith("- ")]
        log_html = ('<section id="changelog">\n  <h2>Changelog</h2>\n  <ul class="changelog">\n%s\n  </ul>\n</section>'
                    % "\n".join("    <li>%s</li>" % inline(i) for i in items))
    else:
        (below if seen_index else above).append(named(c))

# every index row needs a card and vice versa, with the same severity
problems = []
idx_ids = [r[0] for r in idx_rows]
for r in idx_rows:
    if len(r) < 4:
        problems.append("index row %s has %d cells, needs 4" % (r[0], len(r)))
    elif r[0] not in card_sev:
        problems.append("index row %s has no card" % r[0])
    elif r[1] != card_sev[r[0]]:
        problems.append("%s: index says %s, card says %s" % (r[0], r[1], card_sev[r[0]]))
problems += ["card %s has no index row" % cid for cid in card_sev if cid not in idx_ids]
problems += ["duplicate ID %s" % cid for cid in set(idx_ids) if idx_ids.count(cid) > 1]
if problems:
    sys.exit("REPORT.md problems:\n  " + "\n  ".join(problems))
if CHECK:
    print("ok:", len(cards), "cards,", len(idx_rows), "index rows")
    sys.exit(0)

counts = {}
for r in idx_rows:
    counts[r[1]] = counts.get(r[1], 0) + 1
tally = " · ".join("%d %s" % (counts[k], k.lower()) for k in ("Critical", "High", "Medium", "Low") if k in counts)
updated = fm.get("updated") or datetime.datetime.now().strftime("%d %b %Y")
eyebrow = " · ".join(x for x in (fm.get("edition"), fm.get("subject"), "last updated " + updated) if x)
facts = "\n".join("    <span>%s <b>%s</b></span>" % (inline(k.strip()), inline(v.strip()))
                  for k, _, v in (f.partition(": ") for f in fm.get("facts", [])))
rows = "\n".join('        <tr><td class="mono">%s</td><td><span class="sev %s">%s</span></td><td><a href="#%s">%s</a></td><td>%s</td></tr>'
                 % (r[0], SEV.get(r[1].lower(), "med"), r[1], r[0].lower(), inline(r[2]), inline(r[3])) for r in idx_rows)
out = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title>
%s
<style>
%s</style>
</head><body>
<div class="wrap">
<header>
  <div class="eyebrow">%s · %d breakages (%s)</div>
  %s
  <h1>%s</h1>
  <p class="lede">%s</p>
  <div class="facts">
%s
  </div>
</header>
%s
<section id="index">
  <h2>Breakage index</h2>
  <div class="table-scroll"><table>
    <thead><tr><th>#</th><th>Severity</th><th>Breakage</th><th>Status</th></tr></thead>
    <tbody>
%s
    </tbody></table></div>
</section>
<section id="cards">
  <h2>The 5Ws, per breakage</h2>
%s
</section>
%s
%s
<footer class="mono">%s</footer>
</div></body></html>
""" % (html.escape(fm.get("title", "Breakage report")), FONTS, css, html.escape(eyebrow), len(idx_rows), tally,
       '<div class="final-status">%s</div>' % inline(fm["status"]) if fm.get("status") else "",
       inline(fm.get("h1", "")), inline(" ".join(intro)), facts, "\n".join(above), rows, "\n".join(cards),
       "\n".join(below), log_html, inline(fm.get("footer", "")))
dst = os.path.join(ROOT, "index.html")
open(dst, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", dst, len(out), "bytes,", len(cards), "cards,", len(idx_rows), "index rows")
