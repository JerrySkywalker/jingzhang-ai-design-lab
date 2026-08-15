# Release policy simulation

## Current unsafe world

```text
Draft -> CI skipped -> no trusted review (safe wait)
Ready -> CI pass -> trusted score -> score >= 60 -> intake/merge path
                                             ^ historical 77 is not protected
```

## Required future-safe world

```text
Ready -> CI pass -> discover historical trusted best for same submission (77)
      -> trusted rescore -> score < 77 : HOLD / DO NOT MERGE
                            score >=77 : eligible for normal intake flow
```

The participant-side gate does not activate this policy. It only refuses `SAFE_TO_MARK_READY` unless a deployed current-main guard proves the exact directory and historical score. An open infrastructure PR is not deployed protection.
