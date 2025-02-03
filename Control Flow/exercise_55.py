# Exercise 55: Sum odd numbers in a list.
numbers = [1, 2, 3, 4, 5, 6]
odd_sum = 0
for num in numbers:
if num % 2 != 0:
odd_sum += num
print("Sum of odd numbers:", odd_sum)
