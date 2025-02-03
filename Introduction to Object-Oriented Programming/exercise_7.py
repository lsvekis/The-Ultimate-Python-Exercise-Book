# Exercise 7: Show that self refers to the instance inside methods.
class Calculator:
def __init__(self, value):
self.value = value

def add(self, amount):
self.value += amount
return self.value

calc = Calculator(10)
print("After adding 5:", calc.add(5))
