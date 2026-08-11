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
        self.assertEqual(comparison["lower_index_strategy"], "B_SHARED")

    def test_coincident_peak_can_favour_dedicated(self):
        comparison = self.result["strategy_comparisons"]["coincident_event_peak"]
        self.assertEqual(comparison["lower_index_strategy"], "A_DEDICATED")

    def test_human_contact_tool_is_not_shared(self):
        entry = self.result["resource_shareability"]["tool:assistive_contact_tool"]
        self.assertFalse(entry["shareable"])

    def test_degraded_compute_pauses_automated_delivery(self):
        action = self.result["degraded_modes"]["edge_compute_slot_unavailable"]["low_speed_delivery"]
        self.assertEqual(action["action"], "PAUSE")
        self.assertEqual(action["automated_allocation"], "WITHHELD")


if __name__ == "__main__":
    unittest.main()
