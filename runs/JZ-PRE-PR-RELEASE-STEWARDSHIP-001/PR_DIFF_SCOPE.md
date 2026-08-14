# Effective PR content scope

At local head `1d5cb1a…`, the merge base with the admitted upstream contract is
`b8e630c5b689207f994ae9ff2ebad35af4cddcbe`.

```text
git diff --name-only b8e630c… 1d5cb1a…
```

Result:

- `PR_CHANGED_FILE_COUNT=45`
- `PR_CHANGED_PATH_PREFIXES=submissions/JerrySkywalker/jingzhang-in-place`
- `PR_DIFF_SCOPE=PASS`
- No effective changes under `scripts/`, `brief/`, `data/`, `docs/`, `skills/`,
  another participant directory, `submissions-data.js`, or gallery metadata.

Normal merge ancestry contains peer churn; it does not pollute the effective
PR content diff.
