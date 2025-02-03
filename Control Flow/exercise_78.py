# Exercise 78: Continue looping until the sum exceeds 20.
numbers = [3, 4, 5, 6, 7]
total = 0
i = 0
while i < len(numbers) and total <= 20:
total += numbers[i]
i += 1
print("Total:", total)
