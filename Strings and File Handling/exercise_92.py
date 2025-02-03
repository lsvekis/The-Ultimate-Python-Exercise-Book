# Exercise 92: Read a CSV file and convert it to a list of dictionaries.
import csv

with open("colors.csv", "r", newline="") as f:
reader = csv.DictReader(f)
data = list(reader)
print("CSV data as list of dictionaries:", data)
