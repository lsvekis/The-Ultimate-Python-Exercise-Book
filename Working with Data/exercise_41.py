# Exercise 41: A function that returns multiple values as a tuple.
def min_max(numbers):
return min(numbers), max(numbers)

mn, mx = min_max([3, 1, 4, 2])
print("Minimum:", mn, "Maximum:", mx)
