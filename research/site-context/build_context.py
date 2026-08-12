#!/usr/bin/env python3
"""Build a bounded, reproducible contextual base for Round 3.

Outputs are contextual/derived design-research aids. They are NOT official,
NOT statutory, NOT site-calibrated, and must not be used to infer ownership,
population, service capacity, service hours, or engineering feasibility.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
CONTEXT = ROOT / "context"
DERIVED = ROOT / "derived"
FIGURES = ROOT / "figures"
OFFICIAL_HEAD = "e9741a415aeb5cf09ca27608f6c97c33145a589f"
RAW_BASE = f"https://raw.githubusercontent.com/open-city-ai/haidian/{OFFICIAL_HEAD}"
OFFICIAL_FILES = {
    "official-provisional-boundaries.geojson": (
        f"{RAW_BASE}/brief/site-package/geometry/provisional_boundaries.geojson"
    ),
    "study-area-bbox.geojson": (
        f"{RAW_BASE}/brief/site-package/geometry/study_area_bbox.geojson"
    ),
}
OVERPASS_ENDPOINTS = (
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
)
ATTRIBUTION = "© OpenStreetMap contributors, ODbL 1.0"
USER_AGENT = "jingzhang-ai-design-lab-round3/1.0 (public design research)"

LAYER_FILES = {
    "streets": "osm-streets.geojson",
    "rail": "osm-rail.geojson",
    "transit": "osm-transit.geojson",
    "daily_life": "osm-public-services.geojson",
    "commercial_services": "osm-commercial-services.geojson",
    "green_water": "osm-green-water.geojson",
    "innovation": "osm-research-innovation.geojson",
    "buildings": "osm-building-footprints.geojson",
}

KEEP_TAGS = {
    "name", "name:en", "name:zh", "alt_name", "highway", "railway",
    "public_transport", "station", "subway", "amenity", "shop", "office",
    "research_institution", "landuse", "leisure", "natural", "waterway",
    "building", "foot", "bicycle", "access", "service", "bridge", "tunnel",
    "covered", "wheelchair", "opening_hours", "operator", "heritage",
    "historic", "tourism",
}

PUBLIC_AMENITIES = {
    "school", "kindergarten", "college", "university", "library", "hospital",
    "clinic", "pharmacy", "community_centre", "social_facility", "toilets",
    "marketplace", "arts_centre", "theatre", "cinema", "place_of_worship",
    "police", "fire_station", "post_office", "townhall",
}
SELECTED_SHOPS = {
    "supermarket", "convenience", "mall", "bakery", "greengrocer", "chemist",
    "books", "bicycle", "department_store", "laundry", "hairdresser",
}
GREEN_LANDUSE = {"grass", "forest", "recreation_ground", "meadow", "village_green"}
INNOVATION_AMENITIES = {"university", "college", "research_institute", "library"}


def ensure_dirs() -> None:
    for path in (CONTEXT, DERIVED, FIGURES):
        path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_json(url: str, data: bytes | None = None, timeout: int = 120) -> Any:
    request = urllib.request.Request(
        url,
        data=data,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        method="POST" if data is not None else "GET",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def bbox_from_geojson(payload: dict[str, Any]) -> tuple[float, float, float, float]:
    coords: list[tuple[float, float]] = []

    def visit(value: Any) -> None:
        if isinstance(value, list) and len(value) >= 2 and all(
            isinstance(item, (int, float)) for item in value[:2]
        ):
            coords.append((float(value[0]), float(value[1])))
        elif isinstance(value, list):
            for item in value:
                visit(item)

    for feature in payload.get("features", []):
        visit(feature.get("geometry", {}).get("coordinates", []))
    if not coords:
        raise ValueError("no coordinates found")
    xs, ys = zip(*coords)
    return min(xs), min(ys), max(xs), max(ys)


def feature_by_id(payload: dict[str, Any], feature_id: str) -> dict[str, Any]:
    for feature in payload.get("features", []):
        if feature.get("id") == feature_id or feature.get("properties", {}).get("id") == feature_id:
            return feature
    raise KeyError(feature_id)


def overpass_query(study_bbox: tuple[float, float, float, float], site_bbox: tuple[float, float, float, float]) -> str:
    west, south, east, north = study_bbox
    swest, ssouth, seast, snorth = site_bbox
    b = f"{south},{west},{north},{east}"
    sb = f"{ssouth},{swest},{snorth},{seast}"
    return f"""[out:json][timeout:120];
