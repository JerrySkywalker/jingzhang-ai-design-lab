# AGY Reviewer A Probe Owner Handoff

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Reviewer Target**: Reviewer A (`claude-opus-4-6-thinking`)  
**Date**: 2026-08-20  

---

## 1. Executive Instructions for Owner

Follow these exact 3 steps to execute the qualification probe:

---

### STEP 1: HOST LAUNCH COMMAND

Run the following command in PowerShell on the host machine:

```powershell
powershell -ExecutionPolicy Bypass -File V:\src\_review_isolation\Start-JZReviewerAProbe-AGY.ps1
```

*What happens:* Validates runtime paths, checks packet SHA256, verifies WSB XML settings, and launches Windows Sandbox.

---

### STEP 2: SANDBOX PROBE COMMAND

Inside the newly opened Windows Sandbox window:
1. Complete normal interactive device sign-in if prompted by AGY.
2. Run the probe runner:

```powershell
.\reviewer-runner-agy.ps1 -Reviewer A -Mode Probe
```

*What happens:* Executes confinement checks, runs `claude-opus-4-6-thinking` against the neutral prompt, and writes `confinement-probe.json` to `C:\ReviewerOutput`.

---

### STEP 3: HOST RESULT COMMAND

After the Sandbox probe finishes (or Sandbox is closed), verify the qualification status on the host machine:

```powershell
powershell -ExecutionPolicy Bypass -File V:\src\_review_isolation\Get-JZReviewerAProbeStatus-AGY.ps1
```

*Expected Output:*
```
AGY_RUNTIME_FOUND=True
REVIEWER_A_WSB_FOUND=True
PACKET_HASH_MATCH=True
PROBE_OUTPUT_FOUND=True
REQUESTED_MODEL=claude-opus-4-6-thinking
EFFECTIVE_MODEL=claude-opus-4-6-thinking
MEMORY_CONTAMINATION=false
PROBE_PASS=True
```
