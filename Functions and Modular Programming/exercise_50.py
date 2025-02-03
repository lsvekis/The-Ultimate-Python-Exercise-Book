# Exercise 50: Sum two numbers, with the second defaulting to 10.
def add_with_default(a, b=10):
return a + b

print("Sum (5 + default):", add_with_default(5))
print("Sum (5 + 7):", add_with_default(5, 7))
