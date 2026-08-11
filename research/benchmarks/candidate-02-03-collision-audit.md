# Candidate 02–03 Collision Audit

**Status:** research record for architecture exploration

**Read-only snapshot:** open-city-ai/haidian main at 6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4

**Snapshot date:** 2026-08-12, Asia/Shanghai
**Mutation boundary:** no official-repository file, branch, issue, pull request, fork or submission was created or changed.

## 1. Purpose

This audit tests whether Candidate 02 and Candidate 03 occupy already-developed competition territory. It is not a title search. Similar spatial structures, public-value propositions, user journeys, operating systems and implementation methods count as collision even when names differ.

## 2. Method and limits

The review used GitHub CLI read-only calls to:

- resolve the current main commit;
- read the required official skill, brief, taskbook, allowed design space, tracks, template and submission guidance;
- enumerate the exact-current Git tree;
- inspect the gallery index while treating it as a lagging discovery aid;
- search and read representative merged proposals;
- inspect open pull requests and issues;
- compare the previous review snapshot with the final snapshot.

At the final snapshot:

- the exact Git tree contained **608** paths matching submissions/author/slug/proposal.md;
- the current submissions-data.js blob still indexed **507** gallery entries;
- GitHub reported **441 open pull requests** through pagination metadata;
- GitHub CLI returned **21 open issues**.

These counts are snapshot facts and will drift. The Git tree, not the gallery count, was used to establish current merged coverage. Candidate comparison is qualitative; 608 proposals were enumerated, then likely collisions were selected through keyword, title, heading and substantive proposal review. Absence from a short table is not proof of uniqueness.

The first working snapshot was 59ed095693e94636ee1f3d5994aaff88189abce6. A later snapshot, fb7b54ffca4419c502999e8dd36dfc349a2bb3df, was 12 commits ahead and changed only four existing submission packages. The final head is one further commit ahead: it changes the repository README, a manifest-refresh script, the submission skill and a related test. The skill change adds a safe manifest-refresh step for iterating an existing ready-for-review formal package; it does not change this lab exploration's spatial or completeness requirements. The current skill was re-read in full. No brief, taskbook, allowed-design-space, track, template, formal-guide, submission-guide, geometry or submission path changed in that final increment. Peer links below remain pinned to fb7b54ffca4419c502999e8dd36dfc349a2bb3df because their contents are exact-current at the final head.

- sofizhang/jingzhang-ai-meridian;
- openvictory/jingzhang-ai-symbiotic-corridor;
- Monostar-14/jingzhang-ai-belt;
- wocaonimaworinixi-collab/jingzhang-ai-native-belt.

They reinforce the crowding around a north–south AI/heritage operating spine, but do not remove the specific Candidate 02/03 collision findings below.

## 3. Canonical task recheck

The latest versions of these files were checked:

