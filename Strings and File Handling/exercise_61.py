# Exercise 61: Open a file for reading (assumes file 'example.txt' exists).
f = open("example.txt", "r")
content = f.read()
print("File content:")
print(content)
f.close()
