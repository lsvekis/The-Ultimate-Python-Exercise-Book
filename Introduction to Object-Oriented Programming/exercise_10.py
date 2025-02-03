# Exercise 10: Create a static method that does not depend on instance or class data.
class Utils:
@staticmethod
def add(a, b):
return a + b

print("Static method add(3, 4):", Utils.add(3, 4))
