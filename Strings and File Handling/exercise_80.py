# Exercise 80: Use os.stat() to get the size of a file.
import os
file_stats = os.stat("example.txt")
print("Size of example.txt in bytes:", file_stats.st_size)
