# Save as args_example.py
import sys

if __name__ == "__main__":
if len(sys.argv) > 1:
print("Arguments passed:", sys.argv[1:])
else:
print("No arguments provided.")
