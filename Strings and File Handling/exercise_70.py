# Exercise 70: Print every second line from a file.
with open("example.txt", "r") as f:
lines = f.readlines()
for i in range(1, len(lines), 2):
print("Line", i+1, ":", lines[i].strip())
