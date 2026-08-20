# Program Control Airlock

This document prevents internal Program/control artifacts from leaking into the official participant submission.

## Repository roles

### `JerrySkywalker/jingzhang-ai-design-lab`
`ROLE=PROGRAM_CONTROL_AND_DESIGN_MEMORY`

Allowed here:
- canonical Program roadmap and DAG
- Goal contracts and gate transitions
- machine-readable Program state
- ADRs and design decisions
- benchmark and trusted-anchor research
- calibration models and jury receipts
- experiments, rejected candidates, run evidence
- agent instructions and execution policy

### `JerrySkywalker/haidian`
`ROLE=SUBMISSION_PRODUCT`

Only curated product artifacts belong in `submissions/JerrySkywalker/jingzhang-in-place/**`, including proposal text, approved figures, GeoJSON, structured evidence, HTML, A3/A0 and manifest-required files.

Do **not** migrate:
- `goals/`
- `runs/`
- `state/`
- Program DAG/roadmap
- score calibration or jury verdicts
- benchmark comparisons or competitor strategy
- agent/subagent instructions
- internal release strategy

### `open-city-ai/haidian`
`ROLE=OFFICIAL_CANONICAL_REPOSITORY`

Mutation only through the official participant PR workflow.

### `V:\src\_review_isolation`
`ROLE=LOCAL_EPHEMERAL_JURY_RUNTIME`

Contains blind packets, runtime, Sandbox configs and local reviewer outputs. It is neither Program source nor submission content.

## Mechanical release rule

Every release reconstruction must verify that the participant diff against the current official base contains only paths matching:

```text
^submissions/JerrySkywalker/jingzhang-in-place/
```

Any control-plane file appearing in the product diff is a blocking error.

## Information hygiene

The design-lab repository is public. Do not commit credentials, private/proprietary data, auth material, browser/session state or secrets. Blind jury mappings and calibration strategy may be public under the current repository policy; if the Owner later requires secrecy, move only that sensitive control subset to a private control repository through an explicit ADR rather than silently splitting state.

## Migration principle

Material flows one way only after curation:

```text
Program/design memory
        |
        | selected product result only
        v
participant submission fork
        |
        | scoped PR
        v
official canonical repository
```

Never copy control-plane directories wholesale into the product repo.