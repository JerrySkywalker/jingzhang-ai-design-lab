# JZ97-G01-G02 — Official Truth and Anchor Corpus Unattended Train

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
RUN_ID=`JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001`  
TARGET_RUNTIME=`8–12 useful unattended hours`  
ENGINE=`AGY gemini-3.7-flash-high`

## 0. Mandatory bootstrap

Before mutation read exactly:

1. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`
2. `docs/CURRENT_PROGRAM.md`
3. `state/JZ97_PROGRAM_STATE.json`
4. `docs/PROGRAM_CONTROL_AIRLOCK.md`
5. `goals/JZ97-G01-OFFICIAL-RUBRIC-AND-PACKET-LOCK-001.md`
6. `goals/JZ97-G02-TRUSTED-ANCHOR-CORPUS-001.md`

If current state is not at G01 with C0 PASS and C1 pending, stop `BLOCKED_PROGRAM_STATE`.

## 1. Safety / unattended contract

Owner is unavailable. Make safe reversible research/tooling decisions without asking for routine confirmation. Stop only for credentials, destructive/irreversible external action, official PR mutation, proprietary/private data, or an ambiguous truth claim that cannot be safely labeled.

Do not:
- modify `JerrySkywalker/haidian` submission content;
- create v0.4.3/v0.4.4;
- mutate/open/Ready/close/merge PR #2774;
- enter official trusted review;
- run formal isolated AGY jury (Owner login is reserved for G03);
- copy competitor media/PDF archives into design-lab;
- write Program control files into `haidian`.

## 2. G01 — lock current official truth

Fetch latest `open-city-ai/haidian` at start and again before closeout. Record exact SHAs.

Inspect current authoritative files necessary to reconstruct:
- review rubric dimensions and weights;
- integer 0–5 schema and weighted formula;
- mandatory rejection conditions;
- deterministic/spatial/visual/professional gates;
- AI review prompt/system instructions;
- review packet structured-text fields;
- core figure selection/order;
- PDF page selection;
- HTML screenshot selection;
- image limits/defaults;
- queue eligibility and decision semantics;
- high-water protection status in actual merged code/tests, not PR state alone.

Write exact evidence with repository path, upstream SHA and file/blob SHA where available. Compare to previous assumptions and classify `UNCHANGED`, `TOOLING_CHANGE`, `RUBRIC_CHANGE`, `PACKET_CHANGE`, `RELEASE_POLICY_CHANGE`.

Formal local bands must be integer 0..5. Mark any older 3.5/4.5 estimates as `DEV_ADVISORY_ONLY` rather than silently rewriting history.

G01 outputs under `runs/<RUN_ID>/`:
- `RUN_STATE.md`
- `G01_CURRENT_OFFICIAL_RUBRIC.md`
- `G01_CURRENT_OFFICIAL_RUBRIC.json`
- `G01_REVIEW_PACKET_CONTRACT.md`
- `G01_QUEUE_POLICY.md`
- `G01_UPSTREAM_CHANGE_AUDIT.md`
- `G01_EXIT.md`

Do not enter G02 unless all G01 exit criteria pass.

## 3. G02 — trusted anchor discovery

Build a calibration corpus with target >=5 **trusted exact-head** anchors spanning roughly:
- 77: Jing-Zhang In Place merged baseline;
- ~86 strong package;
- ~90 high package A;
- ~90 high package B;
- 96 ceiling package (Human Hours / verified equivalent).

Do not rely on remembered scores. For each anchor verify:
- official PR/review source;
- trusted maintainer/reviewer provenance;
- exact reviewed head SHA;
- exact official score;
- official dimension vector if explicitly available;
- review timestamp;
- package path/title;
- whether later revisions changed the package.

A score without exact-head trusted provenance is not admitted.

## 4. Anchor selection quality

Prefer anchors that collectively test:
- low/mid vs high separation;
- two independently scored ~90 packages to detect instability at equal official quality;
- recent official packet compatibility;
- high-quality visual/professional packages;
- diversity of design concept so calibration does not become style matching.

Keep rejected/ambiguous anchor candidates in a rejection ledger with reason.

## 5. Neutral blinding

Generate neutral random IDs such as `Q7`, `M3`, `K8`, `R2`, `T9`. IDs must not encode version, chronology, author, score or host preference.

Store mapping only in coordinator receipts; it must not enter reviewer packets.

Do not use names such as `BASELINE`, `V042`, `OFFICIAL96`, `HOST_PREFERRED`.

## 6. Packet builder

Using G01's current official packet contract, build a deterministic local packet for every admitted anchor.

The packet should mirror official review visibility as closely as legally/technically possible without executing contributor code or copying unnecessary repository assets. Include only review-authorized artifacts. Keep any downloaded/generated packet material in local ephemeral review workspace, not permanent public design-lab history when licensing/size makes that inappropriate.

For each packet record:
- neutral ID;
- source exact head;
- file inventory;
- per-file SHA-256;
- overall packet hash;
- visual surface inventory;
- provenance metadata stored outside packet.

## 7. Reproducibility

Build every anchor packet twice from clean inputs. Require identical file list and hashes. Diagnose nondeterminism rather than accepting approximate equality.

`PACKET_REPRODUCIBLE=true` is mandatory for admission to G03.

## 8. No scoring in this run

Do not run Opus/Sonnet/Gemini formal jury. Do not generate synthetic official scores. Development agents may assess packet completeness only.

G03 is explicitly Owner-interactive because each exact-model Windows Sandbox reviewer requires fresh authentication.

## 9. Research hygiene

The design-lab repository is public. Commit only source metadata, short analytical findings, hashes, schemas and permitted text. Do not commit third-party large media, secret blind reviewer credentials, cookies, tokens, private material or proprietary planning data.

## 10. Program state transition

If G01 PASS and G02 PASS:
- `last_completed_goal = JZ97-G02-TRUSTED-ANCHOR-CORPUS-001`
- `current_goal = JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`
- `current_train = A_CALIBRATION_FOUNDATION`
- C1 remains `PENDING` until G04
- `next_goal = JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`

Update `docs/CURRENT_PROGRAM.md` consistently.

If G01 PASS but G02 incomplete, state must remain at G02 and report exact blocker; do not claim the combined train passed.

## 11. Git / receipt policy

AGY owns Git operations.

Create or use a dedicated design-lab run branch:
`runs/JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001`

Commit durable receipts at major checkpoints and push this design-lab run branch. Do not push product repo branches.

## 12. Required G02 receipts

Under `runs/<RUN_ID>/` write at minimum:
- `G02_TRUSTED_ANCHOR_LEDGER.json`
- `G02_TRUSTED_ANCHOR_PROVENANCE.md`
- `G02_REJECTED_ANCHORS.md`
- `G02_BLINDING_MAP.json`
- `G02_PACKET_LEDGER.json`
- `G02_PACKET_REPRODUCIBILITY.md`
- `G02_EXIT.md`
- `FINAL_REPORT.md`
- `OWNER_BRIEF.md`

Do not put score/identity mappings inside the packets themselves.

## 13. Useful use of remaining runtime

If G01/G02 finish before the unattended window ends, do not start G03 and do not modify content. Use remaining useful time for:
- re-running packet reproducibility from clean state;
- deeper trusted-score provenance verification;
- finding a sixth/seventh backup anchor;
- checking official review changes at final upstream SHA;
- improving deterministic packet tooling/tests;
- validating future Sandbox launch manifests without authenticated inference;
- documentation and failure-recovery hardening.

Do not create work solely to fill twelve hours.

## 14. Final report schema

```text
DISPOSITION=
RUN_ID=JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001

