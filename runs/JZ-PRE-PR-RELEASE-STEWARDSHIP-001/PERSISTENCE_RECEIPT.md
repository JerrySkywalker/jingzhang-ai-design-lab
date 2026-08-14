# Persistence receipt

## Local, auditable commit chain

1. `4184d9d0e229270067dd513bcfcd140a3561edef` — persisted the pre-existing
   admission evidence (`manifest.json`, `self_check.json`) on top of `5f32…`.
2. `b837f4e64537c2bbb592014c4222d5e7808f0e21` — normal merge of current
   `upstream/main` (`b8e630…`) to admit participant-facing official tooling.
3. `1d5cb1aaa9d76edc3532e593c803cb936070a744` — current-contract
   recertification (`manifest.json`, `self_check.json` only).

All staged changes passed `git diff --check` before their commits. The final
formal worktree is clean.

## Remote attempt

`git push --porcelain origin HEAD:refs/heads/submission/JerrySkywalker/jingzhang-in-place`
was attempted normally. It ended with:

```text
error: RPC failed; HTTP 408 curl 22 The requested URL returned error: 408
send-pack: unexpected disconnect while reading sideband packet
fatal: the remote end hung up unexpectedly
```

The remote ref remained `e3334510f9d8df07e20f7a5bfcd40e1f916f8e7b`.
The range then needing transfer had 8,744 reachable objects / 1,687,154,310
raw bytes (about 1.61 GiB), inherited through normal published merge ancestry.
`participant_preflight.py --check-push` and a clean-clone `git push --dry-run`
both passed, establishing credentials/access but not upload completion.

No unchanged real push was retried after the explicit HTTP 408. This is a
recoverable transport/persistence HOLD, not a branch rewrite request.
