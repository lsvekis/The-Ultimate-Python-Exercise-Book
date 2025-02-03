# Save as usage.py:
import sys

if len(sys.argv) != 3:
print("Usage: python usage.py <arg1> <arg2>")
sys.exit(1)
print("Argument 1:", sys.argv[1])
print("Argument 2:", sys.argv[2])
