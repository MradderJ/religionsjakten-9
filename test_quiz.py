#!/usr/bin/env python3
"""Sanity check / test for Religionsjakten 9.

Verifies the embedded question bank in index.html:
- exactly 200 questions
- all question texts are unique
- each has exactly 4 options
- answer index is in [0,3]
- mini-essay / mission / story-world elements have been removed
- no PyScript/Pyodide/CDN/Google Fonts/Fontshare references
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"

errors: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


def main() -> int:
    if not INDEX.exists():
        print("FAIL: index.html missing")
        return 1

    html = INDEX.read_text(encoding="utf-8")

    # 1) Extract embedded JSON question bank.
    match = re.search(r"var QUESTIONS=(\[.*?\]);", html, re.DOTALL)
    check(match is not None, "Could not locate QUESTIONS array in index.html")
    if match is None:
        print("\n".join("- " + e for e in errors))
        return 1

    try:
        questions = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        print(f"FAIL: QUESTIONS array is not valid JSON: {exc}")
        return 1

    # 2) Exactly 200.
    check(
        len(questions) == 200,
        f"Expected exactly 200 questions, got {len(questions)}",
    )

    # 3) Unique question texts.
    texts = [q.get("q", "") for q in questions]
    seen: dict[str, int] = {}
    duplicates: list[str] = []
    for t in texts:
        seen[t] = seen.get(t, 0) + 1
    for t, n in seen.items():
        if n > 1:
            duplicates.append(t)
    check(not duplicates, f"Duplicate question texts: {duplicates[:3]}")

    # 4) Structure: 4 options, answer index valid, fields populated.
    valid_modes = {"v", "e", "s", "k"}
    for i, q in enumerate(questions):
        check(
            isinstance(q.get("q"), str) and q["q"].strip() != "",
            f"Question {i} has empty/invalid text",
        )
        check(
            isinstance(q.get("o"), list) and len(q["o"]) == 4,
            f"Question {i} does not have exactly 4 options",
        )
        if isinstance(q.get("o"), list):
            for j, opt in enumerate(q["o"]):
                check(
                    isinstance(opt, str) and opt.strip() != "",
                    f"Question {i} option {j} is empty/invalid",
                )
        a = q.get("a")
        check(
            isinstance(a, int) and 0 <= a <= 3,
            f"Question {i} answer index out of range: {a}",
        )
        check(
            isinstance(q.get("w"), str) and q["w"].strip() != "",
            f"Question {i} missing explanation",
        )
        check(
            q.get("m") in valid_modes,
            f"Question {i} has invalid mode {q.get('m')}",
        )

    # 5) Mode coverage: all four categories must appear.
    mode_counts: dict[str, int] = {}
    for q in questions:
        m = q.get("m")
        if isinstance(m, str):
            mode_counts[m] = mode_counts.get(m, 0) + 1
    for required in valid_modes:
        check(
            mode_counts.get(required, 0) >= 10,
            f"Category '{required}' has too few questions ({mode_counts.get(required, 0)})",
        )

    # 6) Obsolete elements removed.
    obsolete_markers = [
        "essay-answer",
        "essay-check",
        "essay-prompt",
        "essay-feedback",
        "Mini-essä",
        "ESSAYS=",
        "Dagens uppdrag",
        "missions",
        "story",
        "Story",
        "PyScript",
        "pyscript",
        "pyodide",
        "Pyodide",
        "fontshare",
        "Fontshare",
        "fonts.googleapis",
        "cdn.jsdelivr",
        "unpkg.com",
    ]
    for marker in obsolete_markers:
        check(
            marker not in html,
            f"Obsolete element/dep still present: '{marker}'",
        )

    # 7) Required UI hooks present.
    required_ids = [
        'id="answers"',
        'id="question-text"',
        'id="next-question"',
        'id="streak"',
        'id="score"',
        'id="badges"',
        'id="summary"',
        'id="progress"',
        'id="mode-grid"',
    ]
    for rid in required_ids:
        check(rid in html, f"Missing required UI element: {rid}")

    # 8) No external resource references.
    bad_url_patterns = [
        r"https?://[^\"'\s>]*\.(?:js|css|woff2?|ttf|otf|eot)\b",
    ]
    for pat in bad_url_patterns:
        m = re.search(pat, html)
        check(m is None, f"External asset reference found: {m.group(0) if m else ''}")

    # Report
    if errors:
        print(f"FAIL: {len(errors)} issue(s):")
        for e in errors:
            print("  - " + e)
        return 1

    print("OK: 200 unique questions, structure valid, no obsolete elements, no external deps.")
    print(f"   Category distribution: {mode_counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
