# Save as os_based_script.py:
import platform

if platform.system() == "Windows":
print("Running on Windows")
elif platform.system() == "Darwin":
print("Running on macOS")
else:
print("Running on Linux or other OS")
