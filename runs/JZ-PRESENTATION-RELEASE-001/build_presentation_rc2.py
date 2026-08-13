#!/usr/bin/env python3
"""Deterministic, presentation-only RC2 builder for Jing-Zhang In Place.

This run-local builder deliberately reads the already-certified package truth and
writes only declared presentation surfaces: the paired core figures, paired
offline visual narratives and paired A3/A0 PDFs.  It never calls the historic
fact/geometry/proposal builders and therefore cannot change design semantics.
"""

from __future__ import annotations

import html
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from shapely.geometry import shape


RUN = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(r"V:\src\haidian\submissions\JerrySkywalker\jingzhang-in-place")
HISTORIC = Path(r"V:\src\_worktrees\JZ-FORMAL-DEPTH-CLOSURE-001\runs\JZ-FORMAL-DEPTH-CLOSURE-001\build_formal_package.py")
FIG = ROOT / "assets" / "figures"
VISUAL = ROOT / "visual"
DRAWINGS = ROOT / "drawings"


def _load_primitives():
    spec = importlib.util.spec_from_file_location("jingzhang_rc1_primitives", HISTORIC)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Historic RC1 primitive module is unavailable: {HISTORIC}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Its guarded main is not invoked.  Rebinding avoids accidental output paths.
    module.ROOT = ROOT
    module.FIG = FIG
    module.VISUAL = VISUAL
    module.DRAWINGS = DRAWINGS
    return module


m = _load_primitives()

PAPER = m.PAPER
WHITE = m.WHITE
INK = m.INK
NAVY = m.NAVY
GREEN = m.GREEN
TEAL = m.TEAL
AMBER = m.AMBER
MAGENTA = m.MAGENTA
SLATE = m.SLATE
ACCENT = m.ACCENT
PALE_BLUE = m.PALE_BLUE
PALE_GREEN = m.PALE_GREEN
PALE_AMBER = m.PALE_AMBER
PALE_MAGENTA = m.PALE_MAGENTA

W, H = 3600, 2250

ACTION_ZH = {
    "RETAIN": "保留",
    "REPAIR": "修复",
    "OPEN_EDGE": "打开边界",
    "SUBDIVIDE_RECONNECT": "细分／重连",
    "ADAPT": "适应性更新",
    "INFILL": "条件性填补",
    "INFILL_CONDITIONAL": "条件性填补",
    "SURVEY": "调查后决定",
    "SURVEY_REQUIRED": "调查后决定",
    "ALIGN": "先对齐证据",
}
ACTION_EN = {
    "RETAIN": "RETAIN",
    "REPAIR": "REPAIR",
    "OPEN_EDGE": "OPEN EDGE",
    "SUBDIVIDE_RECONNECT": "SUBDIVIDE / RECONNECT",
    "ADAPT": "ADAPT",
    "INFILL": "INFILL",
    "INFILL_CONDITIONAL": "CONDITIONAL INFILL",
    "SURVEY": "SURVEY FIRST",
    "SURVEY_REQUIRED": "SURVEY FIRST",
    "ALIGN": "ALIGN EVIDENCE",
}
AREA_ZH = {"north": "众智园", "middle": "AI 原点", "south": "大钟寺", "overall": "总体场"}
AREA_EN = {"north": "ZHONGZHIYUAN", "middle": "AI ORIGIN", "south": "DAZHONGSI", "overall": "WHOLE FIELD"}

PATCH_ZH = {
    "P-N1": ("清河到达与院区边界", "到达前场／遮阴等候／可读服务边"),
    "P-N2": ("水岸公共项目接口", "软边界／维护门／防涝与避暑"),
    "P-N3": ("生产性院区验证载体", "需任务、调查、消防与权属确认后才可受控验证"),
    "P-N4": ("水—院区安静界面", "遮阴、停留、安静缓冲；不预设滨水新建"),
    "P-N5": ("可适应遗存／公共空间边", "保留载体，打开可确认的公共边"),
    "P-M1": ("校园公开侧阈值", "城市公共路在校园外侧；预约进入不能替代公共路"),
    "P-M2": ("公园与社区服务界面", "雨天停留、无障碍与日常服务"),
    "P-M3": ("公共项目边界修复", "确认交付状态后再接入公共边"),
    "P-M4": ("公开侧普通房间／庭院", "普通学习与社区使用优先；无差异即不新建"),
    "P-M5": ("创新社区受控协作边", "公共学习边—临时受控项目房—可复位服务"),
    "P-S1": ("站城到达与四向可达", "到达判读、无障碍与人工帮助"),
    "P-S2": ("立体交通连续性审计", "先查地面／下穿／桥接连续性；不虚构桥隧"),
    "P-S3": ("混合临街更新界面", "活跃首层、安静上层、可见服务；不默认新建"),
    "P-S4": ("专业采用与责任界面", "有人员的采用／合规评审与转介"),
    "P-S5": ("普通城市安静边", "日常商业、遮阴与安静回家；不新建"),
    "P-C1": ("公园项目接口", "低遗憾修复与维护协同"),
    "P-C2": ("服务与活动状态场", "配送、清洁、维护与活动复位"),
}

PROJECT_ZH = {
    "PRJ-01": "证据与项目接口登记", "PRJ-02": "全时无障碍审计", "PRJ-03": "清河到达修复",
    "PRJ-04": "水岸与公园维护接口", "PRJ-05": "验证载体调查", "PRJ-06": "一项可撤验证试点",
    "PRJ-07": "公开侧房间与学习阈值", "PRJ-08": "可撤受控协作状态", "PRJ-09": "公园／公共项目阈值修复",
    "PRJ-10": "站城可达场审计", "PRJ-11": "混合临街连续性复核", "PRJ-12": "有人员采用／责任界面",
    "PRJ-13": "服务与活动状态规程", "PRJ-14": "适应性更新候选审查", "PRJ-15": "经需求证明后的填补与运营修订",
}

SCENARIO_ZH = {
    "S01": "有限物理模型／设备验证", "S02": "真实环境稳健性验证", "S03": "有人参与的安全评估",
    "S04": "限时受控项目房", "S05": "开放学习与模型说明", "S06": "人才与社区服务协同",
    "S07": "有人员的采用／合规评审", "S08": "无障碍换乘协助", "S09": "公园维护与雨后巡检",
    "S10": "无障碍设施状态告知", "S11": "活动容量与安静边界管理", "S12": "证据状态变更复核",
}

PERSONA_ZH = {
    "PERS-01": "居民与沿街商户：步行、购物、收货与休息；数字失效仍有固定导视与人工帮助。",
    "PERS-02": "儿童与照护者：短距离游戏、学习与等候；需要可见、安静的公共阈值。",
    "PERS-03": "老年人与无障碍敏感使用者：连续无障碍路、座椅、厕所与雨天绕行。",
    "PERS-04": "学生与研究人员：在公开侧学习、会面与转换；受控空间只能预约进入。",
    "PERS-05": "企业与独立工作者：专业服务与采用评审，但不依赖强制活动状态。",
    "PERS-06": "维护、配送与清洁人员：服务、装卸、废弃物与复位工作保持可见、安全。",
    "PERS-07": "访客与区域通勤者：到达、辨路、换乘与休息；离线时仍有物理备选路径。",
    "PERS-08": "公共项目与运营人员：协调施工、开放、维护与反馈；保有停／行权限。",
}

PERSONA_EN = {
    "PERS-01": "Residents and street-front merchants: walk, shop, receive goods and rest; fixed signs and staffed help remain when digital services are down.",
    "PERS-02": "Children and caregivers: short-step play, learning and waiting through a visible, calm public threshold.",
    "PERS-03": "Older people and access-sensitive users: step-free routes, seating, toilets and a dry weather detour.",
    "PERS-04": "Students and researchers: learn and meet on the public side; controlled rooms remain scheduled rather than becoming public routes.",
    "PERS-05": "Companies and independent workers: receive professional service and adoption review without dependence on event state.",
    "PERS-06": "Maintenance, delivery and cleaning workers: retain visible, safe servicing, loading, waste and reset work.",
    "PERS-07": "Visitors and regional commuters: arrive, orient, transfer and rest with physical alternatives when digital services are down.",
    "PERS-08": "Public-project and operations staff: coordinate works, opening, maintenance and feedback while retaining STOP / GO authority.",
}


def read_json(rel: str) -> Any:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def features(rel: str) -> list[dict[str, Any]]:
    return read_json(rel)["features"]


def draw_text(d: ImageDraw.ImageDraw, xy, value: str, size: int, zh: bool, fill=INK, bold=False, anchor=None):
    m.draw_text(d, xy, value, size, zh, fill, bold, anchor)


def wrap(text: str, limit: int) -> list[str]:
    return m.wrap(text, limit)


def draw_wrapped(d, x, y, value: str, size: int, zh: bool, limit: int, fill=INK, leading: int | None = None, bold=False):
    leading = leading or int(size * 1.34)
    for line in wrap(value, limit):
        draw_text(d, (x, y), line, size, zh, fill, bold)
        y += leading
    return y


def language(lang: str) -> bool:
    return lang == "zh"


def l(lang: str, zh: str, en: str) -> str:
    return zh if language(lang) else en


def status_name(status: str, lang: str) -> str:
    return (m.STATUS_NAMES_ZH if language(lang) else m.STATUS_NAMES_EN)[status]


