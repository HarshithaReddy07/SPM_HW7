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



class TeamMember:
    """
    Represents a single team member, storing their availability and commitments.
    """
    def __init__(self, daily_hours, pto_hours, ceremony_hours):
        """
        Initializes a TeamMember with their daily available hours, PTO hours, and ceremony hours.

        Parameters:
            daily_hours (int): Daily available hours for the sprint.
            pto_hours (int): Hours taken off as PTO during the sprint.
            ceremony_hours (int): Hours committed to ceremonies during the sprint.
        """
        self.daily_hours = daily_hours
        self.pto_hours = pto_hours
        self.ceremony_hours = ceremony_hours


class TeamCapacityCalculator:
    """
    Calculates and displays the team's total and individual member capacity in effort-hours for a sprint.
    """
    def __init__(self, sprint_days):
        """
        Initializes the TeamCapacityCalculator with sprint duration and an empty list for team members.

        Parameters:
            sprint_days (int): The number of days in the sprint.
        """
        self.team_members = []
        self.sprint_days = sprint_days

    def collect_team_capacity_data(self):
        """
        Collects and validates team member data from user input.
        """
        print("\nEnter team member details (type 'done' when finished):")
        while True:
            try:
                daily_hours_input = input("Enter daily available hours (or type 'done' to finish): ")
                if daily_hours_input.lower() == 'done':
                    break
                daily_hours = int(daily_hours_input)
                pto_days = int(input("Enter PTO days this sprint: "))
                ceremony_hours = int(input("Enter hours committed to ceremonies: "))
                self.team_members.append(TeamMember(daily_hours, pto_days, ceremony_hours))
            except ValueError:
                print("Invalid input. Please enter valid numbers or 'done' to finish.")
            except EOFError:
                break  # Allows ending input in environments like interactive notebooks

    def calculate_individual_capacity(self, team_member):
        """
        Calculates the individual capacity for a given team member.

        Parameters:
            team_member (TeamMember): The team member for whom to calculate capacity.

        Returns:
            int: The individual capacity in effort-hours for the team member.
        """
        return team_member.daily_hours * (self.sprint_days - team_member.pto_hours) - team_member.ceremony_hours

    def calculate_team_capacity(self):
        """
        Calculates the total team capacity in effort-hours for the sprint.
        
        Returns:
            int: The total effort-hours available from all team members for the sprint.
        """
        total_capacity = sum(self.calculate_individual_capacity(member) for member in self.team_members)
        return total_capacity

    def display_team_and_individual_capacity(self):
        """
        Displays the calculated team capacity and individual capacities.
        """
        print(f"\nTotal Team Capacity: {self.calculate_team_capacity()} effort-hours")
        for i, member in enumerate(self.team_members, start=1):
            print(f"Member {i} Capacity: {self.calculate_individual_capacity(member)} effort-hours")


def main():
    """
    Main function to run the program.
    """
    print("Select feature to run:\nA: Calculate Sprint Velocity\nB: Calculate Team Capacity")
    choice = input("Enter your choice (A/B): ").upper()


    if choice == 'A':
        calculator = SprintVelocityCalculator()
        calculator.collect_sprint_points()
        calculator.display_average_velocity()
    elif choice == 'B':
        sprint_days = int(input("Enter the number of sprint days: "))
        calculator = TeamCapacityCalculator(sprint_days)
        calculator.collect_team_capacity_data()
        calculator.display_team_and_individual_capacity()
    else:
        print("Invalid selection. Please choose either 'A' or 'B'.")

if __name__ == "__main__":
    main()
