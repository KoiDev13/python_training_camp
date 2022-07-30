class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

kbus = Bus("Khoi bus", 200, 15)
print("Bus name: " + kbus.name + "\nSpeed: " + str(kbus.max_speed) + "\nMileage: " + str(kbus.mileage ))