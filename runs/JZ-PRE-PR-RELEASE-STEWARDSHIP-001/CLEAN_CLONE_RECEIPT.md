# Fresh remote-byte clean-clone admission

Scratch workspace (new for this run, never reused):

```text
V:\src\_scratch\JZ-PRE-PR-CLEAN-20260815-003402\remote-formal-current-tools
```

Construction:

1. fresh shallow, blobless, sparse clone of official `upstream/main` at
   `b8e630…` for the current scripts and policy inputs;
2. fresh fetch of Owner fork branch at remote `e333451…`;
3. overlay only the 45 package files from that remote branch;
4. mark Owner fork as the promisor remote so its package blobs are fetched
   from the actual fork, not from the local working tree.

The first sparse set omitted root `scenarios/` and `tracks.json`, which the
current validator needs as policy inputs; they were added before the recorded
result. The final clean test is therefore not a false sparse failure.

| Check on remote `e333…` bytes | Result |
| --- | --- |
| Current validator | FAIL — only the two unpushed CRLF/LF manifest hashes. |
| Spatial review | PASS — three non-blocking `KEY_AREA_PROVISIONAL` notices. |
| Visual review | PASS |
| Professional review | PASS |
| Preflight with `--check-push` | FAIL because its current self-check reproduces those two deterministic hash errors. Its scope, fork identity, package size, and `git push --dry-run` checks pass. |

This is the intended high-value proof: remote bytes are not yet sufficient for
admission, while the local certified `1d5cb1a…` bytes are. The only missing
step is successful ordinary persistence of the already-certified commit chain.
