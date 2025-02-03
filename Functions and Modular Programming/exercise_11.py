# Exercise 11: Define a recursive function to compute factorial.
def factorial(n):
if n == 0:
return 1
else:
return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
