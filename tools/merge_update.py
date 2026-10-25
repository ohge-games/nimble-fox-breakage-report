"""Apply an update file (updates/YYYY-MM-DD-*.md) to REPORT.md.

    python tools/merge_update.py updates/2026-11-02-full-build.md [--dry-run] [--force]
    python tools/merge_update.py --pending [--dry-run]     every update not yet in updates/APPLIED.txt

An update file uses REPORT.md's own syntax. Each "## " chunk is one operation:
    front matter            scalar keys replace the report's (edition, subject, status...);
                            "updated" defaults to the file's date
    ## Index                table rows: an existing ID changes the cells you fill (leave a cell
                            empty or "-" to keep it); a new ID adds a row
    ## N27. Title           new ID: adds the card (it needs an index row too)
    ## N6 / ## N6. Title    existing ID: patch. A title replaces the title, a "**Sev. Why: ...**"
                            line replaces the severity line (and the index severity), each
                            "- **Field:**" replaces that field or adds it, other text is appended
                            as a paragraph
    ## N6. Title {replace}  existing ID: replaces the whole card
    ## Changelog            bullets go on top (newest first)
    ## Current state        any other section: replaces that section's body
    ## What worked {append} ...or appends to it; a section that doesn't exist yet is added before
                            the Changelog
REPORT.md is only written if the result passes tools/build_report.py --check.
"""
import datetime, difflib, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from reportlib import CARD, SEVLINE, FIELD, read, dump, chunks, heading, num, table_rows, row_line

REPORT = os.path.join(ROOT, "REPORT.md")
UPDATES = os.path.join(ROOT, "updates")
APPLIED = os.path.join(UPDATES, "APPLIED.txt")
NAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-.+\.md$")


def fail(msg):
    sys.exit("%s: %s" % (CURRENT, msg))


def split_sep(chunk):
    """-> (chunk without a trailing '---' separator, the separator text or '')"""
    m = re.search(r"\n---[ \t]*\n\s*$", chunk)
    return (chunk[:m.start()] + "\n", "\n---\n\n") if m else (chunk, "")


