# Exercise 72: Use try/except to handle file reading errors.
try:
with open("nonexistent.txt", "r") as f:
content = f.read()
except FileNotFoundError:
print("Error: File not found.")
