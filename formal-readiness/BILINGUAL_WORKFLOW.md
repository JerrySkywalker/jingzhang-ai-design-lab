# Bilingual Workflow

## Contract

- pair `proposal.md` with `proposal.en.md` (or the declared primary/translated equivalent);
- render both `report/proposal.html` and `report/proposal.en.html`;
- pair `visual/index.html` and `visual/index.en.html`;
- pair A3 and A0 primary/English PDFs;
- pair every text-bearing figure; register genuinely text-free figures as neutral;
- keep all IDs, metrics, source references, data references and spatial claims aligned across languages.

## Production order

1. Freeze project terminology, place names, evidence labels and required disclaimers in a glossary.
2. Translate section by section after design intent freezes; do not wait for one final bulk pass.
3. Preserve identifiers and numbers mechanically; reconcile changed facts in the source language first.
4. Generate both HTML files from their paired Markdown.
5. Export primary/English figures and boards from the same geometry/metrics inputs.
6. Run an ID/number/link/display-asset parity check before feature freeze.
7. Conduct human architectural copy review for public clarity and non-jargon naming.

The repository's `backfill_bilingual_*` scripts are maintainer-only and are not a participant workflow. The optional local-ML translation requirements are heavy and were not installed for rehearsal. Translation can be produced independently, but final factual and spatial parity must be reviewed by the participant.
