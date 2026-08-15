# Current participant-tool contract

The supported current ready-package sequence is:

1. Render only affected derived presentation artifacts when a source change requires it.
2. Run `python scripts/refresh_submission_manifest.py <submission>`.
3. Run `python scripts/self_check_submission.py <submission> --pr-author JerrySkywalker --mark-self-checked --json`.

The frozen v0.4.1a change did not alter figures, PDFs, geometry, or visual indexes. This rehearsal did not regenerate them. It refreshed only `manifest.json` and `self_check.json` after the frozen source tree was restored.

Current validator commands require an explicit `--pr-author`; this is included in the release capsule and future procedure.
