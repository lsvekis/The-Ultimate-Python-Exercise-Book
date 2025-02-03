# Exercise 40: Compute factorial using recursion (revisited).
def fact(n):
if n <= 1:
return 1
else:
return n * fact(n - 1)

print("Factorial of 6:", fact(6))
