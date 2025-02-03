# Exercise 58: Define a function that rounds a number, with default precision.
def round_number(num, precision=2):
return round(num, precision)

print("Rounded 3.14159:", round_number(3.14159))
print("Rounded 3.14159 to 3 decimals:", round_number(3.14159, 3))
