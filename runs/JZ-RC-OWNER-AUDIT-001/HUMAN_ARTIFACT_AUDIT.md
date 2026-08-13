# Human Artifact Audit — RC1

Result: `PASS_WITH_ISSUES`
Blockers: 0
Major issues: 3
Minor issues: 3
Polish issues: 2

This is a juror/human-reader audit, not a validator rerun. Machine PASS results are treated as corroborating package integrity, not as proof of presentation quality.

## Artifact disposition

| Artifact group | Human result | Finding |
| --- | --- | --- |
| `proposal.md` | PASS | The proposition, three areas, implementation gates, provisional limits, and AI restraint are understandable without JSON. |
| `proposal.en.md` | PASS | Strong semantic parity and natural professional English; the core argument survives translation. |
| 10 required figures | PASS_WITH_ISSUES | Consistent, clean and deterministic, but too abstract and diagrammatic to carry an urban-design proposition. |
| `visual/index.html` | PASS_WITH_ISSUES | Structurally complete and offline, but reads as a metric/register dashboard; core Chinese lists remain in English. |
| `visual/index.en.html` | PASS_WITH_ISSUES | Structurally clear, but the register/list order and multi-column figure grid weaken spatial comprehension. |
| `report/proposal.html` | PASS_WITH_ISSUES | Readable report CSS and complete figures/tables; duplicated title and abstract figures reduce polish. |
| `report/proposal.en.html` | PASS_WITH_ISSUES | Same as Chinese report; semantic parity is strong. |
| A3 booklets, 10 pages each | PASS_WITH_ISSUES | No observed page clipping, but repeated figures and large unused areas make the booklet feel padded. |
| A0 boards, 3 pages each | PASS_WITH_ISSUES | No observed page clipping, but content is underscaled and surrounded by excessive blank space for an A0 juror board. |

## MAJOR findings

### HAA-MAJOR-01 — The visual system does not yet show urban design

Affected artifacts: all ten figures, both visual HTML files, both A3 booklets, both A0 board sets, and the figure sequence inside both rendered reports.

The visual vocabulary is nested rounded rectangles, categorical columns, identical polylines, number cards, and registers. It does not show a recognizable site plan, patch distribution, public-realm network, street/threshold section, three-area spatial sequence, building/interface transformation, or ordinary-day urban scene. Labels such as “总览地图 / Overview” and “控制断面 / controlling sections” promise spatial evidence that the graphics do not actually depict.

Human consequence: a juror can understand the governance thesis in 30 seconds, but cannot see where or how the city changes. The evidence layer overwhelms the design layer, and several pages look like an engineering or product-governance report rather than an urban-design submission.

Required release closure: one bounded visual pass that makes the existing, frozen proposition spatially legible without adding new factual claims. At minimum it should show the provisional field, the 17 patch logic at a readable scale, three genuinely different sections/sequences, and AI-on/AI-off spatial consequences. All provisional labels and evidence limits must remain.

### HAA-MAJOR-02 — A3/A0 composition is repetitive, sparse, and underscaled

Affected artifacts: all four PDFs.

The 10-page A3 booklets reuse the same five figures multiple times with only a chapter label or one-line caption changing. The three A0 boards place one or two underscaled diagrams in the upper half and leave very large blank fields below. This produces weak page rhythm, insufficient information density, and poor board-distance legibility despite the absence of technical clipping.

Human consequence: the set feels auto-expanded from five figures rather than deliberately edited as a booklet/board narrative. Repetition reduces rather than reinforces the concept.

Required release closure: recompose rather than add filler. Give every page/board a unique question and spatial answer; enlarge decisive diagrams; remove duplicate pages; use captions only where they add a new judgment.

### HAA-MAJOR-03 — The Chinese offline visual is partly English and register-first

Affected artifact: `visual/index.html`; the same information-order weakness also affects `visual/index.en.html`.

The Chinese page keeps all 15 renewal-project descriptions and all 12 AI-scenario descriptions in English. After the first metric block and five figure cards, the page leads with a 17-row control register, then long project and scenario lists. This is valid machine-facing evidence, but it is not natural Chinese juror communication and makes the page read like an audit dashboard.

Human consequence: the Chinese visual is not fully Chinese in its most implementation-rich sections, and the spatial differences among the three areas are harder to find than the register data.

Required release closure: translate the Chinese lists and move the three-area spatial story, ordinary-day baseline, and implementation sequence ahead of the full register. Keep the complete register available lower on the page.

## MINOR findings

### HAA-MINOR-01 — Area labels collide with figure geometry

The native site-overview figures place long area names and subtitles across or very close to circle outlines; `ZHONGZHIYUAN` is especially cramped. At report/PDF scale the collision becomes small, dense text.

### HAA-MINOR-02 — Rendered reports repeat the H1 title

Both report HTML files render the title in the hero and immediately repeat the same H1 from Markdown. This is harmless but visually redundant and weakens the opening hierarchy.

### HAA-MINOR-03 — Visual-page grid has a small-screen overflow risk

The figure grid uses `minmax(420px, 1fr)` and the mobile media query does not reduce that minimum. A viewport narrower than the 420 px track plus page padding can force horizontal overflow. On wide screens, the same auto-fit grid can show several fine-text figures too small for comfortable reading.

## POLISH findings

### HAA-POLISH-01 — PDF metadata and accessibility are unfinished

