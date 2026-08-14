# Class Vehicle

class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

modelx = Vehicle(209,18)
print("The max speed is ",modelx.maxspeed)
print("The Mileage is ",modelx.mileage)