# Design Decision Log

This is the owner-level decision record. Detailed alternatives can live elsewhere; this file records project-direction changes that future sessions must not silently reverse.

## D-001 — Separate design-memory repository from formal submission

**Date:** 2026-08-11  
**Status:** Accepted

Create `JerrySkywalker/jingzhang-ai-design-lab` as an independent public design/research repository. The eventual competition entry will use a separate fork of `open-city-ai/haidian`.

**Reason:** preserve ideas, evidence, rejected alternatives and human/AI discussion without polluting the formal submission scope or depending on chat context.

## D-002 — Treat official task as a complete urban-design commission

**Date:** 2026-08-11  
**Status:** Accepted

Tracks are treated as emphasis labels, not as permission to submit a narrow technology topic. Candidate concepts must be capable of covering the complete official urban-design package.

**Reason:** re-reading the taskbook, design brief, proposal template and design-depth requirements showed that complete coverage is mandatory.

## D-003 — Reclassify “minimum-sufficient sensing”

**Date:** 2026-08-11  
**Status:** Accepted

“Minimum-sufficient sensing / Know-Enough” is no longer treated as a possible total-city concept. It is retained as a technical subsystem that may strengthen selected AI/robotics/public-service scenarios.

## D-004 — Candidate 01: Re-Embodied Jingzhang

**Date:** 2026-08-11  
**Status:** Superseded by D-008 for current candidate status

Record `Re-Embodied Jingzhang / 再具身京张` as Candidate 01. This is **not** a final selection.

Before selection it must survive comparison against at least two materially different complete urban-design concepts and demonstrate credible coverage of the full requirements matrix.

## D-005 — Candidate 02: Three Neighbourhoods Jingzhang

**Date:** 2026-08-12

**Status:** Superseded by D-008

Record **Three Neighbourhoods Jingzhang / 京张三邻** as Candidate 02 for architecture comparison. Its first-principles proposition is that the three key areas should become independently complete innovation neighbourhoods before they are treated as specialised nodes on a branded corridor.

This is **not** a final selection. The current collision audit rates it HIGH because mature stay, belong, living and local-city-unit proposals already occupy much of the territory. It proceeds only if verified catchments, distinct urban forms and a many-to-many federation can demonstrate more than vocabulary-level difference.

## D-006 — Candidate 03: Jingzhang Habitat Mosaic

**Date:** 2026-08-12

**Status:** Superseded by D-007 and D-008

Record **Jingzhang Habitat Mosaic / 京张生境拼图** as Candidate 03 for architecture comparison. Its first-principles proposition is that soil, water, canopy, habitat continuity and seasonal comfort should determine urban form and renewal before technology display.

This is **not** a final selection. The current collision audit rates it HIGH TO VERY HIGH because habitat, season, shade, forest-rail and ground-first proposals already occupy this field. It proceeds only if qualified landscape, ecology and hydrology work can establish a distinct non-linear spatial structure.

No decision among Candidates 01, 02 and 03 is made by D-005 or D-006.

## D-007 — Round-1 downselect and Round-2 falsification

**Date:** 2026-08-12

**Status:** Accepted by Human Owner

Supersede the Round-1 evaluation status for the purpose of the next research round:

```text
C01 = KEEP_HARDEN
C02 = KEEP_CHALLENGER
C03 = KILL_STANDALONE / SALVAGE_REVIEW_LENS
ROUND_2 = C01_VS_C02_FALSIFICATION
NEW_CANDIDATE_REQUIRED = false
FORMAL_SUBMISSION_READY = false
```

Candidate 03 remains preserved as design memory; its reusable ecological and recovery reasoning becomes the candidate-neutral Living Systems Gate. This downselect does not choose a final winner or authorize formal-submission work. Full rationale and consequences are recorded in `decisions/ADR-0002-round1-candidate-downselect.md`.

## D-008 — Round-3 Owner downselect and Round-4 professional admission

**Date:** 2026-08-12

**Status:** Superseded by D-009 for current candidate status

Materialize the Owner-approved Round-3 convergence:

```text
C01 = SOLE_SURVIVING_PROVISIONAL_CANDIDATE
C01_NEXT_GATE = PROFESSIONAL_SPATIAL_ADMISSION
C01_FINAL_WINNER = false

C02 = KILL
C02_ORDINARY_DAY_COMPLETENESS_GATE = KEEP

C03 = KILL_STANDALONE
C03_LIVING_SYSTEMS_GATE = KEEP

CANDIDATE_04 = TRIGGER_ONLY_IF_C01_FAILS_NEXT_GATE
RE_EMBODIMENT_TOTAL_BRAND = NOT_LOCKED
RE_EMBODIMENT_TECHNICAL_SUBSYSTEM = KEEP_FOR_NOW
FORMAL_FORK = NOT_YET
```

