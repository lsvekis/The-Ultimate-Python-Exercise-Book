# Exercise 17: Define a method that returns both area and perimeter.
class Rectangle:
def __init__(self, width, height):
self.width = width
self.height = height

def dimensions(self):
area = self.width * self.height
perimeter = 2 * (self.width + self.height)
return area, perimeter

rect = Rectangle(4, 6)
area, perimeter = rect.dimensions()
print("Area:", area, "Perimeter:", perimeter)
