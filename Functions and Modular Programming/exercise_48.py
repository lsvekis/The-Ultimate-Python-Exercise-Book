# Exercise 48: Define a function that calculates the volume of a box.
def box_volume(length, width=1, height=1):
return length * width * height

print("Volume with only length (5):", box_volume(5))
print("Volume (5, 2, 3):", box_volume(5, 2, 3))
