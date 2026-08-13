# Spatial Visual Grammar — RC2

## Purpose and scope

This is a presentation grammar for the locked `JINGZHANG_IN_PLACE` proposition. It translates existing package truth into legible plan, atlas, section and sequence drawings. It is not a new design layer, land-use control, survey, parcel map, or implementation claim.

All geometric positions remain derived from the package's provisional conceptual geometry. Every graphic carries the same qualification: **conceptual / provisional / not an official redline, parcel plan, statutory control, ownership map, or engineering drawing.**

## Evidence-status family

| Machine value | Reader label (ZH) | Reader label (EN) | Colour | Graphic treatment |
| --- | --- | --- | --- | --- |
| `BUILT_OPERATING` | 已建 / 运行 | Built / operating | navy `#17324D` | solid fill with a small operational dot |
| `APPROVED_OR_IN_DELIVERY` | 获批 / 实施中 | Approved / in delivery | green `#3C7C69` | solid fill with diagonal construction hatch |
| `CONTROLLED_ACCESS` | 受控 / 限制进入 | Controlled / limited access | amber `#C17B13` | outline plus threshold bars |
| `SURVEY_ONLY_UNKNOWN` | 待调查 | Survey required | magenta `#A33B6B` | dashed outline plus question mark marker |
| `VERIFIED_ADAPTABLE` | 经核验可适应 | Proven adaptable candidate | teal `#287E8E` | solid outline plus reversible-arrow marker |

Status is never a permission. It is always paired with a current limit, an evidence trigger, a stop condition and an exit/reuse condition from `status-action-register.json`.

## Action family

| Action | Reader label (ZH) | Reader label (EN) | Symbolic move |
| --- | --- | --- | --- |
| `RETAIN` | 保留 | Retain | unbroken existing-use line |
| `REPAIR` | 修复 | Repair | stitched line |
| `OPEN_EDGE` | 开放边缘 | Open edge | outward opening arrow |
| `SUBDIVIDE_RECONNECT` | 细分 / 重连 | Subdivide / reconnect | paired links across a threshold |
| `ADAPT` | 适应改造 | Adapt | reversible loop arrow |
| `INFILL` | 条件性填补 | Conditional infill | light dot field with a gate icon |
| `NO_BUILD` | 不建设 | No build | open ground / no-volume mark |

Actions are shown as line/symbol overlays, never as a second competing land-use palette. Where a register uses an auxiliary action such as `ALIGN` or `SURVEY_REQUIRED`, the drawing states the evidence action in words rather than inventing a new spatial class.

## Relationship family

| Relationship | Line / surface treatment | Required reading |
| --- | --- | --- |
| ordinary public route | wide navy line, white centre | continuous everyday walking; may not depend on a controlled interior |
| controlled threshold | amber dashed gate line | timed, booked or task-bound access; never substitutes for public continuity |
| service / logistics route | magenta dashed fine line | visible, time/state-bounded servicing and maintenance |
| blue-green interface | green/teal translucent band | shade, drainage, rain refuge, maintenance or seasonal operation |
| transit / grade-separated interface | graphite double line / split level | audit question or typological interface, never a claimed built crossing |

## Plan hierarchy

1. Human routes, public-space sequence and key-area callouts lead the eye.
2. Status-action patches sit above a quiet conceptual fabric.
3. Buildings, land-use fields and provisional boundaries remain low contrast and explicitly conceptual.
4. Status uses colour plus label/pattern; accessibility never depends on colour alone.
5. AI only appears at the three existing task-dependent conditions. Ordinary city uses and `NO_BUILD` findings remain visible.

## Area-specific prototypes

- **众智园**: water → public arrival / landscape → visible maintenance and productive edge → controlled validation, with ordinary arrival kept outside the test envelope.
- **AI 原点**: street / park → ordinary public learning room → reversible controlled project state → controlled campus; public movement stays on the public side.
- **大钟寺**: grade-separated arrival → accessible walking / cycling continuity → mixed frontage / service side → staffed adoption interface, with no invented station parcel, bridge or tunnel.

## Bilingual and accessibility rules

- Chinese figures contain Chinese reader-facing copy; English figures contain English reader-facing copy. IDs remain neutral.
- Each plan/section has an on-image title, legend, data/provisional note and visual-text alternative in the corresponding HTML.
- Patterns, labels, line weight and symbols duplicate colour semantics.
- Motion is not required for any meaning. Interactive registers use native `<details>` and retain a static summary.
