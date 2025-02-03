# Save as conditional_import.py:
import sys

if len(sys.argv) < 2:
print("Usage: python conditional_import.py <module_name>")
sys.exit(1)

module_name = sys.argv[1]
try:
module = __import__(module_name)
print(f"Module {module_name} imported successfully.")
except ImportError:
print(f"Module {module_name} not found.")
