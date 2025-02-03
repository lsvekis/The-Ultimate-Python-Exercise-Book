# Exercise 100: Create a list of different shapes and call their area() methods.
class Shape:
def area(self):
raise NotImplementedError("Must implement area")

class Rectangle(Shape):
def __init__(self, width, height):
self.width = width
self.height = height

def area(self):
return self.width * self.height

class Circle(Shape):
def __init__(self, radius):
self.radius = radius

def area(self):
import math
return math.pi * (self.radius ** 2)

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
print(f"Area: {shape.area():.2f}")
