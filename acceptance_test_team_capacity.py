class TeamMember:
    def __init__(self, daily_hours, pto_hours, ceremony_hours):
        self.daily_hours = daily_hours
        self.pto_hours = pto_hours
        self.ceremony_hours = ceremony_hours

class TeamCapacityCalculator:
    def __init__(self, sprint_days):
        self.team_members = []
        self.sprint_days = sprint_days

    def add_team_member(self, daily_hours, pto_days, ceremony_hours):
        self.team_members.append(TeamMember(daily_hours, pto_days, ceremony_hours))

    def calculate_individual_capacity(self, team_member):
        return team_member.daily_hours * (self.sprint_days - team_member.pto_hours) - team_member.ceremony_hours

    def calculate_team_capacity(self):
        return sum(self.calculate_individual_capacity(member) for member in self.team_members)

    def display_team_and_individual_capacity(self):
        print(f"\nTotal Team Capacity: {self.calculate_team_capacity()} effort-hours")
        for i, member in enumerate(self.team_members, start=1):
            print(f"Member {i} Capacity: {self.calculate_individual_capacity(member)} effort-hours")

def acceptance_test():
    # Setup
    sprint_days = 10
    calculator = TeamCapacityCalculator(sprint_days)

    # Test data
    team_members_data = [
        (8, 2, 4),  # Member 1
        (7, 0, 3)   # Member 2
    ]
    
    # Expected results
    expected_individual_capacities = [60, 67]  # Calculated based on the test data
    expected_total_capacity = sum(expected_individual_capacities)

    # Execution
    for daily_hours, pto_days, ceremony_hours in team_members_data:
        calculator.add_team_member(daily_hours, pto_days, ceremony_hours)

    # Verification
    actual_total_capacity = calculator.calculate_team_capacity()
    actual_individual_capacities = [calculator.calculate_individual_capacity(member) for member in calculator.team_members]
    
    assert actual_total_capacity == expected_total_capacity, "Total capacity does not match the expected result."
    assert actual_individual_capacities == expected_individual_capacities, "Individual capacities do not match the expected results."
    
    # Display the result
    calculator.display_team_and_individual_capacity()
    print("\nACCEPTANCE TEST PASSED: All capacities match the expected results.")

if __name__ == "__main__":
    acceptance_test()
