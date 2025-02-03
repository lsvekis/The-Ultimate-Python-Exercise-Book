# Exercise 61: Modify an instance attribute and show class attribute remains unchanged.
class Example:
shared = []

def __init__(self, value):
self.value = value

e1 = Example(1)
e2 = Example(2)
e1.shared.append("data")
print("e1 shared:", e1.shared)
print("e2 shared:", e2.shared)
