"""Deterministic synthetic falsification model for C01 shared infrastructure.

This is not a site model, a performance forecast, or an optimizer for deployment.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path


EVIDENCE_LABELS = ["SYNTHETIC", "NOT_SITE_CALIBRATED", "NOT_PERFORMANCE_EVIDENCE"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sensor_covers(sensor: dict, need: dict) -> bool:
    capability = sensor["states"].get(need["state"])
    return bool(
        capability
        and capability["max_error"] <= need["max_error"]
        and capability["update_seconds"] <= need["ttl_seconds"]
    )


def minimum_sensor_bundle(task: dict, sensors: dict, privacy_weight: float) -> dict:
    names = sorted(sensors)
    feasible = []
    for size in range(1, len(names) + 1):
        for bundle in itertools.combinations(names, size):
            if all(any(sensor_covers(sensors[name], need) for name in bundle) for need in task["state_needs"]):
                privacy = sum(sensors[name]["privacy_cost"] for name in bundle)
                if privacy > task["max_bundle_privacy"]:
                    continue
                capital = sum(sensors[name]["capital_cost"] for name in bundle)
                feasible.append((capital + privacy_weight * privacy, capital, privacy, bundle))
        if feasible:
            break
    if not feasible:
        return {"status": "INFEASIBLE", "modules": [], "reason": "no bundle satisfies accuracy, TTL and privacy ceiling"}
    score, capital, privacy, bundle = min(feasible)
    return {
        "status": "FEASIBLE",
        "modules": list(bundle),
        "selection_score": round(score, 3),
        "capital_cost": round(capital, 3),
        "privacy_cost": round(privacy, 3),
        "derived_from": task["state_needs"],
    }


def compatible_platforms(task: dict, sensor_bundle: dict, platforms: dict) -> list[str]:
    required_capabilities = set(task["platform_capabilities"])
    required_tools = set(task["tools"])
    required_sensors = set(sensor_bundle["modules"])
    compatible = []
    for name, platform in platforms.items():
        if not required_capabilities.issubset(platform["capabilities"]):
            continue
        if not required_tools.issubset(platform["tools"]):
            continue
        if not required_sensors.issubset(platform["sensor_modules"]):
            continue
        compatible.append(name)
    return sorted(compatible, key=lambda name: (platforms[name]["unit_cost"], name))


def task_resource_bundle(task: dict, sensor_bundle: dict, platform: dict) -> dict[str, int]:
    bundle = dict(task["base_resources"])
    for sensor in sensor_bundle["modules"]:
        bundle[f"sensor_module:{sensor}"] = 1
    bundle[f"energy_port:{platform['energy_interface']}"] = 1
    bundle[f"maintenance_bay:{platform['maintenance_interface']}"] = task["maintenance_units"]
    for tool in task["tools"]:
        bundle[f"tool:{tool}"] = 1
    return bundle


def is_shareable(resource_spec: dict) -> bool:
    """Return whether a resource may be pooled under its declared boundary."""
    if "shareability_class" in resource_spec:
        return resource_spec["shareability_class"] != "non_shareable"
    return bool(resource_spec["shareable"])


def installed_capacity(profile: dict, task_bundles: dict, catalog: dict, shared: bool) -> dict[str, int]:
    if shared:
        by_slot: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        dedicated_only: dict[str, int] = defaultdict(int)
        for slot, counts in profile["slots"].items():
            for task_name, count in counts.items():
                for resource, units in task_bundles[task_name].items():
                    demand = count * units
                    if is_shareable(catalog[resource]):
                        by_slot[slot][resource] += demand
                    else:
                        dedicated_only[f"{resource}@{task_name}"] = max(
                            dedicated_only[f"{resource}@{task_name}"], demand
                        )
        capacity: dict[str, int] = defaultdict(int)
        for slot_demand in by_slot.values():
            for resource, demand in slot_demand.items():
                capacity[resource] = max(capacity[resource], demand)
        capacity.update(dedicated_only)
        return dict(sorted(capacity.items()))

    capacity = defaultdict(int)
    for task_name in task_bundles:
        task_peak = max(slot.get(task_name, 0) for slot in profile["slots"].values())
        for resource, units in task_bundles[task_name].items():
            capacity[f"{resource}@{task_name}"] = task_peak * units
    return dict(sorted(capacity.items()))


def catalog_entry(resource: str, catalog: dict) -> dict:
    return catalog[resource.split("@")[0]]


def strategy_metrics(
    profile: dict,
    task_bundles: dict,
    tasks: dict,
    catalog: dict,
    config: dict,
    strategy: str,
) -> dict:
    shared = strategy != "dedicated"
    capacity = installed_capacity(profile, task_bundles, catalog, shared)
    raw_capital = sum(units * catalog_entry(resource, catalog)["unit_cost"] for resource, units in capacity.items())
    footprint = sum(units * catalog_entry(resource, catalog)["footprint_units"] for resource, units in capacity.items())
    task_executions = sum(sum(slot.values()) for slot in profile["slots"].values())
    if shared:
        universal = strategy == "universal_hub"
        failure_cells = 1 if universal else config["shared_failure_cells"]
        premium = config["universal_hub_modularization_premium"] if universal else config["shared_modularization_premium"]
        capital = raw_capital * (1 + premium)
        fixed = failure_cells * config["shared_hub_fixed_cost"]
        fixed_footprint = failure_cells * config["shared_hub_footprint_units"]
        resource_users = defaultdict(set)
        for task_name, bundle in task_bundles.items():
            for resource in bundle:
                if is_shareable(catalog[resource]):
                    resource_users[resource].add(task_name)
        coordination = sum(
            max(0, len(users) - 1) * catalog[resource]["changeover_cost"]
            for resource, users in resource_users.items()
        )
        routing = task_executions * config["shared_routing_penalty_per_execution"]
        peak_weighted = max(
            sum(count * tasks[name]["criticality"] for name, count in slot.items())
            for slot in profile["slots"].values()
        )
        failure_exposure = peak_weighted / failure_cells
    else:
        capital = raw_capital
        fixed = len(task_bundles) * config["dedicated_station_fixed_cost"]
        fixed_footprint = len(task_bundles) * config["dedicated_station_footprint_units"]
        coordination = 0.0
        routing = 0.0
        failure_exposure = max(
            max(slot.get(name, 0) for slot in profile["slots"].values()) * task["criticality"]
            for name, task in tasks.items()
        )
    total = capital + fixed + coordination + routing + failure_exposure * config["failure_exposure_cost_weight"]
    return {
        "strategy": strategy,
        "installed_capacity": capacity,
        "raw_resource_capital_index": round(raw_capital, 3),
        "capital_with_modularity_index": round(capital, 3),
        "fixed_site_index": round(fixed, 3),
        "coordination_changeover_index": round(coordination, 3),
        "routing_index": round(routing, 3),
        "single_failure_exposure_weighted_tasks": round(failure_exposure, 3),
        "total_cost_risk_index": round(total, 3),
        "synthetic_footprint_units": round(footprint + fixed_footprint, 3),
        "failure_cell_count": 0 if strategy == "dedicated" else failure_cells,
        "resilience_gate": (
            "FAIL_CORRELATED_SINGLE_DOMAIN"
            if strategy == "universal_hub"
            else "PASS_IN_THIS_ABSTRACTION"
        ),
    }


def compare_profile(profile: dict, task_bundles: dict, tasks: dict, catalog: dict, config: dict) -> dict:
    dedicated = strategy_metrics(profile, task_bundles, tasks, catalog, config, strategy="dedicated")
    shared = strategy_metrics(profile, task_bundles, tasks, catalog, config, strategy="shared_distributed")
    universal = strategy_metrics(profile, task_bundles, tasks, catalog, config, strategy="universal_hub")
    delta = shared["total_cost_risk_index"] - dedicated["total_cost_risk_index"]
    economic = min(
        (dedicated, shared, universal), key=lambda item: item["total_cost_risk_index"]
    )["strategy"]
    return {
        "A_dedicated": dedicated,
        "B_shared_distributed": shared,
        "C_universal_hub": universal,
        "B_minus_A_total_index": round(delta, 3),
        "lower_index_strategy": "B_SHARED_DISTRIBUTED" if delta < 0 else "A_DEDICATED" if delta > 0 else "TIE",
        "economic_lower_index_including_inadmissible": economic,
        "universal_hub_admission": "FAIL_CORRELATED_SINGLE_DOMAIN",
        "interpretation": (
            "Distributed pooling beats duplication under this demand timing and the stated synthetic penalties."
            if delta < 0
            else "Coincidence, modular overhead and shared failure exposure erase the distributed-pooling benefit under this profile."
        ),
    }


def evaluate_failure_modes(data: dict) -> dict:
    results = {}
    for failure, actions in data["degraded_modes"].items():
        automated_withheld = 0
        human_or_local_continuity = 0
        task_results = {}
        for task, action in actions.items():
            withheld = action in {"PAUSE", "CONTINUE_MANUAL", "CONTINUE_LOCAL_LOGGING", "REDUCE_TO_HUMAN_INSPECTION"}
            continuity = action in {
                "CONTINUE_MANUAL", "CONTINUE_LOCAL_LOGGING", "REDUCE_TO_HUMAN_INSPECTION",
                "PRIORITIZE_SAFE_RECOVERY", "REDUCE_AND_REROUTE", "QUEUE_FOR_HUMAN_OPERATOR",
            }
            automated_withheld += int(withheld)
            human_or_local_continuity += int(continuity)
            task_results[task] = {
                "action": action,
                "automated_allocation": "WITHHELD" if withheld else "LIMITED_OR_ISOLATED",
                "ordinary_service_continuity": "HUMAN_OR_LOCAL" if continuity else "PAUSED_OR_RESTRICTED",
            }
        results[failure] = {
            "tasks": task_results,
            "automated_withheld_task_count": automated_withheld,
            "human_or_local_continuity_task_count": human_or_local_continuity,
            "required_spatial_response": data["failure_spatial_responses"][failure],
        }
    return results


def run(data: dict) -> dict:
    tasks = data["task_families"]
    sensor_choices = {
        name: minimum_sensor_bundle(task, data["sensors"], data["model_config"]["privacy_weight"])
        for name, task in tasks.items()
    }
    matrix = {}
    task_bundles = {}
    for name, task in tasks.items():
        platforms = compatible_platforms(task, sensor_choices[name], data["platforms"])
        if not platforms:
            raise ValueError(f"No compatible platform for {name}")
        chosen = platforms[0]
        matrix[name] = {"compatible_platforms": platforms, "selected_lowest_unit_cost": chosen}
        task_bundles[name] = task_resource_bundle(task, sensor_choices[name], data["platforms"][chosen])

    comparisons = {
        name: compare_profile(profile, task_bundles, tasks, data["resource_catalog"], data["model_config"])
        for name, profile in data["demand_profiles"].items()
    }
    degraded = evaluate_failure_modes(data)

    shareability = {
        name: {
            "resource_class": spec["resource_class"],
            "shareability_class": spec["shareability_class"],
            "shareable": is_shareable(spec),
            "reason": spec["shareability_reason"],
        }
        for name, spec in data["resource_catalog"].items()
    }
    compatibility_by_class = defaultdict(list)
    for name, spec in shareability.items():
        compatibility_by_class[spec["shareability_class"]].append(name)
    return {
        "evidence_status": EVIDENCE_LABELS,
        "model_purpose": "falsify the structural logic of shared modular infrastructure; not forecast deployment",
        "minimum_sensing_from_task_requirements": sensor_choices,
        "task_platform_compatibility_matrix": matrix,
        "derived_task_resource_bundles": task_bundles,
        "resource_shareability": shareability,
        "resource_compatibility_classes": {
            key: sorted(values) for key, values in sorted(compatibility_by_class.items())
        },
        "strategy_comparisons": comparisons,
        "universal_station_test": {
            "result": "DELETE_AS_CITYWIDE_TYPE",
            "reason": "A single pooled domain can be economically compact under some synthetic profiles but fails the correlated-failure admission gate.",
            "retained_pattern": "distributed service cells + selected specialised backends + lightweight public accountability interfaces",
        },
        "failure_isolation": {
            "dedicated": "one station failure is bounded to one task family in this abstraction",
            "shared": f"one cell failure affects tasks routed through roughly 1/{data['model_config']['shared_failure_cells']} of the pooled system",
            "design_requirement": "shared infrastructure must be split into isolatable cells with manual recovery; a single central mega-hub is rejected",
        },
        "degraded_modes": degraded,
        "conclusions": [
            "The shared object is a bounded set of compatible compute, energy, generic/special sensing, tooling, general maintenance, storage, cleaning, isolation and accountability resources—not every resource.",
            "Assistive contact tools, hazardous tooling, hygiene/contamination stores and safety-specific supervision remain segregated even when co-located.",
            "Distributed shared modular capacity can reduce duplication when peaks are staggered, but can be worse during coincident peaks after modular, routing and failure penalties.",
            "Task requirements can eliminate sensors that exceed accuracy/TTL needs or the privacy ceiling; more sensing is not automatically preferred.",
            "A universal station creates unacceptable correlated loss even when its synthetic cost index is attractive; spatial distribution and safe manual recovery are core urban requirements.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="synthetic_inputs.json")
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    result = run(load_json(Path(args.input)))
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
