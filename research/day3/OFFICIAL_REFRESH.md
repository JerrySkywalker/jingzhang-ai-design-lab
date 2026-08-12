# Round-3 Official Environment Refresh

Retrieval date: 2026-08-12 (Asia/Shanghai)

```text
OFFICIAL_HEAD_START=e9741a415aeb5cf09ca27608f6c97c33145a589f
PRIOR_R2_OFFICIAL_HEAD=4467e00b87e189dd3dcc3e27ca33da2fd58c3432
COMMITS_AHEAD=280
OFFICIAL_REQUIREMENTS_CHANGED=false
AUTHORITATIVE_GEOMETRY_APPEARED=false
```

## Canonical contract recheck

`FACT` — The following blobs at the start head are byte-identical to the Round-2 end snapshot. The 280-commit delta is dominated by new/iterated submissions and package/tooling work, not a change to these controlling inputs.

| Canonical path | Git blob | Result |
|---|---|---|
| `skills/urban-design-ai-submission/SKILL.md` | `9d26223484db675e8516f0bccb541d12f502dd79` | unchanged |
| `brief/site-package/design_brief.json` | `f30f7f855c093f81252cb82c624c0d8b4466683c` | unchanged |
| `brief/site-package/agent_taskbook.json` | `30ba653513f6e09eb1d86998f2491aa8a657a1fb` | unchanged |
| `brief/site-package/allowed_design_space.json` | `b2aec48767766b2b233a0c11c37f16127dc667f2` | unchanged |
| `brief/site-package/geometry/provisional_boundaries.geojson` | `b050e0813882a034a7deb976ddd4a43ad56aec0c` | unchanged; provisional only |
| `brief/site-package/geometry/provisional_boundaries_basis.md` | `27792f2753aef9e9f3d41bebcd2d71e8f29c3f7a` | unchanged |
| `brief/site-package/geometry/study_area_bbox.geojson` | `37c47cb147c2cfad94798e1ed66f1855f5853604` | unchanged; viewport/discovery only |
| `data/source_registry.json` | `c5e2243c85f1a62edb295911439e1847b9e634fb` | unchanged |
| `tracks.json` | `dbcc92f4cee2158b82ee545b5ae39ecf9786f081` | unchanged |
| `templates/proposal.md` | `19a22ef6290e3ea45202f223a6570ea742599da6` | unchanged |
| `docs/formal-submission-guide.md` | `4109d02197b65ac60809316fe5531157df2af6a7` | unchanged |
| `submissions/README.md` | `e757812b143ace480b20804cc4a962188d78f35c` | unchanged |

The controlling interpretation therefore remains:

- `FACT` — official text fixes the three scales and approximate areas, but exact official polygons are missing;
- `FACT` — provisional polygons may support concept generation, discussion and intake visualization, not official redlines, statutory controls, precise area claims, ownership or engineering conclusions;
- `FACT` — OSM may supply bootstrap/context layers with ODbL attribution, but not formal boundaries;
- `FACT` — a complete design still must cover three scales, all three key areas, industry/ecosystem, land/buildings/renewal, mobility, municipal/new infrastructure, blue-green/public realm, scenarios, culture/brand, phasing and operations;
- `FACT` — at least ten AI scenario cards, at least three industry test/validation scenes and at least five personas remain required for a future formal package;
- `FACT` — this lab sprint is not a formal package and does not claim formal readiness.

## Geometry findings that control Round 3

`AUTHORITATIVE_DATA_MISSING` — no new CAD/GIS/official polygon appeared under the canonical geometry directory.

`FACT` — the canonical basis continues to report a community OSM cross-check in which the mapped Jing-Zhang heritage park does not overlap `PROV-SITE-001` and is about 412.5 m away; this is a warning, not proof that OSM is authoritative.

