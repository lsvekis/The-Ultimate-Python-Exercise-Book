# Exercise 14: Define a function that prints keyword arguments.
def print_details(**kwargs):
for key, value in kwargs.items():
print(f"{key}: {value}")

print_details(name="Charlie", age=30, city="New York")
