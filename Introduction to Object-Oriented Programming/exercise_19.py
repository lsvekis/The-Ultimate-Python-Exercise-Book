# Exercise 19: Compare the area of two rectangles.
class Rectangle:
def __init__(self, width, height):
self.width = width
self.height = height

def area(self):
return self.width * self.height

def compare_area(self, other):
if self.area() > other.area():
return "Larger"
elif self.area() < other.area():
return "Smaller"
else:
return "Equal"

rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 7)
print("Comparison of areas:", rect1.compare_area(rect2))
