# Exercise 28: Filter out negative numbers using list comprehension.
numbers = [-5, 3, -2, 7, -1, 0]
non_negative = [x for x in numbers if x >= 0]
print("Non-negative numbers:", non_negative)
