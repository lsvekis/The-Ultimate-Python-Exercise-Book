# Save as read_file.py:
import sys

if len(sys.argv) < 2:
print("Usage: python read_file.py filename")
sys.exit(1)

filename = sys.argv[1]
try:
with open(filename, 'r') as f:
content = f.read()
print("File content:")
print(content)
except FileNotFoundError:
print(f"File {filename} not found.")
