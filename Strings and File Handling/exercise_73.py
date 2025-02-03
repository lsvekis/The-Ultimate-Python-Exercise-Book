# Exercise 73: Define a function that reads a file and returns its lines as a list.
def read_file_lines(filename):
with open(filename, "r") as f:
return f.readlines()

lines = read_file_lines("example.txt")
print("Lines from function:")
print(lines)
