import subprocess

try:
subprocess.run(["pip", "--version"], check=True)
print("pip is installed.")
except Exception as e:
print("pip is not installed or not configured properly:", e)
