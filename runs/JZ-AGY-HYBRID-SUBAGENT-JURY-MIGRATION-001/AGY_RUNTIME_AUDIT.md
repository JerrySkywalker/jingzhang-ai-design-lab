# AGY Runtime Audit & Isolation Hygiene

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Runtime Path**: `V:\src\_review_isolation\agy-runtime\`  
**Date**: 2026-08-20  
**Audit Result**: CLEAN ROOM CERTIFIED (ZERO HOST LEAKAGE)  

---

## 1. Runtime Packaging Audit

The runtime directory `V:\src\_review_isolation\agy-runtime\` was created from scratch to provide the absolute minimum execution footprint required for Windows Sandbox reviewers.

### Deployed File Inventory:

| File Path | Size | Description |
| :--- | :--- | :--- |
| `bin\agy.exe` | 184,010,392 bytes | Clean, standalone Antigravity CLI binary (v1.1.15) |
| `agy.exe` | 184,010,392 bytes | Root alias executable for compatibility |
| `reviewer-runner-agy.ps1` | ~3 KB | Sandbox reviewer orchestrator & model invoker |
| `confinement-probe-agy.ps1` | ~2 KB | Confinement & host visibility probe script |

---

## 2. Host Contamination Audit

An automated inspection was performed to verify that **NO** host secrets, session history, or credentials exist within the runtime:

| Protected Artifact Type | Host Location | Present in `agy-runtime`? | Verification Result |
| :--- | :--- | :--- | :--- |
| **Google Auth Tokens** | `C:\Users\jerry\.gemini\antigravity-cli\*` | **NO** | PASS (Zero tokens copied) |
| **Browser Session State** | `%LOCALAPPDATA%\Google\*` | **NO** | PASS (Zero browser cookies copied) |
| **Windows Credential Manager** | Host Keyring | **NO** | PASS (Zero credentials imported) |
| **Conversation Databases** | `~\.gemini\antigravity-cli\conversations\*.db` | **NO** | PASS (Zero conversation history copied) |
| **Host Custom Skills / Plugins** | `~\.gemini\antigravity-cli\builtin\skills\*` | **NO** | PASS (Zero host skills/plugins copied) |
| **Host MCP Configurations** | `~\.gemini\config\mcp_config.json` | **NO** | PASS (Zero host MCP copied) |
| **Host Workspace Agents** | `V:\src\.agents\agents\*` | **NO** | PASS (Zero host agents copied) |

---

## 3. Ephemeral Sandbox Environment Contract

When the Sandbox starts:
1. `GEMINI_HOME` and `ANTIGRAVITY_HOME` are set to `C:\AgyHome` (a freshly created Sandbox-local directory).
2. The user profile is strictly localized to `C:\Users\WDAGUtilityAccount`.
3. The Owner provides interactive device authentication per session; credentials are destroyed upon Sandbox teardown.
4. No API keys or persistent environment variables are injected.
