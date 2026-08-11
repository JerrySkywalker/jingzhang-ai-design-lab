# C02 Ordinary-Day Completeness Experiment

This standard-library, deterministic experiment tests the logic of the `NEIGHBOURHOOD_COMPLETENESS_CONTRACT`. It does not use real population, facility, opening-hour, route or catchment data.

```text
SYNTHETIC
NOT_SITE_CALIBRATED
NOT_AVAILABILITY_EVIDENCE
```

## Reproduce

```powershell
python model.py --input synthetic_inputs.json --output results.json
python -m unittest discover -s tests -v
```

The inputs define eight required personas, seven operating states and three deliberately different synthetic urban units. The evaluator checks each need against physical service tags, time availability, accessibility, non-digital access, weather protection, event displacement, a closed facility and local/external status.

The experiment does not compute travel time or a score. A real C02 test requires cleared geometry, facility and hours evidence, accessible-route observation, operating responsibility and professional spatial analysis.
