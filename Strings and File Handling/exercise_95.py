# Exercise 95: Read a CSV and create a list of values from a specific column.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.DictReader(f)
names = [row["Name"] for row in reader]
print("Names from people.csv:", names)
