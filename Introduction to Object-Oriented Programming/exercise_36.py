# Exercise 36: Create a Calculator class with methods for basic arithmetic.
class Calculator:
def add(self, a, b):
return a + b

def subtract(self, a, b):
return a - b

calc = Calculator()
print("Addition (5 + 3):", calc.add(5, 3))
print("Subtraction (10 - 4):", calc.subtract(10, 4))
