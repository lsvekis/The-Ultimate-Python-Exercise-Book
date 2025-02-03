# Exercise 71: Write and read a file with UTF-8 encoding.
with open("utf8file.txt", "w", encoding="utf-8") as f:
f.write("Café – with accent")
with open("utf8file.txt", "r", encoding="utf-8") as f:
content = f.read()
print("UTF-8 file content:", content)
