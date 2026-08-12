# Method Calibration v0.2 — Competition Rubric Recovery

Decision context: `JZ-R5-RUBRIC-RECOVERY-001`

Status: `DECISION` — governing internal evaluation method for this run

## Why calibration is required

The Candidate-04 one-shot used absolute-white-space pre-admission gates. That run correctly established that none of seven scratch premises passed those gates. It did not establish that every premise is uncompetitive under the official review rubric.

The current official rubric evaluates seven dimensions and recommends these weights:

| Dimension | Weight |
|---|---:|
| `brief_alignment` | 20% |
| `originality` | 10% |
| `ai_planning_innovation` | 15% |
| `implementation_feasibility` | 20% |
| `public_interest_inclusion` | 10% |
| `risk_compliance` | 10% |
| `expression_completeness` | 15% |

Each dimension is scored 0–5. The internal weighted proxy is calculated as:

```text
sum(dimension_score / 5 * dimension_weight)
```

This proxy supports comparison. It is not an official score, is not `formal-review-ready` evidence and cannot replace professional or Owner judgment.

## Reclassification of site portability

The former P2 site-substitution test is no longer an automatic hard kill. It is divided into two questions:

```text
METHOD_PORTABLE
SITE_RESPONSE_GENERIC
```

`METHOD_PORTABLE` means a useful method, analytical frame or implementation discipline could transfer to another district. That is not a defect by itself. Good planning methods often transfer.

`SITE_RESPONSE_GENERIC` means the proposed urban structure, key spatial judgments and differentiated area responses remain nearly unchanged after replacing Jing-Zhang with another AI district. This is a material weakness in `brief_alignment`, `originality`, `spatial_generativity` and `site_specificity`, but it is a hard failure only when the design cannot be made site-responsive without changing its first principle.

The review must name what changes because of Jing-Zhang: primary geometry, urban-fabric response, heritage/public-space relationship, three-area differentiation, institutional/transport/environmental thresholds, or implementation order. Railway vocabulary and official area names do not count.

## Reclassification of collision

Collision is classified by proposition, not keywords:

```text
NEAR_DUPLICATE
SAME_TERRITORY_DIFFERENT_PROPOSITION
THEME_OVERLAP
```

### `NEAR_DUPLICATE`

The peer and premise materially share the same:

1. first-principles problem;
2. primary geometry;
3. three-area roles;
4. core mechanism;
5. implementation path; and
6. AI role.

A direct near duplicate is a hard kill unless the claimed difference changes several of those dimensions and can be demonstrated spatially.

### `SAME_TERRITORY_DIFFERENT_PROPOSITION`

The premise works in a crowded subject area but frames a different urban problem, draws a different primary structure, assigns different key-area roles or changes how the scheme is implemented. This reduces originality only to the degree of actual similarity. The review must explain why a jury would not see a reskin.

### `THEME_OVERLAP`

The premise shares broad themes, systems or vocabulary with peers but has a distinct first principle and urban design. This is normal competition context and is not a kill.

## Current hard failures

Only these conditions automatically prevent promotion:

```text
DIRECT_NEAR_DUPLICATE
CANNOT_GENERATE_COMPLETE_CITY
AI_IS_ONLY_LABEL
URBAN_DESIGN_REQUIRES_FABRICATED_SITE_FACT
IMPLEMENTATION_REQUIRES_UNVERIFIED_MEGAPROJECT
```

Unknown official geometry is not itself a hard failure and may not reduce the official proxy score. A premise fails when it converts an unknown into a necessary fact or can work only through a speculative megaproject.

## Additional Chief Architect dimensions

These do not change or enter the official weighted total:

- `spatial_generativity` — whether the first principle naturally generates the 43.6 km² strategy, drawable 11.4 km² structure, differentiated three-area designs, buildings, streets, public realm and implementation.
- `site_specificity` — whether verified/contextual Jing-Zhang conditions materially alter the city rather than decorate it.
- `owner_contribution` — whether the Owner can make a distinctive, credible contribution after the urban-design premise is selected.

Selection order is:

```text
1 official rubric quality
2 spatial generativity
3 evidence tractability
4 site-specific response
5 distinct but not necessarily unique proposition
6 owner contribution
```

## Promotion threshold

At most one finalist may become a provisional Final Candidate / Candidate 05, and only when all conditions hold:

```text
NO_HARD_KILL=true
OFFICIAL_WEIGHTED_PROXY_SCORE>=70
BRIEF_ALIGNMENT>=4/5
IMPLEMENTATION_FEASIBILITY>=3/5
AI_PLANNING_INNOVATION>=3/5
SPATIAL_GENERATIVITY>=4/5
SIGNIFICANTLY_BETTER_THAN_OTHER_FINALIST=true
```

Promotion is not Owner selection, formal admission, approval or authorization to create a fork.

## Evidence and scoring discipline

Every score records:

```text
evidence
uncertainty
site_evidence_effect
nearest_peer_effect
what_would_change_score
```

Evidence labels remain `FACT`, `DERIVED`, `ASSUMPTION`, `CONCEPT` and `DECISION`. Source absence is not design license. Candidate-neutral Ordinary-Day Completeness, Living Systems and Task-to-Space methods review a promoted candidate; they do not generate or select it.
