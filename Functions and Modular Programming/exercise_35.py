# Exercise 35: Use try/except to handle potential errors.
def robust_divide(a, b):
try:
return a / b
except ZeroDivisionError:
return "Division by zero error"

print("Robust divide 8/2:", robust_divide(8, 2))
print("Robust divide 8/0:", robust_divide(8, 0))
