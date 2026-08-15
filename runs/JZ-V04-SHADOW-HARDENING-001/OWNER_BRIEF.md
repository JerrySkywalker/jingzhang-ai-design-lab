# Owner brief

1. Do not mark PR #2774 ready. The deployed policy still skips Draft PRs, uses an absolute 60
   threshold, and has no proven active 77 high-water guard.
2. Deploy and prove a high-water guard that discovers this exact submission directory and its
   trusted score 77. Re-run the live release gate only after that deployment is on current main.
3. v0.4 remains the certified default. A local-only v0.4.1 candidate (`00e99480`) is available
   for Owner review because three independent re-reviews accepted a narrow authority consistency
   repair. No proposal branch, PR, or remote was touched.
4. If the Owner elects to adopt it, use a fresh authorised successor workflow; do not mutate or
   force-push the certified v0.4 branch or PR #2774.
