"""Merge pending updates, build and publish the Nimble Fox breakage report.
Adapted from SCAR's tools/publish_report.py; this repo is its own GitHub Pages site.

    python tools/publish_report.py ["commit message"]

1. applies every updates/YYYY-MM-DD-*.md not yet listed in updates/APPLIED.txt (tools/merge_update.py)
2. builds index.html from REPORT.md (tools/build_report.py)
3. commits everything in the repo (updates, notes, builds too) and pushes main
   -> https://ohge-games.github.io/nimble-fox-breakage-report/ (Pages rebuilds in ~1 min)
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
URL = "https://ohge-games.github.io/nimble-fox-breakage-report/"
sys.path.insert(0, HERE)
from merge_update import pending


def git(*a):
    return subprocess.run(["git", "-C", ROOT] + list(a), capture_output=True, text=True)


todo = [os.path.basename(p) for p in pending()]
subprocess.run([sys.executable, os.path.join(HERE, "merge_update.py"), "--pending"], check=True)
subprocess.run([sys.executable, os.path.join(HERE, "build_report.py")], check=True)
git("add", "-A")
if git("status", "--porcelain").stdout.strip():
    msg = sys.argv[1] if len(sys.argv) > 1 else ("Report update: " + ", ".join(todo) if todo else "Report update")
    r = git("commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
    print(r.stdout, r.stderr)
elif not git("log", "-1", "--format=%H", "@{u}..").stdout.strip():
    print("no changes;", URL)
    sys.exit(0)
r = git("pull", "-q", "--rebase")
if r.returncode:
    sys.exit("pull --rebase failed, resolve and rerun:\n" + r.stderr)
r = git("push", "-q")
print(r.stdout, r.stderr)
if r.returncode:
    sys.exit("push failed")
print("published:", URL)
