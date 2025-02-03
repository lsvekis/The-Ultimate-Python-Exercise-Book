# Exercise 12: Use default values for instance attributes.
class Car:
def __init__(self, brand="Toyota", model="Corolla"):
self.brand = brand
self.model = model

car1 = Car()
car2 = Car("Honda", "Civic")
print("Car 1:", car1.brand, car1.model)
print("Car 2:", car2.brand, car2.model)
