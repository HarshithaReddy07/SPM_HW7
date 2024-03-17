import unittest
from sprint import TeamMember, TeamCapacityCalculator
class TestTeamCapacityCalculator(unittest.TestCase):

    def setUp(self):
        self.sprint_days = 10  # Example sprint duration

    def test_normal_capacity(self):
        """Test individual capacity calculation with typical input values."""
        member = TeamMember(daily_hours=8, pto_hours=2, ceremony_hours=4)
        calculator = TeamCapacityCalculator(self.sprint_days)
        expected_capacity = 8 * (self.sprint_days - 2) - 4
        self.assertEqual(calculator.calculate_individual_capacity(member), expected_capacity)

    def test_no_pto_capacity(self):
        """Test individual capacity calculation when no PTO is taken."""
        member = TeamMember(daily_hours=8, pto_hours=0, ceremony_hours=4)
        calculator = TeamCapacityCalculator(self.sprint_days)
        expected_capacity = 8 * self.sprint_days - 4
        self.assertEqual(calculator.calculate_individual_capacity(member), expected_capacity)

    def test_all_ceremony_no_capacity(self):
        """Test individual capacity calculation when all time is committed to ceremonies."""
        member = TeamMember(daily_hours=8, pto_hours=0, ceremony_hours=8 * self.sprint_days)
        calculator = TeamCapacityCalculator(self.sprint_days)
        expected_capacity = 0  # All time is committed to ceremonies
        self.assertEqual(calculator.calculate_individual_capacity(member), expected_capacity)

    def test_full_pto_no_capacity(self):
        """Test individual capacity calculation when PTO covers the entire sprint."""
        member = TeamMember(daily_hours=8, pto_hours=self.sprint_days, ceremony_hours=0)
        calculator = TeamCapacityCalculator(self.sprint_days)
        expected_capacity = 0  # PTO covers the entire sprint
        self.assertEqual(calculator.calculate_individual_capacity(member), expected_capacity)

if __name__ == '__main__':
    unittest.main()
