# Exercise 77: Return a sorted list of keys from a class registry.
class Registry:
registry = {}

def __init__(self, key, value):
self.key = key
self.value = value
Registry.registry[key] = value

@classmethod
def sorted_keys(cls):
return sorted(cls.registry.keys())

Registry("b", 2)
Registry("a", 1)
print("Sorted registry keys:", Registry.sorted_keys())
