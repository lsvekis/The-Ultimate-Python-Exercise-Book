# Exercise 47: Update the mileage attribute with an instance method.
class Car:
def __init__(self, make, model, mileage=0):
self.make = make
self.model = model
self.mileage = mileage

def drive(self, miles):
self.mileage += miles

car = Car("Honda", "Accord")
car.drive(50)
print("New mileage:", car.mileage)
