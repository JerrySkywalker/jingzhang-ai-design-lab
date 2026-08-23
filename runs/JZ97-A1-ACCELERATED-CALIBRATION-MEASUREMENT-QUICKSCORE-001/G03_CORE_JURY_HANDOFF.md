# Goal G03 Core Anchor Jury — Owner Execution Handoff

```text
GOAL_ID=JZ97-G03-THREE-MODEL-ANCHOR-JURY-001
RUN_ID=JZ97-A1-ACCELERATED-CALIBRATION-MEASUREMENT-QUICKSCORE-001
STATUS=OWNER_REQUIRED
TARGET_PANEL=3 Reviewers (A: Claude Opus 4.6 Thinking, B: Claude Sonnet 4.6, C: Gemini 3.7 Flash High)
TARGET_ANCHORS=5 Core Anchors (N4=77, X8=86, B2=90, W7=90, J9=96)
DIAGNOSTIC_RESERVES=2 Anchors (L5=90, P3=91) [STANDBY - DO NOT SCORE]
TOTAL_SCORECARDS=15 (5 anchors x 3 reviewers)
```

## Why Owner Action Is Required

Formal local jury scoring must run inside physically isolated **Windows Sandbox (WSB)** environments using authentic Owner device authentication. In accordance with safety airlock rules:
1. Formal jury scoring MUST NOT run on the host AGY session.
2. The agent MUST NOT simulate user authentication or transfer private host session tokens.
3. Host score state mutation is PAUSED until authentic scorecards are written to `_review_isolation/output-[a|b|c]`.

---

## Step-by-Step Operator Runbook

### Step 1: Launch 3 Reviewer Sandbox Windows (Host PowerShell)

Open PowerShell on host and execute:
```powershell
Set-Location V:\src\_review_isolation
.\Start-JZAnchorJury.ps1 -Reviewer All -Mode Score -Anchor Core
```
*This verifies all host paths, prepares output folders, and opens 3 Windows Sandbox windows (A, B, C).*

---

### Step 2: In-Sandbox Reviewer Execution (Inside Each Sandbox Window)

Inside each respective Windows Sandbox window, complete browser device authentication when prompted, then execute:

#### Sandbox Window A (Claude Opus 4.6 Thinking):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer A -Anchor Core -Mode Score
```

#### Sandbox Window B (Claude Sonnet 4.6):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer B -Anchor Core -Mode Score
```

#### Sandbox Window C (Gemini 3.7 Flash High):
```powershell
Set-Location C:\ReviewerRuntime
.\reviewer-runner-agy.ps1 -Reviewer C -Anchor Core -Mode Score
```

*Note: The runner will evaluate N4, X8, B2, W7, J9 sequentially, purging session memory (`C:\AgyHome\brain`) between anchors to ensure zero cross-anchor contamination.*

---

### Step 3: Monitor Live Progress (Host PowerShell)

Inspect real-time scoring progress on host at any time:
```powershell
Set-Location V:\src\_review_isolation
.\Get-JZAnchorJuryStatus.ps1
```
*Displays the live matrix showing completed cards, total scores, spreads, and missing cards.*

---

### Step 4: Resume Compound Train A1

Once all 15 scorecards are complete (3/3 across N4, X8, B2, W7, J9), resume this Compound Train to automatically proceed with:
- **Phase 2 (G04 Calibration Model & Gate C1)**
- **Phase 3 (G05 Candidate Baseline Measurement: v0.4.1a vs v0.4.2)**
- **Phase 4 (G06 97-Band Blocker Matrix & Surgical Target Identification)**
