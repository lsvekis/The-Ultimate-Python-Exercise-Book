import os

# Note: On Windows the home directory might be in a different variable (e.g., USERPROFILE)
print("Home directory:", os.environ.get('HOME', "Not defined"))
