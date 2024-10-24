class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor  # lowest floor number
        self.top_floor = top_floor  # highest floor number
        self.current_floor = bottom_floor  # elevator starts at the bottom floor

    def go_to_floor(self, target_floor):
        """Move the elevator to the specified floor."""
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Error: Floor {target_floor} is out of range.")
            return

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

    def floor_up(self):
        """Move the elevator up one floor."""
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up: now on floor {self.current_floor}")
        else:
            print("Already on the top floor.")

    def floor_down(self):
        """Move the elevator down one floor."""
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down: now on floor {self.current_floor}")
        else:
            print("Already on the bottom floor.")


# Test the Elevator class in the main program
if __name__ == "__main__":
    # Create an elevator that can go between floors 1 and 10
    elevator = Elevator(1, 10)

    # Move to the 5th floor
    print("Moving to floor 5:")
    elevator.go_to_floor(5)

    # Move back to the bottom floor
    print("\nMoving back to the bottom floor:")
    elevator.go_to_floor(1)


