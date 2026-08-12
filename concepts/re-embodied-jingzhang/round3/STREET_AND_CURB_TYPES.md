# Street and Curb Types

## Priority rule

The street system remains an ordinary human city when AI and embodied services are absent. No platform may negotiate away a missing sidewalk, inaccessible crossing, unsafe loading conflict, shade deficit, drainage route or emergency access.

## Types

| Type | Ordinary role | C01 layer | Allowed operation | Prohibited operation |
|---|---|---|---|---|
| S0 public/heritage priority path | walking, wheeling, cycling where appropriate, heritage, shade, refuge, daily stay | accountability/learning only | human help, static status, occasional escorted demonstration | routine logistics, charging, repair, broken-device holding, exclusive robot lane |
| S1 conventional service street/court | goods, waste, building maintenance, emergency/service access | manual recovery baseline | ordinary loading and staff recovery | technology displacing existing safe service or egress |
| S2 managed short-stay edge | accessible pick-up, delivery/visitor handoff, short loading | capped embodied handoff after audit | time windows, marked holding, operator present, human alternative | permanent reservation, uncontrolled queue, curb spill into foot/cycle path |
| S3 controlled technical yard | workshop logistics, calibration, incident isolation | heavy/specialised backend | segregated test/recovery, independent shutdown, technician circulation | public-through route, open event crowd, ecological/drainage occupation |
| S4 temporary event overlay | ordinary plaza/civic forecourt with authorised event | removable module/steward desk | setup/event/closeout windows; conventional evacuation remains | permanent equipment, automated crowd command, blocked refuge or service access |

## Section invariants

Every proposed edge must show:

1. pedestrian/wheelchair clear route and physical separation;
2. cycle relationship;
3. shade/rain refuge that remains public;
4. drainage/tree-root/soil boundary;
5. ordinary loading/waste/emergency route;
6. platform arrival, queue cap and safe stop;
7. manual recovery path;
8. staff position and non-AI service;
9. event mode and normal mode;
10. closure when a cell, power, network or operator is unavailable.

## Stress states

- **AI off:** S0–S2 retain ordinary functions; technical markings read as normal loading/accessible pick-up, not dead robot furniture.
- **80% lower adoption:** no continuous curb is reserved; removable signs/ports leave.
- **peak:** excess demand is queued off-street or refused; pedestrian/green/refuge space is never overflow capacity.
- **cell failure:** affected device moves by human recovery to S1/S3; no repair on S0.
- **rain/heat:** shade/refuge and drainage operate before service; equipment may close.
- **event:** S4 is temporary and cannot consume emergency or ordinary service continuity.
- **maintenance:** waste, wash and staff access use ordinary service routes; public frontage stays clean/quiet.

## Common-base boundary

OSM streets reveal contextual connections and candidate service-edge questions. They do not prove sidewalks, curb regulations, gradients, crossings, access rights or loading capacity. Each S-type is therefore a typology for transport/field review, not an assigned street segment.
