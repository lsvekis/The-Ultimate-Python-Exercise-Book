# Save as file_check.py:
import os

filename = "output.txt"
if os.path.exists(filename):
print(f"{filename} exists.")
else:
print(f"{filename} does not exist.")
