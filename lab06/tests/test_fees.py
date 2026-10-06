"""Check every example in REQUIREMENTS.md against its exact expected fee."""

import unittest

from fees import late_fee


class LateFeeTests(unittest.TestCase):
    def test_ac1_on_time_costs_zero(self):
        self.assertEqual(late_fee(0), 0)

    def test_ac2_one_minute_late_costs_two(self):
        self.assertEqual(late_fee(1), 2)

    def test_ac2_exactly_one_day_late_costs_two(self):
        self.assertEqual(late_fee(1440), 2)

    def test_ac2_one_day_and_one_minute_late_costs_four(self):
        self.assertEqual(late_fee(1441), 4)

    def test_ac3_thirty_days_late_is_capped_at_twenty(self):
        self.assertEqual(late_fee(43200), 20)


if __name__ == "__main__":
    unittest.main()
