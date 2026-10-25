"""Shared parsing for REPORT.md and update files (front matter, ## chunks, the index table)."""
import re

CARD = re.compile(r"^## ([A-Z]\d+)(?:\. (.*))?$")
SEVLINE = re.compile(r"\*\*(Critical|High|Medium|Low)\b([^*]*)\*\*")
FIELD = re.compile(r"^- \*\*([^:*]+):\*\*\s*(.*)$")


def read(path):
    """-> (front matter dict, body). 'key: value' lines between --- fences; a key with no value
    takes '  - item' lines as a list (facts)."""
    text = open(path, encoding="utf-8").read()
    fm, body = {}, text
    if text.startswith("---\n"):
        head, _, body = text[4:].partition("\n---\n")
        key = None
        for line in head.splitlines():
            if line.startswith("  - ") and isinstance(fm.get(key), list):
                fm[key].append(line[4:].strip())
            elif ":" in line:
                key, _, v = line.partition(":")
                key, v = key.strip(), v.strip()
                fm[key] = v if v else []
    return fm, body


def dump(fm, body):
    out = ["---"]
    for k, v in fm.items():
        out += ["%s:" % k] + ["  - %s" % x for x in v] if isinstance(v, list) else ["%s: %s" % (k, v)]
    return "\n".join(out) + "\n---\n" + body


def chunks(body):
    """Split at '## ' headings. chunks[0] is the preamble; every other chunk starts with its heading
    line and keeps its text exactly, so "".join(chunks) == body."""
    return re.split(r"(?m)^(?=## (?!#))", body)


def heading(chunk):
    """'## Current state {#state .x}' -> ('Current state', {'id': 'state', 'class': 'x'})"""
    line = chunk.split("\n", 1)[0][3:].strip()
    attrs = {}
    m = re.match(r"(.*?)\s*\{([^}]*)\}$", line)
    if m:
        line = m.group(1)
        for tok in m.group(2).split():
            if tok.startswith("#"):
                attrs["id"] = tok[1:]
            elif tok.startswith("."):
                attrs["class"] = (attrs.get("class", "") + " " + tok[1:]).strip()
            else:
                attrs[tok] = True
    return line, attrs


def num(cid):
    return int(re.sub(r"\D", "", cid))


def table_rows(text):
    """Markdown table rows as cell lists, without the header and |---| rows."""
    rows = []
    for line in text.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells[0] != "ID" and not all(re.match(r"^:?-+:?$", c) for c in cells):
                rows.append(cells)
    return rows


def row_line(cells):
    return "| " + " | ".join(cells) + " |"
