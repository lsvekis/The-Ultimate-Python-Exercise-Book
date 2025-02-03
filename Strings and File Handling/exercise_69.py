# Exercise 69: Search for a specific word in a file and print matching lines.
search_word = "Python"
with open("example.txt", "r") as f:
for line in f:
if search_word in line:
print("Found:", line.strip())