All four PDFs report title `untitled`, author `anonymous`, and `Tagged: no`. This is not a release blocker but is weak handoff polish.

### HAA-POLISH-02 — Chinese prose still exposes implementation codes

`patch`, `TTL`, `NO BUILD`, and several English action codes are purposeful, but short Chinese explanatory labels would help jurors who are not reading the package as an audit contract.

## Fifteen-question juror audit

| # | Test | Result | Judgment |
| --- | --- | --- | --- |
| 1 | First 30-second comprehension | PASS_WITH_ISSUES | “Keep the ordinary city working; admit AI conditionally” is immediate. The spatial answer is not. |
| 2 | Information hierarchy | PASS_WITH_ISSUES | Reports are coherent; A3/A0 and visual HTML are register/figure-grid heavy. |
| 3 | Visual density | MAJOR | PDF boards/booklets are too sparse and repetitive. |
| 4 | Title/concept legibility | PASS | The bilingual name and central judgment are memorable. |
| 5 | STATUS × ACTION clarity | PASS | Five statuses, conditional actions, stop, and exit are explicit. |
| 6 | Difference among three areas | PASS_WITH_ISSUES | Strong in prose/data, weakly spatialized in graphics. |
| 7 | Evidence vs design balance | MAJOR | Evidence is convincing; visible design is underexpressed. |
| 8 | AI visibility and restraint | PASS_WITH_ISSUES | Restraint is excellent; visible spatial AI consequences are too abstract. |
| 9 | Implementation credibility | PASS | G0–G4 evidence gates, roles, stops, and reuse support credibility. |
| 10 | Provisional-data disclosure | PASS | Repeated, specific, and not used to excuse false precision. |
| 11 | Chinese naturalness | PASS_WITH_ISSUES | Proposal prose is natural; Chinese visual has 27 English project/scenario descriptions. |
| 12 | English semantic parity | PASS | Sections, claims, figures, numbers, limitations, and release state align. |
| 13 | Typography/clipping/page balance | PASS_WITH_ISSUES | No PDF clipping observed; label collisions, mobile overflow risk, and page imbalance remain. |
| 14 | Looks like engineering report rather than urban design | MAJOR | Yes, especially figures, PDFs, and the offline visual register. |
| 15 | Core proposition survives without JSON | PASS | Both proposals carry it independently; the visual-only path does not yet carry the full spatial proposition. |

## Bounded current competition delta

Delta window: `64f424a7026e1e4e1d5d9fbe61e89a53467abf44..284dbb22bd062b39333af20f0edd6bcab9a24e1f`
Scope: primary proposal text only; no peer images, drawings, media, or external/global research.

| Peer | Classification | Reason |
| --- | --- | --- |
| `CatNebulaaaa/grow-with-jingzhang` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Implementation-first project packages and staged prerequisites; retain-first overlaps but not a status-action patch field. |
| `LShengYi/ai-pulse-belt` | THEME_OVERLAP | Strong state machines, evidence gates, rollback, and exit; core is public-AI lifecycle protocol. |
| `XingHE-YX/jingzhang-just-enough` | THEME_OVERLAP | Minimal AI, offline equivalence, and six adoption gates; spatial structure still uses one spine and three fields. |
| `benjaminshe/jingzhang-merge-belt` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Choice, fallback, and rollback overlap, but the core is a mainline/branch Git-merge metaphor—the opposite of no mandatory spine. |
| `cleverwwh/jingzhang-ai-belt-vision` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Historic main axis, three anchors, two wings, and blue-green loop. |
| `jiangmuran/jingzhang-leveling-line` | THEME_OVERLAP | Retesting, non-AI equivalence, and provisional honesty overlap; core is a measurement/closure-error network. |
| `kuankqaq/zhilian-jingzhang` | THEME_OVERLAP | Retain-first, survey gates, and three differentiated links overlap; core is a conventional railway/innovation/AI chain structure. |
| `loyal6/jingzhang-authenticity-commons` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Retain-first and daily/test/recovery states overlap; core is a bidirectional evidence-and-correction commons. |
| `siddhartha-yz/edgecase-jingzhang` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Survey-before-demolition and T1/T2/T3 operating states overlap; core is an edge-condition testing field organized by one Edgecase Mile. |
| `somnus-J-307/jingzhang-co-legible-interfaces` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Reversible interfaces and status visibility overlap; core is shared legibility on a reading spine. |
| `tfcrft/jingzhang-civic-weave` | THEME_OVERLAP | Retain-first, light-first, and provisional limits overlap; core is a perceptible AI public-life belt. |
| `wlaura-wlj/jingzhang-green-smart-ai-belt` | SAME_TERRITORY_DIFFERENT_PROPOSITION | Blue-green infrastructure and smart-core system are materially different. |
| `xie7ge/comind-loop` | THEME_OVERLAP | Existing-first, reversible components, and conditional interfaces overlap; core is a two-way translation protocol. |

`DIRECT_NEAR_DUPLICATE_FOUND=false`. An exact scoped search found no peer-owned use of the combined STATUS × ACTION / multi-status heterogeneous patch proposition. The competitive risk is thematic convergence around evidence gates, human fallback, reversibility, and retain-first—not direct duplication.

## Freeze recommendation

`C05_FUNDAMENTAL_CONTRADICTION=false`.

Freeze the concept, structured evidence, three-area distinctions, AI/NO-BUILD logic, and display name. Do not redesign C05. If authorized, the remaining work should be a bounded presentation release pass only.
