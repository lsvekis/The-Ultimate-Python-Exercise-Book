# Exercise 20: Define a function that returns multiple values as a tuple.
def min_max(numbers):
return min(numbers), max(numbers)

minimum, maximum = min_max([4, 7, 1, 9])
print("Minimum:", minimum, "Maximum:", maximum)
