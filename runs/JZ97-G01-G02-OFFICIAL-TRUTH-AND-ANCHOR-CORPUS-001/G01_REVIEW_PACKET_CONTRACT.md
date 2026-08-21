# Current Review Packet Contract

- Authority Source: `open-city-ai/haidian` (`scripts/export_review_packet.py`, `scripts/ai_review_submission.py`)
- Upstream Head: `78db36c91e1c604c3fc5702f8cb7be4ac4b01e5a`

## 1. Structured Text and Evidence Inventory

The packet extracts raw structured text and JSON files:
- `proposal.md` and `proposal.en.md` (Primary bilingual narrative)
- `manifest.json` (Machine package declaration and checksums)
- `metrics.json` (Quantified KPI targets)
- `assumptions.json` (Assumptions and confidence boundaries)
- `sources.json` (Indexed public sources)
- `self_check.json` (Pre-submit gate results)
- `compliance_matrix.json` (Regulatory/standard compliance mapping)
- `standard_matrix.json` (Planning standards index)
- `design_depth_matrix.json` (Spatial/architectural depth specification)
- `agent.json` (Agent taskbook responses agent.1–agent.6)
- `simulation.json` (Scenario simulations)
- `report/copyright_statement.md`, `report/narrative.md`
- `visual/assets/*.json` (Spatial admission, evidence index, renewal register)

## 2. Core Figure Selection and Order

Multimodal review attaches 5 core figures (and bilingual counterparts):
1. `assets/figures/site-overview.png` (FIG.01 Site Overview / 总览格局)
2. `assets/figures/land-use-structure.png` (FIG.02 Land-Use Structure / 用地与空间结构)
3. `assets/figures/key-areas.png` (FIG.03 Key Areas / 重点片区节点)
4. `assets/figures/mobility-bluegreen.png` (FIG.04 Mobility & Blue-Green / 慢行交通与蓝绿网络)
5. `assets/figures/metrics-evidence.png` (FIG.05 Metrics & Evidence / 规划指标与证据支撑)

## 3. PDF Drawings and HTML Screenshots

- `drawings/a3-booklet.pdf` and `drawings/a0-boards.pdf`:
  - Rasterized at 144 DPI, page 1 only, into `.page-1.png`.
- `report/proposal.html` and `visual/index.html`:
  - Captured at 1440x1600 viewport via headless Chromium/Edge into `.first-window.png`.

## 4. Budgets and Safety Boundaries

- Image budget: Up to 18 images total (5 figure pairs + 2 PDF page-1 pairs + 2 HTML screenshot pairs).
- Maximum image size: 4 MB per image.
- Reviewer Isolation: Reviewers inspect only the inert text/JSON and rendered images in the packet. No contributor code is executed.
