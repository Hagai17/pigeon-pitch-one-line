"""Pigeon Pitch, One Line — entry program.

The pitch is assembled from its three beats, in the order the judge's brief
rewards: (1) the premise — the pigeon's startup manufactures the fake owls
cities buy to scare pigeons off ledges; (2) the proof, delivered live — sales
are up and the founder is sitting on the product, which is also the best seat
in the park, paid for by the city; (3) the escalation — next quarter the
company sells the city a scarier owl, so the market for failing deterrents
never ends. Duel record: candidates.md.
"""

import os

BEATS = [
    "We manufacture the fake owls cities buy to scare pigeons off their ledges.",
    "Sales are up 300% — I'm sitting on one now, best seat in the park, and the city paid for it.",
    "Next quarter: a scarier owl.",
]

LINE = " ".join(BEATS)


def check_gate(text):
    """Mirror of the sealed gate: UTF-8 text of 1 to 200 characters, one
    line, not only whitespace. Fail loudly here rather than be listed
    invalid by the scorer."""
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip() == text and "\n" not in text, "entry must be one clean line"
    text.encode("utf-8")
    return text


def main():
    line = check_gate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
