# Save as read_json.py:
import json

data = '{"name": "Diana", "age": 28}'
parsed = json.loads(data)
print("Parsed JSON:", parsed)
