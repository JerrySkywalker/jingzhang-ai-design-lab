# Owner Brief: AGY Migration & Subagent Jury Qualification

**Run ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  
**State**: MIGRATION QUALIFIED — READY FOR OWNER PROBE  

---

## 1. Executive Summary

We have successfully migrated the Jing-Zhang project execution and review infrastructure from Codex to Google Antigravity CLI (`agy` v1.1.15).

To balance development agility with rigorous evaluation integrity, we have instituted a **Hybrid Architecture**:
- **Host Development Team**: Powered by AGY (`gemini-3.7-flash-high`) with 4 specialized workspace-scoped subagents (`jz-explorer`, `jz-worker`, `jz-critic`, `jz-validator`).
- **Formal Local Jury**: Conducted by 3 independent, physically isolated Windows Sandbox instances running headless AGY with exact model pinning (`claude-opus-4-6-thinking`, `claude-sonnet-4-6`, `gemini-3.7-flash-high`).

---

## 2. Key Qualification Results

1. **Subagent Schema Qualification**:
   - Confirmed `.agents/agents/*.md` schema supports `inherit`, `flash`, and `pro` tiers.
   - Probed and confirmed clean subagent isolation.
   - Identified that subagent YAML does not allow exact model slug pinning or independent `--effort` override; hence, subagents are strictly kept in the development lane and barred from jury scoring.
2. **Fail-Closed Exact Model Pinning**:
   - Verified that headless `agy --model <slug>` fails closed on unrecognized models without silent fallback.
3. **Clean Runtime Packaging**:
   - Built `V:\src\_review_isolation\agy-runtime` containing solely the standalone `agy.exe` and runner scripts.
   - Zero host credentials, Google tokens, browser cookies, or past session logs are present.
4. **Product Integrity**:
   - Product repo `V:\src\haidian` is completely unmodified (`git status: clean`).
   - No scoring of Candidate-X has been performed; no v0.4.2 was created.

---

## 3. Owner Verification Workflow (3 Simple Commands)

To run the Reviewer A qualification probe:

1. **Host Launcher**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File V:\src\_review_isolation\Start-JZReviewerAProbe-AGY.ps1
   ```
2. **Inside Sandbox**:
   ```powershell
   .\reviewer-runner-agy.ps1 -Reviewer A -Mode Probe
   ```
3. **Host Status Verification**:
   ```powershell
   powershell -ExecutionPolicy Bypass -File V:\src\_review_isolation\Get-JZReviewerAProbeStatus-AGY.ps1
   ```
