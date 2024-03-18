class SprintVelocityCalculator:
    def __init__(self):
        self.points_list = []

    def collect_sprint_points(self, test_inputs=None):
        inputs = (test_inputs or iter(lambda: input("> "), 'done'))

        print("Enter sprint points (one at a time, type 'done' to finish):")
        for input_point in inputs:
            if input_point.lower() == 'done':
                break
            try:
                self.points_list.append(int(input_point))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def calculate_average_velocity(self):
        if not self.points_list:
            return 0
        return sum(self.points_list) / len(self.points_list)

    def display_average_velocity(self):
        average_velocity = self.calculate_average_velocity()
        if average_velocity:
            print(f"Average Sprint Velocity: {average_velocity}")
        else:
            print("No sprint points were entered to calculate velocity.")

def acceptance_test():
    # Test Data
    test_inputs = ['8', '13', '21', 'done']
    expected_average_velocity = 14  # Expected result based on test inputs

    # Setup
    calculator = SprintVelocityCalculator()
    
    # Execution
    calculator.collect_sprint_points(test_inputs=test_inputs)
    calculated_average = calculator.calculate_average_velocity()

    # Verification
    if calculated_average == expected_average_velocity:
        print("ACCEPTANCE TEST PASSED: The calculated average velocity matches the expected outcome.")
    else:
        print("ACCEPTANCE TEST FAILED: The calculated average velocity does not match the expected outcome.")

    # Display the result
    calculator.display_average_velocity()

if __name__ == "__main__":
    acceptance_test()
