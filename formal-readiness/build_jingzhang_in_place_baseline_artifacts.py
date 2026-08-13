#!/usr/bin/env python3
"""Build deterministic bilingual v0 figures, visual shells, and A3/A0 PDFs."""

from __future__ import annotations

import hashlib
import html
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(r"V:\src\haidian\submissions\JerrySkywalker\jingzhang-in-place")
FIG = ROOT / "assets" / "figures"
DRAWINGS = ROOT / "drawings"
REPORT = ROOT / "report"
VISUAL = ROOT / "visual"
FONT_ZH = Path(r"C:\Windows\Fonts\msyh.ttc")
FONT_ZH_FALLBACK = Path(r"C:\Windows\Fonts\simhei.ttf")
FONT_EN = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_EN_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")
NAVY = "#17324d"
GREEN = "#3f7f6b"
AMBER = "#c17b13"
MAGENTA = "#a33b6b"
SLATE = "#718096"
PAPER = "#f5f1e8"
INK = "#17212b"
ACCENT = "#d65a3a"


def font_path(zh: bool, bold: bool = False) -> Path:
    if zh:
        return FONT_ZH if FONT_ZH.exists() else FONT_ZH_FALLBACK
    return FONT_EN_BOLD if bold and FONT_EN_BOLD.exists() else FONT_EN


def pil_font(size: int, zh: bool, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(font_path(zh, bold)), size=size, index=0)


def text(draw: ImageDraw.ImageDraw, xy, value: str, size: int, zh: bool, fill=INK, bold=False, anchor=None):
    draw.text(xy, value, font=pil_font(size, zh, bold), fill=fill, anchor=anchor)


def card(draw, box, title, body, zh, color=NAVY):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=22, fill="#ffffff", outline=color, width=4)
    text(draw, (x0 + 26, y0 + 24), title, 28, zh, color, True)
    y = y0 + 72
    for line in body:
        text(draw, (x0 + 28, y), line, 20, zh, INK)
        y += 34


def base(title_zh, title_en, lang):
    zh = lang == "zh"
    im = Image.new("RGB", (2400, 1500), PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 2400, 16), fill=ACCENT)
    text(d, (90, 70), title_zh if zh else title_en, 56, zh, NAVY, True)
    text(d, (90, 136), "京张续城 / Jing-Zhang In Place", 25, True, SLATE)
    text(d, (2310, 90), "FORMAL BASELINE V0.1", 19, False, SLATE, anchor="ra")
    return im, d, zh


def footer(d, zh):
    note = "临时范围｜概念图｜非地块/法定控制" if zh else "PROVISIONAL EXTENT | CONCEPT DIAGRAM | NOT PARCEL OR STATUTORY CONTROL"
    text(d, (90, 1450), note, 18, zh, MAGENTA)
    text(d, (2310, 1450), "offline deterministic export", 17, False, SLATE, anchor="ra")


