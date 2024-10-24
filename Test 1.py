class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f"Car(Registration: {self.registration_number}, Max Speed: {self.max_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km)"

# Main program
my_car = Car("ABC-123", 142)

# Print out all properties of the new car
print(my_car)
