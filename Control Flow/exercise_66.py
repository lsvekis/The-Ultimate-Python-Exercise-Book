# Exercise 66: Generate Fibonacci numbers.
a, b = 0, 1
count = 0
while count < 7:
print(a, end=" ")
a, b = b, a + b
count += 1
print()
