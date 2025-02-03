# Exercise 89: Filter rows where Age > 30 from a CSV file.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.DictReader(f)
filtered = [row for row in reader if int(row["Age"]) > 30]
print("Filtered rows (Age > 30):", filtered)
