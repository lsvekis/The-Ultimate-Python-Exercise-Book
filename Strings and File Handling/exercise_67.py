# Exercise 67: Write to a file using the with statement.
with open("newfile.txt", "w") as f:
f.write("This file was written using 'with'.")
print("newfile.txt written.")
