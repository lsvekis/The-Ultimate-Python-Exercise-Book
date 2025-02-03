# Exercise 64: Append a new line to an existing file.
with open("output.txt", "a") as f:
f.write("\nAppended line.")
print("Data appended to output.txt")
