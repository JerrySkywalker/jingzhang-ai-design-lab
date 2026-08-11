"""Synthetic, deterministic ordinary-day completeness contract evaluator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LABELS = ["SYNTHETIC", "NOT_SITE_CALIBRATED", "NOT_AVAILABILITY_EVIDENCE"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def eligible(service: dict, persona: dict, need: dict, scenario: dict) -> bool:
    if need["tag"] not in service["provides"]:
        return False
    if not service["availability"].get(scenario["time_state"], False):
        return False
    if scenario.get("closed_facility") == service["facility"]:
        return False
    if scenario.get("event_day") and service.get("event_displaced", False):
        return False
    if (persona["requires_accessible"] or need.get("requires_accessible")) and not service["accessible"]:
        return False
    if scenario.get("digital_unavailable") and not service["non_digital"]:
        return False
    if scenario.get("weather_stress") and need.get("exposure_sensitive") and not service["weather_protected"]:
        return False
    if need.get("must_be_local", True) and service["external_dependency"]:
        return False
    return True


def evaluate_unit(unit: dict, personas: dict, scenarios: dict) -> dict:
    scenario_results = {}
    for scenario_name, scenario in scenarios.items():
        persona_results = {}
        for persona_name, persona in personas.items():
            need_results = []
            for need in persona["ordinary_day_needs"]:
                matches = [
                    service["id"]
                    for service in unit["services"]
                    if eligible(service, persona, need, scenario)
                ]
                need_results.append(
                    {
                        "need": need["name"],
                        "service_tag": need["tag"],
                        "pass": bool(matches),
                        "eligible_places": matches,
                    }
                )
            failed_needs = [item["need"] for item in need_results if not item["pass"]]
            persona_results[persona_name] = {
                "pass": not failed_needs,
                "failed_needs": failed_needs,
            }
        failed_personas = [name for name, result in persona_results.items() if not result["pass"]]
        scenario_results[scenario_name] = {
            "pass": not failed_personas,
            "failed_personas": failed_personas,
            "failures": {
                name: result["failed_needs"]
                for name, result in persona_results.items()
                if result["failed_needs"]
            },
            "need_checks": sum(len(persona["ordinary_day_needs"]) for persona in personas.values()),
        }
    external_services = [service["id"] for service in unit["services"] if service["external_dependency"]]
    failed_states = [name for name, result in scenario_results.items() if not result["pass"]]
    return {
        "contract_pass": not failed_states,
        "failed_states": failed_states,
        "external_services_present": external_services,
        "scenario_results": scenario_results,
    }


def run(data: dict) -> dict:
    units = {
        name: evaluate_unit(unit, data["personas"], data["scenarios"])
        for name, unit in data["synthetic_units"].items()
    }
    return {
        "evidence_status": LABELS,
        "contract_rule": "all eight personas must complete every required local service chain in every tested state; a score average cannot hide one excluded role or failed state",
        "tested_personas": list(data["personas"]),
        "tested_states": list(data["scenarios"]),
        "unit_results": units,
        "interpretation": [
            "A workday programme mix is not an ordinary-day complete neighbourhood.",
            "A nearby or digitally reachable service remains an external dependency until physical, time-of-day and non-digital access are evidenced.",
            "One-facility and digital outages expose false completeness hidden by normal weekday conditions.",
            "The contract is a gate, not proof that any real Jing-Zhang area passes.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="synthetic_inputs.json")
    parser.add_argument("--output", default="results.json")
    args = parser.parse_args()
    Path(args.output).write_text(
        json.dumps(run(load(Path(args.input))), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
