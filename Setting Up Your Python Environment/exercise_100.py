# Save as write_json.py:
import json

data = {"name": "Eve", "age": 35}
with open("data.json", "w") as f:
json.dump(data, f, indent=4)
print("JSON data written to data.json.")
