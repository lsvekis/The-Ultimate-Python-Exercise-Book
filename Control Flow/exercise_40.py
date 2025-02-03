# Exercise 40: Create a new list of even numbers.
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
if num % 2 == 0:
even_numbers.append(num)
print("Even numbers:", even_numbers)
