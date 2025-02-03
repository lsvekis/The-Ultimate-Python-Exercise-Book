# Exercise 16: Define a method that calculates the area of a rectangle.
class Rectangle:
def __init__(self, width, height):
self.width = width
self.height = height

def area(self):
return self.width * self.height

rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
