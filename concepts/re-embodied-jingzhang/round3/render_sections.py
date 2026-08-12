#!/usr/bin/env python3
"""Render three typological C01 urban sections as lightweight SVG.

CONCEPT / NOT OFFICIAL / NOT SITE-CALIBRATED / NOT CONSTRUCTION DRAWINGS
"""

from __future__ import annotations

import html
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"

SECTIONS = [
    {
        "file": "section-a-zhongzhiyuan.svg",
        "title": "A · Zhongzhiyuan — productive backend / 生产与验证后端",
        "question": "How can R&D, testing and repair coexist with public life, logistics and drainage?",
        "zones": [
            (50, 245, 205, 260, "#c9d6df", "Existing/adapted building", "ordinary R&D + service rooms"),
            (255, 330, 145, 175, "#9bc5d9", "Accountability front", "human help · state · stop"),
            (400, 345, 150, 160, "#f7c873", "Controlled handoff", "queue cap · supervised transfer"),
            (550, 275, 225, 230, "#e59866", "Two isolated cells", "general bay · recovery · shutdown A/B"),
            (775, 300, 170, 205, "#b47d66", "Specialised back-end", "separate store/wash/waste"),
            (945, 390, 205, 115, "#8fbf9f", "Drainage / landscape edge", "soil · canopy · overflow kept clear"),
        ],
        "ground": [
            (50, 550, 350, 52, "#d8e6d5", "ordinary pedestrian / cycle approach"),
            (400, 550, 375, 52, "#d5d8dc", "controlled court — no public through-route"),
            (775, 550, 175, 52, "#bfc5c8", "technical logistics"),
            (950, 550, 200, 52, "#a8d5ba", "drainage / canopy refuge"),
        ],
        "stress": "AI OFF: bays serve ordinary maintenance · CELL FAIL: independent shutdown + manual recovery · PEAK: refuse overflow, protect public path",
    },
    {
        "file": "section-b-ai-origin.svg",
        "title": "B · AI Origin — civic task and learning front / 公共任务与学习前台",
        "question": "How can optional AI service enter daily learning/community life without colonising it?",
        "zones": [
            (50, 245, 260, 260, "#d7d2c8", "Quiet learning/residential edge", "ordinary rooms above · no heavy backend"),
            (310, 330, 235, 175, "#a7c7e7", "Ordinary civic room", "human service · paper/phone · meeting"),
            (545, 365, 145, 140, "#f3cf7a", "Optional interface", "task script · status · complaint"),
            (690, 395, 135, 110, "#d99f7e", "Light local cell", "locker · safe return · offline stop"),
            (825, 420, 115, 85, "#aab7b8", "Back-of-house", "ordinary operations access"),
            (940, 350, 210, 155, "#9ac7a5", "Shade + public refuge", "accessible walk remains when closed"),
        ],
        "ground": [
            (50, 550, 260, 52, "#e4dfd6", "quiet threshold"),
            (310, 550, 380, 52, "#d8e6d5", "accessible ordinary public walk"),
            (690, 550, 250, 52, "#c9ccce", "small service access — no technical yard"),
            (940, 550, 210, 52, "#a8d5ba", "shade / rain refuge"),
        ],
        "stress": "AI OFF: civic room and route unchanged · 80% LOWER: remove locker/interface · DIGITAL DOWN: staffed paper/phone service",
    },
    {
        "file": "section-c-dazhongsi.svg",
        "title": "C · Dazhongsi — typological metropolitan adoption edge / 都市采用界面原型",
        "question": "How can arrival, commerce, service labour and temporary embodied services coexist?",
        "zones": [
            (50, 250, 260, 255, "#d5cbc0", "Commercial / enterprise building", "ordinary active ground floor"),
            (310, 345, 180, 160, "#9bc5d9", "Public help + exchange", "human fallback · visitor/service worker"),
            (490, 390, 140, 115, "#f4cf7a", "Small recovery room", "temporary holding · no heavy repair"),
            (630, 430, 150, 75, "#d8e6d5", "Arrival / refuge", "walking + accessible wait"),
            (780, 445, 180, 60, "#bfc5c8", "Managed curb", "ordinary loading / pick-up first"),
            (960, 405, 190, 100, "#d99f7e", "Temporary service staging", "event window · capped demand"),
        ],
        "ground": [
            (50, 550, 440, 52, "#e4dfd6", "active frontage / public help"),
            (490, 550, 290, 52, "#d8e6d5", "pedestrian priority + sheltered arrival"),
            (780, 550, 180, 52, "#c0c5c8", "managed curb / ordinary logistics"),
            (960, 550, 190, 52, "#b0b5b8", "service lane / manual recovery"),
        ],
        "stress": "TYPOLOGY ONLY · AI OFF: ordinary help/loading continue · EVENT: temporary overlay · CELL FAIL: remove equipment, no public repair",
    },
]


def text(x: int, y: int, value: str, size: int = 14, weight: int = 400, colour: str = "#263238") -> str:
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{colour}">{html.escape(value)}</text>'


def render(section: dict) -> str:
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="1200" height="720" fill="#f8f6f0"/>',
        text(50, 48, section["title"], 26, 700),
        text(50, 80, section["question"], 15, 400, "#546e7a"),
        '<line x1="50" y1="505" x2="1150" y2="505" stroke="#455a64" stroke-width="3"/>',
    ]
    for x, y, width, height, colour, label, detail in section["zones"]:
        out.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="5" fill="{colour}" stroke="#455a64" stroke-width="1.5"/>')
        out.append(text(x + 10, y + 25, label, 13, 700))
        out.append(text(x + 10, y + 47, detail, 11, 400, "#455a64"))
    for x, y, width, height, colour, label in section["ground"]:
        out.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{colour}" stroke="#78909c"/>')
        out.append(text(x + 8, y + 31, label, 11, 600))
    out += [
        '<rect x="50" y="625" width="1100" height="48" rx="6" fill="#fff3cd" stroke="#d6b656"/>',
        text(65, 655, section["stress"], 12, 700, "#6d4c41"),
        text(50, 700, "CONCEPT / NOT OFFICIAL / NOT SITE-CALIBRATED / NOT A CONSTRUCTION DRAWING", 11, 700, "#9b2c2c"),
        '</svg>',
    ]
    return "\n".join(out) + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for section in SECTIONS:
        (OUT / section["file"]).write_text(render(section), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
