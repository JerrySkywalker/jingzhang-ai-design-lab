# Candidate 01 Collision Audit v0.2

## Snapshot and method

- Official repository: `open-city-ai/haidian`
- Exact main: `7169d68a5d966d1ba97634e80b5f6250c38041e0`
- Retrieval: GitHub API / CLI, read-only
- Scope: proposal Markdown, PR metadata and relevant machine-readable text; no media/PDF and no external mutation
- Interpretation: participant proposals are collision evidence, not official site facts or proof of implementation

Merged submissions were read at the exact merge/head identifiers below. Open PRs were read at their recorded head and may change after this snapshot. Geometry described by submissions is commonly provisional; validation status never proves performance, land availability, safety or adoption.

## Deep comparison set

| Proposal / PR | Snapshot status | Substantive collision with C01 | Classification |
| --- | --- | --- | --- |
| [#1807 智轨织城](https://github.com/open-city-ai/haidian/pull/1807) | merged; head `4014cab7a69e7eaa7d1204c83b76fc2020ef304b`; merge `0ec4af08d8181f03beff573541ba8aef9b961291`; v0.1 | four coexisting lines, AI test/pilot, shared equipment, minimum data, human takeover and isolatable public infrastructure | `PARTIALLY_OCCUPIED` |
| [#1815 轨迹织城 / RailWeave](https://github.com/open-city-ai/haidian/pull/1815) | merged; head `c1e78c49bb07ac2dead0a5acb4c6943cb4aeae08`; merge `ed919067373de5c351a86245c64d03785c2d22b5`; v2.0 | reconfigurable workshop, controlled test, energy/maintenance/offline resilience, reproducible versions, human takeover and exit budget | `PARTIALLY_OCCUPIED` |
| [#1811 AI 朝圣·铁轨新生带](https://github.com/open-city-ai/haidian/pull/1811) | merged and later updated on official main; end-snapshot proposal blob `a3bb9f97087cb960815165b20e3e8b027d888ac7` | dual tracks, validation stations, failure siding, reversible nodes, service-design rights, non-AI civic track, human/no-screen nodes and manual daily fallback | `OCCUPIED_TERRITORY` |
| [#1809 JZ Common Ports](https://github.com/open-city-ai/haidian/pull/1809) | merged; head `3c26823330921dd20bc201a60ac59cde1c2b9122`; merge `3e08283e7ea1a35bd792c082912c4aee322c1d55`; v0.2 | Common Port, request-sandbox-review-release/recall, state passport, red-card stop, minimum data and shared services | `OCCUPIED_TERRITORY`; physical substrate only partial |
| [#1803 Jingzhang AI Commons](https://github.com/open-city-ai/haidian/pull/1803) | merged; head `fd25bde5f37fa7607dd47a49e07c4f1e3adcc8b4`; merge `da39a1a9ad39d8a8eee69e7f7404dcd566006701` | AI commons, public-intelligence spine, open platform, edge compute, reversible pilots and public experience | `OCCUPIED_TERRITORY` |
| [#1799 Jingzhang Neural Spine](https://github.com/open-city-ai/haidian/pull/1799) | merged; head `812ff6aea9bfcc1b1212722b021b537f7fb3d947`; merge `708183f2bb920111b8bafe5377287a53ff7aa2be`; v1.0 | spine plus three areas, open compute, experimental blocks, testing square, lab-to-street and shared GPU/data | `OCCUPIED_TERRITORY`; physical interoperability only partial |
| [#1846 Jingzhang Beacon](https://github.com/open-city-ai/haidian/pull/1846) | merged; head `f2855c3bad596fd9f3c98cede3ec54470a260752`; merge `c101ab26d5fa7b31d9ceb83f969d6813dd560f9d` | green/yellow/red states, removable equipment, rollback, minimum sensing boundary, lifecycle and synthetic failure exercise | `OCCUPIED_TERRITORY` |
| [#1817 ON DUTY JING-ZHANG](https://github.com/open-city-ai/haidian/pull/1817) | merged; head `73c5f245f9f6c904e598db2faf6b0c1d5b5bad66`; merge `7bb29962bf0387a17c947f47557476944b0d3cbe`; V3 | seven states, handover packet, human/paper baseline, maintenance back-of-house, slow robot test and vendor exit | `OCCUPIED_TERRITORY` |
| [#1833 京张交接线](https://github.com/open-city-ai/haidian/pull/1833) | merged; head `c2646103db53b41f7ed1a4ceba2b0375c7325ae7`; merge `86028996dbece473cda25b2fa2b97267ffd4739e`; v1.14 | handover, calibration, device passports, shared stack, maintenance/recall, robot test, human takeover and non-AI equivalent | `OCCUPIED_TERRITORY`; shared physical stack partial |
| [#1805 Jing-Zhang Playtest Commons](https://github.com/open-city-ai/haidian/pull/1805) | open; head `3bf25f613de81dbdf28a13dc5a390edd893b21a9` | closest collision: citywide public AI co-testing infrastructure, low-speed loop, interoperability, shared standards workshop, charging/maintenance, disconnectable sockets, public observation and failure records | `PARTIALLY_OCCUPIED`; severe kernel pressure |
| [#1866 Intelligent Mobility Loop](https://github.com/open-city-ai/haidian/pull/1866) | open; head `2b90b9420599754023bdc66841e1065fa6f0051b` | low-speed robots, fixed nodes, charging/maintenance modules, remote stop, human takeover, minimum event log and controlled test | `OCCUPIED_TERRITORY` |
| [#1869 Programmable City / Urban OS](https://github.com/open-city-ai/haidian/pull/1869) | open; head `9bc3024eb8241f743dc6ec84fb8a9c39b8116a49` | event-driven city OS, protocols/version/rollback, task space, reconfigurable space, minimum data and human arbitration | `OCCUPIED_TERRITORY` |
| [#1893 Jingzhang Open Source Station](https://github.com/open-city-ai/haidian/pull/1893) | open; head `fa07770c76f2da2f56720ca394f2bd3255091734`; v0.1 | small public stations, open services/test kit, human content review, offline downgrade, spares/OPEX and pilot-before-copy | `PARTIALLY_OCCUPIED` |
| [#1851 京张归药线](https://github.com/open-city-ai/haidian/pull/1851) | open; head `8adb729281b6cbbcf6b41306093e0f5fcafc9c76` | task constraint → minimum event ledger → modular logistics → human handoff → offline recovery | `PARTIALLY_OCCUPIED`; shows task inversion alone is not unique |
| [#1870 MEND Corridor](https://github.com/open-city-ai/haidian/pull/1870) | merged during run; audited head `30c6daa877244f34439633b2bde51ece5fa14990`; v0.4 | maintenance/care contract, minimum data, edge compute, reversible components, 90-day pilot, stop/recovery/AI-off and spatial recovery | `PARTIALLY_OCCUPIED` |

## OCCUPIED_TERRITORY

- Agent, Urban LLM, city OS and digital twin;
- public AI/robot testbeds;
- AI spine with three nodes/cores;
- open platform, commons and generic shared interfaces;
- reassembly, reconfiguration, modularity and reversible pilots;
- fallback, rollback, human handover and red-card stops;
- maintenance, repair, recall and service nodes;
- charging, edge compute and robot hubs;
- minimum data and bounded sensing as standalone principles;
- heritage railway plus AI innovation corridor.

## PARTIALLY_OCCUPIED

- cross-vendor shared physical support for changing heterogeneous machines;
- shared charging, payload/tool exchange, maintenance, isolation and recovery;
- task-driven physical resource allocation;
- compatibility, contention and degraded allocation;
- forcing those contracts into land, ground-floor, service-edge and public/back-of-house decisions.

`#1805` is the strongest direct pressure because it already combines common sockets, co-testing, interoperability, standards workshop, charging/maintenance, disconnection and public failure evidence.

The end-of-run delta adds another occupied edge: Jingzhang Full Cost's exact proposal blob `739ae8e1fe9330ae7ba4f81b7fd33c260c97adbf` makes labour/maintenance, lifecycle resources, exit budget, spatial recovery and a reproducible 24-case synthetic stop audit first-class. These are useful C01 disciplines but no longer differentiators.

## POTENTIALLY_DISTINCT

Only the joined kernel may remain:

1. reproducible inversion from public task/state/error/TTL to a minimum sensing/compute/energy/tool/maintenance bundle;
2. cross-vendor physical support with an explicit compatibility/non-shareability matrix;
3. deterministic allocation with capacity, contention, isolation and degraded modes;
4. unavoidable spatial consequences in adaptable ground floors, service edges, maintenance backs and reversible phasing;
5. three non-interchangeable key-area roles.

Items 1–3 form the potential technical kernel. Items 4–5 are the necessary urban-design proof, not separate novelty claims.

## FALSE_DIFFERENTIATORS

```text
Agent
robot
digital twin
fallback / rollback
reconfiguration / reassembly
minimum sensing
charging or service hub
open platform / commons
testbed / proving ground
heritage spine
three differentiated areas
modular / reversible infrastructure
```

## C01_UNIQUE_KERNEL

At most four linked propositions are admissible:

1. task-requirement inversion;
2. cross-vendor shared physical substrate;
3. deterministic shared-resource allocation and isolation;
4. resulting land/building/street/public-space consequences.

## Kill pressure

The visible C01 narrative is largely occupied, especially by #1805, #1811, #1817, #1833, #1809 and #1869. If shared infrastructure is removed, the spine/three areas/AI governance/test/fallback scheme still reads as a generic AI belt. The local prototype uses synthetic compatibility and demand; it cannot prove real interface standards, capacity, maintenance labour, insurance/safety or site benefit.

```text
C01_KILL_PRESSURE=CRITICAL
```

C01 is defensible only if the complete chain is demonstrated:

```text
task → requirement inversion
+ heterogeneous physical common substrate
+ explicit allocation / isolation / degraded modes
+ unavoidable and beneficial spatial consequences
```

## Evidence still absent

- cross-vendor interface and safety evidence;
- task volumes, peak timing and spatial travel distances;
- energy, curb, building and maintenance capacity;
- labour, operator, insurance and certification boundaries;
- proof of implemented shared physical infrastructure in this context.
