# Exercise 96: Define a function that uses the math module inside it.
import math

def circle_metrics(radius):
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
return area, circumference

area, circ = circle_metrics(4)
print("Area:", area, "Circumference:", circ)
