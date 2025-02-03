import sys

def check_python_version(major, minor):
if sys.version_info >= (major, minor):
print(f"Python version is at least {major}.{minor}")
else:
print(f"Python version is lower than {major}.{minor}")

check_python_version(3, 6)