def action_name(action: str, lang: str) -> str:
    return (ACTION_ZH if language(lang) else ACTION_EN).get(action, action)


def area_name(area: str, lang: str) -> str:
    return (AREA_ZH if language(lang) else AREA_EN)[area]


def figure_base(lang: str, number: str, title: str, subtitle: str):
    zh = language(lang)
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 28), fill=ACCENT)
    draw_text(d, (110, 86), "京张续城" if zh else "Jing-Zhang In Place", 62, zh, NAVY, True)
    draw_text(d, (112, 162), l(lang, "在地续城 · 状态 × 行动", "IN-PLACE RENEWAL · STATUS × ACTION"), 26, zh, SLATE)
    draw_text(d, (W - 110, 103), number, 24, False, MAGENTA, True, "ra")
    draw_text(d, (110, 245), title, 52, zh, NAVY, True)
    draw_text(d, (112, 318), subtitle, 25, zh, SLATE)
    d.line((110, 362, W - 110, 362), fill="#CCD6D7", width=3)
    return im, d


def footer(d, lang: str, page_note: str | None = None):
    note = page_note or l(lang, "概念／临时范围｜非地块、非红线、非工程结论", "CONCEPT / PROVISIONAL EXTENT | NOT PARCEL, REDLINE OR ENGINEERING CONCLUSION")
    draw_text(d, (110, H - 70), note, 20, language(lang), MAGENTA, True)
    draw_text(d, (W - 110, H - 70), l(lang, "RC2 · 本地确定性导出 · 2026-08-14", "RC2 · deterministic offline export · 2026-08-14"), 18, language(lang), SLATE, False, "ra")


def panel(d, box: tuple[int, int, int, int], color: str = NAVY, fill: str = WHITE, radius: int = 22, width: int = 3):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=color, width=width)


def draw_lines(d, points, fill, width, dash: bool = False):
    if not dash:
        d.line(points, fill=fill, width=width, joint="curve")
        return
    for a, b in zip(points[:-1], points[1:]):
        ax, ay = a; bx, by = b
        dx, dy = bx - ax, by - ay
        length = max((dx * dx + dy * dy) ** 0.5, 1)
        step = 23
        for start in range(0, int(length), step * 2):
            end = min(start + step, length)
            d.line((ax + dx * start / length, ay + dy * start / length, ax + dx * end / length, ay + dy * end / length), fill=fill, width=width)


class MapProjector:
    def __init__(self, site, rect):
        minx, miny, maxx, maxy = site.bounds
        x0, y0, x1, y1 = rect
        self.minx, self.miny, self.maxx, self.maxy = minx, miny, maxx, maxy
        self.x0, self.y0, self.x1, self.y1 = rect

    def point(self, x: float, y: float):
        return (
            self.x0 + (x - self.minx) / (self.maxx - self.minx) * (self.x1 - self.x0),
            self.y1 - (y - self.miny) / (self.maxy - self.miny) * (self.y1 - self.y0),
        )

    def coords(self, geom):
        return [self.point(x, y) for x, y in geom.exterior.coords]


def polygon_parts(geom):
    if geom.geom_type == "Polygon":
        return [geom]
    if geom.geom_type == "MultiPolygon":
        return list(geom.geoms)
    return []


def draw_polygon(d, geom, project: MapProjector, fill: str, outline: str | None = None, width: int = 1):
    for part in polygon_parts(geom):
        pts = project.coords(part)
        d.polygon(pts, fill=fill)
        if outline:
            d.line(pts + [pts[0]], fill=outline, width=width, joint="curve")


def draw_map(d, data: dict[str, Any], rect, lang: str, *, emphasis: str = "master"):
    site = data["site"]
    project = MapProjector(site, rect)
    x0, y0, x1, y1 = rect
    d.rectangle(rect, fill="#F9F7F1", outline="#C6D1D2", width=3)
    draw_polygon(d, site, project, "#F1EFE6", NAVY, 3)
    land_colors = ["#E5EEE5", "#DEE9EF", "#EEE8F2", "#F2E6CE", "#E2EFEA", "#EEE9E1"]
    for feature, color in zip(data["land"], land_colors):
        draw_polygon(d, shape(feature["geometry"]), project, color)
    for feature in data["green"]:
        draw_polygon(d, shape(feature["geometry"]), project, "#B7D7C3", GREEN, 1)
    for feature in data["public"]:
        draw_polygon(d, shape(feature["geometry"]), project, "#D8EAF1", TEAL, 1)
    road_color = {"greenway": GREEN, "transit_connection": NAVY, "pedestrian": TEAL, "cycleway": "#2E8897", "local_access": MAGENTA}
    road_width = {"greenway": 8, "transit_connection": 10, "pedestrian": 7, "cycleway": 6, "local_access": 5}
    for feature in data["roads"]:
        props = feature["properties"]
        geom = shape(feature["geometry"])
        pts = [project.point(x, y) for x, y in geom.coords]
        draw_lines(d, pts, road_color.get(props.get("road_class"), SLATE), road_width.get(props.get("road_class"), 5), props.get("connection_confidence") == "SURVEY_REQUIRED")
    for area in data["areas"]:
        geom = shape(area["geometry"])
        for part in polygon_parts(geom):
            pts = project.coords(part)
            draw_lines(d, pts + [pts[0]], MAGENTA, 4, True)
    for feature in data["buildings"]:
        props = feature["properties"]
        colour = m.palette_status(props["status"])
        draw_polygon(d, shape(feature["geometry"]), project, "#FBFAF5", colour, 4)
        centroid = shape(feature["geometry"]).centroid
        px, py = project.point(centroid.x, centroid.y)
        draw_text(d, (px, py), props["patch_id"].replace("P-", ""), 17, False, colour, True, "mm")
    if emphasis == "master":
        labels = [
            ("众智园\nZhongzhiyuan", (116.348, 40.018), NAVY),
            ("AI 原点\nAI Origin", (116.348, 39.989), GREEN),
            ("大钟寺\nDazhongsi", (116.349, 39.947), AMBER),
        ]
        for text, point, colour in labels:
            px, py = project.point(*point)
            panel(d, (int(px - 122), int(py - 34), int(px + 122), int(py + 40)), colour, "#FFFFFF", 14, 3)
            first, second = text.split("\n")
            draw_text(d, (px, py - 13), first if language(lang) else second, 21, language(lang), colour, True, "ma")
            draw_text(d, (px, py + 13), l(lang, "概念重点区", "concept key area"), 13, language(lang), SLATE, False, "ma")
    return project


def map_legend(d, x: int, y: int, lang: str):
    rows = [
        (NAVY, l(lang, "常规公共路径／区域到达", "ordinary public route / regional arrival")),
        (AMBER, l(lang, "受控阈值", "controlled threshold")),
        (MAGENTA, l(lang, "服务、装卸、维护", "service / logistics / maintenance")),
        (GREEN, l(lang, "蓝绿接口", "blue-green interface")),
        (TEAL, l(lang, "步行／骑行连接", "walking / cycling connection")),
    ]
    for i, (color, label) in enumerate(rows):
        yy = y + i * 45
        d.line((x, yy + 10, x + 55, yy + 10), fill=color, width=9)
        draw_text(d, (x + 75, yy - 3), label, 20, language(lang), INK)


