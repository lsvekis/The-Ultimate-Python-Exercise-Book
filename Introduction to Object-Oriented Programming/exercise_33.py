# Exercise 33: Define a class to represent a point in 2D space.
class Point:
def __init__(self, x, y):
self.x = x
self.y = y

p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")
