# AGY Model Policy

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  
**Status**: ACTIVE / QUALIFIED  

---

## 1. Overview & Architecture

The Jing-Zhang project uses a **Hybrid Architecture**:
1. **Host Development Team**: Primary Antigravity CLI (`agy`) orchestrator with specialized workspace subagents.
2. **Formal Local Jury**: Physically isolated, headless Windows Sandbox instances with exact model and reasoning effort pinning.

---

## 2. Host Development Team

| Agent Role | Model Configuration | Primary Function | Allowed Tools |
| :--- | :--- | :--- | :--- |
| **Primary Host Implementer** | `gemini-3.7-flash-high` | Orchestration, coordination, tool execution, surgical edits | Full workspace toolset (`--dangerously-skip-permissions`) |
| **JZ Explorer** | `model: pro` | Deep rubric analysis, architecture review, blocker discovery | Read-only tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`, `read_url_content`, `search_web`) |
| **JZ Worker** | `model: inherit` | Code and artifact implementation, blocker surgery | Surgical modification tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`, `replace_file_content`, `write_to_file`, `run_command`) |
| **JZ Critic** | `model: pro` | Adversarial plan challenge, anti-gaming inspection, regression detection | Read-only tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`, `read_url_content`, `search_web`) |
| **JZ Validator** | `model: flash` | Fast gate verification, schema compliance, receipts generation | Validation & testing tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`, `run_command`, `write_to_file`) |

---

## 3. Formal Local Jury (Headless Sandbox Reviewers)

Formal jury members are **NOT** implemented as subagents. They run as independent, headless AGY processes inside dedicated Windows Sandbox environments to enforce exact model pinning, reasoning strength consistency, and strict physical isolation.

| Reviewer | Assigned Model Slug | Architecture & Reasoning Profile | Quota / Usability Status |
| :--- | :--- | :--- | :--- |
| **Reviewer A** | `claude-opus-4-6-thinking` | Anthropic Claude Opus 4.6 with extended reasoning/thinking enabled | Confirmed in runtime inventory |
| **Reviewer B** | `claude-sonnet-4-6` | Anthropic Claude Sonnet 4.6 (Thinking enabled by slug) | Confirmed in runtime inventory |
| **Reviewer C** | `gemini-3.7-flash-high` | Google Gemini 3.7 Flash with High reasoning effort | Confirmed in runtime inventory |
| **Tie-Breaker** | `gpt-oss-120b-medium` | GPT-OSS 120B with Medium reasoning effort (dispute resolution only) | Confirmed in runtime inventory |

---

## 4. Reasoning Effort & Model Pinning Rules

1. **Exact Slug Pinning**: Where model slugs explicitly encode reasoning effort (e.g. `gemini-3.7-flash-high`, `claude-opus-4-6-thinking`, `gpt-oss-120b-medium`), exact slug pinning is mandatory.
2. **Fail-Closed Fallback Policy**: If a requested model slug cannot be resolved, headless AGY execution **fails immediately with a non-zero exit code**. Silent fallback to alternative models or lower reasoning effort is strictly prohibited.
3. **No Quota Degradation in Jury**: Quota constraints must never cause automatic downgrades of jury reasoning strength (e.g. downgrading Gemini from `high` to `medium`/`low` is disallowed for jury runs).
4. **Subagent Model Tier Boundary**: Subagent configurations use tier abstraction (`inherit`, `flash`, `pro`). Because tiers do not guarantee specific provider pinning or reasoning effort, subagents are restricted to development support and are barred from formal scoring decisions.
