# Exercise 25: Define a Counter class with methods to increment and display the count.
class Counter:
def __init__(self):
self.count = 0

def increment(self):
self.count += 1

def display(self):
print("Current count:", self.count)

counter = Counter()
counter.increment()
counter.increment()
counter.display()