(
  way[\"highway\"~\"motorway|trunk|primary|secondary|tertiary|residential|living_street|service|pedestrian|footway|cycleway|path|steps\"]({b});
  way[\"railway\"]({b});
  node[\"railway\"~\"station|halt|subway_entrance|tram_stop\"]({b});
  node[\"public_transport\"=\"station\"]({b});
  nwr[\"amenity\"~\"school|kindergarten|college|university|library|hospital|clinic|pharmacy|community_centre|social_facility|toilets|marketplace|arts_centre|theatre|cinema|place_of_worship|police|fire_station|post_office|townhall|research_institute\"]({b});
  nwr[\"shop\"~\"supermarket|convenience|mall|bakery|greengrocer|chemist|books|bicycle|department_store|laundry|hairdresser\"]({b});
  nwr[\"office\"~\"research|it\"]({b});
  nwr[\"research_institution\"]({b});
  nwr[\"landuse\"~\"grass|forest|recreation_ground|meadow|village_green|education|commercial|retail\"]({b});
  nwr[\"leisure\"=\"park\"]({b});
  nwr[\"natural\"=\"water\"]({b});
  nwr[\"waterway\"]({b});
  way[\"building\"]({sb});
);
out tags center geom qt;"""


def fetch_overpass(query: str) -> tuple[dict[str, Any], str]:
    encoded = urllib.parse.urlencode({"data": query}).encode("utf-8")
    errors: list[str] = []
    for endpoint in OVERPASS_ENDPOINTS:
        try:
            return fetch_json(endpoint, encoded, timeout=150), endpoint
        except Exception as exc:  # bounded endpoint fallback
            errors.append(f"{endpoint}: {type(exc).__name__}: {exc}")
    raise RuntimeError("Overpass unavailable; " + " | ".join(errors))


def osm_geometry(element: dict[str, Any]) -> dict[str, Any] | None:
    if element.get("type") == "node" and "lon" in element and "lat" in element:
        return {"type": "Point", "coordinates": [round(element["lon"], 6), round(element["lat"], 6)]}
    points = element.get("geometry")
    if points:
        coordinates = [[round(point["lon"], 6), round(point["lat"], 6)] for point in points]
        if len(coordinates) >= 4 and coordinates[0] == coordinates[-1]:
            return {"type": "Polygon", "coordinates": [coordinates]}
        if len(coordinates) >= 2:
            return {"type": "LineString", "coordinates": coordinates}
    if element.get("type") == "relation":
        lines = []
        for member in element.get("members", []):
            geometry = member.get("geometry") or []
            line = [[round(point["lon"], 6), round(point["lat"], 6)] for point in geometry]
            if len(line) >= 2:
                lines.append(line)
        if lines:
            return {"type": "MultiLineString", "coordinates": lines}
    center = element.get("center")
    if center:
        return {"type": "Point", "coordinates": [round(center["lon"], 6), round(center["lat"], 6)]}
    return None


def classify(tags: dict[str, Any]) -> set[str]:
    layers: set[str] = set()
    if "highway" in tags:
        layers.add("streets")
    if "railway" in tags and tags.get("railway") not in {"station", "halt", "subway_entrance", "tram_stop"}:
        layers.add("rail")
    if tags.get("railway") in {"station", "halt", "subway_entrance", "tram_stop"} or tags.get("public_transport"):
        layers.add("transit")
    if tags.get("amenity") in PUBLIC_AMENITIES:
        layers.add("daily_life")
    if tags.get("shop") in SELECTED_SHOPS or tags.get("landuse") in {"commercial", "retail"}:
        layers.add("commercial_services")
    if (
        tags.get("leisure") == "park"
        or tags.get("landuse") in GREEN_LANDUSE
        or tags.get("natural") == "water"
        or "waterway" in tags
    ):
        layers.add("green_water")
    if (
        tags.get("amenity") in INNOVATION_AMENITIES
        or tags.get("office") in {"research", "it"}
        or "research_institution" in tags
        or tags.get("landuse") == "education"
    ):
        layers.add("innovation")
    if "building" in tags:
        layers.add("buildings")
    return layers


def geometry_center(geometry: dict[str, Any]) -> tuple[float, float] | None:
    coordinates: list[tuple[float, float]] = []
    if geometry.get("type") == "Point":
        return tuple(geometry["coordinates"][:2])
    for sequence in iter_coordinate_sequences(geometry):
        coordinates.extend((float(point[0]), float(point[1])) for point in sequence)
    if not coordinates:
        return None
    return (
        sum(point[0] for point in coordinates) / len(coordinates),
        sum(point[1] for point in coordinates) / len(coordinates),
    )


def normalized_osm_layers(
    raw: dict[str, Any],
    retrieval_date: str,
    endpoint: str,
    site_bbox: tuple[float, float, float, float],
) -> dict[str, dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = {key: [] for key in LAYER_FILES}
    seen: set[tuple[str, int, str]] = set()
    for element in raw.get("elements", []):
        tags = element.get("tags", {})
        geometry = osm_geometry(element)
        if geometry is None:
            continue
        if "highway" in tags:
            major = tags.get("highway") in {"motorway", "trunk", "primary", "secondary", "tertiary"}
            center = geometry_center(geometry)
            west, south, east, north = site_bbox
            near_site = bool(center) and west - 0.004 <= center[0] <= east + 0.004 and south - 0.004 <= center[1] <= north + 0.004
            named_neighbourhood_street = bool(tags.get("name")) and tags.get("highway") in {"residential", "living_street"}
            if not (major or near_site or named_neighbourhood_street):
                continue
        for layer in classify(tags):
            marker = (element.get("type", "unknown"), int(element.get("id", 0)), layer)
            if marker in seen:
                continue
            seen.add(marker)
            selected = {key: value for key, value in tags.items() if key in KEEP_TAGS}
            if layer == "green_water":
                selected["context_class"] = "water" if ("waterway" in tags or tags.get("natural") == "water") else "green"
            feature_id = f"OSM-{marker[0].upper()}-{marker[1]}-{layer.upper()}"
            buckets[layer].append({
                "type": "Feature",
                "id": feature_id,
                "properties": {
                    "id": feature_id,
                    "layer": layer,
                    "evidence_status": "contextual",
                    "osm_type": marker[0],
                    "osm_id": marker[1],
                    **selected,
                },
                "geometry": geometry,
            })
    result: dict[str, dict[str, Any]] = {}
    for layer, features in buckets.items():
        features.sort(key=lambda f: f["id"])
        result[layer] = {
            "type": "FeatureCollection",
            "name": layer,
            "metadata": {
                "evidence_status": "contextual",
                "source": "OpenStreetMap",
                "retrieval_date": retrieval_date,
                "license": ATTRIBUTION,
                "role": layer,
                "known_limitations": "Not official planning, ownership, population, service-capacity, hours, accessibility, or engineering evidence.",
            },
            "features": features,
        }
    return result


def contextual_anchors(retrieval_date: str) -> dict[str, Any]:
    # Coordinates and distances are transcribed from public Issue #1029.
    records = [
        ("CTX-ANCHOR-DAZHONGSI-STATION", "大钟寺地铁站（OSM community check）", 116.3384, 39.9657, "transit_anchor"),
        ("CTX-ANCHOR-JUESHENGSI", "觉生寺/大钟寺（OSM community check）", 116.3320, 39.9678, "heritage_anchor"),
        ("CTX-ANCHOR-BEIJING-NORTH", "北京北站（OSM community check）", 116.3462, 39.9459, "transit_anchor"),
    ]
    features = []
    for fid, name, lon, lat, role in records:
        features.append({
            "type": "Feature",
            "id": fid,
            "properties": {
                "id": fid,
                "name_zh": name,
                "role": role,
                "evidence_status": "contextual",
                "source": "https://github.com/open-city-ai/haidian/issues/1029",
                "retrieval_date": retrieval_date,
                "license": "Public GitHub issue evidence; attribution required",
                "known_limitations": "Community OSM/Nominatim cross-check; not an official project anchor or survey point.",
            },
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
        })
    return {
        "type": "FeatureCollection",
        "name": "contextual_anchor_warnings",
        "features": features,
    }


def centroid(feature: dict[str, Any]) -> tuple[float, float]:
    coords: list[tuple[float, float]] = []

    def visit(value: Any) -> None:
        if isinstance(value, list) and len(value) >= 2 and all(isinstance(v, (int, float)) for v in value[:2]):
            coords.append((float(value[0]), float(value[1])))
        elif isinstance(value, list):
            for item in value:
                visit(item)

    visit(feature["geometry"].get("coordinates", []))
    return sum(x for x, _ in coords) / len(coords), sum(y for _, y in coords) / len(coords)


def haversine_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    lon1, lat1 = map(math.radians, a)
    lon2, lat2 = map(math.radians, b)
    dlon, dlat = lon2 - lon1, lat2 - lat1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * 6_371_008.8 * math.asin(math.sqrt(h))


def iter_coordinate_sequences(geometry: dict[str, Any]) -> Iterable[list[list[float]]]:
    kind = geometry.get("type")
    coords = geometry.get("coordinates", [])
    if kind == "LineString":
        yield coords
    elif kind == "Polygon":
        yield from coords
    elif kind == "MultiLineString":
        yield from coords
    elif kind == "MultiPolygon":
        for polygon in coords:
            yield from polygon


def svg_path(sequence: list[list[float]], project: Any, close: bool = False) -> str:
    if not sequence:
        return ""
    points = [project(point[0], point[1]) for point in sequence]
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return d + (" Z" if close else "")


def render_svg(
    output: Path,
    title: str,
    subtitle: str,
    bbox: tuple[float, float, float, float],
    official: dict[str, Any],
    layers: dict[str, dict[str, Any]],
    anchors: dict[str, Any],
    mode: str,
) -> None:
    width, height = 1120, 1040
    map_x, map_y, map_w, map_h = 55, 130, 770, 805
    west, south, east, north = bbox
    mid_lat = (south + north) / 2
    x_scale = math.cos(math.radians(mid_lat))
    span_x = max((east - west) * x_scale, 1e-9)
    span_y = max(north - south, 1e-9)
    scale = min(map_w / span_x, map_h / span_y)
    used_w, used_h = span_x * scale, span_y * scale
    x0 = map_x + (map_w - used_w) / 2
    y0 = map_y + (map_h - used_h) / 2

    def project(lon: float, lat: float) -> tuple[float, float]:
        return x0 + (lon - west) * x_scale * scale, y0 + (north - lat) * scale

    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="1040" viewBox="0 0 1120 1040">',
        '<rect width="1120" height="1040" fill="#f7f5ef"/>',
        f'<text x="55" y="52" font-family="Arial, sans-serif" font-size="30" font-weight="700" fill="#17202a">{html.escape(title)}</text>',
        f'<text x="55" y="82" font-family="Arial, sans-serif" font-size="15" fill="#52616b">{html.escape(subtitle)}</text>',
        f'<rect x="{map_x}" y="{map_y}" width="{map_w}" height="{map_h}" rx="8" fill="#ffffff" stroke="#d2d8dc"/>',
    ]

    def draw_collection(
        collection: dict[str, Any],
        stroke: str,
        width_px: float,
        fill: str = "none",
        opacity: float = 1.0,
        dash: str = "",
        max_features: int = 1800,
    ) -> None:
        features = collection.get("features", [])
        if len(features) > max_features:
            stride = math.ceil(len(features) / max_features)
            features = features[::stride]
        for feature in features:
            geometry = feature.get("geometry", {})
            if geometry.get("type") == "Point":
                lon, lat = geometry["coordinates"][:2]
                x, y = project(lon, lat)
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="{stroke}" opacity="{opacity}"/>')
                continue
            close = geometry.get("type") in {"Polygon", "MultiPolygon"}
            for sequence in iter_coordinate_sequences(geometry):
                d = svg_path(sequence, project, close)
                if d:
                    out.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width_px}" opacity="{opacity}" stroke-dasharray="{dash}"/>')

    if mode in {"scope", "transit", "services", "green", "innovation", "warning"}:
        draw_collection(layers.get("streets", {}), "#c3c8cb", 0.7, opacity=0.58, max_features=1800)
    if mode == "scope":
        draw_collection(layers.get("buildings", {}), "#d8d3c7", 0.35, fill="#eeeae0", opacity=0.45, max_features=1100)
    if mode in {"scope", "transit", "warning"}:
        draw_collection(layers.get("rail", {}), "#36454f", 2.2, opacity=0.9, max_features=650)
    if mode == "transit":
        draw_collection(layers.get("transit", {}), "#8e44ad", 3.0, opacity=0.95, max_features=350)
    if mode == "services":
        draw_collection(layers.get("daily_life", {}), "#d35400", 2.8, opacity=0.9, max_features=900)
        draw_collection(layers.get("commercial_services", {}), "#b7950b", 2.6, opacity=0.8, max_features=700)
    if mode == "green":
        for feature in layers.get("green_water", {}).get("features", []):
            context_class = feature.get("properties", {}).get("context_class")
            collection = {"features": [feature]}
            if context_class == "water":
                draw_collection(collection, "#2980b9", 1.5, fill="#b9dcf2", opacity=0.8)
            else:
                draw_collection(collection, "#3c8d5a", 1.0, fill="#bfe0c3", opacity=0.64)
    if mode == "innovation":
        draw_collection(layers.get("innovation", {}), "#00796b", 3.2, fill="#c8e6df", opacity=0.85, max_features=500)

    # Official repository geometry is still provisional; render it last, dashed and transparent.
    for feature in official.get("features", []):
        fid = feature.get("id") or feature.get("properties", {}).get("id", "")
        if fid == "PROV-RESEARCH-001":
            style = ("#8b8f93", 1.1, "none", 0.7, "8 7")
        elif fid == "PROV-SITE-001":
            style = ("#e67e22", 2.0, "none", 0.9, "9 6")
        elif fid.startswith("PROV-KEY-00"):
            style = ("#c0392b", 1.5, "#f5b7b1", 0.32, "5 4")
        else:
            continue
        draw_collection({"features": [feature]}, *style)
        if fid.startswith("PROV-KEY-00"):
            cx, cy = project(*centroid(feature))
            out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="700" fill="#922b21">{html.escape(fid)} PROVISIONAL</text>')

    if mode == "warning":
        for feature in anchors.get("features", []):
            lon, lat = feature["geometry"]["coordinates"]
            x, y = project(lon, lat)
            name = feature["properties"]["name_zh"]
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#1f618d" stroke="#fff" stroke-width="2"/>')
            out.append(f'<text x="{x + 10:.1f}" y="{y - 8:.1f}" font-family="Arial, sans-serif" font-size="12" fill="#154360">{html.escape(name)}</text>')
        key3 = feature_by_id(official, "PROV-KEY-003")
        a = centroid(key3)
        station = feature_by_id(anchors, "CTX-ANCHOR-DAZHONGSI-STATION")["geometry"]["coordinates"]
        ax, ay = project(*a)
        bx, by = project(*station)
        out.append(f'<path d="M {ax:.1f},{ay:.1f} L {bx:.1f},{by:.1f}" stroke="#c0392b" stroke-width="3" stroke-dasharray="8 6" marker-end="url(#arrow)"/>')
        out.insert(1, '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#c0392b"/></marker></defs>')

    legend = [
        ("#e67e22", "Overall design polygon — PROVISIONAL"),
        ("#c0392b", "Key-area polygons — PROVISIONAL"),
        ("#36454f", "OSM rail — CONTEXTUAL"),
        ("#c3c8cb", "OSM street network — CONTEXTUAL"),
    ]
    if mode == "services":
        legend += [("#d35400", "Public/daily service POI"), ("#b7950b", "Selected commercial service")]
    if mode == "green":
        legend += [("#3c8d5a", "Green/open space"), ("#2980b9", "Water/waterway")]
    if mode == "innovation":
        legend += [("#00796b", "Named education/research context")]
    if mode == "warning":
        legend += [("#1f618d", "Community-checked contextual anchor")]
    out.append('<text x="855" y="155" font-family="Arial, sans-serif" font-size="17" font-weight="700" fill="#17202a">Evidence legend</text>')
    for index, (colour, label) in enumerate(legend):
        y = 188 + index * 34
        out.append(f'<line x1="855" y1="{y}" x2="885" y2="{y}" stroke="{colour}" stroke-width="4"/>')
        out.append(f'<text x="895" y="{y + 5}" font-family="Arial, sans-serif" font-size="12" fill="#34495e">{html.escape(label)}</text>')
    notes = [
        "NO commercial map tiles.",
        "OSM completeness and access are unverified.",
        "No ownership, population, hours or capacity inference.",
        "Dashed polygons are not official redlines.",
    ]
    if mode == "warning":
        notes += [
            "Issue #1029: PROV-KEY-003 centroid is about",
            "2.26 km from the contextual Dazhongsi station point.",
            "Issue #846: mapped park/context relationship remains unresolved.",
        ]
    out.append('<text x="855" y="520" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#17202a">Use boundary</text>')
    for index, note in enumerate(notes):
        out.append(f'<text x="855" y="{550 + index * 24}" font-family="Arial, sans-serif" font-size="11" fill="#566573">{html.escape(note)}</text>')
    out.append(f'<text x="55" y="986" font-family="Arial, sans-serif" font-size="12" fill="#566573">Sources: open-city-ai/haidian@{OFFICIAL_HEAD[:12]} (provisional); {html.escape(ATTRIBUTION)}. Generated from committed vector snapshots.</text>')
    out.append('<text x="55" y="1008" font-family="Arial, sans-serif" font-size="12" font-weight="700" fill="#922b21">CONTEXTUAL / DERIVED / NOT OFFICIAL / NOT SITE-CALIBRATED</text>')
    out.append('</svg>')
    output.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def point_in_polygon(point: tuple[float, float], ring: list[list[float]]) -> bool:
    x, y = point
    inside = False
    j = len(ring) - 1
    for i, (xi, yi) in enumerate(ring):
        xj, yj = ring[j]
        if ((yi > y) != (yj > y)) and x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi:
            inside = not inside
        j = i
    return inside


def build_summary(official: dict[str, Any], layers: dict[str, dict[str, Any]], anchors: dict[str, Any], retrieval_date: str) -> dict[str, Any]:
    counts = {layer: len(payload.get("features", [])) for layer, payload in layers.items()}
    key_context = {}
    point_layers = ("transit", "daily_life", "commercial_services", "innovation")
    for key_id in ("PROV-KEY-001", "PROV-KEY-002", "PROV-KEY-003"):
        feature = feature_by_id(official, key_id)
        ring = feature["geometry"]["coordinates"][0]
        layer_counts = Counter()
        for layer in point_layers:
            for item in layers[layer].get("features", []):
                if item.get("geometry", {}).get("type") == "Point" and point_in_polygon(tuple(item["geometry"]["coordinates"][:2]), ring):
                    layer_counts[layer] += 1
        key_context[key_id] = {
            "evidence_status": "derived_from_contextual_points_and_provisional_polygon",
            "point_counts": dict(layer_counts),
            "warning": "Counts do not establish catchments, service completeness, capacity, access, or the correct key-area location.",
        }
    key3 = feature_by_id(official, "PROV-KEY-003")
    station = feature_by_id(anchors, "CTX-ANCHOR-DAZHONGSI-STATION")
    computed_distance = round(haversine_m(centroid(key3), tuple(station["geometry"]["coordinates"])), 1)
    return {
        "schema_version": "1.0",
        "generated_date": retrieval_date,
        "classification": ["CONTEXTUAL", "DERIVED", "NOT_OFFICIAL", "NOT_SITE_CALIBRATED"],
        "official_head": OFFICIAL_HEAD,
        "feature_counts": counts,
        "key_area_context": key_context,
        "geometry_warnings": {
            "authoritative_polygon_available": False,
            "provisional_key_003_to_contextual_dazhongsi_station_centroid_distance_m": computed_distance,
            "issue_1029_reported_distance_m": 2257,
            "issue_846_park_overlap_status": "reported zero overlap; source geometry not promoted to official",
        },
        "decision_boundary": {
            "can_support": [
                "contextual network topology questions",
                "named public-place and service leads for field verification",
                "relative hypothesis comparison on one identical snapshot",
            ],
            "cannot_support": [
                "official boundaries or statutory controls",
                "ownership, population, service capacity or service hours",
                "formal catchment analysis",
                "parcel-specific demolition, transport or engineering conclusions",
            ],
        },
    }


def load_layers() -> dict[str, dict[str, Any]]:
    return {layer: read_json(CONTEXT / filename) for layer, filename in LAYER_FILES.items()}


def build_offline(retrieval_date: str) -> dict[str, Any]:
    official = read_json(CONTEXT / "official-provisional-boundaries.geojson")
    bbox_payload = read_json(CONTEXT / "study-area-bbox.geojson")
    anchors = read_json(CONTEXT / "contextual-anchors.geojson")
    layers = load_layers()
    bbox = bbox_from_geojson(bbox_payload)
    summary = build_summary(official, layers, anchors, retrieval_date)
    write_json(DERIVED / "context-summary.json", summary)
    configs = [
        ("01-scope-context.svg", "01 · Scope and contextual fabric", "One base; provisional constraints remain visually subordinate.", "scope"),
        ("02-transit-and-rail-context.svg", "02 · Transit and rail context", "Named stations and rail/street relations are contextual, not a verified accessible network.", "transit"),
        ("03-public-services-and-daily-life-context.svg", "03 · Public services and daily-life context", "POIs are leads for verification; no hours, capacity or completeness claim.", "services"),
        ("04-green-water-open-space-context.svg", "04 · Green, water and open-space context", "Crowdsourced mapped features do not establish ecology, drainage or public access.", "green"),
        ("05-research-innovation-context.svg", "05 · Research and innovation context", "Only publicly named OSM education/research context; no institutional commitment inferred.", "innovation"),
        ("06-key-area-context-warning.svg", "06 · Key-area context warning", "Provisional geometry and named contextual anchors conflict; typology before parcel precision.", "warning"),
    ]
    hashes = {}
    for filename, title, subtitle, mode in configs:
        path = FIGURES / filename
        render_svg(path, title, subtitle, bbox, official, layers, anchors, mode)
        hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    write_json(DERIVED / "figure-hashes.json", hashes)
    return {"summary": summary, "figure_hashes": hashes}


def refresh(retrieval_date: str) -> None:
    ensure_dirs()
    for filename, url in OFFICIAL_FILES.items():
        payload = fetch_json(url, timeout=90)
        write_json(CONTEXT / filename, payload)
    official = read_json(CONTEXT / "official-provisional-boundaries.geojson")
    bbox_payload = read_json(CONTEXT / "study-area-bbox.geojson")
    study_bbox = bbox_from_geojson(bbox_payload)
    site_bbox = bbox_from_geojson({"type": "FeatureCollection", "features": [feature_by_id(official, "PROV-SITE-001")]})
    raw, endpoint = fetch_overpass(overpass_query(study_bbox, site_bbox))
    layers = normalized_osm_layers(raw, retrieval_date, endpoint, site_bbox)
    for layer, filename in LAYER_FILES.items():
        write_json(CONTEXT / filename, layers[layer])
    write_json(CONTEXT / "contextual-anchors.geojson", contextual_anchors(retrieval_date))
    manifest = {
        "schema_version": "1.0",
        "retrieval_date": retrieval_date,
        "official_head": OFFICIAL_HEAD,
        "overpass_endpoint": endpoint,
        "sources": [
            {
                "source": "open-city-ai/haidian provisional geometry",
                "url": OFFICIAL_FILES["official-provisional-boundaries.geojson"],
                "status": "provisional",
                "role": "temporary scope constraints and warnings",
                "license": "Repository terms; source retained with provenance",
                "known_limitations": "Not official redline, precise area, statutory or engineering evidence.",
            },
            {
                "source": "OpenStreetMap",
                "url": endpoint,
                "status": "contextual",
                "role": "bounded streets, rail, stations, services, open space, water, innovation and broad building context",
                "license": ATTRIBUTION,
                "known_limitations": "Crowdsourced, incomplete and not evidence of operation, access, capacity, ownership or legal status.",
            },
            {
                "source": "open-city-ai/haidian Issue #1029",
                "url": "https://github.com/open-city-ai/haidian/issues/1029",
                "status": "contextual",
                "role": "anchor-warning points and Dazhongsi mismatch cross-check",
                "license": "Public GitHub issue evidence; attribution required",
                "known_limitations": "Community OSM/Nominatim calculation, not official geometry or survey.",
            },
        ],
        "layer_files": LAYER_FILES,
    }
    write_json(CONTEXT / "layer-manifest.json", manifest)
    build_offline(retrieval_date)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="fetch pinned official and bounded OSM snapshots")
    parser.add_argument("--offline", action="store_true", help="rebuild derived summaries and SVGs from committed snapshots")
    parser.add_argument("--retrieval-date", default=date.today().isoformat())
    args = parser.parse_args(argv)
    ensure_dirs()
    if args.refresh:
        refresh(args.retrieval_date)
    elif args.offline:
        build_offline(args.retrieval_date)
    else:
        parser.error("choose --refresh or --offline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
