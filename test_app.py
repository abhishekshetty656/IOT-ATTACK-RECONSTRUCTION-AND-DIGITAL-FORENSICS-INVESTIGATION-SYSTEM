import unittest
from app import calculate_risk_score


class TestRiskScore(unittest.TestCase):

    def test_high_severity(self):
        self.assertEqual(calculate_risk_score(9, 0.9), 81.0)

    def test_low_severity(self):
        self.assertEqual(calculate_risk_score(2, 0.5), 10.0)

    def test_invalid_severity(self):
        with self.assertRaises(ValueError):
            calculate_risk_score(11, 0.5)

    def test_invalid_confidence(self):
        with self.assertRaises(ValueError):
            calculate_risk_score(5, 1.5)


if __name__ == "__main__":
    unittest.main()
