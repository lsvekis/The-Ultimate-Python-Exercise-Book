# Exercise 68: Count the total number of lines in a file.
with open("example.txt", "r") as f:
line_count = sum(1 for line in f)
print("Number of lines in the file:", line_count)
