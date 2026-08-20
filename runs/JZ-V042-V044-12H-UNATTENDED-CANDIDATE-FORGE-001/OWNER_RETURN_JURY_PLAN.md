# Owner Return Plan: Exact-Model Isolated Jury Execution

**Goal ID**: `JZ-V042-V044-12H-UNATTENDED-CANDIDATE-FORGE-001`  
**Host Development Completed**: Candidate `v0.4.2` (`a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`) forged and certified.  
**Active Blind Packet**: `CANDIDATE-V042` (Packet Hash: `394d74ee123079d89175a12a09aaf39991454c70c062c7f826916dfaf1097656`)  
**Packet Location**: `V:\src\_review_isolation\packet\`  
**Date**: 2026-08-20  

---

## 1. Executive Summary for the Owner

During this unattended ~12-hour window:
1. **Remote Safety Verified**: Confirmed `HIGH_WATER_GUARD_ACTIVE=false` on upstream `open-city-ai/haidian`. PR #2774 remains safely in Draft; no unverified upstream releases or PR mutations were performed.
2. **Benchmark Intelligence Integrated**: Analyzed merged 90/100 cases (`Sonike/jingzhang-handover-line`, `anselasimov-web/the-ren-line`) and 86/100 case (`jiangmuran/jingzhang-leveling-line`). Extracted transferable presentation, evidence, and reading hierarchy patterns without compromising the unique `STATUS × ACTION` identity.
3. **Multi-Subagent Deliberation**: 3 Explorers and 3 Critics diagnosed v0.4.1a across all 7 official dimensions and selected 2 high-leverage primary surgery targets: `implementation_feasibility` (20%) and `expression_completeness` / `brief_alignment` (15% + 20%).
4. **Candidate v0.4.2 Forged & Certified**:
   - Added 3-tier reading roadmap (60s / 5min / Deep read) and front-fold thesis.
   - Added standardized 3-step "How to Read This Figure" guides beneath all 5 core figures.
   - Deepened D0–D100 delivery contracts with 3 defined role profiles, T1–T3 telemetry triggers, and modular Plug-and-Play MEP reversibility (30-min reset).
   - Grounded public equity in a vivid persona morning journey (72-year-old resident P4).
   - Passed all 4 local gates (`DETERMINISTIC`, `SPATIAL`, `VISUAL`, `PROFESSIONAL`) with 0 blocking issues.
5. **Deterministic Blind Jury Packets Built**:
   - `V:\src\_review_isolation\packet\` is updated and verified 100% reproducible.
   - Exact-model AGY Windows Sandbox jury environments are fully wired and ready for execution.

---

## 2. Pinned Exact-Model Jury Panel

| Reviewer ID | Sandbox WSB Config | Pinned Exact AGY Model | Host Output Directory | Role & Specialty |
| :---: | :--- | :--- | :--- | :--- |
| **Reviewer A** | `sandbox/reviewer-a-agy-score.wsb` | `claude-opus-4-6-thinking` | `output-a/` | Deep structural reasoning, rubric gaming detection |
| **Reviewer B** | `sandbox/reviewer-b-agy-score.wsb` | `claude-sonnet-4-6` | `output-b/` | Spatial design clarity, urban systems coherence |
| **Reviewer C** | `sandbox/reviewer-c-agy-score.wsb` | `gemini-3.7-flash-high` | `output-c/` | Multimodal packaging, data-drawing consistency |
| **TieBreaker** | `sandbox/reviewer-tb-agy-score.wsb` | `gpt-oss-120b-medium` | `output-tb/` | Invoked only if Reviewers A, B, C score spread > 15 pts |

---

## 3. Owner Step-by-Step Scoring Procedure

When ready to run formal isolated jury scoring:

### Step 1: Launch the Jury
In host PowerShell (as Administrator):
```powershell
Set-Location V:\src\_review_isolation
.\Start-JZJury.ps1 -Reviewer All -Mode Score
```
*This launches three isolated Windows Sandbox instances (one for each reviewer).*

### Step 2: Complete Interactive Sign-in (If Prompted)
In each Sandbox window, AGY CLI will use ephemeral sandbox-local authentication. Complete the browser device-code confirmation if prompted.

### Step 3: Run the Reviewer Script
In each Sandbox PowerShell terminal, execute:
- **Sandbox A**: `.\reviewer-runner-agy.ps1 -Reviewer A -Mode Score`
- **Sandbox B**: `.\reviewer-runner-agy.ps1 -Reviewer B -Mode Score`
- **Sandbox C**: `.\reviewer-runner-agy.ps1 -Reviewer C -Mode Score`

### Step 4: Monitor and Aggregate Results
From the host PowerShell terminal:
```powershell
# Check scorecard generation status:
.\Get-JZJuryStatus.ps1

# When all 3 scorecards are complete, aggregate into final report:
.\Aggregate-JZJury.ps1
```

---

## 4. Promotion Criteria for Official Submission
Once the Jury completes:
- **Threshold for Official Promotion**: Jury Median Score **≥ 85 / 100** (with all 3 reviewers ≥ 80).
- If Jury Median **≥ 85**: The Owner may safely promote candidate `v0.4.2` (`a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`) by pushing `experiment/JZ-V042-12H-FORGE-001` to `haidian` PR #2774.
- If Jury Median **< 85**: Consult `FORMAL_JURY_AGGREGATE.json` to identify specific dimension blockers for bounded iteration.
