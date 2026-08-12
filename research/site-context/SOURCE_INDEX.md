# Common-base Source Index

| ID | Status | Source | Retrieval | License | Role | Known limitation |
|---|---|---|---|---|---|---|
| SC-01 | `FACT` | `open-city-ai/haidian@e9741a415aeb5cf09ca27608f6c97c33145a589f`, design brief/taskbook/allowed space | 2026-08-12 | repository terms | official textual scope and data-use contract | does not provide exact polygons |
| SC-02 | `provisional` | repository `provisional_boundaries.geojson` and basis | 2026-08-12 | repository terms | rough scope/key-area constraints and warning layer | not official; key rectangles are not station/road anchored |
| SC-03 | `contextual` | OpenStreetMap bounded Overpass snapshot | 2026-08-12 | © OpenStreetMap contributors, ODbL 1.0 | streets, rail, stations, public/commercial POIs, green/water, research context, broad footprints | crowdsourced completeness/position/operation unverified |
| SC-04 | `contextual` | [Issue #1029](https://github.com/open-city-ai/haidian/issues/1029) | 2026-08-12 | public issue evidence | Dazhongsi/PROV-KEY-003 anchor mismatch | community OSM/Nominatim check, not survey or official anchor |
| SC-05 | `contextual` | [Issue #846](https://github.com/open-city-ai/haidian/issues/846) and canonical basis summary | 2026-08-12 | public issue evidence | park/provisional-site mismatch warning | OSM park coverage is incomplete and cannot replace official geometry |

The source count counts independently governed source records, not feature count. Individual OSM elements retain their OSM identifiers and common attribution in each GeoJSON file.