C02's exactly-three identity is rejected by its Round-3 falsification result and may not be restored by vocabulary change. Its Ordinary-Day Completeness Contract becomes a candidate-neutral review gate. C03 remains killed as a standalone candidate, while its Living Systems Gate remains active.

C01 is the only surviving provisional candidate. It is not the final winner and may still be killed in Round 4. The next gate is professional spatial admission, including urban-design judgment and the dependent transport, landscape and building-interface questions.

Missing authoritative geometry is a precision and recalculation risk, not an absolute fork or formal-intake blocker. Provisional geometry may support formal intake when its status and limits are disclosed; authoritative data arriving later triggers recomputation of dependent geometry, metrics, figures and claims.

`FORMAL_MIGRATION_READINESS` remains `NOT_READY_TO_FORK`. The controlling gates are `OWNER_FINAL_DIRECTION` and `C01_SPATIAL_ADMISSION`. Full rationale and consequences are recorded in `decisions/ADR-0003-round3-owner-downselect.md`.

## D-009 — Accept C01 kill and authorize Candidate 04

**Date:** 2026-08-12

**Status:** Accepted by Human Owner

Accept the Round-4 proxy-panel C01 kill recommendation and materialize the Owner direction:

```text
C01 = KILLED_AS_STANDALONE_CANDIDATE
C01_TOTAL_BRAND_RE_EMBODIED_JINGZHANG = RETIRED

C01_TASK_TO_SPACE_METHOD = KEEP_CANDIDATE_NEUTRAL
ORDINARY_DAY_COMPLETENESS_GATE = KEEP_CANDIDATE_NEUTRAL
LIVING_SYSTEMS_GATE = KEEP_CANDIDATE_NEUTRAL

C02 = KILLED
C03 = REVIEW_LENS_ONLY

C04_TRIGGER = AUTHORIZED_NOW
C04_GENERATION_MODE = ONE_SHOT_CONSTRAINED

FINAL_WINNER = NONE
FORMAL_FORK = NOT_YET
```

The retired candidate identities are C01 Re-Embodied Jingzhang, C02 Three Neighbourhoods Jingzhang and C03 Habitat Mosaic as a standalone candidate. C01 may not be revived through renaming, deleting two cells while preserving its candidate claim, or relabelling ordinary civic, servicing or back-of-house space.

The Task-to-Space Requirement Method, Ordinary-Day Completeness Gate, Living Systems Gate and evidence/falsification discipline remain reusable candidate-neutral methods. They may review C04 but may not silently determine its concept, name, spatial structure, key-area roles or technical spine.

This decision authorizes the separate next Goal `JZ-C04-ONE-SHOT-001`; it does not create Candidate 04. It selects no final winner and authorizes neither a formal fork nor official-repository mutation. Full rationale and consequences are recorded in `decisions/ADR-0004-accept-c01-kill-and-trigger-c04.md`.

## D-010 — R5 recover provisional Candidate 05

**Date:** 2026-08-13

**Status:** Provisional candidate recovered under Owner-authorized R5 criteria; Owner final lock required

The C04 one-shot correctly proved that no premise passed the old absolute-white-space gates, but did not prove that no direction could compete under the official rubric. R5 reclassified portability and collision, added site evidence v2, rescored the seven unchanged premises, deep-read the top-four peers, developed H6/H2 comparable mini-schemes and ran six independent proxy reviews.

```text
C04 = FAILED_GENERATION_RUN
C05 = JINGZHANG_IN_PLACE
C05_STATUS = PROVISIONAL_FINAL_CANDIDATE_WITH_REQUIRED_CHANGES
C05_SOURCE_PREMISE = H6_FINE_GRAIN_RENEWAL_FIELD
C05_OFFICIAL_RUBRIC_PROXY = 78.7/100
C05_AI_PLANNING_INNOVATION = 3.0/5_CONDITIONAL_SPECIALIST_FLOOR
C05_COLLISION = SAME_TERRITORY_DIFFERENT_PROPOSITION

FINAL_WINNER = OWNER_DECISION_REQUIRED
FORMAL_FORK = NOT_YET
CANDIDATE_06 = NOT_AUTHORIZED
```

C05's binding conditions are: an evidence-derived status/action spatial plan; three Task-to-Space packets with AI-off/no-build/exit; measurable pilot triggers; resident/business continuity, affordability and accessible consultation; exact-geometry and building/title/engineering discipline. Removing these conditions or reducing AI to optional analysis/tenancy returns `KILL_RECOMMENDATION`.

H2 Enterprise Space Ladder is not co-promoted because Growth Mesh materially dominates its enterprise-growth mechanism and three-area roles. Its physical premises taxonomy may be a C05 subsystem only after site/building/demand evidence.

This decision records the working candidate permitted by the Owner's R5 recovery thresholds. It does not select the final winner, create a formal fork, commit a dummy submission, push official changes or authorize Candidate 06. Full rationale is in `decisions/ADR-0005-recover-provisional-candidate-05.md`.
