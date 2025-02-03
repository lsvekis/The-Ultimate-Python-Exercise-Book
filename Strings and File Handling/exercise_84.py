# Exercise 84: Open a CSV file and print each row.
import csv

with open("products.csv", "r", newline="") as f:
reader = csv.reader(f)
for row in reader:
print(row)
