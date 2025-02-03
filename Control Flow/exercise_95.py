# Exercise 95: Sum the digits of a number.
number = 12345
sum_digits = 0
for digit in str(number):
sum_digits += int(digit)
print("Sum of digits:", sum_digits)
