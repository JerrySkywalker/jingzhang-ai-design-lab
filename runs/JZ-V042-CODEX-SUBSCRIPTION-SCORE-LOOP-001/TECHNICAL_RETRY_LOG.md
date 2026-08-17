# Technical retry log

Candidate `CANDIDATE-A`, reviewers A/B/C, attempt 1: no output schema verdict was produced. The documented `codex exec` subcommand rejected the unsupported inherited `-a never` flag before a session started (`unexpected argument '-a'`).

Retry admission: allowed. The failure occurred before any subjective pass or valid verdict. Attempt 2 removes only that unsupported flag; packet, candidate identifier, visual attachments, rubric, output schema, reviewer focus, and read-only sandbox remain unchanged.

Candidate `CANDIDATE-A`, reviewers A/B/C, attempt 2: sessions started but the service rejected the output schema before producing a verdict because the schema-version `const` lacked an explicit JSON type. Attempt 3 adds only `"type": "string"` to that field. No rubric, evidence, prompt, image, candidate, or scoring change is made.

Candidate `CANDIDATE-A`, attempt 3: the corrected schema allowed reviewer execution, but packet-only isolation failed when a reviewer attempted to inspect host memory outside the packet. The coordinator stopped the remaining reviewer processes. Any incomplete or emitted output is invalid, not aggregated, and not eligible for rerun because the required isolation contract was not met.
