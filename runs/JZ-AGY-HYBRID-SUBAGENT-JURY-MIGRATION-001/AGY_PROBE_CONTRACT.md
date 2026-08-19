# AGY Reviewer Probe Contract & Verification Specification

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Reviewer Target**: Reviewer A (`claude-opus-4-6-thinking`)  
**Probe Status**: SPECIFIED & READY FOR OWNER RUN  

---

## 1. Purpose of Non-Scoring Probe

The Probe execution qualifies the physical Windows Sandbox isolation and authentication mechanism using the primary flagship judge (`claude-opus-4-6-thinking`).

This probe is:
- **NON-SCORING**: Does not score the candidate or evaluate urban design quality.
- **DISPOSABLE**: The Sandbox environment is completely destroyed after probe completion.
- **ISOLATED**: Operates with zero host credential transfer.

---

## 2. Machine-Readable Probe JSON Contract

The probe script (`C:\ReviewerRuntime\confinement-probe-agy.ps1` & `reviewer-runner-agy.ps1`) produces a machine-readable output at `C:\ReviewerOutput\confinement-probe.json` matching the following schema:

```json
{
  "MODEL_REQUESTED": "claude-opus-4-6-thinking",
  "MODEL_EFFECTIVE": "claude-opus-4-6-thinking",
  "AUTH_PATH": "ephemeral-sandbox-device-auth",
  "PACKET_HASH": "66f02a67609792aad5234dd860d59c7ae3f6b6012d5f61ab06c9eaf013da5b29",
  "PACKET_VISIBLE": true,
  "OUTPUT_WRITABLE": true,
  "HOST_WORKSPACE_VISIBLE": false,
  "HOST_AGY_HOME_VISIBLE": false,
  "OTHER_OUTPUT_VISIBLE": false,
  "MEMORY_CONTAMINATION": false,
  "PROBE_PASS": true
}
```

---

## 3. Verification Criteria for PASS

1. `PACKET_VISIBLE == true` (Packet manifest and files readable).
2. `OUTPUT_WRITABLE == true` (`C:\ReviewerOutput` writable).
3. `HOST_WORKSPACE_VISIBLE == false` (`V:\src` inaccessible).
4. `HOST_AGY_HOME_VISIBLE == false` (`C:\Users\jerry\.gemini` inaccessible).
5. `OTHER_OUTPUT_VISIBLE == false` (No cross-talk with `output-b` / `output-c`).
6. `MEMORY_CONTAMINATION == false` (No prior conversation memory used).
7. `MODEL_REQUESTED == claude-opus-4-6-thinking` (Exact model resolved).
