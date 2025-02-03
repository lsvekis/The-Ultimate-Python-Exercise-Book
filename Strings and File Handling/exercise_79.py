# Exercise 79: Write a multiplication table for 1 to 10 to a file.
with open("table.txt", "w") as f:
for i in range(1, 11):
line = " ".join(str(i * j) for j in range(1, 11))
f.write(line + "\n")
print("Multiplication table written to table.txt")
