# Exercise 76: Append current date and time to a file.
from datetime import datetime
with open("log.txt", "a") as f:
f.write("Log entry: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
print("Log entry added to log.txt")
