# Save as write_file.py:
import sys

if len(sys.argv) < 2:
print("Usage: python write_file.py filename")
sys.exit(1)

filename = sys.argv[1]
with open(filename, 'w') as f:
f.write("This is a test output.\n")
print(f"Output written to {filename}.")
