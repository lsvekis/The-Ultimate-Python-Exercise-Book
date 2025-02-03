# Exercise 32: Create a class with a static method that adds two numbers.
class MathUtils:
@staticmethod
def add(a, b):
return a + b

print("Static add (7 + 8):", MathUtils.add(7, 8))
