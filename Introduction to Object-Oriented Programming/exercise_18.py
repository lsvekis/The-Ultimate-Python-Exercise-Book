# Exercise 18: Use a class attribute to count instances.
class Tracker:
instance_count = 0

def __init__(self):
Tracker.instance_count += 1

a = Tracker()
b = Tracker()
c = Tracker()
print("Number of Tracker instances:", Tracker.instance_count)
