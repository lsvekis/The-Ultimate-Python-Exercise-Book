# Save as read_lines.py:
filename = "sample.txt"
try:
with open(filename, "r") as f:
for line in f:
print(line.strip())
except FileNotFoundError:
print(f"{filename} not found.")
