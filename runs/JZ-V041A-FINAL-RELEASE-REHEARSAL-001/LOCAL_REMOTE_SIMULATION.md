# Local remote simulation

`LOCAL_REMOTE_SIMULATION=PASS`

The rehearsal commit was exposed through a separate local bare repository and a separate sparse working clone. The clone has its own `.git` directory and worktree and checked out the actual submission files; it does not reuse the rehearsal working tree.

The repository has approximately 10 GiB of shared Git packs and global LFS filtering. A conventional transfer timed out before creating a ref, so the simulation used Git shared-object alternates, direct local LFS storage, and sparse checkout of trusted scripts plus the target package. This avoids copying unrelated peers while retaining a genuine independent checkout. The clean clone head exactly equals `ae860c5e621150d4ac7d5dc08576b6042ecc6dfc`.

Temporary simulation paths are intentionally retained locally for audit; no product remote was contacted or changed.
