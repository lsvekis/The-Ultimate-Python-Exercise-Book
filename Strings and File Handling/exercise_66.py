# Exercise 66: Demonstrate file opening with the with statement.
with open("example.txt", "r") as f:
content = f.read()
print("Content read using with statement:")
print(content)
