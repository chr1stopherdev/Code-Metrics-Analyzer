import unittest
from core.metrics import calculate_metrics

class TestMetrics(unittest.TestCase):
    def test_calculate_metrics(self):
        project_path = "sample_project" # project sample
        metrics = calculate_metrics(project_path)
        self.assertGreater(metrics['total_files'], 0)
        self.assertGreater(metrics['total_lines'], 0)
        self.assertGreaterEqual(metrics['comment_lines'], 0)

if __name__ == "__main__":
    unittest.main()
