# Exercise 36: Recursively calculate factorial (alternative version).
def recursive_factorial(n):
return 1 if n == 0 else n * recursive_factorial(n - 1)

print("Recursive factorial of 4:", recursive_factorial(4))
