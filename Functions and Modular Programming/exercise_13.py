# Exercise 13: Define a function that sums an arbitrary number of numbers.
def sum_all(*numbers):
total = 0
for num in numbers:
total += num
return total

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
