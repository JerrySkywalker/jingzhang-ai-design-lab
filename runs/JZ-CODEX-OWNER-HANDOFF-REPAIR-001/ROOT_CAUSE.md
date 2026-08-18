# Root cause

`LIKELY_ROOT_CAUSE` is confirmed:

```text
broad recursive Get-ChildItem with -ErrorAction Stop encountered an unrelated
AccessDenied path before reviewer-a.wsb was returned.
```

The search was not scoped to the receipt-declared harness root.  With `ErrorActionPreference=Stop`, the unrelated access failure was terminal for discovery rather than a non-fatal inaccessible path.  As a result, the configuration variable was not populated and the subsequent launch was invoked with a null path.

The harness itself is current and valid: the XML parses, its three mappings all resolve inside `V:\src\_review_isolation`, and the paths match the prior receipt's declared layout.  No stale-path repair was required.

The permanent correction is a deterministic fixed-path launcher at `V:\src\_review_isolation\Start-JZReviewerAProbe.ps1`.  It never enumerates `V:\src` or another repository.
