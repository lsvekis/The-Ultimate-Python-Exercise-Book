# Exercise 76: Implement a registry of objects in a class.
class Registry:
registry = {}

def __init__(self, key, value):
self.key = key
self.value = value
Registry.registry[key] = value

r1 = Registry("one", 1)
r2 = Registry("two", 2)
print("Registry contents:", Registry.registry)
