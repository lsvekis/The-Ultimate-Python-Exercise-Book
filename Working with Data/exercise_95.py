# Exercise 95: Determine the maximum value in a list.
numbers = [3, 7, 2, 9, 4]
max_value = numbers[0]
for num in numbers:
if num > max_value:
max_value = num
print("Maximum value:", max_value)
