# Jing-Zhang release safety gate

`tools.jz_release_gate` is a participant-side, read-only decision aid for a successor PR. It never marks a PR ready, edits labels, comments, merges, or changes branches. It proves only the supplied/offline facts or the public facts returned by `gh` GET requests.

It fails closed. A non-Draft successor is blocked unless a current, deployed high-water guard is proven to discover the same submission directory and trusted historical score. An open infrastructure PR is not evidence of deployed policy.

```powershell
python -m tools.jz_release_gate.cli `
  --config runs/JZ-V04-SHADOW-HARDENING-001/jingzhang-in-place.json `
  --json-out runs/JZ-V04-SHADOW-HARDENING-001/release-gate.json
```

Use `--live` only to refresh public GitHub facts; it has no write path. Without it, the command evaluates the embedded or `--fixture` snapshot and labels freshness accordingly. `SAFE_TO_MARK_READY` is false by default and becomes true only for a Draft whose head, scope, merged exact-head baseline, and deployed directory-specific 77-point guard are all proven.

The score contract is deliberately small: a hypothetical score below the historical best is `HOLD`; a score equal to or above it is merely eligible for normal trusted intake. It is not an approval or merge authorization.
