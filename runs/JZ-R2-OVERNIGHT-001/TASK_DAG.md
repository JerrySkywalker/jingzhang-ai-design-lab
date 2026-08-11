# JZ-R2-OVERNIGHT-001 Task DAG

| ID | Task | Depends on | Status | Evidence output |
| --- | --- | --- | --- | --- |
| A0 | Read-only admission and isolated worktree | none | COMPLETE | RUN_MANIFEST.md |
| A1 | Re-read long-term local sources | A0 | COMPLETE | RUN_STATE.md |
| A2 | Refresh official environment | A0 | COMPLETE | research/overnight/official-refresh.md |
| B1 | Materialize Owner Round-1 downselect | A1 | COMPLETE | decisions/ADR-0002-round1-candidate-downselect.md |
| B2 | Extract C03 Living Systems Gate | A1 | COMPLETE | docs/review-lenses/LIVING_SYSTEMS_GATE.md |
| C1 | C01 collision audit | A2 | COMPLETE | research/benchmarks/c01-collision-audit-v0.2.md |
| C2 | C01 unique-kernel falsification | C1 | COMPLETE | concepts/re-embodied-jingzhang/round2/ |
| C3 | C01 shared-infrastructure experiment | C2 | COMPLETE | experiments/c01-shared-embodied-infrastructure/ |
| C4 | Translate C01 technical result into space | C3 | COMPLETE | SPATIAL_CONSEQUENCES.md |
| D1 | C02 federation collision audit | A2 | COMPLETE | research/benchmarks/c02-federation-audit-v0.2.md |
| D2 | C02 why-three falsification | D1 | COMPLETE | concepts/candidate-02-three-neighbourhoods/round2/WHY_THREE.md |
| D3 | C02 ordinary-day completeness experiment | D2 | COMPLETE | experiments/c02-ordinary-day-completeness/ |
| D4 | C02 spatial falsification | D3 | COMPLETE | concepts/candidate-02-three-neighbourhoods/round2/ |
| E1 | Apply Living Systems Gate to C01/C02 | B2,C4,D4 | COMPLETE | two living-systems reviews |
| E2 | Mutual pressure tests | C4,D4 | COMPLETE | two cross-review files |
| E3 | Professional and human gates | C4,D4 | COMPLETE | two PROFESSIONAL_GATES.md |
| F1 | Four-role red team | E1,E2,E3 | COMPLETE | docs/ROUND2_RED_TEAM.md |
| F2 | Evidence-backed comparison v0.2 | F1 | COMPLETE | docs/CANDIDATE_COMPARISON_V0.2.md |
| F3 | Morning review package | F2 | COMPLETE | MORNING_BRIEF.md; NEXT_OWNER_DECISIONS.md |
| G1 | Final official delta, validation and push | F3 | COMPLETE | final Git and run-state receipts |

Only G1 may close the run. Candidate death does not cancel the other candidate's audit.
