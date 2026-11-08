from __future__ import annotations
import datetime
from connstans import LOG_FILE

_entries: list[str] = []


def log_error(message: str) -> None:
    "Create journal error entry."
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{ts}] {message}"
    _entries.append(entry)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except OSError:
        pass


def get_entries() -> list[str]:
    "Return journal copy."
    return list(_entries)


def clear() -> None:
    "Clear journal"
    _entries.clear()