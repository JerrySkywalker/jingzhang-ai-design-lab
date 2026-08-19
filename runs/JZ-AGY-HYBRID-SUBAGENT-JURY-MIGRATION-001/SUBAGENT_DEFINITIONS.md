# Workspace Custom Subagent Definitions

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Location**: `V:\src\.agents\agents\`  
**Status**: INSTALLED & VERIFIED  

---

## 1. Subagent Specifications

All subagents are defined using standard Markdown with YAML frontmatter located in the workspace `.agents/agents/` directory.

### A. `jz-explorer` (`V:\src\.agents\agents\jz-explorer.md`)
- **Role**: Rubric & Architecture Exploration
- **Model Tier**: `pro`
- **Permissions**: Read-only tools
- **Configured Frontmatter**:
  ```yaml
  ---
  name: jz-explorer
  description: Deep rubric, architecture, and blocker analysis specialist for Jing-Zhang project. Read-only exploration and diagnosis.
  subagent: true
  mainAgent: false
  model: pro
  tools:
    - view_file
    - grep_search
    - find_by_name
    - list_dir
    - read_url_content
    - search_web
  ---
  ```
- **Primary Function**: Diagnoses blockers, checks compliance against `CURRENT_OFFICIAL_RUBRIC.md`, discovers unverified assumptions and evidence gaps without mutating codebase files.

---

### B. `jz-worker` (`V:\src\.agents\agents\jz-worker.md`)
- **Role**: Targeted Implementation & Surgery
- **Model Tier**: `inherit` (inherits host orchestrator model)
- **Permissions**: Modification and execution tools
- **Configured Frontmatter**:
  ```yaml
  ---
  name: jz-worker
  description: Implementation and surgical code/artifact modification specialist for Jing-Zhang project.
  subagent: true
  mainAgent: false
  model: inherit
  tools:
    - view_file
    - grep_search
    - find_by_name
    - list_dir
    - replace_file_content
    - write_to_file
    - run_command
  ---
  ```
- **Primary Function**: Executes surgical, bounded code and artifact edits authorized by the primary agent. Strictly avoids scope bloat.

---

### C. `jz-critic` (`V:\src\.agents\agents\jz-critic.md`)
- **Role**: Adversarial Review & Anti-Gaming Challenge
- **Model Tier**: `pro`
- **Permissions**: Read-only tools
- **Configured Frontmatter**:
  ```yaml
  ---
  name: jz-critic
  description: Adversarial challenger and rubric-gaming detector for Jing-Zhang project. Read-only review of proposed plans.
  subagent: true
  mainAgent: false
  model: pro
  tools:
    - view_file
    - grep_search
    - find_by_name
    - list_dir
    - read_url_content
    - search_web
  ---
  ```
- **Primary Function**: Reviews proposed surgical plans, identifies cosmetic changes masquerading as depth, flags rubric gaming, and prevents regressions.

---

### D. `jz-validator` (`V:\src\.agents\agents\jz-validator.md`)
- **Role**: Gate Testing & Schema Verification
- **Model Tier**: `flash`
- **Permissions**: Test execution, inspection, and receipt generation
- **Configured Frontmatter**:
  ```yaml
  ---
  name: jz-validator
  description: Fast gate verifier, consistency checker, and test specialist for Jing-Zhang project.
  subagent: true
  mainAgent: false
  model: flash
  tools:
    - view_file
    - grep_search
    - find_by_name
    - list_dir
    - run_command
    - write_to_file
  ---
  ```
- **Primary Function**: Runs fast automated checks (schema validation, math consistency, linting, regression testing) and outputs structured verification receipts.

---

## 2. Subagent Context & Invocation Policy

1. **Scoped Prompts**: Subagents receive explicit, bounded tasks with file references rather than unbounded historical transcripts.
2. **Deterministic Inputs**: All evidence must be grounded in disk artifacts (`V:\src\haidian`, `V:\src\jingzhang-ai-design-lab`).
3. **Synthesis**: The primary host agent retains final editorial authority and synthesizes subagent outputs.
