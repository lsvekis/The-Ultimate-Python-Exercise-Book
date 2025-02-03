# Exercise 98: Use a common interface to treat different objects uniformly.
class Shape:
def draw(self):
print("Drawing shape...")

class Circle(Shape):
def draw(self):
print("Drawing circle...")

class Square(Shape):
def draw(self):
print("Drawing square...")

shapes = [Circle(), Square(), Shape()]
for shape in shapes:
shape.draw()
