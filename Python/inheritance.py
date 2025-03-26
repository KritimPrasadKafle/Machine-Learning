# class Vehicle:
#     def general_usage(self):
#         print("general use : transportation")
#
# class Car(Vehicle):
#     def __init__(self):
#         print("I'm a car")
#         self.wheels = 4
#         self.has_roof = True
#
#     def specific_usage(self):
#         print("specific use: commute to work, vacation with family")
#
# class MotorCycle(Vehicle):
#     def __init__(self):
#         print("I'm motor cycle")
#         self.wheels = 4
#         self.has_roof = True
#
#     def specific_usage(self):
#         print("specific use : road trip, racing")
#
# c = Car()
# c.general_usage()
# c.specific_usage()
#
# m = MotorCycle()
# m.general_usage()
# m.specific_usage()

class father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(father, Mother):
    def sports(self):
        print("I enjoy sports")

c = Child()
c.gardening()
c.cooking()
c.sports()