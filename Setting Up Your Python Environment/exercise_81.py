# Save as config_reader.py:
import json
import sys

if len(sys.argv) < 2:
print("Usage: python config_reader.py config.json")
sys.exit(1)

config_file = sys.argv[1]
try:
with open(config_file, 'r') as f:
config = json.load(f)
print("Configuration:")
print(config)
except Exception as e:
print("Error reading configuration:", e)
