# Exercise 77: Read a file and print its content in uppercase.
with open("example.txt", "r") as f:
content = f.read().upper()
print("File content in uppercase:")
print(content)
