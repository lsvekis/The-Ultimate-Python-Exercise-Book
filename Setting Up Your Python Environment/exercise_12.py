import __main__

if not hasattr(__main__, '__file__'):
print("Running in interactive mode")
else:
print("Running as a script")
