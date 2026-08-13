# JZ-PRESENTATION-RELEASE-001 — Run State

## Owner boundary

```text
WORKING_PRODUCTION_CANDIDATE=JINGZHANG_IN_PLACE
C05_PROPOSITION_LOCKED=true
DISPLAY_NAME_ZH=京张续城
DISPLAY_NAME_EN=Jing-Zhang In Place
DISPLAY_NAME_LOCKED=true
CONTENT_FREEZE=true
DESIGN_FREEZE=true
FINAL_WINNER=OWNER_DECISION_REQUIRED
OFFICIAL_PR_AUTHORIZED=false
```

## Admission snapshot

```text
FORMAL_REPO=JerrySkywalker/haidian
FORMAL_BRANCH=submission/JerrySkywalker/jingzhang-in-place
FORMAL_HEAD_START=173c8d722d33ef9d53b70f7d7ed6ed8c762512c7
REMOTE_HEAD_START=173c8d722d33ef9d53b70f7d7ed6ed8c762512c7
UPSTREAM_HEAD_START=2ba908ad1cfa0e1db01b92e79b2108258f6b6054
FORMAL_CLEAN_START=true
STASH_COUNT=0
GIT_LOCK_COUNT=0
```

`origin` and `upstream/main` were fetched before this record. The delta from the preceding RC-audit head `284dbb22bd062b39333af20f0edd6bcab9a24e1f` to `UPSTREAM_HEAD_START` contains 20 peer-submission merges and 641 changed paths, all below `submissions/<author>/<slug>/`. It is classified `PEER_SUBMISSIONS_ONLY`; no upstream merge is authorized or required.

## RC1 preservation

```text
RC1_SHA=173c8d722d33ef9d53b70f7d7ed6ed8c762512c7
RC1_PACKAGE_STATE=ready_for_review
RC1_SELF_CHECK=PASS
RC1_DETERMINISTIC=PASS
RC1_SPATIAL=PASS
RC1_VISUAL=PASS
RC1_PROFESSIONAL=PASS
RC1_PREFLIGHT_CHECK_PUSH=PASS
RC1_MANIFEST_SHA256=a3bc03712ca9c9e243ab05e39092862785904d5edc04e6019768760300d86f57
RC1_FILE_COUNT=45
RC1_PACKAGE_BYTES=4251745
```

The baseline spatial review carries only the known, non-blocking provisional-geometry disclosure for three key areas. No formal package file has been edited at this checkpoint. A complete independent SHA-256 inventory is retained in `RC1_ARTIFACT_HASHES.md`.

## Runtime declaration

```text
MODEL_REQUESTED=gpt-5.6-terra
REASONING_REQUESTED=ULTRA
PROFILE_MAPPED_MODEL=gpt-5.6-terra
PROFILE_MAPPED_REASONING=xhigh
EFFECTIVE_RUNTIME_METADATA_VERIFIED=false
```

The local routing metadata identifies the active Implementer profile mapping, but does not attest to an externally exposed per-turn runtime override. This record keeps the requested and profile-mapped values distinct.

## Completion snapshot

```text
FORMAL_HEAD_END=e3334510f9d8df07e20f7a5bfcd40e1f916f8e7b
REMOTE_HEAD_END=e3334510f9d8df07e20f7a5bfcd40e1f916f8e7b
UPSTREAM_HEAD_END=17ae1c94f0f4d51875fff4ce603af283d8635897
UPSTREAM_CHANGE_CLASS=PEER_SUBMISSIONS_ONLY
FORMAL_BRANCH_PUSHED=true
OFFICIAL_PR_CREATED=false
OFFICIAL_REPO_MUTATED=false
DIRECT_NEAR_DUPLICATE_FOUND=false
```

The terminal upstream delta contains only peer-submission paths. Its last two
additions are follow-on peer merges for `jingzhang-leveling-line` and
`every-sense-jingzhang`; both are included in the bounded
direct-near-duplicate screen. No upstream merge was performed.
