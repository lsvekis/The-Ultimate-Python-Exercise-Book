# Exercise 72: Search for a specific value.
numbers = [3, 7, 9, 2, 5]
i = 0
found = False
while i < len(numbers):
if numbers[i] == 9:
found = True
break
i += 1
print("9 found?" , found)