def field_blocks(lines):
    """Index ranges [start, end) of each '- **Field:**' line plus its sub-bullets / continuation lines."""
    out, i = {}, 0
    while i < len(lines):
        m = FIELD.match(lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip() and not FIELD.match(lines[j]) and \
                    (lines[j].startswith("  ") or lines[j].strip().startswith("|")):
                j += 1
            out[m.group(1)] = (i, j)
            i = j
        else:
            i += 1
    return out


def patch_card(old, title, body):
    core, sep = split_sep(old)
    lines = core.rstrip("\n").split("\n")
    cid = CARD.match(lines[0]).group(1)
    if title:
        lines[0] = "## %s. %s" % (cid, title)
    new_sev = None
    ulines = body.strip("\n").split("\n") if body.strip() else []
    blocks = field_blocks(ulines)
    taken = set()
    for k, (a, b) in blocks.items():
        taken.update(range(a, b))
    for i, l in enumerate(ulines):
        m = SEVLINE.match(l.strip())
        if m and m.end() == len(l.strip()):
            taken.add(i)
            new_sev = m.group(1)
            for j, ol in enumerate(lines):
                if SEVLINE.match(ol.strip()):
                    lines[j] = SEVLINE.sub(lambda _: m.group(0), ol, count=1)
                    break
            else:
                lines.insert(1, m.group(0))
    for k, (a, b) in blocks.items():
        have = field_blocks(lines)
        if k in have:
            s, e = have[k]
            lines[s:e] = ulines[a:b]
        else:
            last = max((e for s, e in have.values()), default=None)
            if last is None:
                lines += [""] + ulines[a:b]
            else:
                lines[last:last] = ulines[a:b]
    rest = "\n".join(l for i, l in enumerate(ulines) if i not in taken).strip()
    if rest:
        lines += ["", rest]
    return "\n".join(lines) + "\n" + (sep or "\n"), new_sev


def find(parts, pred):
    return next((i for i, c in enumerate(parts) if i and pred(c)), None)


def apply(path, dry=False):
    global CURRENT
    CURRENT = os.path.basename(path)
    m = NAME.match(CURRENT)
    if not m:
        fail("update files are named YYYY-MM-DD-what.md")
    date = datetime.date(*map(int, m.groups()))
    ufm, ubody = read(path)
    fm, body = read(REPORT)
    parts = chunks(body)
    uparts = chunks(ubody)
    if uparts[0].strip() and not uparts[0].lstrip().startswith("# "):
        fail("text before the first '## ' heading: %r" % uparts[0].strip()[:60])

    fm["updated"] = ufm.pop("updated", "%d %s" % (date.day, date.strftime("%b %Y")))
    fm.update(ufm)

    idx = find(parts, lambda c: heading(c)[0] == "Index")
    sev_changes, sev_in_index = {}, set()
    for uc in uparts[1:]:
        title, attrs = heading(uc)
        ubody_ = uc.split("\n", 1)[1] if "\n" in uc else ""
        cm = CARD.match(uc.split("\n", 1)[0].split(" {")[0].rstrip())
        if title == "Index":
            core, sep = split_sep(parts[idx])
            lines = core.rstrip("\n").split("\n")
            for cells in table_rows(ubody_):
                cells += [""] * (4 - len(cells))
                if cells[1] and cells[1] != "-":
                    sev_in_index.add(cells[0])
                row = next((i for i, l in enumerate(lines) if l.startswith("| %s |" % cells[0])), None)
                if row is not None:
                    have = table_rows(lines[row])[0]
                    lines[row] = row_line([c if c and c != "-" else h for c, h in zip(cells, have)])
                else:
                    if not all(cells[:4]) or "-" in cells[:4]:
                        fail("new index row %s needs all four cells" % cells[0])
                    rows = [i for i, l in enumerate(lines) if re.match(r"\| [A-Z]\d+ \|", l)]
                    after = max([i for i in rows if num(table_rows(lines[i])[0][0]) < num(cells[0])] or [rows[0] - 1])
                    lines.insert(after + 1, row_line(cells[:4]))
            parts[idx] = "\n".join(lines) + "\n" + (sep or "\n")
        elif cm:
            cid, ctitle = cm.group(1), cm.group(2)
            i = find(parts, lambda c: (CARD.match(c.split("\n", 1)[0]) or [None, None])[1] == cid)
            text = re.sub(r"\s*\{replace\}\s*$", "", uc.split("\n", 1)[0]) + "\n" + ubody_.strip("\n") + "\n"
            if i is not None and attrs.get("replace"):
                core, sep = split_sep(parts[i])
                parts[i] = text + (sep or "\n")
            elif i is not None:
                parts[i], sev = patch_card(parts[i], ctitle, ubody_)
                if sev:
                    sev_changes[cid] = sev
            else:
                if not ctitle:
                    fail("new card %s needs a title" % cid)
                cards = [j for j, c in enumerate(parts) if j and CARD.match(c.split("\n", 1)[0])]
                before = [j for j in cards if num(CARD.match(parts[j].split("\n", 1)[0]).group(1)) < num(cid)]
                at = (max(before) if before else cards[0] - 1) + 1
                sep = "\n"
                if at - 1 == cards[-1]:  # new last card: move the closing separator below it
                    core, sep = split_sep(parts[at - 1])
                    parts[at - 1] = core.rstrip("\n") + "\n\n"
                parts.insert(at, text + (sep or "\n"))
        elif title == "Changelog":
            i = find(parts, lambda c: heading(c)[0] == "Changelog")
            head, _, rest = parts[i].partition("\n")
            parts[i] = head + "\n" + ubody_.strip("\n") + "\n" + rest.lstrip("\n")
        else:
            i = find(parts, lambda c: heading(c)[0].lower().startswith(title.lower()) and not CARD.match(c.split("\n", 1)[0]))
            if i is None:
                at = find(parts, lambda c: heading(c)[0] == "Changelog") or len(parts)
                hline = re.sub(r"\s*\{append\}", "", uc.split("\n", 1)[0])
                parts.insert(at, hline + "\n" + ubody_.strip("\n") + "\n\n")
            elif attrs.get("append"):
                parts[i] = parts[i].rstrip("\n") + "\n" + ubody_.strip("\n") + "\n\n"
            else:
                parts[i] = parts[i].split("\n", 1)[0] + "\n" + ubody_.strip("\n") + "\n\n"

    # a severity changed on a card follows into the index unless the update set it there
    sev_changes = {k: v for k, v in sev_changes.items() if k not in sev_in_index}
    if sev_changes:
        core, sep = split_sep(parts[idx])
        lines = core.rstrip("\n").split("\n")
        for i, l in enumerate(lines):
            r = table_rows(l)
            if r and r[0][0] in sev_changes:
                r[0][1] = sev_changes[r[0][0]]
                lines[i] = row_line(r[0])
        parts[idx] = "\n".join(lines) + "\n" + (sep or "\n")

    new = dump(fm, "".join(parts))
    tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8", newline="\n")
    tmp.write(new)
    tmp.close()
    r = subprocess.run([sys.executable, os.path.join(HERE, "build_report.py"), "--check", tmp.name], capture_output=True, text=True)
    os.unlink(tmp.name)
    if r.returncode:
        fail("result does not validate, REPORT.md left unchanged\n" + (r.stderr or r.stdout))
    old = open(REPORT, encoding="utf-8").read()
    if dry:
        sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), new.splitlines(True), "REPORT.md", "REPORT.md (+%s)" % CURRENT))
        return
    open(REPORT, "w", encoding="utf-8", newline="\n").write(new)
    with open(APPLIED, "a", encoding="utf-8", newline="\n") as f:
        f.write(CURRENT + "\n")
    print("applied", CURRENT)


def applied():
    return set(open(APPLIED, encoding="utf-8").read().split()) if os.path.exists(APPLIED) else set()


def pending():
    done = applied()
    return [os.path.join(UPDATES, n) for n in sorted(os.listdir(UPDATES)) if NAME.match(n) and n not in done]


CURRENT = ""
if __name__ == "__main__":
    sys.stdout.reconfigure(errors="replace")
    dry, force = "--dry-run" in sys.argv, "--force" in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--pending" in sys.argv:
        files = pending()
        if not files:
            print("no pending updates")
    elif not files:
        sys.exit(__doc__)
    for p in files:
        if os.path.basename(p) in applied() and not force:
            sys.exit("%s is already applied (see updates/APPLIED.txt); --force to apply again" % os.path.basename(p))
        apply(p, dry)
