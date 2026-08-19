# AGY Windows Sandbox Layout & Configuration Matrix

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Location**: `V:\src\_review_isolation\sandbox\`  
**Date**: 2026-08-20  

---

## 1. Windows Sandbox Security Baseline

All `.wsb` configuration files enforce the following strict virtualization constraints:

```xml
<Configuration>
  <VGpu>Disable</VGpu>
  <Networking>Enable</Networking>
  <ClipboardRedirection>Disable</ClipboardRedirection>
  <PrinterRedirection>Disable</PrinterRedirection>
  <AudioInput>Disable</AudioInput>
  <VideoInput>Disable</VideoInput>
  <ProtectedClient>Enable</ProtectedClient>
  ...
</Configuration>
```

---

## 2. Sandbox Filesystem Mapping Matrix

| Sandbox Config File | Host Packet (Read-Only) | Host Runtime (Read-Only) | Assigned Output (Read/Write) | Target Reviewer Model |
| :--- | :--- | :--- | :--- | :--- |
| `reviewer-a-agy.wsb` | `V:\src\_review_isolation\packet` | `V:\src\_review_isolation\agy-runtime` | `V:\src\_review_isolation\output-a` | `claude-opus-4-6-thinking` (Probe) |
| `reviewer-a-agy-score.wsb` | `V:\src\_review_isolation\packet` | `V:\src\_review_isolation\agy-runtime` | `V:\src\_review_isolation\output-a` | `claude-opus-4-6-thinking` (Formal Score) |
| `reviewer-b-agy-score.wsb` | `V:\src\_review_isolation\packet` | `V:\src\_review_isolation\agy-runtime` | `V:\src\_review_isolation\output-b` | `claude-sonnet-4-6` (Formal Score) |
| `reviewer-c-agy-score.wsb` | `V:\src\_review_isolation\packet` | `V:\src\_review_isolation\agy-runtime` | `V:\src\_review_isolation\output-c` | `gemini-3.7-flash-high` (Formal Score) |

---

## 3. Forbidden Paths (Enforced by Sandbox Hypervisor)

The following paths are completely inaccessible from inside the Sandbox:
- `V:\` (Entire Host Workstation Drive)
- `V:\src` (Host Development Root)
- `C:\Users\jerry` (Host User Profile & Documents)
- `C:\Users\jerry\.gemini` (Host Antigravity Configuration & Tokens)
- `C:\Users\jerry\.codex` (Host Codex Workspace)
- `V:\src\_reviewer-isolation-canary` (Host Canary Token Path)
- Cross-Reviewer Output Directories (`C:\ReviewerOutput-B`, `C:\ReviewerOutput-C`)
