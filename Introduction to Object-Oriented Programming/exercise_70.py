# Exercise 70: Track created instances using a class attribute.
class Tracker:
instances = []

def __init__(self, name):
self.name = name
Tracker.instances.append(self)

a = Tracker("A")
b = Tracker("B")
for instance in Tracker.instances:
print("Tracked instance:", instance.name)
