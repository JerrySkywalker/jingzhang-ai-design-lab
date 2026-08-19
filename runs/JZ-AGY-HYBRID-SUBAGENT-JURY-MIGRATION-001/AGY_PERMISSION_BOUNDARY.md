# AGY Permission Boundary & Security Specification

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  
**Status**: APPROVED  

---

## 1. Dual-Domain Permission Model

The Jing-Zhang migration establishes two distinct operational security domains:

```
[ HOST WORKSPACE DOMAIN ]                   [ SANDBOX JURY DOMAIN ]
- Interactive / Autonomous Development     - Isolated Evaluation / Scoring
- Flag: --dangerously-skip-permissions     - NO --dangerously-skip-permissions
- Full Filesystem Read/Write Access        - Read-Only Packet + Write-Only Output
- Workspace Subagents Enabled              - Ephemeral Sandboxed AGY CLI
```

---

## 2. Host Development Team Policy

For the host development team and orchestrator:
- **Startup Mode**: `agy --dangerously-skip-permissions --model gemini-3.7-flash-high`
- **Rationale**: Frictionless pair-programming, tool execution, and code manipulation across `V:\src\haidian` and `V:\src\jingzhang-ai-design-lab`.

---

## 3. Reviewer Exception to Dangerous Permission Mode

Formal isolated reviewers are a **deliberate and mandatory exception**.

### Why `--dangerously-skip-permissions` is Forbidden in Jury Execution:
1. **Tool Confinement**: Jury validity requires that a reviewer model cannot access web browsing, MCP servers, GitHub repositories, or execute unvetted system utilities.
2. **Deterministic Inputs**: The reviewer must evaluate **only** what is explicitly provided in the fixed packet (`C:\ReviewPacket`).
3. **No Project Memory Leakage**: The reviewer must not access past conversation databases, host `.gemini` configurations, or peer reviewer outputs.

### Reviewer Runtime Boundaries:
- **Packet Access**: Read-only mapping of `V:\src\_review_isolation\packet` -> `C:\ReviewPacket`.
- **Output Access**: Read/write mapping of `V:\src\_review_isolation\output-X` -> `C:\ReviewerOutput`.
- **Runtime Access**: Read-only mapping of `V:\src\_review_isolation\agy-runtime` -> `C:\ReviewerRuntime`.
- **Network Access**: Restricted strictly to standard model API endpoint communication for device authentication and inference transport.
