# Exercise 65: Read all lines of a file into a list.
with open("example.txt", "r") as f:
lines = f.readlines()
print("List of lines:")
print(lines)
