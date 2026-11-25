"""Snooze Button Roast — a one-line roast of an alarm clock.

The joke treats the alarm clock as a litigant: after it wakes the sleeper
at 6 AM on a Saturday, the sleeper files a noise complaint against it, and
the alarm answers in kind, counter-suing over the nine minutes lost to
snoozing — the snooze button itself becomes the damages.
"""

import os

LINE = "My alarm rang at 6 AM on a Saturday, so I filed a noise complaint — it counter-sued me for the nine minutes I snoozed."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
