# Exercise 26: Create a function that returns a dictionary mapping numbers to their cubes.
def cubes_dict(n):
return {i: i ** 3 for i in range(1, n + 1)}

print("Cubes dictionary (1 to 4):", cubes_dict(4))
