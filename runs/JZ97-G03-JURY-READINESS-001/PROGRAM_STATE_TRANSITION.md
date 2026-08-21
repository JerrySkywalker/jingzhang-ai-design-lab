# Program State Transition Receipt

**Current Program**: `JZ-97-CONVERGENCE-TRAIN-001`  
**Current Train**: `A_CALIBRATION_FOUNDATION`  
**Completed Preparation Goal**: `JZ97-G03-JURY-READINESS-001`  
**Next Goal for Owner Execution**: `JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`  

---

## Gate Status Matrix

| Gate | Name | State | Readiness / Condition |
| :---: | :--- | :---: | :--- |
| **C0** | `CONTENT_BASELINE` | **PASS** | Frozen v0.4.1a & candidate v0.4.2 certified |
| **C1** | `CALIBRATION_READY` | **PENDING** | Infrastructure 100% ready; awaits in-Sandbox jury scores across 7 anchors for G04 calibration |
| **C2** | `CANDIDATE_LIFT` | **BLOCKED** | Admitted only after C1 PASS |
| **C3** | `97_CLASS_READY` | **BLOCKED** | Requires C2 PASS + ceiling qualification |
| **C4** | `RELEASE_SAFE` | **BLOCKED** | Requires official high-water proof or Owner explicit release |
| **C5** | `TRUSTED_RESULT` | **BLOCKED** | Formal maintainer review of exact winner head |

---

## State Transition Roadmap

1. **Owner returns**: Executes in-Sandbox 3-model anchor scoring via `Start-JZAnchorJury.ps1` and `reviewer-runner-agy.ps1`.
2. **Aggregation**: Generates `FORMAL_ANCHOR_JURY_AGGREGATE.json` via `Aggregate-JZAnchorJury.ps1`.
3. **Goal G04**: Calibration Model computed. If error <= 5 pts and rank order >= 80%, transition `C1_CALIBRATION_READY -> PASS` and advance to G05.
