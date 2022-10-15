class Vehicle:
    """This is my Vehicle class."""
    def __init__(self, max_speed, mileage):
        # Atrributes of class Vehicle
        self.max_speed = max_speed
        self.mileage = mileage

kcar = Vehicle(500, 180)
print(kcar.max_speed, kcar.mileage)