- [urban-design-ai-submission skill](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/skills/urban-design-ai-submission/SKILL.md);
- [design brief](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/brief/site-package/design_brief.json);
- [agent taskbook](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/brief/site-package/agent_taskbook.json);
- [allowed design space](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/brief/site-package/allowed_design_space.json);
- [tracks](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/tracks.json);
- [proposal template](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/templates/proposal.md);
- [formal submission guide](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/docs/formal-submission-guide.md);
- [submissions guide](https://github.com/open-city-ai/haidian/blob/6d4f56abadb2dda1c8b0e21fbd9fc31f18b8b8e4/submissions/README.md).

### Stable constraints relevant to exploration

- **FACT:** the working scales are approximately 43.6 km², 11.4 km² and 368.4 ha;
- **FACT:** the key-area working figures are 192.1 ha, 104.3 ha and 72 ha;
- **FACT:** exact official polygons and several statutory controls remain unavailable in the package;
- **FACT:** tracks are emphases, not permission to replace a complete design with a technical topic;
- **FACT:** formal tasks require all three scales, all three key areas, complete urban systems, at least 10 AI scenarios, at least 3 tests, at least 5 personas, at least 3 landmark directions, culture/VI, operations and implementation;
- **FACT:** this lab exploration is not a valid formal submission package.

## 4. Geometry and evidence warnings from Issues

| Evidence | Relevance to both candidates | Design consequence |
| --- | --- | --- |
| [Issue #1029](https://github.com/open-city-ai/haidian/issues/1029) | Reports that provisional Dazhongsi key-area geometry is not station-anchored and appears close to Beijing North Railway Station | Neither candidate locates an exact Dazhongsi station project; both require an authoritative geometry gate |
| [Issue #846](https://github.com/open-city-ai/haidian/issues/846) | Reports a gap between provisional overall geometry and an OSM-mapped park representation | Neither candidate treats OSM park geometry as the official design boundary or guaranteed intersection |
| [Issue #1774](https://github.com/open-city-ai/haidian/issues/1774) | Records missing public-source/constraint information | FAR, height, density, green ratio, setbacks, ownership and performance are left open |
| [Issue #1781](https://github.com/open-city-ai/haidian/issues/1781) | Shows how missing controls and shared/provisional geometry distort package-wide metric comparisons | No invented quantitative control or “benchmark average” is used to validate a candidate |
| [Issue #840](https://github.com/open-city-ai/haidian/issues/840) | Records gallery snapshot lag | Exact Git tree and proposal paths take precedence over the gallery index |
| [Issue #1061](https://github.com/open-city-ai/haidian/issues/1061) | Critiques vague Agent language, lack of place experience and missing implementation/ownership | Both candidates include field/professional gates, operators, maintenance and kill criteria; no fieldwork is claimed |

Issue text is treated as participant evidence and critique, not official fact. Personal or unrelated details are intentionally excluded.

## 5. Candidate 02 — closest collisions

### Candidate tested

**京张三邻 / Three Neighbourhoods Jingzhang**

First-principles claim: the belt should first become three complete innovation neighbourhoods capable of supporting an ordinary day, linked as a federation rather than a linear specialist pipeline.

| Proposal or PR | Similarity | Difference being tested | Occupied? | Audit decision |
| --- | --- | --- | --- | --- |
| [Arrive & Belong](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/whatevertogo/arrive-belong) | human-centred innovation life, arrival/belonging and differentiated areas | three parallel complete neighbourhood economies instead of a north–south life journey | **High** | Continue only if federation and local completeness change the plan |
| [The Staying Line](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/MochenRay/jingzhang-staying-line) | affordability, daily life and reasons to remain | neighbourhood catchments and local civic centres rather than six conditions along a line | **High** | “People can stay” is not a differentiator |
| [Stay Longer Jingzhang](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/zhanwenbin520-ui/stay-longer-jingzhang) | talent life cycle and three living-yard prototypes | multi-user ordinary-city value rather than talent retention as the organising story | **High** | Needs non-talent value and non-identical forms |
| [Jingzhang Living Meridian](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/masfrank/jingzhang-living-meridian) | organic renewal, living support and three detailed areas | polycentric federation rather than a meridian | **Medium–high** | Plan-level difference remains unproven |
| [Jingzhang Cross Streets](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/jianshi-codes/jingzhang-cross-streets) | local completeness, public ground floors and precise street prototypes | three whole-neighbourhood catchments rather than repeated cross-streets | **Medium–high** | Existing proposal is more specific at street scale |
| [PR #1455 — Jingzhang Local City Units](https://github.com/open-city-ai/haidian/pull/1455) | nine local units, corridor correction and thick interfaces | three complete but unequal official-key-area neighbourhoods | **High** | “Three” requires site evidence, not taskbook inheritance |
| [PR #1513 — One Desk, One City](https://github.com/open-city-ai/haidian/pull/1513) | room/desk/street ladder for making innovation locally habitable | neighbourhood completeness is broader than a workspace-to-city ladder | **Medium** | Avoid importing its room-scale identity |
| [PR #1508 — Jingzhang Open House](https://github.com/open-city-ai/haidian/pull/1508) | three civic living rooms and a series of ports | three complete catchments rather than three rooms on one corridor | **Medium–high** | Civic centres alone cannot prove difference |

### Candidate 02 finding

**COLLISION LEVEL: HIGH.**

The field is occupied substantively, not merely lexically. Candidate 02 is retained for architecture comparison because its strongest potential difference is a many-to-many federation of three independently complete urban economies. It should not advance if field/facility evidence cannot show three distinct catchments and distinct urban forms.

### Rejected precursor

An earlier cross-weave/cross-streets direction was rejected before Candidate numbering. Jingzhang Cross Streets, Jingzhang Crossings, Jingzhang Mending Belt and PR #1455 already make the transversal/local-unit argument with greater specificity. A new name would not have fixed that collision.

## 6. Candidate 03 — closest collisions

### Candidate tested

**京张生境拼图 / Jingzhang Habitat Mosaic**

First-principles claim: soil, water, canopy, habitat continuity and seasonal comfort should determine land use, building edges, mobility and phasing before technology display; the railway park is a seed corridor inside a non-linear living-system mosaic.

| Proposal or PR | Similarity | Difference being tested | Occupied? | Audit decision |
| --- | --- | --- | --- | --- |
| [Jingzhang Season Line](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/dengpan1234/jingzhang-season-line) | seasonal climate infrastructure, public-space states and tests | non-linear living-system/urban-form framework rather than a seasonal public line | **High** | Difference must appear in land use, edges and renewal |
| [Jingzhang Habitat Commons](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/zzzzls/jingzhang-habitat-commons) | habitat, public commons, observation and stewardship | physical non-AI substrate plus three matrices/four cross-meshes rather than a habitat-common service layer | **Very high** | Professional spatial proof is mandatory |
| [Shade the Cloud](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/PelyYan/shade-the-cloud) | ground comfort and shade before cloud/compute spectacle | soil, water, habitat, seasonal refuge and renewal beyond a heat/shade compact | **High** | “Ground before AI” is already occupied |
| [Jingzhang Climate Intelligence Line](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/luther-3/jingzhang-climate-intelligence-line) | climate states, evidence and testable intelligence | AI is subordinate; the spatial mosaic leads | **Medium–high** | State/test logic is not novel |
| [Forest Rail](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/percivalcorleone-ux/forest-rail) and [PR #1876](https://github.com/open-city-ai/haidian/pull/1876) | canopy, park-city relationship and operating layers | park as seed corridor within a wider block/building/soil/refuge mosaic | **High** | Must not collapse into a greener rail park |
| [PR #1813 — Ground First](https://github.com/open-city-ai/haidian/pull/1813) | accessible, shaded, stormwater-ready and reversible public ground before AI | a living-system hierarchy shaping land use and three distinct matrices | **High** | Priority wording is occupied; spatial structure must differ |
| [The Living Weave — PR #1791](https://github.com/open-city-ai/haidian/pull/1791) | a warp/weft structure connecting public and living systems | three matrices and four need-based ecological cross-meshes rather than one warp/three wefts | **Medium** | Avoid generic weave language and uniform cross-lines |

### Candidate 03 finding

**COLLISION LEVEL: HIGH TO VERY HIGH.**

Candidate 03 is retained because it creates the strongest internal challenge to technology- or programme-led city making. It is not unoccupied competition territory. It should not advance without a professionally grounded, diagrammable non-linear structure that materially changes retain/repair/reuse/subtract/add decisions.

## 7. Boundary comparisons with Candidate 01 territory

The exact-current submissions also contain many infrastructure-, Agent-, interface- and corridor-led proposals, including:

- [Jingzhang AI Native Belt](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/wocaonimaworinixi-collab/jingzhang-ai-native-belt);
- [Jingzhang AI Meridian](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/sofizhang/jingzhang-ai-meridian);
- [Jingzhang Open Platforms](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/realMisakaMikoto/jingzhang-open-platforms);
- [Jingzhang Ground Truth](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/XuejiFang/jingzhang-ground-truth);
- [Jingzhang Reassembly Yard](https://github.com/open-city-ai/haidian/tree/fb7b54ffca4419c502999e8dd36dfc349a2bb3df/submissions/JAVA-LW/jingzhang-reassembly-yard).

These reinforce why Candidates 02 and 03 must not converge back toward Candidate 01's visible adaptive infrastructure, service interfaces and embodied/operational spine.

## 8. Audit conclusions

1. Neither Candidate 02 nor Candidate 03 is unoccupied.
2. Candidate 02's closest collision is the family of staying/belonging/local-unit/complete-life proposals.
3. Candidate 03's closest collision is Habitat Commons plus the seasonal-climate/ground-first/forest-rail family.
4. Candidate 02 remains distinct from Candidate 01 only if three local catchments—not the railway—organise the plan.
5. Candidate 03 remains distinct from both only if living systems govern urban-form decisions and AI remains removable.
6. Both candidates require a new collision review after authoritative geometry, field evidence and professional spatial work.
7. The audit supports **conditional retention for comparison**, not selection or formal submission.
