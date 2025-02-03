# Exercise 74: Write a function that writes a list of strings to a file.
def write_lines(filename, lines_list):
with open(filename, "w") as f:
for line in lines_list:
f.write(line + "\n")

write_lines("lines_output.txt", ["Line 1", "Line 2", "Line 3"])
print("Lines written to lines_output.txt")
