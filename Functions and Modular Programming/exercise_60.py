# Exercise 60: Define a function that counts down from a given number, defaulting to 5.
def countdown(start=5):
while start > 0:
print(start)
start -= 1
print("Blast off!")

countdown()
countdown(3)
