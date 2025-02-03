# Exercise 78: Count how many times a specific word appears in a file.
word_to_count = "Python"
with open("example.txt", "r") as f:
content = f.read()
count = content.count(word_to_count)
print(f"The word '{word_to_count}' occurs {count} times.")
