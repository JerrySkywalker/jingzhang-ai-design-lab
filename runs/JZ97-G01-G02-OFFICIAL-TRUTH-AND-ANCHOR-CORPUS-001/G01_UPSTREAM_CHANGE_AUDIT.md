# Upstream Change Audit vs Prior Assumptions

- Upstream Repository: `open-city-ai/haidian`
- Start Upstream SHA: `78db36c91e1c604c3fc5702f8cb7be4ac4b01e5a`

## Classification Matrix

| Dimension / Policy | Prior Program Assumption | Upstream Exact State | Classification | Evidence / Blob SHA |
|---|---|---|---|---|
| Rubric Dimensions | 7 dimensions (20/10/15/20/10/10/15) | 7 dimensions (20/10/15/20/10/10/15) | `UNCHANGED` | `docs/review-rubric.md` (`6825222e3198b5ccfe01499bf11737901143cf1d`) |
| Integer Score Schema | Integer 0..5 per dimension | Integer 0..5 per dimension | `UNCHANGED` | `scripts/ai_review_submission.py` (`f5bb0c8394bff0f11616653d24626195021aee8c`) |
| Mandatory Rejection | 6 mandatory conditions | 6 mandatory conditions | `UNCHANGED` | `docs/review-rubric.md` (`6825222e3198b5ccfe01499bf11737901143cf1d`) |
| Four Gates | Deterministic, Spatial, Visual, Professional | Deterministic, Spatial, Visual, Professional | `UNCHANGED` | `scripts/review_submission.py` (`f30f4485417809466ab0507c38662b32a7455a68`) |
| Packet Composition | 5 figures, 2 PDFs (p1), 2 HTML screenshots | 5 figures, 2 PDFs (p1), 2 HTML screenshots | `UNCHANGED` | `scripts/export_review_packet.py` (`fe4ffc5e9202df72efddca666b05ec118225bdba`) |
| Queue Threshold | Score >= 60.0 to merge | Score >= 60.0 to merge | `UNCHANGED` | `scripts/auto_review_queue.py` (`e35c138a428192383970321b0cedd12d1c372512`) |
| High-Water Guard | Inactive (`false`) | Inactive (`false`) | `UNCHANGED` | Grep across `upstream/main` returned 0 occurrences |
| Bilingual Requirement | V2 Chinese + English deliverables | V2 Chinese + English deliverables | `UNCHANGED` | `scripts/validate_submission.py` (`2b78304069bd8a7bc0e8407ec361c3a9dd8fb7a6`) |

Overall Audit Classification: `UNCHANGED`
