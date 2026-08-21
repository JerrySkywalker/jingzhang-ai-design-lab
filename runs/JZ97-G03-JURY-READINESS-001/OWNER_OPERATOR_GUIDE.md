# Owner Operator Guide — Goal G03 Anchor Jury Execution

**Target**: Run Goal `JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`  
**Panel**: 3 Isolated Reviewers + 1 Optional TieBreaker  
**Anchors**: 7 Blind Packets (`N4`, `X8`, `B2`, `W7`, `J9`, `L5`, `P3`)  
**Total Target Scorecards**: 21 (7 anchors × 3 reviewers)  

---

## Architecture Overview

All 7 blinded anchor packets are staged in `V:\src\_review_isolation\packets\`.  
Each Windows Sandbox instance mounts `V:\src\_review_isolation\packets` as `C:\ReviewPackets` (ReadOnly) and its respective output directory as `C:\ReviewerOutput` (ReadWrite).

```text
Host (V:\src\_review_isolation)
 ├── packets/ (N4, X8, B2, W7, J9, L5, P3) ──> Mount as C:\ReviewPackets (ReadOnly)
 ├── agy-runtime/ ────────────────────────────> Mount as C:\ReviewerRuntime (ReadOnly)
 ├── output-a/ ───────────────────────────────> Mount as C:\ReviewerOutput (Reviewer A)
 ├── output-b/ ───────────────────────────────> Mount as C:\ReviewerOutput (Reviewer B)
 ├── output-c/ ───────────────────────────────> Mount as C:\ReviewerOutput (Reviewer C)
 └── output-tb/ ──────────────────────────────> Mount as C:\ReviewerOutput (TieBreaker)
```

---

## Step-by-Step Operator Instructions

### Step 1: Preflight Health Check (Host)
In host PowerShell:
```powershell
Set-Location V:\src\_review_isolation
.\Test-JZJuryReadiness.ps1
```
*Verify that all 64/64 checks pass before launching Sandboxes.*

---

### Step 2: Launch Windows Sandbox Instances (Host)
In host PowerShell:
```powershell
Set-Location V:\src\_review_isolation
.\Start-JZAnchorJury.ps1 -Reviewer All -Mode Score
```
*This launches 3 isolated Windows Sandbox windows (Reviewer A, Reviewer B, Reviewer C).*

---

### Step 3: Run In-Sandbox Scoring (Inside Each Sandbox Window)

In each Windows Sandbox window, authenticate AGY CLI if prompted by browser, then execute:

#### Sandbox Window A (Claude Opus 4.6 Thinking):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer A -Anchor All -Mode Score
```

#### Sandbox Window B (Claude Sonnet 4.6):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer B -Anchor All -Mode Score
```

#### Sandbox Window C (Gemini 3.7 Flash High):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer C -Anchor All -Mode Score
```

*Note: You can also evaluate a single anchor by passing `-Anchor <ID>` (e.g. `.\reviewer-runner-agy.ps1 -Reviewer A -Anchor N4 -Mode Score`).*  
*Memory purge is automatically executed between anchors (`C:\AgyHome\brain` cleanup).*

---

### Step 4: Monitor 7×3 Dashboard (Host)
From host PowerShell, run at any time to inspect real-time progress:
```powershell
Set-Location V:\src\_review_isolation
.\Get-JZAnchorJuryStatus.ps1
```
*This displays a 7×3 matrix showing progress across all 21 scorecards, total scores, spreads, and missing cards.*

---

### Step 5: Aggregate Results & Generate G04 Inputs (Host)
When all 21 scorecards are generated:
```powershell
Set-Location V:\src\_review_isolation
.\Aggregate-JZAnchorJury.ps1
```
*This outputs `V:\src\_review_isolation\output\FORMAL_ANCHOR_JURY_AGGREGATE.json` and `FORMAL_ANCHOR_JURY_REPORT.md`.*

---

### Step 6 (Optional): Tie-Breaker Execution
If `Aggregate-JZAnchorJury.ps1` reports any anchor with a score spread `> 15.0` points between Reviewers A, B, and C:
1. Launch TieBreaker Sandbox from host:
   ```powershell
   .\Start-JZAnchorJury.ps1 -Reviewer TieBreaker -Mode Score
   ```
2. In the TieBreaker Sandbox window:
   ```powershell
   .\reviewer-runner-agy.ps1 -Reviewer TieBreaker -Anchor <AnchorId> -Mode Score
   ```
3. Re-run aggregation:
   ```powershell
   .\Aggregate-JZAnchorJury.ps1
   ```
