#!/usr/bin/env python3
"""Build eight deterministic, evidence-status-controlled SVG maps.

The builder is deliberately offline. OSM is a committed contextual snapshot;
official repository polygons remain provisional constraints. Nothing produced
here establishes access, ownership, building condition or engineering fact.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / "site-context"
CONTEXT = BASE / "context"
FIGURES = ROOT / "figures"
RECEIPT = ROOT / "figure-hashes.json"
ATTRIBUTION = "© OpenStreetMap contributors, ODbL 1.0"
STATUS = {"VERIFIED", "CONTEXTUAL", "ASSUMED", "UNKNOWN", "PROVISIONAL"}
COLOURS = {
    "VERIFIED": "#17324d",
    "CONTEXTUAL": "#718096",
    "ASSUMED": "#c17b13",
    "UNKNOWN": "#a33b6b",
    "PROVISIONAL": "#6b46a1",
}


@dataclass(frozen=True)
class Claim:
    text: str
    status: str
    source_id: str
    as_of_date: str
    retrieval_date: str = "2026-08-12"


SPECS = (
    (
        "01-urban-fabrics.svg",
        "01 · Urban fabrics",
        "Footprint morphology is contextual; use, height, condition and renewal eligibility remain unknown.",
        "fabrics",
        (
            Claim("2095 contextual building footprints permit common-base morphology comparison only.", "CONTEXTUAL", "OSM-SNAPSHOT-R3", "2026-08-12"),
            Claim("The corridor has heterogeneous functions and cannot use one renewal method.", "VERIFIED", "S03", "2021-12-16"),
            Claim("Building adaptability and parcel action require survey.", "UNKNOWN", "S07+S30", "2026-07-14"),
        ),
    ),
    (
        "02-institutional-public-edges.svg",
        "02 · Institutional–public edges",
        "Named education/research context and entrances are leads; only access rules are verified.",
        "edges",
        (
            Claim("Public campus entry is reserved, timed and controlled.", "VERIFIED", "S20+S21", "2026-07-07"),
            Claim("OSM institutional polygons and entrances are contextual, not ownership/access evidence.", "CONTEXTUAL", "OSM-SNAPSHOT-R3", "2026-08-12"),
            Claim("Permanent public routes must not depend on campus interiors.", "VERIFIED", "S20+S21", "2026-07-07"),
        ),
    ),
    (
        "03-transit-thresholds.svg",
        "03 · Transit thresholds",
        "Three unequal gateways; contextual alignments are not catchments or engineering geometry.",
        "transit",
        (
            Claim("Qinghe is an operating regional multimodal gateway.", "VERIFIED", "S13", "2023-05-11"),
            Claim("Qinghua East Road West is current Line 15 and planned future 13×15 interchange.", "VERIFIED", "S17+S18", "2026-04-01"),
            Claim("Dazhongsi is an operating 12×13 interchange with a four-quadrant design task.", "VERIFIED", "S06+S14+S15", "2026-04-30"),
        ),
    ),
    (
        "04-public-space-and-heritage.svg",
        "04 · Public space and heritage",
        "Built, works-complete and planned states must not be collapsed into one future green line.",
        "public_heritage",
        (
            Claim("Phase 1 is open: Qinghua East Road–Zhichun Road, 2.5 km / 16.8 ha.", "VERIFIED", "S04", "2023-06-26"),
            Claim("Phase 2 supporting works are reported complete; full public continuity remains unproven.", "UNKNOWN", "S29", "2026-07-14"),
            Claim("Heritage anchors require professional control-band verification.", "VERIFIED", "S05+S28", "2026-07-14"),
        ),
    ),
    (
        "05-research-enterprise-service-relationships.svg",
        "05 · Research–enterprise–service relationships",
        "Official roles are real; firm movement, partnership and space-demand arrows remain hypotheses.",
        "relationships",
        (
            Claim("District strategy links knowledge, technology and industrial cultivation.", "VERIFIED", "S09", "2026-04-28"),
            Claim("AI Origin already contains named carriers and public programmes.", "VERIFIED", "S12", "2026-03-26"),
            Claim("Actual enterprise moves, shared-facility demand and floor-area transitions are unknown.", "UNKNOWN", "S06+S12", "2026-08-12"),
        ),
    ),
    (
        "06-servicing-and-barrier-questions.svg",
        "06 · Servicing and barrier questions",
        "Map questions, not invented freight routes, waste flows or current blockages.",
        "servicing",
        (
            Claim("Grade-separated road/rail relationships are verified in the southern context.", "VERIFIED", "S27", "2025-02-08"),
            Claim("Current delivery, waste, repair and worker conflicts are not evidenced.", "UNKNOWN", "S07+S30", "2026-08-12"),
            Claim("Every proposed crossing or service route requires a current field/engineering audit.", "ASSUMED", "R5-METHOD", "2026-08-12"),
        ),
    ),
    (
        "07-three-area-context-comparison.svg",
        "07 · Three-area context comparison",
        "Context windows use the same scale and source base; they are not official key-area redlines.",
        "comparison",
        (
            Claim("North: regional gateway + compound/water interface.", "VERIFIED", "S06+S13+S25", "2026-04-30"),
            Claim("Middle: controlled campus + delivered park + current/future transit.", "VERIFIED", "S04+S17+S20", "2026-07-07"),
            Claim("South: 12×13 interchange + heterogeneous renewal + grade separation.", "VERIFIED", "S14+S27+S30", "2026-07-14"),
        ),
    ),
    (
        "08-site-problem-atlas.svg",
        "08 · Site problem atlas",
        "Composite of evidence statuses A01–A14; no design move or candidate is encoded.",
        "atlas",
        (
            Claim("Layered rail/road and unequal fabrics are verified at corridor scale.", "VERIFIED", "S03+S27", "2025-02-08"),
            Claim("OSM provides contextual topology and named-place leads only.", "CONTEXTUAL", "OSM-SNAPSHOT-R3", "2026-08-12"),
            Claim("Exact polygons, buildings, access and environmental performance remain unknown.", "UNKNOWN", "OFFICIAL-GEOMETRY-CONTRACT", "2026-08-12"),
        ),
    ),
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_coords(value: Any) -> Iterable[tuple[float, float]]:
    if isinstance(value, list) and len(value) >= 2 and all(isinstance(v, (int, float)) for v in value[:2]):
        yield float(value[0]), float(value[1])
    elif isinstance(value, list):
        for item in value:
            yield from all_coords(item)


def sequences(geometry: dict[str, Any]) -> Iterable[list[list[float]]]:
    kind, coords = geometry.get("type"), geometry.get("coordinates", [])
    if kind == "LineString":
        yield coords
    elif kind == "Polygon":
        yield from coords
    elif kind == "MultiLineString":
        yield from coords
    elif kind == "MultiPolygon":
        for polygon in coords:
            yield from polygon


def bbox(payload: dict[str, Any]) -> tuple[float, float, float, float]:
    points = [p for f in payload.get("features", []) for p in all_coords(f.get("geometry", {}).get("coordinates", []))]
    xs, ys = zip(*points)
    return min(xs), min(ys), max(xs), max(ys)


def centroid(feature: dict[str, Any]) -> tuple[float, float]:
    points = list(all_coords(feature.get("geometry", {}).get("coordinates", [])))
    return sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)


def fid(feature: dict[str, Any]) -> str:
    return str(feature.get("id") or feature.get("properties", {}).get("id", ""))


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


class Renderer:
    def __init__(self, study_bbox: tuple[float, float, float, float]) -> None:
        self.width, self.height = 1280, 980
        self.map_x, self.map_y, self.map_w, self.map_h = 48, 120, 820, 770
        west, south, east, north = study_bbox
        x_scale = math.cos(math.radians((south + north) / 2))
        scale = min(self.map_w / ((east - west) * x_scale), self.map_h / (north - south))
        used_w, used_h = (east - west) * x_scale * scale, (north - south) * scale
        x0 = self.map_x + (self.map_w - used_w) / 2
        y0 = self.map_y + (self.map_h - used_h) / 2
        self.project = lambda lon, lat: (x0 + (lon - west) * x_scale * scale, y0 + (north - lat) * scale)

    def path(self, sequence: list[list[float]], close: bool) -> str:
        points = [self.project(p[0], p[1]) for p in sequence]
        if not points:
            return ""
        return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points) + (" Z" if close else "")

    def collection(self, out: list[str], data: dict[str, Any], stroke: str, width: float, *, fill: str = "none", opacity: float = 1.0, dash: str = "", limit: int = 1800, points: bool = True) -> None:
        features = sorted(data.get("features", []), key=fid)
        if len(features) > limit:
            features = features[:: math.ceil(len(features) / limit)]
        for feature in features:
            geom = feature.get("geometry", {})
            if geom.get("type") == "Point":
                if points:
                    x, y = self.project(*geom["coordinates"][:2])
                    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{stroke}" opacity="{opacity}"/>')
                continue
            close = geom.get("type") in {"Polygon", "MultiPolygon"}
            for seq in sequences(geom):
                d = self.path(seq, close)
                if d:
                    out.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" opacity="{opacity}" stroke-dasharray="{dash}"/>')

    def point(self, out: list[str], lon: float, lat: float, label: str, status: str, dx: int = 9, dy: int = -8) -> None:
        x, y = self.project(lon, lat)
        colour = COLOURS[status]
        if status == "UNKNOWN":
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#fff" stroke="{colour}" stroke-width="2.5"/>')
            out.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="700" fill="{colour}">?</text>')
        else:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{colour}" stroke="#fff" stroke-width="2"/>')
        out.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" font-family="Arial,Microsoft YaHei,sans-serif" font-size="11" fill="{colour}">{esc(label)}</text>')


def load_inputs() -> dict[str, dict[str, Any]]:
    names = {
        "official": "official-provisional-boundaries.geojson",
        "study": "study-area-bbox.geojson",
        "anchors": "contextual-anchors.geojson",
        "buildings": "osm-building-footprints.geojson",
        "streets": "osm-streets.geojson",
        "rail": "osm-rail.geojson",
        "transit": "osm-transit.geojson",
        "innovation": "osm-research-innovation.geojson",
        "commercial": "osm-commercial-services.geojson",
        "services": "osm-public-services.geojson",
        "green": "osm-green-water.geojson",
    }
    return {key: read_json(CONTEXT / name) for key, name in names.items()}


def official_constraints(renderer: Renderer, out: list[str], official: dict[str, Any]) -> None:
    for feature in official.get("features", []):
        feature_id = fid(feature)
        if feature_id == "PROV-RESEARCH-001":
            renderer.collection(out, {"features": [feature]}, COLOURS["PROVISIONAL"], 1.0, dash="8 7")
        elif feature_id == "PROV-SITE-001":
            renderer.collection(out, {"features": [feature]}, COLOURS["PROVISIONAL"], 2.0, dash="8 5")
        elif feature_id.startswith("PROV-KEY-00"):
            renderer.collection(out, {"features": [feature]}, COLOURS["PROVISIONAL"], 1.5, dash="4 4")
            x, y = renderer.project(*centroid(feature))
            out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" font-weight="700" fill="{COLOURS["PROVISIONAL"]}">{esc(feature_id)} · CONTEXT WINDOW</text>')


def named_points(renderer: Renderer, out: list[str], data: dict[str, Any], names: tuple[str, ...], status: str) -> None:
    used: set[str] = set()
    for feature in sorted(data.get("features", []), key=fid):
        props = feature.get("properties", {})
        name = str(props.get("name:en") or props.get("name") or props.get("name:zh") or "")
        if feature.get("geometry", {}).get("type") != "Point" or not name or name in used:
            continue
        if any(token.casefold() in name.casefold() for token in names):
            renderer.point(out, *feature["geometry"]["coordinates"][:2], name, status)
            used.add(name)


def render(path: Path, spec: tuple[Any, ...], data: dict[str, dict[str, Any]]) -> None:
    filename, title, subtitle, mode, claims = spec
    for claim in claims:
        if claim.status not in STATUS or not claim.source_id or not claim.as_of_date or not claim.retrieval_date:
            raise ValueError(f"invalid claim metadata in {filename}")
    renderer = Renderer(bbox(data["study"]))
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="980" viewBox="0 0 1280 980">',
        '<g data-evidence-id="PROV-SITE-001" data-status="PROVISIONAL"></g>',
        '<rect width="1280" height="980" fill="#f7f5ef"/>',
        f'<text x="48" y="48" font-family="Arial,Microsoft YaHei,sans-serif" font-size="29" font-weight="700" fill="#17202a">{esc(title)}</text>',
        f'<text x="48" y="78" font-family="Arial,Microsoft YaHei,sans-serif" font-size="14" fill="#52616b">{esc(subtitle)}</text>',
        '<rect x="48" y="120" width="820" height="770" rx="8" fill="#fff" stroke="#d2d8dc"/>',
    ]

    # Neutral common base.
    renderer.collection(out, data["streets"], "#c7cdd1", 0.65, opacity=0.55, limit=1900)
    if mode in {"fabrics", "edges", "comparison", "atlas"}:
        renderer.collection(out, data["buildings"], "#b9afa0", 0.35, fill="#e7e1d6", opacity=0.55, limit=1300)
    if mode in {"transit", "public_heritage", "servicing", "atlas"}:
        renderer.collection(out, data["rail"], "#40515d", 2.0, opacity=0.85, limit=600)
    if mode in {"transit", "comparison", "atlas"}:
        renderer.collection(out, data["transit"], COLOURS["CONTEXTUAL"], 2.0, opacity=0.75, limit=400)
    if mode in {"edges", "relationships", "comparison", "atlas"}:
        renderer.collection(out, data["innovation"], "#2c7a7b", 1.4, fill="#c6ede7", opacity=0.68, limit=500)
    if mode == "relationships":
        renderer.collection(out, data["commercial"], "#b7791f", 2.4, opacity=0.65, limit=650)
        renderer.collection(out, data["services"], "#c05621", 2.2, opacity=0.55, limit=750)
    if mode in {"public_heritage", "atlas"}:
        for feature in data["green"].get("features", []):
            props = feature.get("properties", {})
            is_water = props.get("context_class") == "water" or "waterway" in props
            renderer.collection(out, {"features": [feature]}, "#3182a5" if is_water else "#4f8a5b", 1.0, fill="#c6e2ee" if is_water else "#cce5c8", opacity=0.55)

    official_constraints(renderer, out, data["official"])

    if mode == "transit":
        named_points(renderer, out, data["transit"], ("Qinghe", "清河", "Wudaokou", "五道口", "Dazhongsi", "大钟寺", "Qinghuadongluxikou", "清华东路西口"), "CONTEXTUAL")
    elif mode == "edges":
        named_points(renderer, out, data["innovation"], ("Tsinghua", "清华", "Beihang", "北航", "Beijing Forestry", "林业大学"), "CONTEXTUAL")
        for lon, lat, label in ((116.347, 40.000, "gate/access audit"), (116.348, 39.991, "public-side interface?"), (116.344, 40.008, "opening hours?")):
            renderer.point(out, lon, lat, label, "UNKNOWN")
    elif mode == "public_heritage":
        for feature in data["anchors"].get("features", []):
            renderer.point(out, *feature["geometry"]["coordinates"][:2], feature["properties"]["name_zh"], "CONTEXTUAL")
        renderer.point(out, 116.346, 39.989, "Phase 1 open (schematic anchor)", "VERIFIED")
        renderer.point(out, 116.343, 39.958, "later works: continuity audit", "UNKNOWN")
    elif mode == "relationships":
        for lon, lat, label in ((116.346, 40.019, "North: validation context"), (116.347, 39.997, "Middle: transfer context"), (116.3384, 39.9657, "South: market/service context")):
            renderer.point(out, lon, lat, label, "VERIFIED")
        for (a, b) in (((116.346, 40.019), (116.347, 39.997)), ((116.347, 39.997), (116.3384, 39.9657))):
            ax, ay = renderer.project(*a); bx, by = renderer.project(*b)
            out.append(f'<path d="M {ax:.1f},{ay:.1f} L {bx:.1f},{by:.1f}" stroke="{COLOURS["UNKNOWN"]}" stroke-width="2" stroke-dasharray="6 6" fill="none"/>')
    elif mode == "servicing":
        for lon, lat, label in ((116.340, 39.967, "four-quadrant/grade audit"), (116.349, 39.996, "delivery/service audit"), (116.347, 40.018, "equipment/service audit")):
            renderer.point(out, lon, lat, label, "UNKNOWN")
    elif mode == "comparison":
        for feature in data["official"].get("features", []):
            if fid(feature).startswith("PROV-KEY-00"):
                x, y = renderer.project(*centroid(feature))
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="28" fill="none" stroke="{COLOURS["UNKNOWN"]}" stroke-width="2" stroke-dasharray="2 5"/>')
    elif mode == "atlas":
        for lon, lat, label, status in (
            (116.346, 40.020, "A03 regional threshold", "VERIFIED"),
            (116.348, 39.997, "A05 controlled edge", "VERIFIED"),
            (116.3384, 39.9657, "A03 south geometry conflict", "CONTEXTUAL"),
            (116.343, 39.956, "A02 current crossing?", "UNKNOWN"),
            (116.349, 40.008, "A10 servicing?", "UNKNOWN"),
        ):
            renderer.point(out, lon, lat, label, status)

    # Evidence sidecar.
    out.append('<text x="900" y="145" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="#17202a">Evidence claims</text>')
    y = 180
    for claim in claims:
        colour = COLOURS[claim.status]
        out.append(f'<rect x="900" y="{y-11}" width="10" height="10" fill="{colour}"/>')
        words = claim.text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            if len(current) + len(word) > 43:
                lines.append(current); current = word
            else:
                current = (current + " " + word).strip()
        if current: lines.append(current)
        for line in lines:
            out.append(f'<text x="918" y="{y}" font-family="Arial,Microsoft YaHei,sans-serif" font-size="11" fill="#34495e">{esc(line)}</text>'); y += 16
        out.append(f'<text x="918" y="{y}" font-family="Arial,sans-serif" font-size="9.5" fill="{colour}">{claim.status} · {esc(claim.source_id)} · as of {esc(claim.as_of_date)}</text>')
        y += 34

    out.append('<text x="900" y="560" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="#17202a">Status legend</text>')
    for index, key in enumerate(("VERIFIED", "CONTEXTUAL", "ASSUMED", "UNKNOWN", "PROVISIONAL")):
        yy = 590 + index * 28
        out.append(f'<line x1="900" y1="{yy}" x2="930" y2="{yy}" stroke="{COLOURS[key]}" stroke-width="4" stroke-dasharray="{("5 4" if key in {"ASSUMED", "PROVISIONAL"} else "")}"/>')
        out.append(f'<text x="940" y="{yy+4}" font-family="Arial,sans-serif" font-size="11" fill="#34495e">{key}</text>')
    notes = ("No commercial map tiles or remote assets.", "No ownership/access/capacity/condition inference.", "Dashed violet polygons are provisional and unfilled.", "Exact official geometry replacement is mandatory.")
    for index, note in enumerate(notes):
        out.append(f'<text x="900" y="{760 + index*20}" font-family="Arial,sans-serif" font-size="10.5" fill="#566573">{esc(note)}</text>')
    out.append(f'<text x="48" y="935" font-family="Arial,sans-serif" font-size="11" fill="#566573">Sources: public primary-source ledger + committed vector snapshot. {esc(ATTRIBUTION)}.</text>')
    out.append('<text x="48" y="957" font-family="Arial,sans-serif" font-size="11" font-weight="700" fill="#922b21">EVIDENCE ATLAS · NOT OFFICIAL · NOT A REDLINE · NOT A CANDIDATE DESIGN</text>')
    out.append('</svg>')
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def build(output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data = load_inputs()
    hashes: dict[str, str] = {}
    for spec in SPECS:
        path = output_dir / spec[0]
        render(path, spec, data)
        text = path.read_text(encoding="utf-8")
        if "<image" in text or " href=" in text or " xlink:href=" in text:
            raise ValueError(f"remote/unlicensed asset reference in {path.name}")
        if "PROV-SITE-001" not in text or "PROVISIONAL" not in text or ATTRIBUTION not in text:
            raise ValueError(f"missing evidence boundary in {path.name}")
        hashes[path.name] = digest(path)
    return hashes


def receipt(hashes: dict[str, str]) -> dict[str, Any]:
    input_paths = sorted(CONTEXT.glob("*.geojson"))
    return {
        "schema_version": "1.0",
        "generated_date": "2026-08-12",
        "builder": "research/site-evidence-v2/generate_maps.py",
        "classification": ["EVIDENCE_ATLAS", "NOT_OFFICIAL", "NOT_A_REDLINE", "NOT_A_CANDIDATE_DESIGN"],
        "input_hashes": {str(p.relative_to(ROOT.parent.parent)).replace("\\", "/"): digest(p) for p in input_paths},
        "figure_hashes": dict(sorted(hashes.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="rebuild in a temporary directory and compare hashes")
    args = parser.parse_args()
    if args.check:
        if not RECEIPT.exists():
            raise SystemExit("missing figure-hashes.json; run builder first")
        expected = read_json(RECEIPT)
        with tempfile.TemporaryDirectory(prefix="jz-site-v2-") as temp:
            hashes = build(Path(temp))
        actual = receipt(hashes)
        if actual != expected:
            raise SystemExit("site evidence map determinism check failed")
        for name, expected_hash in hashes.items():
            if not (FIGURES / name).exists() or digest(FIGURES / name) != expected_hash:
                raise SystemExit(f"committed output drift: {name}")
        print("SITE_EVIDENCE_V2_MAP_CHECK=PASS")
        return 0
    hashes = build(FIGURES)
    RECEIPT.write_text(json.dumps(receipt(hashes), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(f"SITE_MAPS_GENERATED={len(hashes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
