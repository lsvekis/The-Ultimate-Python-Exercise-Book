# Exercise 55: Compare two objects based on an attribute.
class Box:
def __init__(self, volume):
self.volume = volume

def is_larger_than(self, other):
return self.volume > other.volume

box1 = Box(100)
box2 = Box(80)
print("Is box1 larger than box2?", box1.is_larger_than(box2))
