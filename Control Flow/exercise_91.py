# Exercise 91: Simulate a number guessing game.
secret_number = 7
guess = 0  # Simulated guess; replace with int(input(...)) in real use.
attempts = 0
while guess != secret_number and attempts < 5:
# Simulate a guess for demonstration.
guess = 7
attempts += 1
if guess == secret_number:
print("Correct guess!")
else:
print("Try again.")
