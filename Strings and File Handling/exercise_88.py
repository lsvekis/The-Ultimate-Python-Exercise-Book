# Exercise 88: Count rows in a CSV file.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.reader(f)
row_count = sum(1 for row in reader) - 1  # subtract header
print("Number of data rows in people.csv:", row_count)
