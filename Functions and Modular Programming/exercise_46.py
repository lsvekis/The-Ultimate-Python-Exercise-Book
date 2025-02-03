# Exercise 46: Use keyword-only arguments by placing * in the parameter list.
def print_coordinates(*, x, y):
print(f"Coordinates: ({x}, {y})")

print_coordinates(x=10, y=20)
