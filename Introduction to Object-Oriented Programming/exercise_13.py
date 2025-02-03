# Exercise 13: Update an instance attribute via a method.
class Counter:
def __init__(self):
self.count = 0

def increment(self):
self.count += 1

counter = Counter()
counter.increment()
counter.increment()
print("Counter value:", counter.count)
