import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "build_context.py"
SPEC = importlib.util.spec_from_file_location("build_context", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ContextBuildTests(unittest.TestCase):
    def test_classification_is_explicit_and_non_exclusive(self):
        layers = MODULE.classify({"amenity": "university", "building": "university"})
        self.assertEqual(layers, {"daily_life", "innovation", "buildings"})

    def test_contextual_anchor_distance_matches_issue_scale(self):
        anchors = MODULE.contextual_anchors("2026-08-12")
        station = MODULE.feature_by_id(anchors, "CTX-ANCHOR-DAZHONGSI-STATION")
        distance = MODULE.haversine_m((116.34850, 39.94692), tuple(station["geometry"]["coordinates"]))
        self.assertGreater(distance, 2200)
        self.assertLess(distance, 2310)

    def test_geojson_writer_round_trips_utf8(self):
        payload = MODULE.contextual_anchors("2026-08-12")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "anchors.geojson"
            MODULE.write_json(path, payload)
            parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(parsed["type"], "FeatureCollection")
        self.assertEqual(len(parsed["features"]), 3)

    def test_required_output_names_are_stable(self):
        expected = {
            "01-scope-context.svg",
            "02-transit-and-rail-context.svg",
            "03-public-services-and-daily-life-context.svg",
            "04-green-water-open-space-context.svg",
            "05-research-innovation-context.svg",
            "06-key-area-context-warning.svg",
        }
        self.assertEqual(len(expected), 6)


if __name__ == "__main__":
    unittest.main()
