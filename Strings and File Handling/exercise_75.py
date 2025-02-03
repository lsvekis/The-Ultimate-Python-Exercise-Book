# Exercise 75: Copy the contents of one file to another.
with open("example.txt", "r") as src:
content = src.read()
with open("copy.txt", "w") as dst:
dst.write(content)
print("File copied from example.txt to copy.txt")
