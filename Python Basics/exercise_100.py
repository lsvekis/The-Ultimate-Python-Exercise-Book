# Exercise 100: A simple calculator using simulated input
num1 = float("10")  # Replace with float(input("Enter first number: "))
num2 = float("5")   # Replace with float(input("Enter second number: "))
operator = "+"      # Replace with input("Enter operator (+, -, *, /): ")

if operator == "+":
result = num1 + num2
elif operator == "-":
result = num1 - num2
elif operator == "*":
result = num1 * num2
elif operator == "/":
result = num1 / num2
else:
result = "Invalid operator"

print("Result:", result)
