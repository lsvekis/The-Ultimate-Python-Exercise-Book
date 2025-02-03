# Exercise 9: Define a function that returns early if a condition is met.
def check_number(num):
if num < 0:
return "Negative number"
return "Positive number or zero"

print(check_number(-5))
print(check_number(3))
