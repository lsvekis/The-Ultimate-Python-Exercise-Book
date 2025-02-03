# Exercise 62: Read and print a file line by line.
with open("example.txt", "r") as f:
for line in f:
print(line.strip())
