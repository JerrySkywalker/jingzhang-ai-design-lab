# Goal G03 Core Anchor Jury — Sequential Owner Execution Runbook

```text
GOAL_ID=JZ97-G03-THREE-MODEL-ANCHOR-JURY-001
RUN_ID=JZ97-A1-ACCELERATED-CALIBRATION-MEASUREMENT-QUICKSCORE-001
STATUS=OWNER_REQUIRED
WSB_CONCURRENCY_LIMIT=1
FORMAL_JURY_EXECUTION_MODE=SEQUENTIAL_FRESH_SANDBOX
TARGET_PANEL=3 Reviewers (A: Claude Opus 4.6 Thinking, B: Claude Sonnet 4.6, C: Gemini 3.7 Flash High)
TARGET_ANCHORS=5 Core Anchors (N4=77, X8=86, B2=90, W7=90, J9=96)
DIAGNOSTIC_RESERVES=2 Anchors (L5=90, P3=91) [STANDBY - DO NOT SCORE]
CORE_FORMAL_SCORECARDS=15 (5 anchors x 3 reviewers)
RESERVE_SCORECARDS=6_OPTIONAL
```

## Physical Sandbox Isolation Rules

1. **Strict Single-Instance Concurrency (`WSB_CONCURRENCY_LIMIT=1`)**: Microsoft Windows Sandbox supports only one active Sandbox instance at a time. The launcher strictly enforces sequential execution with a fresh Sandbox instance for each reviewer.
2. **Reviewer Output Isolation**: Each reviewer's `.wsb` file mounts ONLY their own respective output directory (`output-a`, `output-b`, `output-c`). No reviewer can see prior reviewer scorecards or outputs.
3. **Session Memory Purge**: The runner purges `C:\AgyHome\brain` between anchor evaluations to eliminate cross-anchor memory contamination.

---

## Sequential Step-by-Step Operator Instructions

### Step 1: Reviewer A (Claude Opus 4.6 Thinking)

1. **Launch Sandbox A from host PowerShell:**
   ```powershell
   Set-Location V:\src\_review_isolation
   .\Start-JZAnchorJury.ps1 -Reviewer A -Mode Score -Anchor Core
   ```
2. **Inside Sandbox Window A:**
   - Complete browser device authentication if prompted.
   - Run scoring:
     ```powershell
     Set-Location C:\ReviewerRuntime
     .\reviewer-runner-agy.ps1 -Reviewer A -Anchor Core -Mode Score
     ```
3. **Close Sandbox A window** once all 5 core anchors (`N4`, `X8`, `B2`, `W7`, `J9`) finish.

---

### Step 2: Reviewer B (Claude Sonnet 4.6)

1. **Launch Sandbox B from host PowerShell:**
   ```powershell
   Set-Location V:\src\_review_isolation
   .\Start-JZAnchorJury.ps1 -Reviewer B -Mode Score -Anchor Core
   ```
2. **Inside Sandbox Window B:**
   - Complete browser device authentication if prompted.
   - Run scoring:
     ```powershell
     Set-Location C:\ReviewerRuntime
     .\reviewer-runner-agy.ps1 -Reviewer B -Anchor Core -Mode Score
     ```
3. **Close Sandbox B window** once all 5 core anchors finish.

---

### Step 3: Reviewer C (Gemini 3.7 Flash High)

1. **Launch Sandbox C from host PowerShell:**
   ```powershell
   Set-Location V:\src\_review_isolation
   .\Start-JZAnchorJury.ps1 -Reviewer C -Mode Score -Anchor Core
   ```
2. **Inside Sandbox Window C:**
   - Complete browser device authentication if prompted.
   - Run scoring:
     ```powershell
     Set-Location C:\ReviewerRuntime
     .\reviewer-runner-agy.ps1 -Reviewer C -Anchor Core -Mode Score
     ```
3. **Close Sandbox C window** once all 5 core anchors finish.

---

### Step 4: Monitor Progress & Validate 15 Scorecards (Host PowerShell)

Inspect the status matrix across the 15 required core scorecards at any time:
```powershell
Set-Location V:\src\_review_isolation
.\Get-JZAnchorJuryStatus.ps1 -Anchor Core
```

---

### Step 5: Resume Compound Train A1

Once all 15 scorecards are complete (3/3 across `N4`, `X8`, `B2`, `W7`, `J9`), resume this Compound Train run to automatically execute:
1. **Phase 2 (G04 Calibration Model & Gate C1)**
2. **Phase 3 (G05 Candidate Measurement: v0.4.1a vs v0.4.2)**
3. **Phase 4 (G06 97-Band Blocker Matrix & Surgical Target Identification)**
