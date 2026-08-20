# Jury Review Packet Reproducibility & Integrity Proof

**Goal ID**: `JZ-V042-V044-12H-UNATTENDED-CANDIDATE-FORGE-001`  
**Target Candidate**: v0.4.2 (`a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`)  
**Active Packet Location**: `V:\src\_review_isolation\packet\`  
**Verification Date**: 2026-08-20T09:07:00+08:00  

---

## 1. Deterministic Packet Build Proof

The review packet was constructed directly from candidate `v0.4.2` (`a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`).

- **Total Tracked Files**: 60 files
- **Primary Packet SHA-256 Digest**: `394d74ee123079d89175a12a09aaf39991454c70c062c7f826916dfaf1097656`
- **Reproducibility Test Clone Digest**: `394d74ee123079d89175a12a09aaf39991454c70c062c7f826916dfaf1097656`
- **Reproducibility Status**: **100% BYTE-FOR-BYTE IDENTICAL (MATCH)**

---

## 2. Packet Composition Breakdown

1. **Review Contracts & Prompts (5 files)**:
   - `CANDIDATE_CONTEXT.md` (Neutral evaluation context)
   - `CURRENT_OFFICIAL_RUBRIC.md` (7 official dimensions and weights)
   - `SCORECARD_SCHEMA.json` (Structured scorecard schema)
   - `HARNESS_TEST_PROMPT.md` (Disposable harness test prompt)
   - `REVIEWER_PROBE_PROMPT.md` (Non-scoring sandbox probe prompt)
2. **Submission Deliverables & Structured Evidence (17 files)**:
   - `proposal.md` & `proposal.en.md`
   - `manifest.json` & `self_check.json`
   - `metrics.json`, `assumptions.json`, `sources.json`
   - `compliance_matrix.json`, `standard_matrix.json`, `design_depth_matrix.json`
   - `agent.json`, `changelog.md`
   - `geometry/` (6 GeoJSON layers: site_boundary, key_areas, land_use, buildings, roads, constraints)
3. **Core Figures (10 PNGs)**:
   - 5 bilingual pairs in `assets/figures/`
4. **PDF & HTML Deliverables (10 files)**:
   - `drawings/a3-booklet.pdf` & `.en.pdf`
   - `drawings/a0-boards.pdf` & `.en.pdf`
   - `report/proposal.html` & `.en.html`
   - `visual/index.html` & `.en.html`
   - `visual/assets/` structured data indices
5. **Pre-rendered Visual Surfaces for Vision Models (18 PNGs)**:
   - 10 core figure PNGs
   - 4 PDF first-page PNGs (`a3-booklet`, `a0-boards`, zh/en)
   - 4 HTML first-window PNGs (`report/proposal`, `visual/index`, zh/en)

---

## 3. Physical Isolation Integrity
- Host credentials, git remotes, branch histories, and PR numbers are completely stripped from the packet.
- The packet is mapped read-only into Windows Sandbox at `C:\ReviewPacket` with write access confined strictly to `C:\ReviewerOutput`.
