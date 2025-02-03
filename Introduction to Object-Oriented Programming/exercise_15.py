# Exercise 15: Define __repr__ for an unambiguous representation.
class Point:
def __init__(self, x, y):
self.x = x
self.y = y

def __repr__(self):
return f"Point({self.x}, {self.y})"

pt = Point(3, 4)
print("Representation of Point:", repr(pt))
