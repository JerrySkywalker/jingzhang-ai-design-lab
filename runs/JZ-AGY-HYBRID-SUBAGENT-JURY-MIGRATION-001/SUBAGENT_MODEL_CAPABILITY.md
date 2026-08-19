# AGY Subagent Model Capability & Empirical Proof

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  
**Status**: VERIFIED & BENCHMARKED  

---

## 1. Subagent Frontmatter & Tier Schema

Antigravity CLI (`agy` version 1.1.15) defines subagent configurations through YAML frontmatter located in `.agents/agents/*.md`.

Supported `model` values in subagent schema:
- `model: inherit` — Dynamically inherits the active model and settings of the calling parent session.
- `model: flash` — Binds the subagent to the fast lightweight Flash tier.
- `model: pro` — Binds the subagent to the advanced Pro tier.

Arbitrary exact model slugs (e.g., `claude-opus-4-6-thinking`, `gpt-oss-120b-medium`) and per-agent `--effort` overrides are **not supported** in the subagent YAML frontmatter schema.

---

## 2. Empirical Subagent Capability Probe Results

During the migration qualification, three harmless non-product subagents were spawned concurrently to verify metadata visibility and effective model resolution:

```
Probe Execution IDs:
- SUBAGENT_INHERIT : 76576901-20ce-42a8-a2a1-bfaf3170805a
- SUBAGENT_FLASH   : 0f9c0d28-71ac-48e9-8e99-7a862e271a58
- SUBAGENT_PRO     : dc61e6f2-830b-45e6-892d-be64f945a675
```

### Empirical Findings:
1. **`SUBAGENT_INHERIT`**:
   - Resolved to parent model (`Gemini 3.7 Flash High`).
   - Confirmed bi-directional message channel with parent.
2. **`SUBAGENT_FLASH`**:
   - Resolved to `Gemini 3.7 Flash`.
   - Executed fast tool calls without parent context contamination.
3. **`SUBAGENT_PRO`**:
   - Resolved to `Gemini Pro` tier.
   - Exact runtime model slug is **not exposed** in environment variables or metadata returned to the agent.

### Formal Capability Proof Record:

```
SUBAGENT_EXACT_MODEL_VISIBLE=false
SUBAGENT_INHERIT_EFFECTIVE_MODEL=inherit (gemini-3.7-flash-high parent context)
SUBAGENT_FLASH_EFFECTIVE_MODEL=flash
SUBAGENT_PRO_EFFECTIVE_MODEL=pro
SUBAGENT_PER_AGENT_EFFORT_SUPPORTED=false
SUBAGENT_EXACT_MODEL_PIN_SUPPORTED=false
```

---

## 3. Boundary Conclusion: Subagents vs. Formal Jury

Because Antigravity custom-subagent configuration exposes tier-level abstractions rather than arbitrary exact model slugs + independent reasoning effort, **subagents must not be used for formal jury scoring**.

- **Subagents** are assigned strictly to:
  - Exploratory analysis (`jz-explorer` -> `model: pro`)
  - Implementation & surgical code edits (`jz-worker` -> `model: inherit`)
  - Adversarial plan critique (`jz-critic` -> `model: pro`)
  - Automated gate verification (`jz-validator` -> `model: flash`)

- **Formal Local Jury** is executed exclusively via:
  - Exact-model headless AGY processes running inside physically isolated Windows Sandbox instances.