`FACT` — [Issue #1029](https://github.com/open-city-ai/haidian/issues/1029) remains open. Its reproducible contextual check places the `PROV-KEY-003` centroid about 2.26 km from the Dazhongsi station reference and inside the Beijing North Station context. Maintainers clarified that the rectangle is sequence/area-fitted and not station/road anchored; contributors should not independently move it.

**Round-3 consequence:** Dazhongsi work must remain a typological metropolitan-adoption interface. No parcel, station-corner, exact walking catchment or four-quadrant intervention may be presented as site-resolved.

## Progressive competition read

The review started from recent merged/open PR metadata, then fetched proposal text only for twelve high-collision works. No figures, HTML or A3/A0 PDFs were downloaded. Eight additional works were screened through title, PR body and package metadata.

### Twelve proposal-text deep reads

| PR | Work | Collision evidence | Round-3 implication |
|---:|---|---|---|
| [#1809](https://github.com/open-city-ai/haidian/pull/1809) | 京张接口公地 / JZ Common Ports | one spine, three ports, twelve public interfaces; passports, human final decision, recall/retirement and non-AI equivalence | “interface”, “commons”, public accountability, pause/exit and three differentiated ports are occupied; C01 cannot claim them as originality |
| [#1811](https://github.com/open-city-ai/haidian/pull/1811) | AI 朝圣·铁轨新生带 / maintenance urbanism | ordinary track plus validation track, repair/maintenance and failure siding; three area roles verify/co-create/publish | maintenance, failure visibility, reversible service layer and ordinary-first rhetoric are occupied |
| [#1910](https://github.com/open-city-ai/haidian/pull/1910) | 京张常新场 / Service-Life Covenant | distributed maintenance-debt work-order network; service/care/material/public-value closing accounts | lifecycle, maintenance debt, retirement, resource and public-value accounting are occupied; C01 must be about resource compatibility and spatial allocation, not lifecycle vocabulary |
| [#1930](https://github.com/open-city-ai/haidian/pull/1930) | 京张交接带 / Handover Line | handover promenade/courts linking research→test→daily life and product→public service | handover/fallback/transition space is occupied |
| [#1938](https://github.com/open-city-ai/haidian/pull/1938) | 智行京张 / Autonomy Commons | public infrastructure framing, legible curb, pedestrian/maintenance priority and reversible low-speed test | curb management, human takeover and autonomous-service governance are occupied |
| [#1851](https://github.com/open-city-ai/haidian/pull/1851) | 京张归药线 / Safe Return Line | staffed acceptance, sealed storage, handover, transport and compliant disposal as responsibility infrastructure | safe exit/recovery is mature but scenario-specific; C01 must not repackage it as a general station |
| [#1868](https://github.com/open-city-ai/haidian/pull/1868) | 京张安心充 / Safe Charge Line | parking/charging, fault response, responsibility and battery exit; “inspect–connect responsibility–then build” | charging and reliability hubs are occupied; energy infrastructure is not a differentiator |
| [#1954](https://github.com/open-city-ai/haidian/pull/1954) | 京张城市完整度 / City Completeness (open) | HOME/LEARN/CARE/MOVE/GREEN/WORK/COMMON LIFE; one spine, six sections, six seams, three cores; AI optional | direct C02 language and ordinary-city collision; C02 cannot own “completeness” or three cores |
| [#1856](https://github.com/open-city-ai/haidian/pull/1856) | 京张日用 / Everyday Jing-Zhang (open) | city-led, one everyday line, staffed public rooms, service cells, zero automated public decisions | ordinary-day, staffed/non-digital completeness and AI-not-leading are occupied |
| [#1916](https://github.com/open-city-ai/haidian/pull/1916) | 京张智轨 / Future City Ideal Units (open) | 1×3×6×5×N; exactly three flagship ideal units and six modules | direct occupation of “three urban units”; H3 needs site/network proof, not brand novelty |
| [#1897](https://github.com/open-city-ai/haidian/pull/1897) | 京张流线公地 / Enterprise–Resident Flow Commons | resident/enterprise/accessible/night-worker flows, shared feeder guard and auditable curb/transfer ledger | cross-boundary everyday mobility and shared feeder logic are occupied; C02 needs a spatial unit argument beyond mobility equity |
| [#1901](https://github.com/open-city-ai/haidian/pull/1901) | 京张居业接力 / Home-Work Relay | one line, three stations, housing/work/public-service relay and repair/night-return paths | work–life continuity, service dependency and three-station narrative are occupied |

### Eight additional relevant screens

| PR | Work | Reason retained in delta set |
|---:|---|---|
| [#1810](https://github.com/open-city-ai/haidian/pull/1810) | COUNT THE FULL COST | full-cost/responsibility allocation constrains C01 resource claims |
| [#1913](https://github.com/open-city-ai/haidian/pull/1913) | 京张等高线 | vertical-access reliability infrastructure overlaps degraded/failure service logic |
| [#1862](https://github.com/open-city-ai/haidian/pull/1862) | 京张晨昏带 | day/night operation and youth-friendly public realm overlap ordinary-day state coverage |
| [#1845](https://github.com/open-city-ai/haidian/pull/1845) | AI Civic Services Belt | civic-service network overlaps daily-service completeness |
| [#1805](https://github.com/open-city-ai/haidian/pull/1805) | Playtest Commons (open) | public testbed/commons overlaps C01 validation and public interface |
| [#1813](https://github.com/open-city-ai/haidian/pull/1813) | GROUND FIRST (open) | city ground, public baseline and physical-first framing overlaps both candidates |
| [#1893](https://github.com/open-city-ai/haidian/pull/1893) | 京张开源驿站 (open) | one pilot plus three replicable public-service node types tests C01’s “no universal station” decision |
| [#1932](https://github.com/open-city-ai/haidian/pull/1932) | Shared-feeder guard | counterfactual mode competition and failure gates overlap shared-resource evaluation method |

## Environment delta judgment

### C01

`OCCUPIED` — Agent/OS, robot/AV, digital twin, fallback/rollback, human takeover, reconfiguration, charging, maintenance, public interface/commons, handover, service-life, safe exit and reversible pilots.

`POTENTIALLY_DISTINCT, HIGH COLLISION RISK` — the chain that starts with a public task and tolerated uncertainty/TTL, derives a minimum resource bundle, explicitly classifies resources as fully shareable/time-shareable/shareable-with-isolation/non-shareable, then produces distributed physical cells and specialized backends with isolated allocation and degraded recovery. None of the twelve deep reads demonstrates that complete chain as its urban kernel. Round 3 must still prove that this chain changes three different urban sections; otherwise the distinction is only a systems diagram.

### C02

`DIRECTLY_OCCUPIED` — ordinary-day completeness, city-first/AI-optional, staffed/non-digital service, three cores/units, work-life relay, day/night and service networks.

`DECISION EFFECT` — “exactly three complete neighbourhoods” has no naming or competition-space protection. It survives only if the common contextual base shows three independent, unequal catchments outperforming H2/H4+/Corridor+N. If the data cannot decide, H3 remains unsupported; if H3 loses, the exactly-three identity is killed while the ordinary-day gate is retained.

## Network/tool incidents

- One attempt to create a depth-1 blobless no-checkout temporary official clone failed at the GitHub GraphQL TLS handshake before any directory was created.
- Two proposal-content API calls timed out once. The sprint continued using successful proposal-text reads plus PR bodies/metadata and did not download media.
- Classification: `NETWORK_FAILURE`, local to peer-reading; no effect on canonical hash comparison or geometry status.

## What must influence the run

1. C01 must formally reject the crowded differentiators and delete the universal-station assumption unless the resource model proves it.
2. C01’s three sections must be materially different and show where ordinary urban service space is sufficient.
3. C02’s H3 identity faces a direct open-PR collision and a direct ideal-unit collision; same-base hypothesis testing is mandatory.
4. Dazhongsi remains typological, not site-precise.
5. The official end head must be checked again; only `OFFICIAL_HEAD_START..OFFICIAL_HEAD_END` will be audited.
