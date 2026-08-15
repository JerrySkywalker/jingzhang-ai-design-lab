# Review-packet model

`tools.jz_review_packet` is `SHADOW_ONLY`, `NOT_OFFICIAL`, and `NOT_TRUSTED_REVIEW`. It intentionally makes no paid model call and never assigns an official score.

The source of the visible-surface rule is the locally available trusted `scripts/ai_review_submission.py`. Its default 18-image packet is language paired:

- five core figures in zh/en (10);
- first page of A3 and A0 in zh/en (4);
- screenshots of report and visual HTML in zh/en (4).

The harness separately compares hashes and sizes, confirms PNG signatures and non-empty first-page-capable PDFs, checks bilingual structural parity, and applies the v0.4 semantic contract. It is deliberately stricter about loss of an already-passing semantic or bilingual invariant than about a new baseline capability.

The official reviewer also receives the proposal text, structured matrices, self-check and gate results. This harness is therefore regression evidence, not a simulation of its qualitative judgment.
