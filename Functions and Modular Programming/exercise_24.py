# Exercise 24: Return a tuple containing the quotient and remainder.
def divide_and_remainder(a, b):
return a // b, a % b

quotient, remainder = divide_and_remainder(17, 4)
print("Quotient:", quotient, "Remainder:", remainder)
