# Exercise 90: Read CSV data, sort by Age, and print sorted rows.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.DictReader(f)
data = list(reader)
sorted_data = sorted(data, key=lambda row: int(row["Age"]))
for row in sorted_data:
print(row)
