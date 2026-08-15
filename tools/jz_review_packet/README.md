# Jing-Zhang review-packet regression harness

`tools.jz_review_packet` compares two local submission snapshots using the same visible-surface family selected by the trusted Review Agent code: five figures, first pages of A3/A0 PDFs, and report/visual HTML, each language-paired where present. It never calls a paid model and does not claim an official score.

```powershell
python -m tools.jz_review_packet.cli compare `
  --baseline runs/JZ-V04-SHADOW-HARDENING-001/snapshots/baseline `
  --candidate runs/JZ-V04-SHADOW-HARDENING-001/snapshots/v04 `
  --json-out runs/JZ-V04-SHADOW-HARDENING-001/BASELINE_V04_DELTA.json `
  --markdown-out runs/JZ-V04-SHADOW-HARDENING-001/BASELINE_V04_DELTA.md
```

For immutable refs instead of local paths, add `--repo V:\src\haidian`; the command archives only `submissions/JerrySkywalker/jingzhang-in-place` into a temporary directory. The exit code is nonzero only for a candidate semantic/bilingual stop-ship regression. In addition to the frozen STATUS × ACTION / 12-to-3 contract, the v0.4.1a contract requires an explicit Owner selection, a locked selection, `COMPETITION_RESULT=NOT_DETERMINED`, and false award, implementation, and government-endorsement claims. First-window coverage, hashes, artifact decodability, and structured deltas are evidence for review, not a trusted score or merge authorization.
