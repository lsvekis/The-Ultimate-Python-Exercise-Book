# Exercise 87: Read a CSV file and access rows as dictionaries.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.DictReader(f)
for row in reader:
print("Name:", row["Name"], "| Age:", row["Age"], "| City:", row["City"])
