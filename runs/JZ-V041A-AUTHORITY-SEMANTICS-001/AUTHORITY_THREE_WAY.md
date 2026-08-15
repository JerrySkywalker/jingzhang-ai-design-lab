# Owner-selection authority — three-way comparison

| Version | Semantic state | Reader effect | Finding |
| --- | --- | --- | --- |
| A: v0.4 `ac2a41c` | `final_winner=JINGZHANG_IN_PLACE`, while copyright says Owner decision required | Overclaims a result and conflicts with the authority statement | Contradictory |
| B: v0.4.1 `00e99480` | `final_winner=OWNER_DECISION_REQUIRED` | Removes the overclaim but retains an overloaded bare final-winner label and suppresses the made Owner selection | Incomplete |
| C: v0.4.1a `94c51f2` | `owner_selected_candidate=JINGZHANG_IN_PLACE`; `owner_selection_locked=true`; `competition_result=NOT_DETERMINED`; award, implementation, and government flags false | States the internal selection in bilingual plain language and denies any competition, adoption, approval, or endorsement outcome | Correct |

v0.4.1a uses no reader-facing `FINAL_WINNER` or `OWNER_DECISION_REQUIRED` language. Its
Chinese and English proposals state that the Owner selected Jing-Zhang In Place as the final
submission candidate, and that the selection is not a competition result, award claim,
official adoption, implementation approval, or government endorsement.

`AUTHORITY_CONTRADICTION_RESOLVED=true`
`OWNER_SELECTION_PRESERVED=true`
`COMPETITION_OVERCLAIM=false`
