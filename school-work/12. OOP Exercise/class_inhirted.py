class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        """Adding default capacity."""
        return f"The seating capacity of a {self.name} is {capacity} passengers"

kbus = Bus("Khoi bus", 200, 15)
print(kbus.seating_capacity())