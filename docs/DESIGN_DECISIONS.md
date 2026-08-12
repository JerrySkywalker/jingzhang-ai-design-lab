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

**Status:** Accepted by Human Owner

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
