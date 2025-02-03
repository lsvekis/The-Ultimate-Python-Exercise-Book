# Exercise 60: Use a class method as a factory method.
class Circle:
def __init__(self, radius):
self.radius = radius

@classmethod
def unit_circle(cls):
return cls(1)

circle = Circle.unit_circle()
print("Unit circle radius:", circle.radius)
