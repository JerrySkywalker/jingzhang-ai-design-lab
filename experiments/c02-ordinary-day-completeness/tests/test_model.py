import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model import load, run  # noqa: E402


class CompletenessContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run(load(ROOT / "synthetic_inputs.json"))

    def test_all_required_personas_are_present(self):
        self.assertEqual(len(self.result["tested_personas"]), 8)

    def test_all_required_states_are_present(self):
        self.assertEqual(len(self.result["tested_states"]), 7)

    def test_redundant_mixed_unit_passes(self):
        self.assertTrue(self.result["unit_results"]["redundant_mixed_unit"]["contract_pass"])

    def test_workday_enclave_fails_evening_and_weekend(self):
        failed = self.result["unit_results"]["workday_innovation_enclave"]["failed_states"]
        self.assertIn("evening", failed)
        self.assertIn("weekend", failed)

    def test_external_federation_is_not_local_completeness(self):
        result = self.result["unit_results"]["federation_dependent_unit"]
        self.assertFalse(result["contract_pass"])
        self.assertIn("shared_remote_civic_hub", result["external_services_present"])

    def test_digital_outage_exposes_enclave(self):
        state = self.result["unit_results"]["workday_innovation_enclave"]["scenario_results"]["digital_service_unavailable"]
        self.assertFalse(state["pass"])


if __name__ == "__main__":
    unittest.main()
