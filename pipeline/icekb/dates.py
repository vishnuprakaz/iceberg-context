"""Tolerant parsing of the date formats used in meeting notes and recording titles."""
from __future__ import annotations

import datetime as dt
import re

_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], start=1)}
_MON = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?"
_PATTERNS = [
    (re.compile(r"(20\d{2})[-/. ](\d{1,2})[-/.–— ](\d{1,2})"), "ymd"),
    (re.compile(_MON + r"\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(20\d{2})", re.I), "Mdy"),
    (re.compile(r"(\d{1,2})(?:st|nd|rd|th)?\s+" + _MON + r",?\s+(20\d{2})", re.I), "dMy"),
    (re.compile(r"(\d{1,2})[/. -](\d{1,2})[/. -](20\d{2})"), "mdy"),
]


def find_date(text: str) -> tuple[dt.date, int, int] | None:
    """Return (date, start, end) of the first date found in text, or None."""
    best = None
    for pattern, kind in _PATTERNS:
        m = pattern.search(text)
        if not m:
            continue
        g = m.groups()
        try:
            if kind == "ymd":
                d = dt.date(int(g[0]), int(g[1]), int(g[2]))
            elif kind == "Mdy":
                d = dt.date(int(g[2]), _MONTHS[g[0][:3].lower()], int(g[1]))
            elif kind == "dMy":
                d = dt.date(int(g[2]), _MONTHS[g[1][:3].lower()], int(g[0]))
            else:
                d = dt.date(int(g[2]), int(g[0]), int(g[1]))
        except (ValueError, KeyError):
            continue
        if best is None or m.start() < best[1]:
            best = (d, m.start(), m.end())
    return best
