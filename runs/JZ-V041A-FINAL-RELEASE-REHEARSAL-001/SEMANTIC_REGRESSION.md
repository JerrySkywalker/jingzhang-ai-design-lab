# Semantic regression

`tools.jz_review_packet` compared frozen `94c51f2011a365a1cb2674a62f8cc3af7aba59e5` to the ready rehearsal package: `RESULT=PASS`.

All stop-ship invariants pass:

- `STATUS_ACTION_PRESENT=true`; `AI_OFF_CITY=PASS`
- `TASK_COUNT=12`; `DEEP_TASK_COUNT=3`; `DEEP_TASK_IDS=S01,S04,S07`; `NO_BUILD_TASK_COUNT=9`
- `INTERFACE_COUNT=3`; `DELIVERY_CONTRACT_COUNT=3`
- `OWNER_SELECTED_CANDIDATE=JINGZHANG_IN_PLACE`; `OWNER_SELECTION_LOCKED=true`
- `COMPETITION_RESULT=NOT_DETERMINED`; award, implementation, and government-endorsement claims are false.

The only frozen-to-ready structured differences are current-tool derived `manifest.json` and `self_check.json` hashes.
