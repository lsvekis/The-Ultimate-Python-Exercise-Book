# Exercise 97: Read CSV data and convert numeric fields to integers.
import csv

with open("people.csv", "r", newline="") as f:
reader = csv.DictReader(f)
data = []
for row in reader:
row["Age"] = int(row["Age"])
data.append(row)
print("CSV data with Age as integer:", data)
