# Exercise 69: Compute a class attribute based on other attributes.
class Circle:
pi = 3.14159

def __init__(self, radius):
self.radius = radius

@classmethod
def unit_area(cls):
return cls.pi * (1 ** 2)

print("Area of a unit circle:", Circle.unit_area())
