# Git blob hash and line-ending audit

## Current contract

The current official `scripts/git_blob_hashes.py` creates a temporary Git
index, `git add`s the declared paths, and hashes `git show :path`. Therefore
the manifest contract is the SHA-256 of the bytes Git would store after trusted
clean filters — not an arbitrary raw working-tree hash. `refresh_submission_manifest.py`
and `validate_submission.py` use that helper.

## Windows observation

- `core.autocrlf=true` came from the Git system configuration.
- `core.eol` was unset.
- `.gitattributes` has `*.pdf binary` but no EOL rule for GeoJSON.
- `geometry/key_areas.geojson` and `geometry/site_boundary.geojson` showed
  `index=LF / worktree=CRLF`.

The pre-refresh current validator reproduced two exact mismatches:

| Path | Old declared CRLF hash | Current Git-blob LF hash |
| --- | --- | --- |
| `geometry/key_areas.geojson` | `6a1b929e…b73e058` | `56692681…861718d3` |
| `geometry/site_boundary.geojson` | `4839158c…d0f9` | `66b8ab3d…4348ff` |

The only repair was the official command:

```text
python scripts/refresh_submission_manifest.py submissions/JerrySkywalker/jingzhang-in-place --json
```

It changed only those two derived hashes and reset `self_checked`. The current
self-check regenerated the self-check hash, and the latest validator passed.

Result:

- `GIT_BLOB_HASH_SEMANTICS=PASS` locally at `1d5cb1a…`
- `LINE_ENDING_RISK=REPAIRED_LOCALLY_UNPERSISTED`
- `HASH_REPRODUCIBILITY=PASS_LOCAL_FAILS_ON_UNPUSHED_REMOTE`

No manifest hash was hand-edited and no geometry bytes were reformatted.
