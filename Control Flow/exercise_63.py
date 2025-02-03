# Exercise 63: Simulate input validation in a while loop.
user_input = "abc"  # Change to a valid numeric string to exit the loop.
attempts = 0
while not user_input.isdigit() and attempts < 3:
print("Invalid input, please enter a number.")
# Simulate a new input for demonstration.
user_input = "123"
attempts += 1
print("Valid input received:", user_input)
