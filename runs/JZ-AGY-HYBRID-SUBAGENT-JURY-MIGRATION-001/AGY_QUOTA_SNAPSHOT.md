# AGY Model Quota & Runtime Inventory Snapshot

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Captured At**: 2026-08-20T01:44:30+08:00  
**Source Command**: `agy models`  

---

## 1. Official Model Inventory

The Antigravity CLI runtime exposes the following 14 verified models:

| Exact Model Slug | Display Name | Model Family / Tier | Role in Jing-Zhang Project |
| :--- | :--- | :--- | :--- |
| `gemini-3.7-flash-high` | Gemini 3.7 Flash (High) | Google Gemini 3.7 (High Effort) | **Primary Host Implementer** & **Reviewer C** |
| `gemini-3.7-flash-medium` | Gemini 3.7 Flash (Medium) | Google Gemini 3.7 (Medium Effort) | Host alternative / scratch |
| `gemini-3.7-flash-low` | Gemini 3.7 Flash (Low) | Google Gemini 3.7 (Low Effort) | Host alternative / scratch |
| `gemini-3.6-flash-high` | Gemini 3.6 Flash (High) | Google Gemini 3.6 (High Effort) | Fallback testing only |
| `gemini-3.6-flash-medium` | Gemini 3.6 Flash (Medium) | Google Gemini 3.6 (Medium Effort) | Fallback testing only |
| `gemini-3.6-flash-low` | Gemini 3.6 Flash (Low) | Google Gemini 3.6 (Low Effort) | Fallback testing only |
| `gemini-3.5-flash-high` | Gemini 3.5 Flash (High) | Google Gemini 3.5 (High Effort) | Legacy reference |
| `gemini-3.5-flash-medium` | Gemini 3.5 Flash (Medium) | Google Gemini 3.5 (Medium Effort) | Legacy reference |
| `gemini-3.5-flash-low` | Gemini 3.5 Flash (Low) | Google Gemini 3.5 (Low Effort) | Legacy reference |
| `gemini-3.1-pro-high` | Gemini 3.1 Pro (High) | Google Gemini 3.1 Pro (High Effort) | Pro tier backend candidate |
| `gemini-3.1-pro-low` | Gemini 3.1 Pro (Low) | Google Gemini 3.1 Pro (Low Effort) | Pro tier backend candidate |
| `claude-sonnet-4-6` | Claude Sonnet 4.6 (Thinking) | Anthropic Claude Sonnet | **Formal Reviewer B** |
| `claude-opus-4-6-thinking` | Claude Opus 4.6 (Thinking) | Anthropic Claude Opus | **Formal Reviewer A** (Primary Judge) |
| `gpt-oss-120b-medium` | GPT-OSS 120B (Medium) | OpenAI / Open Source (Medium Effort) | **Optional Tie-Breaker** |

---

## 2. Jury Availability & Usability Status

All four target jury models are confirmed available and mapped in the local AGY installation:

```
REVIEWER_A_MODEL=claude-opus-4-6-thinking   [STATUS: AVAILABLE]
REVIEWER_B_MODEL=claude-sonnet-4-6          [STATUS: AVAILABLE]
REVIEWER_C_MODEL=gemini-3.7-flash-high      [STATUS: AVAILABLE]
TIE_BREAKER_MODEL=gpt-oss-120b-medium       [STATUS: AVAILABLE]
```

---

## 3. Safe Quota Conservation Policy

- Probe runs are strictly non-scoring and run on a single disposable session.
- Real jury runs will be invoked only when a candidate version freeze is reached.
- No redundant, parallel speculative jury runs are permitted.
