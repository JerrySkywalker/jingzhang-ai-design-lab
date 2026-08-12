import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model import load_json, run  # noqa: E402


class SharedInfrastructureModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run(load_json(ROOT / "synthetic_inputs.json"))

    def test_evidence_labels_are_explicit(self):
        self.assertEqual(
            self.result["evidence_status"],
            ["SYNTHETIC", "NOT_SITE_CALIBRATED", "NOT_PERFORMANCE_EVIDENCE"],
        )

    def test_task_inversion_does_not_choose_camera_for_delivery(self):
        bundle = self.result["minimum_sensing_from_task_requirements"]["low_speed_delivery"]
        self.assertEqual(bundle["modules"], ["lidar_local"])

    def test_staggered_profile_can_favour_sharing(self):
        comparison = self.result["strategy_comparisons"]["staggered_ordinary_day"]
        self.assertEqual(comparison["lower_index_strategy"], "B_SHARED_DISTRIBUTED")

    def test_coincident_peak_can_favour_dedicated(self):
        comparison = self.result["strategy_comparisons"]["coincident_event_peak"]
        self.assertEqual(comparison["lower_index_strategy"], "A_DEDICATED")

    def test_human_contact_tool_is_not_shared(self):
        entry = self.result["resource_shareability"]["tool:assistive_contact_tool"]
        self.assertFalse(entry["shareable"])

    def test_degraded_compute_pauses_automated_delivery(self):
        action = self.result["degraded_modes"]["edge_compute_slot_unavailable"]["tasks"]["low_speed_delivery"]
        self.assertEqual(action["action"], "PAUSE")
        self.assertEqual(action["automated_allocation"], "WITHHELD")

    def test_all_required_demand_patterns_are_present(self):
        required = {
            "staggered_ordinary_day",
            "coincident_event_peak",
            "weekday_baseline",
            "event_day",
            "failure_recovery",
            "low_demand_future",
            "high_demand_future",
        }
        self.assertTrue(required.issubset(self.result["strategy_comparisons"]))

    def test_four_compatibility_classes_are_explicit(self):
        self.assertEqual(
            set(self.result["resource_compatibility_classes"]),
            {"fully_shareable", "time_shareable", "shareable_with_isolation", "non_shareable"},
        )

    def test_universal_station_fails_correlated_failure_gate(self):
        self.assertEqual(
            self.result["universal_station_test"]["result"],
            "DELETE_AS_CITYWIDE_TYPE",
        )
        for comparison in self.result["strategy_comparisons"].values():
            self.assertEqual(comparison["universal_hub_admission"], "FAIL_CORRELATED_SINGLE_DOMAIN")

    def test_low_demand_future_can_favour_dedicated_reuse(self):
        comparison = self.result["strategy_comparisons"]["low_demand_future"]
        self.assertEqual(comparison["lower_index_strategy"], "A_DEDICATED")

    def test_failure_matrix_covers_required_failures(self):
        required = {
            "one_shared_failure_cell_unavailable",
            "power_constrained",
            "network_unavailable",
            "shared_resource_contamination",
            "operator_capacity_exceeded",
        }
        self.assertTrue(required.issubset(self.result["degraded_modes"]))


if __name__ == "__main__":
    unittest.main()