START_UPSTREAM_HEAD=
END_UPSTREAM_HEAD=
UPSTREAM_CHANGE_CLASS=

G01=PASS|FAIL|BLOCKED
RUBRIC_PINNED=
INTEGER_SCORE_SCHEMA_PINNED=
PACKET_CONTRACT_PINNED=
QUEUE_POLICY_PINNED=
HIGH_WATER_GUARD_ACTIVE=

G02=PASS|FAIL|BLOCKED
TRUSTED_ANCHOR_COUNT=
ANCHOR_OFFICIAL_SCORES=
EXACT_HEAD_PROVENANCE=PASS|FAIL
NEUTRAL_BLINDING=PASS|FAIL
PACKET_COUNT=
PACKET_REPRODUCIBILITY=PASS|FAIL
BACKUP_ANCHOR_COUNT=

FORMAL_JURY_RUN=false
PRODUCT_MUTATED=false
PRODUCT_PUSHED=false
PR2774_MUTATED=false
OFFICIAL_REPOSITORY_MUTATED=false

PROGRAM_STATE_UPDATED=
NEXT_GOAL=
DESIGNLAB_BRANCH=
DESIGNLAB_HEAD=
DESIGNLAB_PUSH_STATUS=

NEXT_OWNER_ACTION=RUN_G03_THREE_MODEL_ANCHOR_JURY|REPAIR_G01_G02|OWNER_REQUIRED
```

Proceed autonomously and preserve the Program DAG.