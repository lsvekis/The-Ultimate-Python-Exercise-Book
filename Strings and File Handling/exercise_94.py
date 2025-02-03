# Exercise 94: Read a tab-separated CSV file.
import csv

with open("tsv_data.csv", "r", newline="") as f:
reader = csv.reader(f, delimiter="\t")
for row in reader:
print("Row:", row)
