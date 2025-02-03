# Exercise 69: Use a module-level constant inside a function.
PI = 3.14159

def circle_circumference(radius):
return 2 * PI * radius

print("Circumference of circle with radius 3:", circle_circumference(3))
