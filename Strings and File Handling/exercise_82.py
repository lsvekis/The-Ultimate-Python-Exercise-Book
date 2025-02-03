# Exercise 82: Read a CSV file and print its rows.
import csv

with open("data.csv", "r", newline="") as csvfile:
reader = csv.reader(csvfile)
for row in reader:
print("Row:", row)
