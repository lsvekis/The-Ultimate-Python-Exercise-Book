# Exercise 99: Find and print the maximum number in a list.
numbers = [5, 9, 2, 7, 3]
max_num = numbers[0]
for num in numbers:
if num > max_num:
max_num = num
print("Largest number:", max_num)
