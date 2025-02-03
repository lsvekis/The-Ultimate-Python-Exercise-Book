# Exercise 97: Override a method completely in the subclass.
class Vehicle:
def start(self):
return "Vehicle starting..."

class Bike(Vehicle):
def start(self):
return "Bike starting with a kick!"

b = Bike()
print(b.start())
