# Save as import_error_handling.py:
try:
import nonexistent_module
except ImportError:
print("Module not found. Please install the module and try again.")
