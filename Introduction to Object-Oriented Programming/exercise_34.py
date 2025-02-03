# Exercise 34: Create a class with a method to update an attribute.
class Counter:
def __init__(self):
self.count = 0

def increment(self, value=1):
self.count += value

c = Counter()
c.increment()
c.increment(3)
print("Updated count:", c.count)
