# Frozen reconstruction diff

Source package tree from `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`:

```text
25c8a684452dfaec169483da0633041f156cb6ce
```

The rehearsal replaced only `submissions/JerrySkywalker/jingzhang-in-place/**` from that Git tree. Before current-tool refresh, the staged reconstructed subtree was exactly the same tree object:

```text
RECONSTRUCTED_PRE_REFRESH_SUBTREE_HASH=25c8a684452dfaec169483da0633041f156cb6ce
```

Relative to rehearsal base `6ee92a35…`, the committed PR-shaped delta has 25 files and `OUTSIDE_SCOPE_FILES=[]`.

- Design delta: ten core figures, four A3/A0 PDFs, visual indexes, and source/report package files are restored from frozen v0.4.1a rather than recreated.
- Authority-semantics delta: `proposal.md`, `proposal.en.md`, `report/copyright_statement.md`, `report/proposal.html`, `report/proposal.en.html`, and `visual/assets/ai-spatial-admission.json`.
- Derived delta after current-tool refresh: only `manifest.json` and `self_check.json` differ from frozen source. Ready-package tree: `c0a51eb4f10b82c1c6f72488d99836900a44a63e`.
