# Exercise 33: Calculate Euclidean distance between two points.
import math

def distance(p1, p2):
return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

print("Distance between (1,2) and (4,6):", distance((1,2), (4,6)))
