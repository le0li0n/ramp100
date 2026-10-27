#!/usr/bin/env python3
"""Mechanical checks for the brain's rules in AGENTS.md. Exits 1 if any check fails.

Errors (fail the run):
  line-limit   rule 4: markdown files stay under 150 lines
  links        every relative markdown link points to a file that exists
Warnings (printed for review; fail only with --strict, because they rely on heuristics):
  sourcing     rule 3: a figure (%, $, range, count of people) has a source tag on its line or in its block
  duplicates   rule 1: the same range or figure appears in several files

Paraphrased copies still need judgment, which is what the brain-review skill is for.
Run from anywhere: python3 scripts/check_brain.py [--only line-limit,links] [--strict]
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_LINES = 150
# Brain files that hold facts. outputs/, examples/ and _inbox/ are generated or raw.
FACT_DIRS = ["context", "knowledge"]
LINE_LIMIT_PATHS = ["AGENTS.md", "context", "knowledge", "skills"]
LINK_PATHS = ["AGENTS.md", "README.md", "EXERCISES.md", "context", "knowledge", "skills"]
SKIP_FILES = {"knowledge/log.md"}  # append-only history, dates are not claims

TAG = re.compile(r"\[(source:[^\]]*|stated by user|assumption)\]|TODO", re.I)
DATE = re.compile(r"\b\d{4}-\d{2}(?:-\d{2})?\b")
FIGURE = re.compile(
    r"\$\d|\b\d[\d,.]*\s*%|\b\d[\d,]*\+|\b\d[\d,]*\s*(?:to|-|–)\s*\d"
    r"|\b\d[\d,]*\s*(?:employees|users|days|accounts|customers|people|opportunities|months|weeks)\b",
    re.I,
)
URL = re.compile(r"https?://")
RANGE = re.compile(r"\b\d[\d,]*(?:\.\d+)?\s*(?:to|-|–)\s*\d[\d,]*(?:\.\d+)?%?|\$\d[\d,.]*[KMB]?\+?|\b\d+%")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def md_files(paths):
    for p in paths:
        path = ROOT / p
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from sorted(path.rglob("*.md"))


def rel(path):
    return str(path.relative_to(ROOT))


def body_lines(path):
    """Yield (line number, text) outside code fences, front matter and headings."""
    in_fence = False
    in_front = False
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if n == 1 and line.strip() == "---":
            in_front = True
            continue
        if in_front:
            in_front = line.strip() != "---"
            continue
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or line.startswith("#") or not line.strip():
            continue
        if re.fullmatch(r"[\s|:-]+", line):  # table separator row
            continue
        yield n, line


def check_line_limit():
    problems = []
    for f in md_files(LINE_LIMIT_PATHS):
        n = len(f.read_text().splitlines())
        if n > MAX_LINES:
            problems.append(f"{rel(f)}: {n} lines (limit {MAX_LINES})")
    return problems


def blocks(path):
    """Group body lines into blocks: runs of consecutive non-blank lines (a table, a paragraph, a list)."""
    block, last = [], None
    for n, line in body_lines(path):
        if last is not None and n != last + 1:
            yield block
            block = []
        block.append((n, line))
        last = n
    if block:
        yield block


def check_sourcing():
    problems = []
    for f in md_files(FACT_DIRS):
        if rel(f) in SKIP_FILES:
            continue
        for block in blocks(f):
            block_tagged = any(TAG.search(line) for _, line in block)
            for n, line in block:
                text = DATE.sub("", line)
                if FIGURE.search(text) and not block_tagged and not TAG.search(line) and not URL.search(line):
                    problems.append(f"{rel(f)}:{n}: figure without a source tag: {line.strip()[:90]}")
    return problems


def check_duplicates():
    seen = defaultdict(set)
    for f in md_files(FACT_DIRS):
        if rel(f) in SKIP_FILES:
            continue
        for _, line in body_lines(f):
            for m in RANGE.finditer(DATE.sub("", line)):
                key = re.sub(r"\s+", " ", m.group(0).lower().replace("–", "-").replace(" to ", "-").replace(" ", ""))
                seen[key].add(rel(f))
    return [
        f"'{k}' appears in {len(files)} files: {', '.join(sorted(files))}"
        for k, files in sorted(seen.items())
        if len(files) > 1
    ]


def check_links():
    problems = []
    for f in md_files(LINK_PATHS):
        for n, line in body_lines(f):
            for target in LINK.findall(line):
                if re.match(r"[a-z]+:", target) or target.startswith("#"):
                    continue
                path = target.split("#")[0]
                if path and not (f.parent / path).exists():
                    problems.append(f"{rel(f)}:{n}: broken link: {target}")
    return problems


CHECKS = {
    "line-limit": (check_line_limit, True),
    "links": (check_links, True),
    "sourcing": (check_sourcing, False),
    "duplicates": (check_duplicates, False),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated checks to run: " + ", ".join(CHECKS))
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()
    names = args.only.split(",") if args.only else list(CHECKS)
    unknown = [n for n in names if n not in CHECKS]
    if unknown:
        sys.exit(f"unknown check: {', '.join(unknown)}")

    failed = False
    for name in names:
        check, is_error = CHECKS[name]
        problems = check()
        label = "FAIL" if problems and (is_error or args.strict) else "warn" if problems else "ok  "
        print(f"{label} {name}" + (f" ({len(problems)})" if problems else ""))
        for p in problems:
            print(f"     {p}")
        failed = failed or (bool(problems) and (is_error or args.strict))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
