# C04 Official State and Competition Refresh

Retrieval date: 2026-08-12 (Asia/Shanghai)

```text
OFFICIAL_HEAD_START=8912dacebec2a943cfa3480be6e66ba90c4eb746
OFFICIAL_HEAD_END=e35d8376e30110e36021658cfa81ece6f1e7011a
R4_OFFICIAL_HEAD_END=58acb254a06ecf85f080300c6c6c4a2584401d34
FIRST_PARENT_COMMITS_SINCE_R4_AT_END=4
OFFICIAL_REQUIREMENTS_CHANGED=false
AUTHORITATIVE_GEOMETRY_APPEARED=false
```

## Canonical contract recheck

`FACT` — the current official head is merge commit `8912dacebec2a943cfa3480be6e66ba90c4eb746`. A bounded tree compare against the Round-4 end head found 939 changed paths: 933 under `submissions/` and six under `scripts/` or `tests/`. The latter extract a dependency-free front-matter parser, add folded/literal scalar coverage, and harden network-error handling. They do not alter design tasks, admissible space, geometry, formal contents or submission structure.

`FACT` — the twelve controlling canonical blobs are byte-identical to the Round-4 end seal:

| Canonical path | Git blob at C04 start |
|---|---|
| `skills/urban-design-ai-submission/SKILL.md` | `9d26223484db675e8516f0bccb541d12f502dd79` |
| `brief/site-package/design_brief.json` | `f30f7f855c093f81252cb82c624c0d8b4466683c` |
| `brief/site-package/agent_taskbook.json` | `30ba653513f6e09eb1d86998f2491aa8a657a1fb` |
| `brief/site-package/allowed_design_space.json` | `b2aec48767766b2b233a0c11c37f16127dc667f2` |
| `brief/site-package/geometry/provisional_boundaries.geojson` | `b050e0813882a034a7deb976ddd4a43ad56aec0c` |
| `brief/site-package/geometry/provisional_boundaries_basis.md` | `27792f2753aef9e9f3d41bebcd2d71e8f29c3f7a` |
| `brief/site-package/geometry/study_area_bbox.geojson` | `37c47cb147c2cfad94798e1ed66f1855f5853604` |
| `data/source_registry.json` | `c5e2243c85f1a62edb295911439e1847b9e634fb` |
| `tracks.json` | `dbcc92f4cee2158b82ee545b5ae39ecf9786f081` |
| `templates/proposal.md` | `19a22ef6290e3ea45202f223a6570ea742599da6` |
| `docs/formal-submission-guide.md` | `4109d02197b65ac60809316fe5531157df2af6a7` |
| `submissions/README.md` | `e757812b143ace480b20804cc4a962188d78f35c` |

The official skill, brief, taskbook, allowed design space, source registry, formal guide and submission guide were re-read at the exact start head. The run does not redo unchanged R2–R4 requirement extraction.

## Controlling spatial facts and limits

- `FACT` — the coordinated research scale is about 43.6 km², the overall design scale about 11.4 km², and the three detailed-design areas total about 368.4 ha: Zhongzhiyuan 192.1 ha, Beijing AI Origin Community 104.3 ha and Dazhongsi 72.0 ha.
- `FACT` — exact official polygons remain unavailable. The repository polygons are `official_boundary=false`, `geometry_role=provisional_constraint`; GeoJSON exchange is EPSG:4326 and area recomputation is EPSG:4548.
- `FACT` — the public/contextual common base may identify street, rail, transit, broad building, service, innovation, green and water leads. It cannot establish ownership, legal land use, population, capacity, opening hours, accessibility, building condition, utilities, ecology, transport demand or engineering feasibility.
- `FACT` — the provisional 11.4 km² polygon has a reported zero-overlap warning with the OSM-mapped heritage-park context. `PROV-KEY-003` has a reported roughly 2.26 km mismatch with the contextual Dazhongsi station point and contains the contextual Beijing North Station point.
- `DECISION` — all three-area design will remain typological and relational where exact anchors are missing. No parcel, station-corner, exact catchment, demolition, road-redline or engineering claim is permitted.

## Complete-design and later formal obligations

The selected premise, if any, must already support the three scales; innovation ecosystem; land use; buildings and renewal; transport; municipal/new infrastructure; blue-green/public space; three genuinely different key areas; AI scenarios; culture/brand; phasing; operations; evidence and risk.

The later formal fork, if separately authorized, must produce a bilingual v2 professional package: proposal and translation, nine required GeoJSON families, sources/assumptions/metrics and three matrices, five derived figures in both required languages where text-bearing, offline report and visual HTML, bilingual A3/A0 PDFs, at least 10 AI scenario cards, at least 3 industry test/validation scenarios, at least 5 personas, at least 3 pilgrimage/honor nodes, and complete deterministic/spatial/visual/professional self-check evidence. This design-lab run does not create those formal artifacts.

## R4-to-C04 competition delta

The one current merge substantially expands the merged catalog. A progressive read used the generated text catalog first, then fetched only selected proposal text. The corpus is extremely saturated in the Owner-listed exclusion zones: one-spine/three-core, railway metaphors, Urban/Agent OS, test/proof/calibration, fallback/rollback, complete neighbourhood/stay/belong, habitat/climate, generic commons/open campus, cross-street/stitching and evidence-as-brand.

Additional close territories found in the current catalog include:

- public frontage and institution edge: `Jingzhang Common Eaves`, `Jingzhang Public Foyer`, `Jingzhang Open Ground`, `AI Main Street`;
- urban-form-first regeneration: `Jingzhang Intelligence Commons V6`, `Jingzhang Cross-Streets`;
- production and research-to-adoption: `Jingzhang Civic Foundry`, `Jingzhang Works`, `Common Table`, `Jingzhang First Mile`;
- learning and talent: `Five-University Origin Ring`, `Open Campus`, `Curiosity Line`, `Stay Longer`;
- time and shared use: `Chrono Commons`, `Hearth Line`, `Human Hours`.

Open pull requests were sampled by title/body after the merged-corpus read. They add further collision pressure around in-situ sections, talent/open-source districts, daily action scripts, handover, public interfaces and conventional one-line/three-node schemes. Open PR state is volatile and is used only as a bounded warning, not as merged-corpus fact.

### Terminal official drift check

`FACT` — the official branch advanced during this run. Submission work was paused and the end state was fetched before the premise decision was sealed. From start head `8912dacebec2a943cfa3480be6e66ba90c4eb746` to end head `e35d8376e30110e36021658cfa81ece6f1e7011a`, three first-parent proposal merges changed 107 paths, all under `submissions/`:

- `Winnie1014/jingzhang-ai-vein` — a conventional one-belt/three-core AI-vein scheme;
- `gentlexyl/jingzhang-ai-civic-spine` — public-first/open-co-creation with non-AI equivalents and exit gates;
- `miyuuteshima984/jingzhang-ai-civic-infrastructure` — C7 city completeness across home, learn, care, move, green, work and common life.

The same twelve controlling blobs listed above remain byte-identical at the end head. No authoritative geometry or requirement changed. The three added proposals do not open a white-space premise; the latter two increase collision pressure on generic public-first, ordinary-completeness, cross-link and reversible-pilot territory. The tournament conclusion was rechecked against this end delta.

## Decision effect for premise generation

No title or metaphor earns admission. Each internal premise must show a primary 11.4 km² geometry, a genuine Jing-Zhang dependency and a natural path to complete-city coverage before it may receive Candidate 04. A visually promising premise is killed when its core territory is already held more maturely, its site problem is only assumed, or its missing chapters have to be bolted on after selection.
