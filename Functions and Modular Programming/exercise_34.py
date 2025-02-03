# Exercise 34: Return an error message if division by zero is attempted.
def safe_divide(a, b):
if b == 0:
return "Error: Division by zero"
return a / b

print("Safe divide 10/2:", safe_divide(10, 2))
print("Safe divide 10/0:", safe_divide(10, 0))
