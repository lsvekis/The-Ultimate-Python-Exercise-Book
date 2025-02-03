# Exercise 90: Define a subclass that adds extra functionality to an overridden method.
class Shape:
def area(self):
return 0

class Square(Shape):
def __init__(self, side):
self.side = side

def area(self):
base_area = super().area()  # Though base returns 0, demonstrate usage.
return self.side * self.side

sq = Square(5)
print("Area of square:", sq.area())
