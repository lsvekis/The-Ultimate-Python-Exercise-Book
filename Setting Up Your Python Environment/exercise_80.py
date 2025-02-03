# Save as print_env.py:
import os

for key, value in os.environ.items():
print(f"{key}: {value}")
