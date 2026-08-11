# AI and Embodied Infrastructure v0.1

This is the main technical-depth work package of Candidate 01. It must support the city design rather than dominate it.

## Layered architecture

```text
Public goals / service requirements
        ↓
Human governance + service owners
        ↓
Urban Agents / planning & operations layer
        ↓
Edge / data / interoperability layer
        ↓
Sensing + public interfaces
        ↓
Robots / mobility / adaptive facilities
        ↓
Physical public realm
```

## 1. Re-Embodiment Stations

A candidate shared infrastructure type for heterogeneous physical AI services.

Potential functions:

- charging / energy exchange;
- maintenance and inspection;
- cleaning and safe storage;
- tool / payload / sensor-module exchange;
- task upload / dispatch;
- controlled staging;
- fault isolation;
- human-supervised recovery;
- public-facing transparency display where appropriate.

Design principle: one shared service infrastructure can support multiple changing tasks, reducing pressure to deploy dedicated permanent hardware for every scenario.

## 2. Know-Enough / minimum-sufficient sensing

Instead of asking “what sensors can we deploy?”, begin from a public-service requirement:

`task → required state → tolerable uncertainty → update interval / TTL → minimum information → candidate sensing combination → privacy / failure check`

Example logic for low-speed robotic passage:

Need: free-space occupancy, usable width and relative conflict state.  
Do not automatically need: identity, face, phone ID or long-term personal trajectory.

This principle should be demonstrated quantitatively in a few selected scenarios later; it is not yet a validated citywide standard.

## 3. Robust operation states

Every public-facing AI service should be designed for at least:

- `NORMAL` — service meets evidence and operating requirements;
- `DEGRADED` — partial capability with narrower scope or lower speed;
- `PAUSE` — automated service suspends because required evidence/resource is unavailable;
- `HUMAN_FALLBACK` — equivalent or acceptable manual path is available;
- `RECOVERY` — explicit checks are satisfied before automation resumes.

## 4. Resource scheduling

Shared compute, sensing, service hubs and embodied platforms should be allocated by service requirement and priority rather than permanently dedicated to every use.

Candidate scheduling dimensions:

- time of day;
- crowding / public-space priority;
- service criticality;
- robot/tool compatibility;
- charging/maintenance state;
- sensing confidence;
- human-supervision capacity.

## 5. Interoperability

Avoid vendor-locked physical urban infrastructure where possible. Future detailed work should define open interface contracts for:

- task handoff;
- service-state reporting;
- safety/fallback status;
- energy/charging compatibility;
- public data disclosure;
- logs required for human review.

## Owner technical contribution track

The project owner can make a genuine non-generic contribution by leading four technical packages:

- **WP-A:** city AI / embodied-infrastructure systems architecture;
- **WP-B:** re-embodiment station functional architecture and resource interfaces;
- **WP-C:** sensing-requirement inversion for selected scenarios;
- **WP-D:** robust scheduling and normal/degraded/fallback logic.

These packages should eventually produce reproducible diagrams, requirement tables and small simulations rather than remain narrative claims.
