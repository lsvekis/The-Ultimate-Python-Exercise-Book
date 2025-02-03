# Exercise 100: Define a function that uses both math and random modules.
import math
import random

def random_circle_area():
# Generate a random radius between 1 and 10
radius = random.uniform(1, 10)
area = math.pi * radius ** 2
return radius, area

r, a = random_circle_area()
print(f"Random radius: {r:.2f} yields area: {a:.2f}")
