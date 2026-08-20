# High-Score Benchmark Research & Reviewer Behavioral Patterns

**Goal ID**: `JZ-V042-V044-12H-UNATTENDED-CANDIDATE-FORGE-001`  
**Date**: 2026-08-20  
**Sample Corpus**: Merged & Scored Submissions in `open-city-ai/haidian`  

---

## 1. High-Score Case Ledger (85+ and 90+)

| Submission Slug & Author | PR Number | Exact Reviewed HEAD | Trusted Score | Key Architectural Mechanism | Review Date |
| :--- | :---: | :--- | :---: | :--- | :--- |
| `Sonike/jingzhang-handover-line` | #3441 / #3451 | `bc8d96bfc303fb7d38fb1d496025381d634d0c06`<br>`43ba0392818b65f318f539201289d6a1c25f4ec4` | **90 / 100** | Handover Line ("BUILD->VERIFY->SHARE->SERVE->RETURN"); 12/12 offline simulation; 48/48 assertions; 0/12 field; 3 reading paths (60s, 5min, deep); "How to Read Figure" guides | 2026-08-19 |
| `anselasimov-web/the-ren-line` | #3453 | `6a118f1240c50f74ab27eb4cc22337b3b9c448cf` | **90 / 100** | "The Ren Line" (人字线); blueprint graphics; 23 tasks covered; full GeoJSON cross-referencing; explicit provisional boundary disclosures | 2026-08-19 |
| `jiangmuran/jingzhang-leveling-line` | #3456 | `83ae2fc3bd3f8a2cd418a4cb4aaa4c0662258d6a` | **86 / 100** | Leveling Line / Closure Error mechanism ("测得回来"); P4 elderly persona morning journey; explicit reporting of adverse metrics | 2026-08-19 |
| `JerrySkywalker/jingzhang-in-place` | #2744 | `1d5cb1aaa9d76edc3532e593c803cb936070a744` | **77 / 100** | STATUS × ACTION; retain-first; AI_OFF_CITY; NO-BUILD=9; deep spatial packets S01/S04/S07 | 2026-08-19 |

---

## 2. Reviewer Behavioral Insights (What AI Reviewers Visibly Rewarded)

1. **First-Fold Comprehension (First 30–60 Seconds)**:
   - High-scoring submissions do not bury the core thesis in bureaucratic preambles.
   - They present a single declarative sentence, 3 reading paths (60s / 5min / deep), and a "How to Read This Figure" box right under the hero graphic.
2. **Boundary Honesty & Reality Partitioning**:
   - The AI reviewer heavily penalizes submissions that blur digital simulation with field implementation.
   - Submissions that explicitly proclaim `Offline Simulation: 12/12 PASS` while clearly stating `Field Trials: 0/12 (Pending Official Authorization)` earned high trust and perfect `risk_compliance` marks.
3. **Cross-Artifact Arithmetic Parity**:
   - Discrepancies between JSON counts (e.g. `metrics.json` vs `compliance_matrix.json`) trigger immediate reviewer skepticism.
   - Exact mathematical reconciliation across narrative, tables, and JSON files is rewarded with band 4/5 in `expression_completeness`.
4. **Human-Scale Lived Experience**:
   - A vivid persona day walk (e.g. an elderly resident navigating a morning service without smartphone access) grounds technical AI mechanisms into spatial reality.

---

## 3. Pattern Transferability Classification

### A. `TRANSFERABLE_REVIEW_PATTERN` (Adopt in Jing-Zhang)
- **3-Tier Reading Paths Table**: Provide 60-second, 5-minute, and Deep-read roadmaps in Section 1.
- **"How to Read This Figure" Explanatory Callouts**: Add 3-step reading guides beneath each of the 5 core figures.
- **Reality Partitioning**: Explicitly state digital verification status vs field readiness.

### B. `TRANSFERABLE_PRESENTATION_PATTERN` (Adopt in Jing-Zhang)
- **Stronger Opening Fold**: Crystal-clear thesis and hero graphic on `proposal.md` and HTML index pages.
- **Persona Day Grounding**: Ground the 12 tasks in an ordinary resident's daily routine along the corridor.

### C. `TRANSFERABLE_EVIDENCE_PATTERN` (Adopt in Jing-Zhang)
- **Zero-Discrepancy Cross-Referencing**: Ensure all metrics, assumptions, and sources cite identical counts across all tables and JSON files.
- **Provisional Data Disclaimers**: Disclose organizer boundary limits proactively without diminishing design depth.

### D. `TRANSFERABLE_IMPLEMENTATION_PATTERN` (Adopt in Jing-Zhang)
- **Role Authority Tables**: Specify who decides, who verifies, and what triggers an immediate stop/reversion.

### E. `NONTRANSFERABLE_DESIGN_IDEA` (Strictly Avoid)
- Do NOT adopt competitor concepts ("Handover Line", "Leveling Line", "Ren Line").
- Retain our unique urban-design philosophy: **`STATUS × ACTION`**, **`AI_OFF_CITY`**, **`12→3 spatial admission`**, **`NO-BUILD=9`**, and **`minimum reversible spatial delta`**.
