# RC1 → RC2 Presentation Delta

## Scope

This pass is presentation-only for the locked `JINGZHANG_IN_PLACE` candidate.
It translates existing package truth into a spatially legible visual system;
it does not alter the proposal, geometry, metrics, status/action register,
project portfolio, task packets, sources, assumptions, or design conclusions.

## What changed

- Rebuilt all five paired core figures from the package's existing geometry,
  status/action register, project portfolio, simulation and metrics inputs:
  1. overall conceptual spatial plan;
  2. STATUS → ACTION → trigger → spatial-consequence patch atlas;
  3. three distinct key-area sections plus urban-space sequence;
  4. mobility, blue-green, public and service system;
  5. evidence, unknowns and implementation gates.
- Rebuilt the three A0 boards as **The City / The Three Places / How It
  Works**, with different long-distance roles.
- Rebuilt the 12-page A3 booklet as a close-reading sequence of plan, atlas,
  overview, individual sections, system, task/ordinary-day, evidence and
  closing pages.
- Rebuilt both offline visual narratives with spatial story first and complete
  registers behind native expandable sections.
- Localised reader-facing Chinese and English presentation copy, report
  language links and PDF footer treatment; added semantic skip links, visible
  focus styling, reduced-motion support and larger derived report references.
- Regenerated both report HTML files from the frozen Markdown, followed by a
  derived-only heading-outline normalisation so each document has one H1.

## What did not change

```text
STATUS × ACTION=true
NO_MANDATORY_SINGLE_SPINE=true
HETEROGENEOUS_RENEWAL_FIELD=true
THREE_KEY_AREA_ROLES=true
RETAIN_FIRST=true
EVIDENCE_GATED_ACTION=true
AI_OFF_CITY=PASS
AI_MATTERS=PASS_CONDITIONAL
NO_BUILD_FINDINGS=true
PROVISIONAL_GEOMETRY_DISCLOSURE=true
```

The frozen-truth comparison against RC1 returned no differences in
`geometry/**`, `metrics.json`, `simulation.json`, `assumptions.json`,
`sources.json`, `proposal.md`, `proposal.en.md`,
`visual/assets/status-action-register.json`, or
`visual/assets/renewal-project-portfolio.json`.

## Reproducibility

`build_presentation_rc2.py` is the run-local, deterministic RC2 presentation
builder. It reads only the formal package's existing truth inputs and imports
the historical RC1 builder solely for isolated drawing primitives. It does not
call historical fact, geometry, proposal, manifest or self-check writers.

The release workflow was:

```text
frozen package truth
→ official report render
→ RC2 presentation builder
→ manifest refresh
→ marked self-check (four gates)
→ PDF/figure/HTML QA
→ preflight
```
