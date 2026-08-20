# Current Official Review Rubric & Evaluation Contract

**Extracted From**: `open-city-ai/haidian` `upstream/main` (`6f381212abcf8cc2f690517a6654f8c437845f03`)  
**Date**: 2026-08-20  
**Source Scripts**: `scripts/ai_review_submission.py`, `scripts/review_submission.py`, `scripts/auto_review_queue.py`  

---

## 1. Rubric Dimensions and Weights

| Dimension ID | Dimension Name (ZH) | Weight | Official Review Focus |
| :--- | :--- | :---: | :--- |
| `brief_alignment` | 任务书相关性 | **20** | 是否围绕百年京张 AI 创新带、三层范围、三大重点片区和公告 1.5 任务展开。 |
| `originality` | 原创性 | **10** | 是否提出清晰的新概念、新机制或新场景，避免空泛拼贴。 |
| `ai_planning_innovation` | AI 与城市规划创新性 | **15** | 是否将 AI 能力与产业、空间、交通、公共服务、文化和治理结合。 |
| `implementation_feasibility` | 可实施性 | **20** | 是否有阶段路径、试点区域、参与主体、指标和可核验数据边界。 |
| `public_interest_inclusion` | 公共利益与包容性 | **10** | 是否兼顾居民、青年人才、企业、高校、游客和弱势群体。 |
| `risk_compliance` | 风险与合规意识 | **10** | 是否尊重公开资料边界、隐私、版权和政策不确定性。 |
| `expression_completeness` | 表达完整性 | **15** | 是否形成可读正文、图纸、HTML、指标、图层和证据引用的完整闭环。 |

**Total Score**: 100

---

## 2. Rating Scale & Scoring Calibration

- **0**: 缺失或无效 (Absent / Invalid)
- **1**: 严重不足 (Seriously Deficient)
- **2**: 较弱 (Weak)
- **3**: 充分 / 达标 (Adequate / Compliant)
- **4**: 较强 / 优秀 (Strong / Distinctive)
- **5**: 卓越 / 示范 (Exceptional / Exemplary)

**Review Rules**:
1. Calibrate dimensions independently based on visible evidence.
2. Do not multiply-punish a single defect across multiple dimensions.
3. Missing organizer-owned geometry (official redline / site polygons) is an organizer gap, not a score reduction by itself.

---

## 3. Mandatory Rejection & Gate Requirements

Before scoring can occur, a submission must pass all 4 deterministic local gates:
1. `DETERMINISTIC_VALIDATION`: Schema compliance, YAML frontmatter, file manifest integrity, no orphan files.
2. `SPATIAL_REVIEW`: GeoJSON geometry formatting, coordinate systems, topology, land use coverage.
3. `VISUAL_PACKAGING`: Figure resolutions, PDF rendering, bilingual visual pair integrity.
4. `PROFESSIONAL_EVIDENCE`: Structured source citations, assumption ledger, metrics consistency.

---

## 4. Review Packet Composition & Multimodal Inspection

The AI review worker consumes:
- **Raw Structured Data**: `proposal.md`, `manifest.json`, `metrics.json`, `assumptions.json`, `sources.json`, `self_check.json`, `compliance_matrix.json`, `standard_matrix.json`, `design_depth_matrix.json`.
- **Core Figures (Paired ZH/EN)**:
  1. `assets/figures/site-overview.png` & `.en.png`
  2. `assets/figures/land-use-structure.png` & `.en.png`
  3. `assets/figures/key-areas.png` & `.en.png`
  4. `assets/figures/mobility-bluegreen.png` & `.en.png`
  5. `assets/figures/metrics-evidence.png` & `.en.png`
- **PDF Deliverables**: `drawings/a3-booklet.pdf` & `.en.pdf`, `drawings/a0-boards.pdf` & `.en.pdf`
- **HTML Surfaces**: `report/proposal.html` & `.en.html`, `visual/index.html` & `.en.html`
- **Max Image Budget**: Up to 18 images rendered per package turn.