def status_legend(d, x: int, y: int, lang: str, compact: bool = False):
    statuses = list(m.STATUS_NAMES_ZH)
    for i, status in enumerate(statuses):
        xx = x + (i % (3 if compact else 5)) * (250 if compact else 430)
        yy = y + (i // (3 if compact else 5)) * 44
        d.rounded_rectangle((xx, yy, xx + 28, yy + 28), radius=5, fill=m.palette_status(status))
        draw_text(d, (xx + 40, yy - 2), status_name(status, lang), 18 if compact else 19, language(lang), INK)


def figure_site(lang: str, data: dict[str, Any]) -> Image.Image:
    im, d = figure_base(lang, l(lang, "01 / 城市", "01 / THE CITY"), l(lang, "京张续城总体空间设计图", "Jing-Zhang In Place Spatial Plan"), l(lang, "11.4 km² 概念场：让既有城市先继续工作；再以状态、行动与证据门决定何处、何时、如何更新。", "An 11.4 km² conceptual field: keep the existing city working first; then decide where, when and how to renew through status, action and evidence gates."))
    map_rect = (130, 430, 2370, 2025)
    draw_map(d, data, map_rect, lang)
    status_legend(d, 150, 2065, lang, compact=True)
    panel(d, (2440, 430, 3470, 920), NAVY, WHITE)
    draw_text(d, (2490, 480), l(lang, "一个不是“单脊”的更新场", "A renewal field, not a mandatory spine"), 32, language(lang), NAVY, True)
    draw_wrapped(d, 2490, 550, l(lang, "北—中—南不是被一条形象轴串联，而是按水—院区—到达、公开侧阈值、立体站城三种不同城市条件分别行动。", "North, middle and south are not staged along an image-axis. They act through three distinct urban conditions: water–compound–arrival, public-side threshold and grade-separated station-city."), 24, language(lang), 21 if language(lang) else 34, INK)
    d.line((2490, 760, 3425, 760), fill="#CCD6D7", width=2)
    draw_text(d, (2490, 795), l(lang, "三个重点区｜公告名称与临时表达", "THREE KEY AREAS | ANNOUNCED NAMES + PROVISIONAL EXPRESSION"), 21, language(lang), MAGENTA, True)
    areas = [
        (NAVY, l(lang, "众智园AI自主创新加速区｜约192.1 公顷", "Zhongzhiyuan AI Acceleration Area | approx. 192.1 ha")),
        (GREEN, l(lang, "北京AI原点社区｜约104.3 公顷", "Beijing AI Origin Community | approx. 104.3 ha")),
        (AMBER, l(lang, "大钟寺AI产业集聚区｜约72.0 公顷", "Dazhongsi AI Industry Cluster | approx. 72.0 ha")),
    ]
    for i, (colour, text) in enumerate(areas):
        yy = 850 + i * 58
        d.ellipse((2490, yy, 2516, yy + 26), fill=colour)
        draw_text(d, (2530, yy - 3), text, 20, language(lang), INK, True)
    draw_text(d, (2490, 1050), l(lang, "图上虚线范围仅为临时几何／不代表红线、地块、权属或站点角部。", "Dashed extents are provisional geometry only—not redlines, parcels, ownership or station corners."), 19, language(lang), MAGENTA, True)
    panel(d, (2440, 1130, 3470, 1695), GREEN, WHITE)
    draw_text(d, (2490, 1180), l(lang, "空间系统同时工作", "SYSTEMS WORK TOGETHER"), 30, language(lang), GREEN, True)
    map_legend(d, 2490, 1240, lang)
    panel(d, (2440, 1745, 3470, 2025), MAGENTA, "#FFFDFC")
    draw_text(d, (2490, 1790), l(lang, "AI 只在必须改变空间状态处出现", "AI APPEARS ONLY WHERE IT CHANGES SPACE"), 26, language(lang), MAGENTA, True)
    draw_wrapped(d, 2490, 1840, l(lang, "三项深度任务包进入受控、可撤、可审查的载体；日常学习、商业、导视和普通城市不因 AI 而新建。", "Three deep task packets enter controlled, reversible and reviewable carriers; ordinary learning, commerce, wayfinding and city life do not create a new building merely because of AI."), 20, language(lang), 24 if language(lang) else 37)
    footer(d, lang)
    return im


def controlling_patch_rows(register: list[dict[str, Any]]):
    # Seven strips intentionally cover all five evidence-status families and
    # the three area roles without turning the atlas into a register dump.
    wanted = ["P-N1", "P-N3", "P-N5", "P-M1", "P-M4", "P-S2", "P-S3"]
    lookup = {x["patch_id"]: x for x in register}
    return [lookup[x] for x in wanted]


def figure_atlas(lang: str, data: dict[str, Any]) -> Image.Image:
    im, d = figure_base(lang, l(lang, "02 / 状态 → 行动", "02 / STATUS → ACTION"), l(lang, "状态 × 行动拼贴图谱", "STATUS × ACTION Patch Atlas"), l(lang, "不是图例：每个控制单元从状态进入行动、触发条件与可感知的空间后果。", "Not a legend: each control patch moves from status to action, trigger and a perceptible spatial consequence."))
    draw_map(d, data, (130, 435, 1365, 1960), lang, emphasis="atlas")
    status_legend(d, 175, 1982, lang, compact=True)
    x0, x1 = 1450, 3470
    headings = [l(lang, "状态", "STATUS"), l(lang, "行动", "ACTION"), l(lang, "触发", "TRIGGER"), l(lang, "空间后果", "SPATIAL CONSEQUENCE")]
    cols = [x0, 1780, 2135, 2615]
    for x, title in zip(cols, headings):
        draw_text(d, (x, 445), title, 25, language(lang), NAVY if x != 2135 else MAGENTA, True)
    d.line((x0, 492, x1, 492), fill="#BFCBCD", width=3)
    for i, patch in enumerate(controlling_patch_rows(data["register"])):
        y = 535 + i * 197
        colour = m.palette_status(patch["status"])
        if i % 2 == 0:
            d.rounded_rectangle((1450, y - 16, 3470, y + 178), radius=15, fill="#FBFAF6")
        d.rounded_rectangle((1475, y, 1660, y + 42), radius=12, fill=colour)
        draw_text(d, (1568, y + 9), patch["patch_id"], 20, False, WHITE, True, "ma")
        draw_text(d, (1475, y + 64), status_name(patch["status"], lang), 18, language(lang), colour, True)
        action = action_name(patch["action"], lang)
        draw_text(d, (1780, y + 11), action, 22, language(lang), GREEN if patch["action"] in {"REPAIR", "OPEN_EDGE"} else AMBER, True)
        if language(lang):
            title, consequence = PATCH_ZH[patch["patch_id"]]
            trigger = l(lang, "先核实：", "") + ("公共／受控关系、权利与安全" if patch["patch_id"] in {"P-N3", "P-M1", "P-M4", "P-S2", "P-S4"} else "项目接口、连续性与维护")
        else:
            title = patch["urban_fabric_type"]
            consequence = patch["spatial_section_consequence"]
            trigger = patch["action_trigger"]
        draw_wrapped(d, 2135, y + 6, trigger, 17, language(lang), 22 if language(lang) else 33, INK, 23)
        draw_text(d, (2615, y + 5), title, 20, language(lang), NAVY, True)
        draw_wrapped(d, 2615, y + 37, consequence, 17, language(lang), 33 if language(lang) else 43, INK, 22)
        draw_text(d, (1475, y + 133), l(lang, "停／行：", "STOP / GO: ") + (l(lang, "不降低连续性、应急、公共使用与安全", "do not reduce continuity, emergency access, public use or safety")), 16, language(lang), MAGENTA, True)
    footer(d, lang)
    return im


def section_scene(d, rect, lang: str, kind: str, title: str, subtitle: str, colour: str):
    x0, y0, x1, y1 = rect
    zh = language(lang)
    panel(d, rect, colour, WHITE, 18, 4)
    draw_text(d, (x0 + 34, y0 + 28), title, 32, zh, colour, True)
    draw_text(d, (x0 + 34, y0 + 73), subtitle, 19, zh, SLATE)
    gx0, gx1 = x0 + 36, x1 - 36
    gy0, base_y = y0 + 118, y1 - 138
    gw = gx1 - gx0
    # The section is a deliberately typological illustration, never a survey.
    d.rectangle((gx0, gy0, gx1, base_y), fill="#FBFCF9")
    d.rectangle((gx0, base_y - 22, gx1, base_y), fill="#B5AA97")
    d.rectangle((gx0, base_y, gx1, base_y + 68), fill="#E3DACB")
    d.line((gx0, base_y + 22, gx1, base_y + 22), fill="#FFFFFF", width=2)

    def person(px: int, ground: int, col: str = NAVY):
        d.ellipse((px - 10, ground - 68, px + 10, ground - 48), fill=col)
        d.line((px, ground - 48, px, ground - 16), fill=col, width=5)
        d.line((px, ground - 35, px - 12, ground - 23), fill=col, width=4)
        d.line((px, ground - 35, px + 12, ground - 23), fill=col, width=4)
        d.line((px, ground - 16, px - 9, ground), fill=col, width=4)
        d.line((px, ground - 16, px + 9, ground), fill=col, width=4)

    def tree(px: int, height: int, canopy: str = "#AFCFB1"):
        d.line((px, base_y - 22, px, base_y - height), fill="#688D6D", width=7)
        d.ellipse((px - 38, base_y - height - 42, px + 38, base_y - height + 34), fill=canopy, outline=GREEN)

    # A soft back-plane makes scale and the conceptual building edge readable.
    for i in range(7):
        px = gx0 + 65 + i * int(gw / 7.2)
        bh = 65 + (i % 3) * 42
        d.rectangle((px, base_y - bh, px + 72, base_y - 22), fill="#ECECE5", outline="#D7D9D0")

    if kind == "north":
        water_end = gx0 + int(gw * .20); park_end = gx0 + int(gw * .58); carrier_start = gx0 + int(gw * .68)
        d.rectangle((gx0, base_y - 35, water_end, base_y - 2), fill="#A9D4DD")
        for wave in range(4): d.arc((gx0 + 15 + wave * 38, base_y - 31, gx0 + 62 + wave * 38, base_y - 8), 180, 350, fill=TEAL, width=3)
        d.polygon([(water_end, base_y - 22), (park_end, base_y - 22), (park_end - 35, base_y - 86), (water_end + 35, base_y - 86)], fill="#DCECE1", outline=GREEN)
        d.line((water_end + 20, base_y - 53, park_end - 20, base_y - 53), fill=TEAL, width=7)
        d.line((water_end + 20, base_y - 74, park_end - 20, base_y - 74), fill=MAGENTA, width=4)
        for px, height in ((water_end + 70, 155), (water_end + 165, 195), (park_end - 135, 180), (park_end - 55, 145)):
            tree(px, height)
        d.rectangle((park_end - 45, base_y - 160, carrier_start - 12, base_y - 22), fill="#F1E5D0", outline=NAVY, width=4)
        d.rectangle((carrier_start, base_y - 360, gx1 - 70, base_y - 22), fill="#E8E1D7", outline=AMBER, width=5)
        for level in range(3): d.line((carrier_start + 16, base_y - 105 - level * 78, gx1 - 86, base_y - 105 - level * 78), fill="#C8BA9E", width=3)
        d.rectangle((gx1 - 135, base_y - 100, gx1 - 70, base_y - 22), fill="#F6F1E5", outline=MAGENTA, width=3)
        person(water_end + 128, base_y - 22); person(park_end - 95, base_y - 22, GREEN); person(carrier_start + 135, base_y - 22, AMBER)
        labels = [(gx0 + 88, l(lang, "水／雨洪界面", "water / rain interface"), TEAL), (gx0 + int(gw*.41), l(lang, "公共河园｜步行＋骑行", "public river-park | walk + cycle"), GREEN), (gx0 + int(gw*.80), l(lang, "受控生产／服务边｜验证仅在条件满足后", "controlled productive / service edge | validation only after gates"), AMBER)]
    elif kind == "middle":
        street_end = gx0 + int(gw*.22); room_end = gx0 + int(gw*.57); control_end = gx0 + int(gw*.73)
        d.rectangle((gx0, base_y - 102, street_end, base_y - 22), fill="#DEE9EF", outline=NAVY, width=4)
        d.line((gx0 + 20, base_y - 53, room_end - 25, base_y - 53), fill=TEAL, width=8)
        for px in (gx0 + 60, gx0 + 140): tree(px, 142)
        d.rectangle((street_end + 20, base_y - 218, room_end - 20, base_y - 22), fill="#E9F0E5", outline=GREEN, width=4)
        d.rectangle((street_end + 74, base_y - 154, room_end - 78, base_y - 22), fill="#FFFFFF", outline=GREEN, width=3)
        d.rectangle((room_end, base_y - 260, control_end, base_y - 22), fill="#F3E4C8", outline=AMBER, width=5)
        draw_lines(d, [(control_end, base_y - 280), (control_end, base_y - 22)], AMBER, 5, True)
        d.rectangle((control_end + 8, base_y - 390, gx1 - 42, base_y - 22), fill="#E8E2D5", outline=NAVY, width=5)
        for level in range(4): d.line((control_end + 25, base_y - 95 - level*70, gx1 - 58, base_y - 95 - level*70), fill="#C8C2B7", width=3)
        person(gx0 + 105, base_y - 22); person(street_end + 135, base_y - 22, GREEN); person(room_end + 70, base_y - 22, AMBER)
        labels = [(gx0 + 100, l(lang, "街道／公园｜公共路", "street / park | public route"), NAVY), (gx0 + int(gw*.40), l(lang, "普通公共房间／庭院", "ordinary public room / court"), GREEN), (gx0 + int(gw*.65), l(lang, "可撤受控状态", "reversible controlled state"), AMBER), (gx0 + int(gw*.88), l(lang, "校园（受控）", "controlled campus"), NAVY)]
    else:
        arrival_end = gx0 + int(gw*.22); frontage_start = gx0 + int(gw*.62)
        d.line((gx0 + 48, gy0 + 95, gx1 - 42, gy0 + 95), fill=NAVY, width=18)
        d.line((gx0 + 48, gy0 + 95, gx1 - 42, gy0 + 95), fill=WHITE, width=4)
        d.line((gx0 + int(gw*.30), gy0 + 105, gx0 + int(gw*.30), base_y - 22), fill=NAVY, width=11)
        d.rectangle((gx0, base_y - 130, arrival_end, base_y - 22), fill="#E5EEF2", outline=NAVY, width=4)
        d.polygon([(arrival_end, base_y - 22), (frontage_start, base_y - 22), (frontage_start - 85, base_y - 150), (arrival_end + 50, base_y - 150)], fill="#E9F0E5", outline=GREEN)
        d.line((arrival_end + 30, base_y - 63, frontage_start - 35, base_y - 63), fill=TEAL, width=8)
        d.line((arrival_end + 30, base_y - 92, frontage_start - 35, base_y - 92), fill=MAGENTA, width=4)
        d.rectangle((frontage_start, base_y - 322, gx1 - 42, base_y - 22), fill="#F1E4CD", outline=AMBER, width=5)
        for level in range(3): d.line((frontage_start + 20, base_y - 104 - level*75, gx1 - 60, base_y - 104 - level*75), fill="#D3BF99", width=3)
        person(gx0 + 100, base_y - 22); person(arrival_end + 125, base_y - 22, TEAL); person(frontage_start + 115, base_y - 22, MAGENTA)
        labels = [(gx0 + 100, l(lang, "站城到达／人工帮助", "station-city arrival / staffed help"), NAVY), (gx0 + int(gw*.41), l(lang, "步行＋骑行｜服务可见", "walk + cycle | visible service"), TEAL), (gx0 + int(gw*.82), l(lang, "混合临街／专业采用", "mixed frontage / professional adoption"), AMBER)]
    for px, label, col in labels:
        draw_text(d, (px, base_y + 36), label, 17, zh, col, True, "ma")
    draw_text(d, (gx0, y1 - 72), l(lang, "概念断面：人物、地面、步行／骑行、公共／受控关系、服务与可复位状态同时呈现。", "Concept section: people, ground, walk/cycle, public/control relation, service and reversible state appear together."), 16, zh, SLATE)


def figure_key_areas(lang: str, data: dict[str, Any]) -> Image.Image:
    im, d = figure_base(lang, l(lang, "03 / 三个地方", "03 / THREE PLACES"), l(lang, "三个重点区：三种空间对象", "Three Key Areas: Three Spatial Objects"), l(lang, "北部水—院区—到达；中部公开侧校园阈值；南部立体交通站城。它们不共享一套形式。", "North water–compound–arrival; middle public-side campus threshold; south grade-separated station city. They do not share one formal answer."))
    section_scene(d, (115, 430, 3485, 1110), lang, "north", l(lang, "众智园AI自主创新加速区", "ZHONGZHIYUAN AI ACCELERATION AREA"), l(lang, "水 → 公共景观 → 受控生产／服务边", "water → public landscape → controlled productive / service edge"), NAVY)
    section_scene(d, (115, 1160, 1765, 1950), lang, "middle", l(lang, "北京AI原点社区", "BEIJING AI ORIGIN COMMUNITY"), l(lang, "街道／公园 → 普通公共房间 → 可撤受控状态 → 校园", "street / park → ordinary public room → reversible control → campus"), GREEN)
    section_scene(d, (1835, 1160, 3485, 1950), lang, "south", l(lang, "大钟寺AI产业集聚区", "DAZHONGSI AI INDUSTRY CLUSTER"), l(lang, "到达 → 步行／骑行 → 混合临街 → 专业采用", "arrival → walking / cycling → mixed frontage → professional adoption"), AMBER)
    draw_text(d, (115, 1992), l(lang, "城市体验序列（概念插图）：区域到达 → 日常城市 → 公共阈值 → 适应性载体 → 受控任务 → 回到日常城市", "Urban-space sequence (concept illustration): regional arrival → ordinary city → public threshold → adapted carrier → controlled task → ordinary city"), 23, language(lang), NAVY, True)
    sequence = [
        (NAVY, l(lang, "区域\n到达", "regional\narrival")), (TEAL, l(lang, "日常\n城市", "ordinary\ncity")),
        (GREEN, l(lang, "公共\n阈值", "public\nthreshold")), (AMBER, l(lang, "适应\n载体", "adapted\ncarrier")),
        (MAGENTA, l(lang, "受控\n任务", "controlled\ntask")), (NAVY, l(lang, "回到\n日常", "return to\nordinary")),
    ]
    for i, (colour, label) in enumerate(sequence):
        cx = 300 + i * 605
        d.ellipse((cx - 76, 2074, cx + 76, 2226), fill=WHITE, outline=colour, width=7)
        a, b = label.split("\n")
        draw_text(d, (cx, 2112), a, 19, language(lang), colour, True, "ma")
        draw_text(d, (cx, 2142), b, 17, language(lang), INK, False, "ma")
        if i < len(sequence) - 1:
            d.line((cx + 84, 2150, cx + 500, 2150), fill="#A7B4B8", width=5)
            d.polygon([(cx + 500, 2150), (cx + 478, 2137), (cx + 478, 2163)], fill="#A7B4B8")
    # Footer is deliberately inside the lower visual rhythm, not an additional card.
    draw_text(d, (W - 105, H - 40), l(lang, "概念／临时几何；非红线、非现状测绘", "concept / provisional geometry; not a redline or as-built survey"), 17, language(lang), MAGENTA, True, "rs")
    return im


def figure_mobility(lang: str, data: dict[str, Any]) -> Image.Image:
    im, d = figure_base(lang, l(lang, "04 / 移动与蓝绿", "04 / MOVE + BREATHE"), l(lang, "移动、呼吸与服务：一套可运营的城市系统", "Move, Breathe and Service: One Operable Urban System"), l(lang, "步行、无障碍、骑行、区域到达、服务维护与蓝绿公共空间不是分层叠图，而是在同一城市断面里协调。", "Walking, accessibility, cycling, regional arrival, service/maintenance and blue-green public realm are coordinated in one urban section—not overlaid as separate systems."))
    draw_map(d, data, (125, 430, 2240, 2015), lang, emphasis="systems")
    panel(d, (2310, 430, 3475, 1000), NAVY, WHITE)
    draw_text(d, (2370, 485), l(lang, "五类关系，不是一条单线", "FIVE RELATIONS, NOT ONE LINE"), 31, language(lang), NAVY, True)
    map_legend(d, 2370, 550, lang)
    draw_wrapped(d, 2370, 835, l(lang, "公共路不依赖校园内部；服务和维护不被景观遮蔽；立体交通连接先经可达与连续性审计。", "Public routes do not depend on campus interior; service and maintenance are not hidden by landscape; grade-separated connections begin with access and continuity audit."), 21, language(lang), 28 if language(lang) else 43, INK)
    panel(d, (2310, 1060, 3475, 1535), GREEN, WHITE)
    draw_text(d, (2370, 1115), l(lang, "蓝绿不是背景", "BLUE-GREEN IS NOT BACKGROUND"), 30, language(lang), GREEN, True)
    draw_wrapped(d, 2370, 1170, l(lang, "根域、排水、遮阴、雨天避难、维护通道、夜间边界共同决定公共空间是否能运行。", "Root zones, drainage, shade, rain refuge, maintenance access and night boundaries together determine whether public space works."), 22, language(lang), 25 if language(lang) else 39)
    panel(d, (2310, 1590, 3475, 2015), MAGENTA, "#FFFDFC")
    draw_text(d, (2370, 1645), l(lang, "AI 关闭后仍然成立", "AI OFF STILL HOLDS"), 30, language(lang), MAGENTA, True)
    draw_wrapped(d, 2370, 1700, l(lang, "固定导视、物理备选路、人工帮助、公开空间与服务规程在数字设施关闭时继续运行。", "Fixed signs, physical alternatives, staffed help, public space and service protocols remain usable when digital systems are off."), 22, language(lang), 25 if language(lang) else 39)
    footer(d, lang)
    return im


def figure_evidence(lang: str, data: dict[str, Any]) -> Image.Image:
    metrics = data["metrics"]["metrics"]
    im, d = figure_base(lang, l(lang, "05 / 证据与实施", "05 / PROVE + PAUSE"), l(lang, "证据、未知与实施门：先证明，再行动", "Evidence, Unknowns and Gates: Prove Before Acting"), l(lang, "可信度不来自更多数字，而来自清楚地区分已知、可复算、概念建议与必须暂停调查的条件。", "Credibility does not come from more numbers. It comes from clearly separating known, derived, conceptual and survey-required conditions."))
    # A single evidence river makes hierarchy, rather than an Excel dashboard.
    d.line((175, 655, 3425, 655), fill="#C9D5D5", width=10)
    stages = [
        ("G0", NAVY, l(lang, "调查／对齐", "survey / align")), ("G1", GREEN, l(lang, "低遗憾／可撤", "low-regret / reversible")),
        ("G2", TEAL, l(lang, "专业复核", "professional review")), ("G3", AMBER, l(lang, "需求证明后填补", "infill after need")),
        ("G4", MAGENTA, l(lang, "运营／修订", "operate / revise")),
    ]
    for i, (code, colour, label) in enumerate(stages):
        x = 265 + i * 770
        d.ellipse((x - 65, 590, x + 65, 720), fill=WHITE, outline=colour, width=8)
        draw_text(d, (x, 625), code, 26, False, colour, True, "ma")
        draw_text(d, (x, 755), label, 21, language(lang), INK, True, "ma")
    columns = [
        ("已知／可复算" if language(lang) else "KNOWN / DERIVED", GREEN, [
            l(lang, "临时场地几何：11.4 km²", "provisional site geometry: 11.4 km²"),
            l(lang, f"17 个控制单元；15 项项目族；12 个场景", "17 control patches; 15 project families; 12 scenarios"),
            l(lang, f"概念绿地／公共空间比例：{metrics['green_ratio']['value']:.1%}／{metrics['public_space_ratio']['value']:.1%}", f"concept green/public ratios: {metrics['green_ratio']['value']:.1%} / {metrics['public_space_ratio']['value']:.1%}"),
        ]),
        ("设计规则" if language(lang) else "DESIGN RULES", NAVY, [
            l(lang, "保留优先；状态不自动授权行动", "retain first; status never authorizes action"),
            l(lang, "公共路径不依赖受控校园内部", "public route never depends on controlled campus interior"),
            l(lang, "无真实任务／空间差异／安全条件，即不新建", "no real task, spatial delta or safety condition = NO BUILD"),
        ]),
        ("未知／必须暂停" if language(lang) else "UNKNOWN / PAUSE", MAGENTA, [
            l(lang, "法定 FAR、限高、权属、容量与正式边界", "statutory FAR, height, rights, capacity and official boundaries"),
            l(lang, "建筑状态、文保、道路／轨道工程与环境调查", "building condition, heritage, road/rail engineering and environmental survey"),
            l(lang, "官方数据到位后整套复算，而不是补一条注释", "official data triggers full recalculation, not a footnote"),
        ]),
    ]
    for i, (heading, colour, items) in enumerate(columns):
        x0 = 135 + i * 1150
        panel(d, (x0, 950, x0 + 1040, 1765), colour, WHITE)
        draw_text(d, (x0 + 48, 1008), heading, 33, language(lang), colour, True)
        y = 1090
        for text in items:
            d.ellipse((x0 + 55, y + 10, x0 + 70, y + 25), fill=colour)
            y = draw_wrapped(d, x0 + 92, y, text, 23, language(lang), 24 if language(lang) else 37, INK, 34) + 43
    draw_text(d, (155, 1845), l(lang, "实施判断", "IMPLEMENTATION JUDGMENT"), 27, language(lang), NAVY, True)
    draw_wrapped(d, 155, 1905, l(lang, "把“不新建”、调查、可撤试验、专业复核与退出复用放在项目链前端，才使“在地续城”具备实施可信度。", "Placing NO BUILD, survey, reversible testing, professional review and exit/reuse at the start of the project chain is what gives in-place renewal implementation credibility."), 25, language(lang), 42 if language(lang) else 59, INK, 32)
    footer(d, lang)
    return im


def crop_area_panel(lang: str, index: int) -> Image.Image:
    source = Image.open(FIG / ("key-areas" + (".en" if lang == "en" else "") + ".png"))
    if index == 0:
        return source.crop((85, 400, 3515, 1140))
    if index == 1:
        return source.crop((80, 1130, 1795, 1980))
    return source.crop((1805, 1130, 3520, 1980))


def pdf_font():
    return m.pdf_font()


def pdf_header(c, w, h, lang, page_no, title):
    """Use the shared RC1 visual identity with reader-facing localized footer."""
    zh = language(lang); mm = 72 / 25.4; font = pdf_font()
    c.setFillColor(HexColor(PAPER)); c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(HexColor(ACCENT)); c.rect(0, h - 5 * mm, w, 5 * mm, fill=1, stroke=0)
    c.setFillColor(HexColor(NAVY)); c.setFont(font, 23)
    c.drawString(17 * mm, h - 23 * mm, "京张续城 / Jing-Zhang In Place" if zh else "Jing-Zhang In Place")
    c.setFont(font, 12); c.setFillColor(HexColor(SLATE)); c.drawString(17 * mm, h - 31 * mm, title)
    c.setFont(font, 8); c.drawRightString(w - 14 * mm, 11 * mm, f"{page_no:02d}  |  " + l(lang, "概念／临时范围 · 离线导出", "PROVISIONAL CONCEPT · OFFLINE EXPORT"))
    return font


def draw_pdf_lines(c, font, x, y, lines, size=12, leading=16, color=INK):
    return m.draw_pdf_text(c, font, x, y, lines, size, leading, color)


def pdf_draw_image(c, image, x, y, width, height):
    if isinstance(image, Path):
        c.drawImage(str(image), x, y, width, height, preserveAspectRatio=True, anchor="c", mask="auto")
    else:
        c.drawImage(ImageReader(image), x, y, width, height, preserveAspectRatio=True, anchor="c", mask="auto")


def build_a3(lang: str):
    zh = language(lang); suffix = "" if zh else ".en"
    mm = 72 / 25.4; w, h = 420 * mm, 297 * mm
    c = Canvas(str(DRAWINGS / f"a3-booklet{suffix}.pdf"), pagesize=(w, h), pageCompression=1, invariant=1)
    pages = [
        (l(lang, "封面｜让既有城市继续工作", "Cover | Keep the Existing City Working"), "site-overview", l(lang, "京张续城不是一条必经形象轴；它是一片由状态、行动与证据门组织的异质更新场。", "Jing-Zhang In Place is not a compulsory image-axis. It is a heterogeneous renewal field organized by status, action and evidence gates.")),
        (l(lang, "场地与证据边界", "Site and Evidence Boundary"), "metrics-evidence", l(lang, "临时几何用于概念一致性，不替代正式边界、地块、权属或工程调查。", "Provisional geometry supports conceptual consistency; it never substitutes for official boundaries, parcels, rights or engineering survey.")),
        (l(lang, "总体空间设计图", "Overall Spatial Plan"), "site-overview", l(lang, "看见 11.4 km² 概念场、公共空间、蓝绿、移动与 17 个控制单元。", "Read the 11.4 km² conceptual field, public space, blue-green, movement and 17 control patches.")),
        (l(lang, "STATUS × ACTION", "STATUS × ACTION"), "land-use-structure", l(lang, "从状态到行动、触发和空间后果；不是一个颜色图例。", "From status to action, trigger and spatial consequence; not a colour legend.")),
        (l(lang, "三个重点区｜概览", "Three Key Areas | Overview"), "key-areas", l(lang, "水—院区—到达、公开侧阈值、立体站城：三种空间对象，三种实施起点。", "Water–compound–arrival, public-side threshold and grade-separated station city: three spatial objects and three implementation starts.")),
        (l(lang, "众智园｜水、院区与区域到达", "Zhongzhiyuan | Water, Compound and Regional Arrival"), 0, l(lang, "水 → 公共景观 → 受控生产／服务边。没有真实任务、载体和安全条件，即不新建验证空间。", "Water → public landscape → controlled productive/service edge. Without a real task, carrier and safety condition, no validation space is built.")),
        (l(lang, "AI 原点｜公开侧校园阈值", "AI Origin | Public-side Campus Threshold"), 1, l(lang, "公共路线留在校园外侧；普通学习房和庭院优先，受控项目状态必须可撤。", "Public routes remain outside campus; ordinary learning rooms and courts come first, while controlled project state must be reversible.")),
        (l(lang, "大钟寺｜立体交通中的日常城市", "Dazhongsi | Ordinary City in Grade-separated Mobility"), 2, l(lang, "类型学站城场：先审计四向可达、地面连续与服务，再讨论载体。", "A typological station-city field: audit four-way access, surface continuity and service before considering any carrier.")),
        (l(lang, "移动、蓝绿与运营", "Mobility, Blue-green and Operations"), "mobility-bluegreen", l(lang, "步行、无障碍、骑行、服务维护和生态运营在一张城市图中共同工作。", "Walking, accessibility, cycling, service/maintenance and ecological operations work together in one urban field.")),
        (l(lang, "普通城市与 AI 任务", "Ordinary City and AI Tasks"), "key-areas", l(lang, "AI 关闭时，固定导视、人工帮助、物理备选路径、公开空间与服务规程仍完整。", "When AI is off, fixed signs, staffed help, physical alternatives, public space and service protocols remain complete.")),
        (l(lang, "项目、分期与退出", "Projects, Phasing and Exit"), "metrics-evidence", l(lang, "调查 → 可撤 → 专业复核 → 需求证明 → 运营修订；替换不属于默认行动。", "Survey → reversible → professional review → demonstrated need → operate/revise; replacement is not a default action.")),
        (l(lang, "结语｜一座可被证据修订的城市", "Closing | A City That Can Be Revised by Evidence"), "site-overview", l(lang, "保留优先、证据分层、条件行动与不新建让方案既有空间表达，也有实施克制。", "Retain-first, tiered evidence, conditional action and NO BUILD provide both spatial expression and implementation restraint.")),
    ]
    for index, (title, source, blurb) in enumerate(pages, 1):
        font = pdf_header(c, w, h, lang, index, title)
        image = crop_area_panel(lang, source) if isinstance(source, int) else FIG / f"{source}{suffix}.png"
        pdf_draw_image(c, image, 17 * mm, 60 * mm, 386 * mm, 174 * mm)
        c.setFillColor(HexColor(WHITE)); c.roundRect(17 * mm, 21 * mm, 386 * mm, 28 * mm, 5 * mm, fill=1, stroke=0)
        draw_pdf_lines(c, font, 25 * mm, 39 * mm, [blurb], 10.7 if zh else 10.1, 13, NAVY)
        c.showPage()
    c.save()


def build_a0(lang: str):
    zh = language(lang); suffix = "" if zh else ".en"; mm = 72 / 25.4; w, h = 1189 * mm, 841 * mm
    c = Canvas(str(DRAWINGS / f"a0-boards{suffix}.pdf"), pagesize=(w, h), pageCompression=1, invariant=1)
    boards = [
        (l(lang, "01 这座城市", "01 THE CITY"), "site-overview", None, l(lang, "让既有城市继续工作；再以状态、行动与证据门决定更新。", "Keep the existing city working; then decide renewal through status, action and evidence gates.")),
        (l(lang, "02 三个地方", "02 THE THREE PLACES"), "key-areas", None, l(lang, "不是三座同款 AI 地标，而是三种城市条件的不同空间回答。", "Not three matching AI landmarks, but different spatial answers to three urban conditions.")),
        (l(lang, "03 如何运行", "03 HOW IT WORKS"), "mobility-bluegreen", "metrics-evidence", l(lang, "公共系统、AI 任务、不新建、项目分期与证据边界一起构成实施逻辑。", "Public systems, AI tasks, NO BUILD, project phasing and evidence boundaries together form the implementation logic.")),
    ]
    for index, (title, main, inset, blurb) in enumerate(boards, 1):
        font = pdf_header(c, w, h, lang, index, title)
        c.setFillColor(HexColor(NAVY)); c.setFont(font, 50 if zh else 45); c.drawString(28 * mm, h - 64 * mm, title)
        c.setFillColor(HexColor(MAGENTA)); c.setFont(font, 20 if zh else 18); c.drawString(28 * mm, h - 85 * mm, blurb)
        if inset is None:
            # Far-view boards reserve the overwhelming majority for one drawing.
            pdf_draw_image(c, FIG / f"{main}{suffix}.png", 28 * mm, 108 * mm, 1133 * mm, 596 * mm)
            notes = [
                l(lang, "北：水—院区—区域到达", "north: water–compound–regional arrival"),
                l(lang, "中：公开侧校园阈值", "middle: public-side campus threshold"),
                l(lang, "南：立体交通站城", "south: grade-separated station city"),
            ]
        else:
            pdf_draw_image(c, FIG / f"{main}{suffix}.png", 28 * mm, 130 * mm, 745 * mm, 565 * mm)
            pdf_draw_image(c, FIG / f"{inset}{suffix}.png", 795 * mm, 217 * mm, 366 * mm, 392 * mm)
            notes = [
                l(lang, "概念／临时范围，非红线", "concept / provisional extent, not a redline"),
                l(lang, "保留优先，替换不是默认行动", "retain first; replacement is not default"),
                l(lang, "每一后期动作均有前期证据门", "each later action has an earlier evidence gate"),
            ]
        if index == 1:
            c.setFillColor(HexColor(MAGENTA)); c.setFont(font, 17 if zh else 15)
            c.drawCentredString(w / 2, 94 * mm, l(lang, "状态  →  行动  →  触发  →  空间后果", "STATUS  →  ACTION  →  TRIGGER  →  SPATIAL CONSEQUENCE"))
        for j, text in enumerate(notes):
            x = (42 + j * 372) * mm
            col = [NAVY, GREEN, MAGENTA][j]
            c.setStrokeColor(HexColor(col)); c.setLineWidth(4); c.line(x, 72 * mm, x + 330 * mm, 72 * mm)
            c.setFillColor(HexColor(col)); c.setFont(font, 16 if zh else 14); c.drawCentredString(x + 165 * mm, 49 * mm, text)
        c.showPage()
    c.save()


def patch_title(patch: dict[str, Any], lang: str) -> str:
    if language(lang):
        return PATCH_ZH[patch["patch_id"]][0]
    return patch["urban_fabric_type"]


def patch_consequence(patch: dict[str, Any], lang: str) -> str:
    if language(lang):
        return PATCH_ZH[patch["patch_id"]][1]
    return patch["spatial_section_consequence"]


def build_visual(lang: str, data: dict[str, Any]):
    zh = language(lang); suffix = "" if zh else ".en"; register = data["register"]; projects = data["projects"]; tasks = data["simulation"]["tasks"]; personas = data["simulation"]["personas"]
    metric_values = data["metrics"]["metrics"]
    nav = [("plan", l(lang, "总体空间图", "Spatial plan")), ("atlas", l(lang, "状态 × 行动", "STATUS × ACTION")), ("places", l(lang, "三个重点区", "Three key areas")), ("systems", l(lang, "移动与蓝绿", "Mobility + blue-green")), ("ai", l(lang, "AI 何时重要", "Where AI matters")), ("evidence", l(lang, "证据与限制", "Evidence + limits")), ("registers", l(lang, "完整登记册", "Full registers"))]
    nav_html = "".join(f'<a href="#{key}">{html.escape(label)}</a>' for key, label in nav)
    patch_rows = "".join(f"<tr><td><b>{p['patch_id']}</b><br><span>{html.escape(patch_title(p, lang))}</span></td><td>{html.escape(status_name(p['status'], lang))}</td><td>{html.escape(action_name(p['action'], lang))}</td><td>{html.escape(patch_consequence(p, lang))}</td><td>{html.escape(p['phase'])}</td></tr>" for p in register)
    project_rows = "".join(f"<li><b>{p['project_id']}</b> — {html.escape(PROJECT_ZH[p['project_id']] if zh else p['title'])}<br><span>{html.escape(l(lang, '状态：', 'Status: ') + status_name(p['status'], lang) + ' ｜ ' + l(lang, '行动：', 'Action: ') + action_name(p['action'], lang) + ' ｜ ' + l(lang, '阶段：', 'Phase: ') + p['phase'])}</span></li>" for p in projects)
    task_rows = "".join(f"<li><b>{t['id']}</b> — {html.escape(SCENARIO_ZH[t['id']] if zh else t['title_en'])}<br><span>{html.escape(l(lang, '空间状态：', 'Spatial state: ') + (('深度任务包／有人工替代' if t.get('deep_task_packet') else '普通城市辅助／有人工替代') if zh else ('deep task packet / human fallback' if t.get('deep_task_packet') else 'ordinary-city assist / human fallback')))}</span></li>" for t in tasks)
    persona_rows = "".join(f"<li><b>{p['id']}</b> — {html.escape(PERSONA_ZH.get(p['id'], p['name']) if zh else PERSONA_EN.get(p['id'], p['name']))}</li>" for p in personas)
    area_items = "".join(f"<article><h3>{title}</h3><p>{body}</p></article>" for title, body in [
        (l(lang, "众智园", "Zhongzhiyuan"), l(lang, "水—院区—区域到达；将公共河园、受控生产／服务边与验证门放在同一断面。", "Water–compound–regional arrival; put public river-park, controlled productive/service edge and validation gates in one section.")),
        (l(lang, "AI 原点", "AI Origin"), l(lang, "公开侧校园阈值；日常公共房间优先，受控项目状态可撤。", "Public-side campus threshold; ordinary public rooms first, controlled project state reversible.")),
        (l(lang, "大钟寺", "Dazhongsi"), l(lang, "类型学立体站城；先审计可达与连续性，后讨论专业采用载体。", "Typological grade-separated station city; audit access and continuity before considering professional-adoption carriers.")),
    ])
    title = l(lang, "京张续城｜离线展阅", "Jing-Zhang In Place | Offline Presentation")
    html_text = f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<style>
:root{{--paper:{PAPER};--ink:{INK};--navy:{NAVY};--green:{GREEN};--teal:{TEAL};--amber:{AMBER};--magenta:{MAGENTA};--rule:#cbd5d6}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--paper);color:var(--ink);font-family:"Microsoft YaHei",Arial,sans-serif;line-height:1.6}}a{{color:inherit}}.skip{{position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;background:var(--navy);color:#fff;padding:10px 14px;z-index:10}}.skip:focus{{left:16px;top:16px;width:auto;height:auto;outline:3px solid var(--teal);outline-offset:3px}}header{{border-top:12px solid {ACCENT};background:#fff;padding:34px max(5vw,28px) 24px}}.brand{{color:var(--navy);font-weight:800;font-size:clamp(29px,4.5vw,62px);line-height:1.08}}.tag{{color:var(--magenta);font-weight:800;margin:10px 0}}nav{{display:flex;flex-wrap:wrap;gap:10px 19px;margin-top:22px}}nav a{{font-size:14px;font-weight:800;text-decoration:none;border-bottom:2px solid transparent}}nav a:hover{{border-bottom-color:var(--magenta)}}nav a:focus-visible{{border-bottom-color:var(--magenta);outline:3px solid var(--teal);outline-offset:4px}}main{{max-width:1700px;margin:auto;padding:34px max(4vw,24px) 78px}}section{{margin:0 0 52px}}h1,h2,h3{{line-height:1.16;color:var(--navy)}}h1{{font-size:clamp(30px,4.2vw,58px);margin:0 0 14px}}h2{{font-size:clamp(26px,3.1vw,42px);margin:0 0 11px}}h3{{font-size:20px;margin:0 0 7px}}p{{max-width:95ch}}.lead{{font-size:clamp(18px,2vw,25px);max-width:47ch}}.limit{{font-weight:800;color:var(--magenta)}}figure{{margin:24px 0 0}}figure img{{width:100%;height:auto;display:block;background:#fff;border:1px solid var(--rule)}}figcaption{{font-size:14px;color:#56666d;margin:9px 2px 0}}.split{{display:grid;grid-template-columns:1.38fr .62fr;gap:32px;align-items:start}}.edge{{border-left:5px solid var(--green);padding:12px 0 12px 20px}}.places{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;margin-top:21px}}.places article{{border-top:5px solid var(--navy);padding:17px 0}}.places article:nth-child(2){{border-top-color:var(--green)}}.places article:nth-child(3){{border-top-color:var(--amber)}}.quiet{{background:#fff;padding:31px;border:1px solid var(--rule)}}.callout{{border-left:7px solid var(--magenta);padding:12px 0 12px 22px;font-weight:700}}.audit{{display:grid;grid-template-columns:1.15fr .85fr;gap:24px;background:#fff;border-top:6px solid var(--green);padding:28px 30px}}.audit-metrics{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:17px 0}}.audit-metrics div{{border-left:4px solid var(--teal);padding:8px 0 8px 12px}}.audit-metrics b{{display:block;font-size:22px;color:var(--navy)}}.audit-metrics span{{font-size:12px;color:#52626a}}details{{background:#fff;border:1px solid var(--rule);margin:12px 0;padding:0 18px}}summary{{cursor:pointer;padding:17px 0;font-weight:800;color:var(--navy)}}summary:focus{{outline:3px solid var(--teal);outline-offset:4px}}table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:left;vertical-align:top;padding:11px 8px;border-top:1px solid var(--rule)}}th{{color:var(--navy)}}td span,li span{{color:#52626a;font-size:13px}}ul{{padding-left:22px}}li{{margin:0 0 13px}}footer{{border-top:1px solid var(--rule);padding-top:22px;color:#4c5d64;font-size:14px}}@media(max-width:850px){{.split,.places,.audit{{grid-template-columns:1fr}}.audit-metrics{{grid-template-columns:1fr}}main{{padding-inline:22px}}table{{font-size:12px}}th,td{{padding:8px 4px}}.hide-narrow{{display:none}}}}@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
 </style></head><body><a class="skip" href="#main-content">{html.escape(l(lang, '跳到主要内容', 'Skip to main content'))}</a>
<header><div class="brand">{html.escape(l(lang, '京张续城', 'Jing-Zhang In Place'))}</div><div class="tag">{html.escape(l(lang, 'STATUS × ACTION｜离线城市设计展阅', 'STATUS × ACTION | Offline Urban Design Presentation'))}</div><nav aria-label="{html.escape(l(lang, '页面导航', 'Page navigation'))}">{nav_html}</nav></header>
<main id="main-content">
<section id="hero"><p class="limit">{html.escape(l(lang, '概念／临时范围；不是官方红线、地块、权属或工程结论。', 'Concept / provisional extent; not an official redline, parcel, ownership or engineering conclusion.'))}</p><h1>{html.escape(l(lang, '先让既有城市继续工作', 'Keep the Existing City Working First'))}</h1><p class="lead">{html.escape(l(lang, '京张续城不是一条必经的形象主轴；它是一片异质更新场，以状态 × 行动将证据、公共性、受控关系、行动触发和退出复用连在一起。', 'Jing-Zhang In Place is not a compulsory image-axis. It is a heterogeneous renewal field that connects evidence, publicness, controlled relations, action triggers and exit/reuse through STATUS × ACTION.'))}</p><figure><img src="../assets/figures/site-overview{suffix}.png" alt="{html.escape(l(lang, '京张续城总体空间设计图：临时范围、三处重点区、公共空间、蓝绿、移动和状态行动拼贴。', 'Jing-Zhang In Place spatial plan: provisional extent, three key areas, public space, blue-green, mobility and status-action patches.'))}"><figcaption>{html.escape(l(lang, '总体空间设计图｜概念／临时范围', 'Overall spatial plan | concept / provisional extent'))}</figcaption></figure></section>
<section id="plan" class="split"><div><h2>{html.escape(l(lang, '总体空间：不是“单脊”，而是可被证据修订的更新场', 'Overall spatial field: not a spine, but a renewal field revisable by evidence'))}</h2><p>{html.escape(l(lang, '11.4 km² 临时场地将公共路、蓝绿、服务、受控阈值和 17 个控制单元放在同一阅读面中。三处重点区分别处理水—院区—到达、公开侧校园阈值与立体交通站城。', 'The 11.4 km² provisional field puts public routes, blue-green, service, controlled thresholds and 17 control patches on one reading surface. The key areas separately address water–compound–arrival, public-side campus threshold and grade-separated station city.'))}</p></div><aside class="edge"><b>{html.escape(l(lang, '空间边界', 'Spatial boundary'))}</b><br>{html.escape(l(lang, '概念载体不是现状建筑诊断；临时范围不推断地块、道路红线、站点角部或法定开发量。', 'Concept carriers are not existing-building diagnoses; provisional extents do not infer parcels, road redlines, station corners or statutory development quantities.'))}</aside></section>
<section id="atlas"><h2>{html.escape(l(lang, '状态 → 行动', 'STATUS → ACTION'))}</h2><p>{html.escape(l(lang, '状态不自动授权行动。每个控制单元都要回答：证据处于什么状态、可以采取什么行动、何时触发、空间会变成什么样、何时停止并回到普通城市。', 'Status never authorizes action by itself. Each control patch answers: What is the evidence state? Which action is allowed? What triggers it? What spatial consequence results? When does it stop and return to ordinary city?'))}</p><figure><img src="../assets/figures/land-use-structure{suffix}.png" alt="{html.escape(l(lang, '状态到行动拼贴图谱，显示控制单元的状态、行动、触发和空间后果。', 'Status-to-action patch atlas showing status, action, trigger and spatial consequence for control patches.'))}"><figcaption>{html.escape(l(lang, '状态 × 行动拼贴图谱', 'STATUS × ACTION patch atlas'))}</figcaption></figure></section>
<section id="places"><h2>{html.escape(l(lang, '三个重点区：可被想象的城市断面', 'Three key areas: urban sections one can imagine'))}</h2><div class="places">{area_items}</div><figure><img src="../assets/figures/key-areas{suffix}.png" alt="{html.escape(l(lang, '众智园、AI原点和大钟寺的三张概念空间断面与城市体验序列。', 'Three concept spatial sections and an urban-space sequence for Zhongzhiyuan, AI Origin and Dazhongsi.'))}"><figcaption>{html.escape(l(lang, '三种空间对象与概念城市体验序列', 'Three spatial objects and a conceptual urban-space sequence'))}</figcaption></figure></section>
<section id="systems"><h2>{html.escape(l(lang, '移动、蓝绿与服务必须一起运行', 'Mobility, blue-green and service must operate together'))}</h2><figure><img src="../assets/figures/mobility-bluegreen{suffix}.png" alt="{html.escape(l(lang, '移动、蓝绿、公共路径、服务维护和人工替代共同组成的城市系统图。', 'Urban systems diagram combining movement, blue-green, public routes, service/maintenance and human fallback.'))}"><figcaption>{html.escape(l(lang, '移动、蓝绿与运营系统', 'Mobility, blue-green and operational system'))}</figcaption></figure></section>
<section id="ai" class="quiet"><h2>{html.escape(l(lang, 'AI 只在确实改变空间状态处重要', 'AI matters only where it truly changes spatial state'))}</h2><p>{html.escape(l(lang, '三项深度任务包进入受控、可撤、可审查的载体。日常学习、普通商业、导视、等待与公共路径都必须在 AI 关闭时完整成立；没有真实任务、空间差异、同意与安全条件，即不新建。', 'Three deep task packets enter controlled, reversible and reviewable carriers. Ordinary learning, commerce, wayfinding, waiting and public routes must remain complete when AI is off; without a real task, spatial delta, consent and safety condition, there is NO BUILD.'))}</p></section>
<section id="evidence"><h2>{html.escape(l(lang, '证据与限制：把暂停画进设计', 'Evidence and limits: draw the pause into the design'))}</h2><figure><img src="../assets/figures/metrics-evidence{suffix}.png" alt="{html.escape(l(lang, '已知、设计规则和未知条件以及实施阶段门。', 'Known conditions, design rules, unknown conditions and implementation gates.'))}"><figcaption>{html.escape(l(lang, '证据、未知与实施门', 'Evidence, unknowns and implementation gates'))}</figcaption></figure></section>
<section class="audit" aria-label="{html.escape(l(lang, '核验索引', 'Verification index'))}"><div><h2>{html.escape(l(lang, '核心指标与任务覆盖', 'Core metrics and task coverage'))}</h2><p>{html.escape(l(lang, '总览地图把三层范围、重点区域、用地分区、交通慢行、蓝绿公共空间、建筑与更新项目放进空间叙事；AI 场景只在确实改变空间状态时进入。', 'The overall map places three-scale scope, key areas, land-use structure, mobility, blue-green public realm, buildings and renewal projects in the spatial story; AI scenarios enter only where they truly change spatial state.'))}</p><div class="audit-metrics"><div><span>{html.escape(l(lang, '临时场地面积', 'site_area_sqm'))}</span><b data-metric="site_area_sqm" data-value="{metric_values['site_area_sqm']['value']}">{metric_values['site_area_sqm']['value']:,.0f} m²</b></div><div><span>{html.escape(l(lang, '概念绿地比例', 'green_ratio'))}</span><b data-metric="green_ratio" data-value="{metric_values['green_ratio']['value']}">{metric_values['green_ratio']['value']:.1%}</b></div><div><span>{html.escape(l(lang, '概念公共空间比例', 'public_space_ratio'))}</span><b data-metric="public_space_ratio" data-value="{metric_values['public_space_ratio']['value']}">{metric_values['public_space_ratio']['value']:.1%}</b></div></div></div><aside><h3>{html.escape(l(lang, '自检状态、来源与假设', 'Self-check state, sources and assumptions'))}</h3><p>{html.escape(l(lang, '自检状态由官方四门写入。来源见 sources.json；假设见 assumptions.json。临时范围、法定指标、权属、容量与工程条件均须在官方数据到位后重算。', 'The self-check state is written by the official four gates. Sources are in sources.json; assumptions are in assumptions.json. Provisional extents, statutory controls, rights, capacity and engineering conditions all require recalculation when official data arrives.'))}</p></aside></section>
<section id="registers"><h2>{html.escape(l(lang, '完整登记册｜先看空间，再按需展开证据', 'Full registers | spatial story first, evidence on demand'))}</h2><p class="callout">{html.escape(l(lang, '完整机器登记仍保留在 JSON；本页的可展开版本提供离线、键盘可达的读法。', 'The complete machine registers remain in JSON; the expandable versions below provide an offline, keyboard-accessible reading path.'))}</p><details><summary>{html.escape(l(lang, '17 个状态 × 行动控制单元', '17 STATUS × ACTION control patches'))}</summary><table><thead><tr><th>{html.escape(l(lang, '控制单元', 'Patch'))}</th><th>{html.escape(l(lang, '状态', 'Status'))}</th><th>{html.escape(l(lang, '行动', 'Action'))}</th><th>{html.escape(l(lang, '空间后果', 'Spatial consequence'))}</th><th>{html.escape(l(lang, '阶段', 'Phase'))}</th></tr></thead><tbody>{patch_rows}</tbody></table></details><details><summary>{html.escape(l(lang, '15 项更新项目', '15 renewal projects'))}</summary><ul>{project_rows}</ul></details><details><summary>{html.escape(l(lang, '12 个 AI 场景', '12 AI scenarios'))}</summary><ul>{task_rows}</ul></details><details><summary>{html.escape(l(lang, '8 类人物与普通日常', '8 personas and the ordinary day'))}</summary><ul>{persona_rows}</ul></details></section>
<footer>{html.escape(l(lang, '离线页面：无 CDN、远程字体、地图瓦片、表单、追踪器或 API。图、空间与证据均为概念性、临时性表达；来源和假设见 package 内 sources.json 与 assumptions.json。', 'Offline page: no CDN, remote font, map tile, form, tracker or API. Figures, spaces and evidence are conceptual and provisional; see sources.json and assumptions.json in the package.'))}</footer>
</main></body></html>'''
    (VISUAL / f"index{suffix}.html").write_text(html_text + "\n", encoding="utf-8", newline="\n")


def load_data() -> dict[str, Any]:
    return {
        "site": shape(features("geometry/site_boundary.geojson")[0]["geometry"]),
        "areas": features("geometry/key_areas.geojson"),
        "land": features("geometry/land_use.geojson"),
        "roads": features("geometry/roads.geojson"),
        "green": features("geometry/green_space.geojson"),
        "public": features("geometry/public_space.geojson"),
        "buildings": features("geometry/buildings.geojson"),
        "register": read_json("visual/assets/status-action-register.json")["patches"],
        "projects": read_json("visual/assets/renewal-project-portfolio.json")["projects"],
        "simulation": read_json("simulation.json"),
        "metrics": read_json("metrics.json"),
    }


def normalize_report_heading_outline() -> None:
    """Keep the renderer's hero H1 as the single document-level heading.

    The frozen Markdown begins with the display title, while the official
    renderer already supplies that same title in its hero.  This derived-only
    normalization changes the duplicate body heading to H2 without touching a
    word of either proposal.
    """
    for name in ("proposal.html", "proposal.en.html"):
        path = ROOT / "report" / name
        text = path.read_text(encoding="utf-8")
        marker = "</section>\n<h1>"
        start = text.find(marker)
        normalized = text
        if start >= 0:
            content_start = start + len(marker)
            end = text.find("</h1>", content_start)
            if end < 0:
                raise RuntimeError(f"Expected renderer closing H1 is absent: {path}")
            normalized = text[:start] + "</section>\n<h2>" + text[content_start:end] + "</h2>" + text[end + len("</h1>"):]
        elif "</section>\n<h2>" not in text:
            raise RuntimeError(f"Expected renderer heading boundary is absent: {path}")
        if name == "proposal.html":
            normalized = normalized.replace(">Read in English<", ">英文版<")
        else:
            normalized = normalized.replace(">阅读中文版本<", ">Chinese version<")
        # Slightly enlarge superscript evidence references in the derived HTML;
        # their content and linking remain renderer-owned and unchanged.
        normalized = normalized.replace("font-size: 0.68em;", "font-size: 0.82em;")
        path.write_text(normalized, encoding="utf-8", newline="\n")


def main():
    if not ROOT.is_dir():
        raise SystemExit(f"Package root not found: {ROOT}")
    if not HISTORIC.is_file():
        raise SystemExit(f"Historic primitive module not found: {HISTORIC}")
    data = load_data()
    if len(data["register"]) != 17 or len(data["projects"]) != 15 or len(data["simulation"]["tasks"]) != 12:
        raise SystemExit("Refusing generation: RC1 source counts do not match the frozen package truth.")
    FIG.mkdir(parents=True, exist_ok=True); VISUAL.mkdir(parents=True, exist_ok=True); DRAWINGS.mkdir(parents=True, exist_ok=True)
    builders = {
        "site-overview": figure_site,
        "land-use-structure": figure_atlas,
        "key-areas": figure_key_areas,
        "mobility-bluegreen": figure_mobility,
        "metrics-evidence": figure_evidence,
    }
    for slug, builder in builders.items():
        for lang in ("zh", "en"):
            suffix = "" if lang == "zh" else ".en"
            builder(lang, data).save(FIG / f"{slug}{suffix}.png", "PNG", optimize=False, compress_level=9)
    for lang in ("zh", "en"):
        build_visual(lang, data)
        build_a3(lang)
        build_a0(lang)
    normalize_report_heading_outline()
    print(json.dumps({"status": "PASS", "run_id": "JZ-PRESENTATION-RELEASE-001", "package": str(ROOT), "figures": 10, "visual": 2, "pdfs": 4, "source_counts": {"patches": 17, "projects": 15, "tasks": 12}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