def figure_site(lang):
    im, d, zh = base("场地证据状态与三层范围", "Site evidence status and three scales", lang)
    labels = [("43.6 km²\n资产与接口" if zh else "43.6 km²\nassets + interfaces", NAVY, 160),
              ("11.4 km²\n状态—行动拼图" if zh else "11.4 km²\nstatus × action", GREEN, 440),
              ("3 个重点区\n不等断面" if zh else "3 key areas\nunequal sections", AMBER, 720)]
    for label, color, inset in labels:
        d.rounded_rectangle((180+inset, 300+inset//5, 2220-inset, 1260-inset//5), radius=50, outline=color, width=8)
        for i, line in enumerate(label.split("\n")):
            text(d, (1200, 345+inset//5+i*44), line, 30 if i else 34, zh, color, True, "ma")
    statuses = [("已建运行" if zh else "BUILT / OPERATING", NAVY), ("获批/实施" if zh else "APPROVED / IN DELIVERY", GREEN), ("受控进入" if zh else "CONTROLLED", AMBER), ("待调查" if zh else "SURVEY UNKNOWN", MAGENTA)]
    for i,(label,color) in enumerate(statuses):
        x=230+i*505; d.rectangle((x,1190,x+35,1225),fill=color); text(d,(x+52,1188),label,20,zh,INK)
    footer(d, zh); return im


def figure_structure(lang):
    im, d, zh = base("状态—行动总体空间结构", "Status–action overall spatial structure", lang)
    rows = [
        ("北｜水—院区—区域到达" if zh else "NORTH | water–compound–regional arrival", NAVY, ["调查" if zh else "SURVEY", "保留" if zh else "RETAIN", "适应" if zh else "ADAPT"]),
        ("中｜校园公开侧阈值" if zh else "MIDDLE | public-side campus thresholds", GREEN, ["受控" if zh else "CONTROL", "修复" if zh else "REPAIR", "边缘" if zh else "EDGE"]),
        ("南｜立体站城更新" if zh else "SOUTH | grade-separated station-city renewal", AMBER, ["未知" if zh else "UNKNOWN", "重连" if zh else "RECONNECT", "填补" if zh else "INFILL"]),
    ]
    for r,(title,color,acts) in enumerate(rows):
        y=280+r*340; text(d,(120,y),title,30,zh,color,True)
        for c,a in enumerate(acts):
            x=190+c*570
            d.rounded_rectangle((x,y+75,x+430,y+260),radius=26,fill="#ffffff",outline=color,width=5)
            text(d,(x+215,y+145),a,27,zh,color,True,"mm")
            if c<2: d.line((x+430,y+168,x+555,y+168),fill=SLATE,width=6)
    text(d,(120,1335),"公共路 / 立体阈值 / 受控阈值 / 轨道·水系·遗产接口" if zh else "public route / grade threshold / controlled threshold / transit–water–heritage interface",24,zh,MAGENTA)
    footer(d, zh); return im


def figure_areas(lang):
    im, d, zh = base("三个不等片区与控制断面", "Three unequal areas and controlling sections", lang)
    bodies = [
        ((100,260,800,1260),"众智园" if zh else "Zhongzhiyuan",["水—院区—区域到达" if zh else "water–compound–regional arrival","公共河园｜安全边界｜验证载体" if zh else "public river/park | safety | test carrier","先项目协调，后可撤试点" if zh else "coordinate first; reversible pilot"],NAVY),
        ((850,260,1550,1260),"AI 原点" if zh else "AI Origin",["校园公开侧阈值" if zh else "public-side campus threshold","永久城市路｜普通房间｜临时受控" if zh else "city route | ordinary room | timed control","不以校园内部作捷径" if zh else "no campus shortcut"],GREEN),
        ((1600,260,2300,1260),"大钟寺" if zh else "Dazhongsi",["立体站城更新" if zh else "grade-separated station-city renewal","站口｜前庭｜普通服务｜评审" if zh else "exit | forecourt | service | review","不以临时矩形作地块方案" if zh else "no parcel plan from placeholder"],AMBER),
    ]
    for box,title,body,color in bodies:
        card(d,box,title,body,zh,color)
        x0,y0,x1,y1=box
        for j in range(3):
            yy=y0+390+j*185
            d.line((x0+90,yy,x1-90,yy),fill=color,width=10-j*2)
            d.ellipse((x0+145+j*120,yy-35,x0+215+j*120,yy+35),fill="#ffffff",outline=color,width=5)
    footer(d, zh); return im


def figure_systems(lang):
    im, d, zh = base("公共、蓝绿、交通与服务系统", "Public, blue-green, mobility and service systems", lang)
    systems=[("普通公共网络" if zh else "ORDINARY PUBLIC NETWORK",NAVY,330),("河园与生活系统" if zh else "PARK–WATER + LIVING SYSTEMS",GREEN,570),("调查后服务系统" if zh else "SURVEY-GATED SERVICE SYSTEM",AMBER,810)]
    for label,color,y in systems:
        text(d,(140,y-72),label,26,zh,color,True)
        pts=[(240,y),(650,y-55),(1050,y+40),(1450,y-25),(1850,y+55),(2180,y)]
        d.line(pts,fill=color,width=18,joint="curve")
        for p in pts: d.ellipse((p[0]-22,p[1]-22,p[0]+22,p[1]+22),fill=PAPER,outline=color,width=7)
    card(d,(250,1050,1050,1310),"AI-OFF" if not zh else "AI 关闭",["固定导视、人工帮助、普通房间仍运行" if zh else "fixed signs, staffed help and ordinary rooms remain"],zh,NAVY)
    card(d,(1350,1050,2150,1310),"AI MATTERS" if not zh else "AI 实质改变",["少量验证/受控协作/评审改变断面与运营" if zh else "selected validation, controlled work and review change sections/operations"],zh,ACCENT)
    footer(d, zh); return im


def figure_metrics(lang):
    im, d, zh = base("指标、证据状态与生产缺口", "Metrics, evidence state and production gaps", lang)
    stats=[("12","AI 场景" if zh else "AI scenarios",NAVY),("3","产业验证" if zh else "industry tests",GREEN),("8","使用者" if zh else "personas",AMBER),("4","控制 patch" if zh else "control patches",MAGENTA)]
    for i,(n,label,color) in enumerate(stats):
        x=120+i*565
        d.rounded_rectangle((x,260,x+500,650),radius=30,fill="#ffffff",outline=color,width=5)
        text(d,(x+250,380),n,100,False,color,True,"mm")
        text(d,(x+250,550),label,25,zh,INK,True,"mm")
    gaps=[("官方精确边界" if zh else "exact organizer geometry",MAGENTA),("建筑/使用者调查" if zh else "building + incumbent surveys",AMBER),("市政/工程容量" if zh else "utility + engineering capacity",AMBER),("专业断面与终版图件" if zh else "professional sections + final graphics",SLATE)]
    text(d,(120,770),"不得伪精确的缺口" if zh else "GAPS THAT MUST NOT BE FABRICATED",30,zh,NAVY,True)
    for i,(label,color) in enumerate(gaps):
        y=850+i*110; d.rounded_rectangle((150,y,2250,y+72),radius=22,fill="#ffffff",outline=color,width=4); text(d,(190,y+19),label,23,zh,INK)
    footer(d, zh); return im


FIGURES = {
    "site-overview": figure_site,
    "land-use-structure": figure_structure,
    "key-areas": figure_areas,
    "mobility-bluegreen": figure_systems,
    "metrics-evidence": figure_metrics,
}


def build_figures():
    FIG.mkdir(parents=True, exist_ok=True)
    for slug, fn in FIGURES.items():
        for lang in ("zh", "en"):
            suffix = "" if lang == "zh" else ".en"
            path = FIG / f"{slug}{suffix}.png"
            fn(lang).save(path, "PNG", optimize=False, compress_level=9)


def pdf_font():
    path = font_path(True)
    try:
        pdfmetrics.registerFont(TTFont("JZSans", str(path), subfontIndex=0))
    except TypeError:
        pdfmetrics.registerFont(TTFont("JZSans", str(path)))
    return "JZSans"


def build_pdf(path: Path, lang: str, page: str):
    zh = lang == "zh"
    mm = 72 / 25.4
    size_mm = (420, 297) if page == "A3" else (1189, 841)
    w, h = size_mm[0] * mm, size_mm[1] * mm
    c = Canvas(str(path), pagesize=(w, h), pageCompression=1, invariant=1)
    font = pdf_font()
    c.setFillColor(HexColor(PAPER)); c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(HexColor(ACCENT)); c.rect(0, h-5*mm, w, 5*mm, fill=1, stroke=0)
    c.setFillColor(HexColor(NAVY)); c.setFont(font, 24 if page=="A3" else 48)
    title_y = h-(25 if page=="A3" else 32)*mm
    subtitle_y = h-(34 if page=="A3" else 46)*mm
    c.drawString(18*mm, title_y, "京张续城 / Jing-Zhang In Place")
    c.setFont(font, 10 if page=="A3" else 23); c.setFillColor(HexColor(SLATE))
    subtitle = "A3 基线文册｜状态—行动拼图｜非终版" if zh and page=="A3" else "A0 基线展板｜状态—行动拼图｜非终版" if zh else f"{page} BASELINE | STATUS × ACTION PATCHWORK | NOT FINAL"
    c.drawString(18*mm, subtitle_y, subtitle)
    names=list(FIGURES.keys())
    if page=="A3":
        positions=[(18,30,184,106),(218,30,184,106),(18,146,184,106),(218,146,184,106)]
        selected=names[:4]
    else:
        positions=[(25,55,550,330),(614,55,550,330),(25,440,360,330),(414,440,360,330),(803,440,360,330)]
        selected=names
    for slug,(x,y,ww,hh) in zip(selected,positions):
        suffix="" if zh else ".en"
        c.drawImage(str(FIG/f"{slug}{suffix}.png"),x*mm,(size_mm[1]-y-hh)*mm,ww*mm,hh*mm,preserveAspectRatio=True,anchor="c",mask="auto")
    c.setFillColor(white); c.setFont(font, 7 if page=="A3" else 18)
    c.drawRightString(w-12*mm, 9*mm, "PROVISIONAL EXTENT | CONCEPT BASELINE V0.1 | OFFLINE EXPORT")
    c.showPage(); c.save()


def build_visual(lang):
    zh = lang == "zh"
    suffix = "" if zh else ".en"
    title = "京张续城｜离线图件索引" if zh else "Jing-Zhang In Place | Offline visual index"
    cards=[]
    for slug in FIGURES:
        img=f"../assets/figures/{slug}{suffix}.png"
        cards.append(f'<figure id="{slug}"><img src="{html.escape(img)}" alt="{html.escape(slug)}"><figcaption>{html.escape(slug)}</figcaption></figure>')
    body="\n".join(cards)
    if zh:
        appendix = '<section aria-label="核心指标与覆盖"><h2>核心指标 · 任务覆盖 · 自检状态</h2><p><span data-metric="site_area_sqm" data-value="11412825.386">总体设计临时范围 11,412,825.386 m²</span>；<span data-metric="green_ratio" data-value="0.123423">概念绿地率 12.3423%</span>；<span data-metric="public_space_ratio" data-value="0.073281">概念公共空间率 7.3281%</span>。三项均只用于临时范围内的图数一致性检查，不是现状或法定指标。</p><p>本离线阅读壳覆盖：总览地图、三层范围、重点区域、用地分区、交通慢行、蓝绿公共空间、建筑、更新项目、AI 场景、来源与假设。当前自检状态：BASELINE / NOT READY FOR REVIEW。</p></section>'
    else:
        appendix = '<section aria-label="metrics and coverage"><h2>Core metrics · task coverage · self-check state</h2><p><span data-metric="site_area_sqm" data-value="11412825.386">Provisional overall-design envelope 11,412,825.386 m²</span>; <span data-metric="green_ratio" data-value="0.123423">concept green ratio 12.3423%</span>; <span data-metric="public_space_ratio" data-value="0.073281">concept public-space ratio 7.3281%</span>. These values test figure/data consistency inside provisional geometry; they are neither existing-condition nor statutory metrics.</p><p>This offline shell covers the overview map, three scope levels, key areas, land-use structure, mobility, blue-green public space, buildings, renewal actions, AI scenarios, sources and assumptions. Self-check state: BASELINE / NOT READY FOR REVIEW.</p></section>'
    content=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>body{{margin:0;background:{PAPER};color:{INK};font-family:"Microsoft YaHei",Arial,sans-serif}}header{{padding:32px 5vw;border-top:10px solid {ACCENT}}}h1{{color:{NAVY}}}.warn{{color:{MAGENTA};font-weight:700}}main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(430px,1fr));gap:24px;padding:0 5vw 5vw}}figure,section{{margin:0;background:#fff;border:1px solid #ccd4dc;padding:12px}}img{{width:100%;height:auto;display:block}}figcaption{{padding:9px;color:{SLATE}}}</style></head><body><header><h1>{html.escape(title)}</h1><p class="warn">{"临时范围、概念基线；不是地块或法定控制。" if zh else "Provisional extent and concept baseline; not parcel or statutory control."}</p><p>{"AI 关闭时普通城市完整；AI 只改变经核验的少量任务与空间状态。" if zh else "The ordinary city remains complete with AI off; AI changes only selected verified tasks and spatial states."}</p></header><main>{body}{appendix}</main></body></html>'''
    (VISUAL/f"index{suffix}.html").write_text(content,encoding="utf-8",newline="\n")


def receipt():
    outputs=[]
    for p in sorted(list(FIG.glob("*.png"))+list(DRAWINGS.glob("*.pdf"))+list(VISUAL.glob("index*.html"))):
        outputs.append({"path":p.relative_to(ROOT).as_posix(),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size})
    data={"schema_version":"0.1.0","generator":"formal-readiness/build_jingzhang_in_place_baseline_artifacts.py","runtime":"Python 3.12; Pillow 12.3.0; ReportLab project local","fonts":{"zh":"Microsoft YaHei system font; not redistributed","en":"Arial system font; not redistributed"},"offline":True,"outputs":outputs}
    receipt_path = Path(__file__).resolve().parents[1] / "runs" / "JZ-FORMAL-KICKOFF-001" / "EXPORT_RECEIPT.json"
    receipt_path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")


def main():
    DRAWINGS.mkdir(exist_ok=True); REPORT.mkdir(exist_ok=True); VISUAL.mkdir(exist_ok=True)
    build_figures()
    build_pdf(DRAWINGS/"a3-booklet.pdf","zh","A3")
    build_pdf(DRAWINGS/"a3-booklet.en.pdf","en","A3")
    build_pdf(DRAWINGS/"a0-boards.pdf","zh","A0")
    build_pdf(DRAWINGS/"a0-boards.en.pdf","en","A0")
    build_visual("zh"); build_visual("en"); receipt()
    print(json.dumps({"status":"PASS","figures":10,"pdfs":4,"visual_html":2},ensure_ascii=False))


if __name__ == "__main__":
    main()
