import unittest
from sprint import SprintVelocityCalculator  # Ensure this import matches the name of your script

class TestSprintVelocityCalculator(unittest.TestCase):

    def test_calculate_average_velocity_with_points(self):
        """Test that the average velocity is correctly calculated from sprint points."""
        calculator = SprintVelocityCalculator()
        calculator.points_list = [10, 20, 30]  # Example sprint points
        expected_average = 20  # Expected average velocity
        self.assertEqual(calculator.calculate_average_velocity(), expected_average, "The calculated average velocity should match the expected value.")

    def test_calculate_average_velocity_without_points(self):
        """Test that the average velocity is 0 when no sprint points are provided."""
        calculator = SprintVelocityCalculator()
        # No sprint points added to points_list
        expected_average = 0  # Expected average velocity with no points
        self.assertEqual(calculator.calculate_average_velocity(), expected_average, "The calculated average velocity should be 0 when no points are provided.")

if __name__ == '__main__':
    unittest.main()
