from test import Elevator


class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom,top))


    def run_elevator(self, elevator_num, floor):
        print(f'Elevator {elevator_num} is moving')
        self.elevators[elevator_num - 1].go_to_floor(floor)