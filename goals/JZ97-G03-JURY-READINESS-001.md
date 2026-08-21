# JZ97-G03-JURY-READINESS — Three-Model Anchor Jury Infrastructure Readiness

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G03-JURY-READINESS-001`  
PARENT_GOAL=`JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`  
ENGINE=`AGY gemini-3.7-flash-high`

## 1. Admission Prerequisites

- **G01 PASS**: Current official rubric dimensions, weights, and integer 0..5 scorecard schema locked.
- **G02 PASS**: 7 trusted exact-head anchors (N4, X8, B2, W7, J9, L5, P3) discovered, verified, and compiled.
- **Airlock Security**: Zero modifications to `haidian` product repository, PR #2774, or official competition repositories.

## 2. Canonical Deliverables & Specifications

### 2.1 Packet Builder Blinding Sanitize (`build_anchor_packets.py`)
- Removed `source_head` and `source_package_path` from generated `REVIEW_PACKET_MANIFEST.json` envelopes.
- Provenance remains strictly isolated in coordinator receipts (`G02_BLINDING_MAP.json`, `G02_TRUSTED_ANCHOR_LEDGER.json`).
- Envelope contains exclusively: `schema_version`, `neutral_id`, `packet_file_count`, `packet_hash`, `visual_surface_count`, `visual_warnings`, `manifest_envelope_excluded_from_its_own_hash`, and `files`.

### 2.2 7 Blind Evaluation Packets
- All 7 packets in `V:\src\_review_isolation\packets\{N4, X8, B2, W7, J9, L5, P3}` sanitized and verified.
- Contain zero author names, PR numbers, commit SHAs, or historical score tokens.

### 2.3 Windows Sandbox Isolation (`V:\src\_review_isolation\sandbox\`)
- Configured 4 WSBs: `reviewer-a-agy-score.wsb` (Opus), `reviewer-b-agy-score.wsb` (Sonnet), `reviewer-c-agy-score.wsb` (Gemini), and `reviewer-tb-agy-score.wsb` (TieBreaker).
- Strict isolation parameters:
  - `VGpu`: `Disable`
  - `Networking`: `Enable` (required for fresh ephemeral sandbox authentication)
  - `ClipboardRedirection`: `Disable`
  - `PrinterRedirection`: `Disable`
  - `AudioInput` / `VideoInput`: `Disable`
  - `ProtectedClient`: `Enable`
- Mapped Folders:
  - `V:\src\_review_isolation\packets` -> `C:\ReviewPackets` (ReadOnly)
  - `V:\src\_review_isolation\packet` -> `C:\ReviewPacket` (ReadOnly fallback)
  - `V:\src\_review_isolation\agy-runtime` -> `C:\ReviewerRuntime` (ReadOnly)
  - `V:\src\_review_isolation\output-[a|b|c|tb]` -> `C:\ReviewerOutput` (ReadWrite)

### 2.4 In-Sandbox Multi-Anchor Runner (`reviewer-runner-agy.ps1`)
- Multi-anchor execution via `-Anchor <All|N4|X8|B2|W7|J9|L5|P3|Default>`.
- Cross-anchor isolation: purges `C:\AgyHome\brain` before evaluating each anchor to guarantee zero conversation memory carry-over.
- Partitioned output paths: `C:\ReviewerOutput\<AnchorId>\scorecard.json` and `scoring-log.txt`.
- Deterministic score computation: validates integer 0..5 across all 7 dimensions and computes `total_weighted_score` using official weights (brief_alignment=20, originality=10, ai_planning_innovation=15, implementation_feasibility=20, public_interest_inclusion=10, risk_compliance=10, expression_completeness=15).
- Resilient error trapping: writes `error.json` without unhandled script termination.

### 2.5 Host Orchestration & Aggregation Suite
- `Start-JZAnchorJury.ps1` / `Start-JZJury.ps1`: Host preflight path validation, directory creation, numbered step-by-step instructions.
- `Get-JZAnchorJuryStatus.ps1` / `Get-JZJuryStatus.ps1`: 7×3 matrix dashboard showing all 21 scorecards, score spreads, and completion progress.
- `Aggregate-JZAnchorJury.ps1` / `Aggregate-JZJury.ps1`: Scans all anchor output folders, computes medians, means, spreads, tie-breaker triggers (>15 pt spread), and dimension breakdowns. Produces `FORMAL_ANCHOR_JURY_AGGREGATE.json` and `FORMAL_ANCHOR_JURY_REPORT.md`.
- `Test-JZJuryReadiness.ps1`: 5-phase automated preflight verification suite.

## 3. Verification Criteria

- [x] All 7 anchor manifests contain valid schema envelopes with zero blinding leaks.
- [x] All 4 WSB sandbox files contain required mapped folders and security isolation settings.
- [x] Runner script parses with zero PowerShell errors and supports multi-anchor execution.
- [x] Status and aggregation scripts handle partial and complete matrix states gracefully.
- [x] Preflight verification suite `Test-JZJuryReadiness.ps1` passes 100% of checks (64/64).

## 4. State Transition Rules

When the Owner completes the in-Sandbox jury execution for all 7 anchors across Reviewers A, B, and C:
1. `Aggregate-JZAnchorJury.ps1` processes all 21 scorecards.
2. If any anchor has spread >15.0 pt, Reviewer TieBreaker is executed for that anchor.
3. Update `state/JZ97_PROGRAM_STATE.json`:
   - Set `gates.C1_CALIBRATION_READY = "PASS"`.
   - Advance `current_goal` to `JZ97-G04-CALIBRATION-MODEL-001`.

NEXT_ON_PASS=`JZ97-G04-CALIBRATION-MODEL-001`
