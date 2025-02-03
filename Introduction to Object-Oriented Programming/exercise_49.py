# Exercise 49: Calculate the distance between two points stored in an object.
class Point:
def __init__(self, x, y):
self.x = x
self.y = y

def distance_from_origin(self):
return (self.x**2 + self.y**2) ** 0.5

pt = Point(3, 4)
print("Distance from origin:", pt.distance_from_origin())
