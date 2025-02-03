# Exercise 29: Use a for loop to build a list of even numbers from 1 to 10.
even_numbers = []
for num in range(1, 11):
if num % 2 == 0:
even_numbers.append(num)
print("Even numbers:", even_numbers)
