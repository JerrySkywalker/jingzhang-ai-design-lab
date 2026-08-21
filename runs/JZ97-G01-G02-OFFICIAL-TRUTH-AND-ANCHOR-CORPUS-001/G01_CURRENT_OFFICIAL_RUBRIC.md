# Current Official Rubric Lock

- Authoritative Repository: `open-city-ai/haidian`
- Upstream Head Commit: `78db36c91e1c604c3fc5702f8cb7be4ac4b01e5a`
- Primary Document: `docs/review-rubric.md` (blob `6825222e3198b5ccfe01499bf11737901143cf1d`)
- Primary Implementation: `scripts/ai_review_submission.py` (blob `f5bb0c8394bff0f11616653d24626195021aee8c`)
- Packet Contract Implementation: `scripts/export_review_packet.py` (blob `fe4ffc5e9202df72efddca666b05ec118225bdba`)

## 1. Seven Scoring Dimensions and Weights

| Dimension ID | Chinese Title | Weight | Scope & Review Focus |
|---|---|---:|---|
| `brief_alignment` | 任务书相关性 | 20% | Coverage of Centennial Jing-Zhang AI Innovation Belt, Haidian, AI ecosystem, spatial structure, and public governance |
| `originality` | 原创性 | 10% | Novel concept, mechanism, or scenario; avoids generic smart-city collage |
| `ai_planning_innovation` | AI 与城市规划创新性 | 15% | Meaningful integration of AI capabilities with industry, space, transport, public services, culture, and governance |
| `implementation_feasibility` | 可实施性 | 20% | Phasing, pilot areas, participating actors, and measurable indicators |
| `public_interest_inclusion` | 公共利益与包容性 | 10% | Balances benefits for residents, youth, tech enterprises, universities, visitors, and vulnerable groups |
| `risk_compliance` | 风险与合规意识 | 10% | Respects data boundaries, privacy, copyright, policy uncertainty, and human-in-the-loop review |
| `expression_completeness` | 表达完整度 | 15% | Clear structure, sufficient evidence, can be continued and deepened |

Total Weight: 100%

## 2. Integer Score Schema & Calculation Formula

- Each dimension is scored on an integer scale `0..5`:
  - 5: Exceptional / ceiling standard
  - 4: Strong / fully compliant with solid evidence
  - 3: Adequate / basic pass with gaps
  - 2: Needs work / partial evidence
  - 1: Poor / missing essential elements
  - 0: Completely missing or unacceptable
- Fractional host estimates (e.g. 3.5, 4.2) are strictly `DEV_ADVISORY_ONLY` and forbidden from formal jury scorecards.
- Weighted Total Calculation:
  $$\text{total\_weighted\_score\_100} = \sum_{i=1}^{7} \left( \frac{\text{score\_0\_to\_5}_i}{5} \times \text{weight\_percent}_i \right)$$

## 3. Six Mandatory Rejection Rules

A submission is immediately rejected if it:
1. Contains personal private data, classified materials, internal information, or non-public spatial data.
2. Fabricates official endorsement, government approval conclusions, or implementation commitments.
3. Submits offensive, discriminatory, illegal, or malicious content.
4. Has no substantial relevance to the open-call brief.
5. Does not respond to any of the six agent tasks (`agent.1`–`agent.6`) in `agent_taskbook.json`.
6. Presents conceptual recommendations, activity proposals, or policy mechanisms as confirmed government decisions.

## 4. Four Deterministic Local Gates

1. `deterministic_validation`: PR validation CI, manifest schema, metadata, checksums, bilingual parity.
2. `spatial_review`: Geometry validity, GeoJSON structure, coordinate sanity, key-area boundaries.
3. `visual_review`: 5 core figures format, dimensions, readability, bilingual counterparts, max 18 images budget, max 4MB per image.
4. `professional_evidence_review`: Structured sources registry, public source citation, no ungrounded claims, standard matrices.

All four gates must be `PASS` before formal professional scoring can proceed.
