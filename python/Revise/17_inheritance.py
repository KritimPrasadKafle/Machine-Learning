class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

c = Car()
m = MotorCycle()
print(c.general_usage())
print(issubclass(Car, MotorCycle))
print(issubclass(Vehicle, MotorCycle))