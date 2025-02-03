# Exercise 88: Define a multi-level inheritance structure.
class Vehicle:
def __init__(self, brand):
self.brand = brand

class Car(Vehicle):
def drive(self):
return "Driving"

class ElectricCar(Car):
def charge(self):
return "Charging"

ec = ElectricCar("Tesla")
print(ec.brand, "-", ec.drive(), "and", ec.charge())
