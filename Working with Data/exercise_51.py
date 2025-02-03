# Exercise 51: Unpack a tuple using the * operator to capture remaining items.
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first, "Middle:", middle, "Last:", last)
