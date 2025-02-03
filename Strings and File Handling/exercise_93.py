# Exercise 93: Write a tab-separated CSV file.
import csv

data = [
["ID", "Name", "Score"],
[1, "Alice", 90],
[2, "Bob", 85]
]

with open("tsv_data.csv", "w", newline="") as f:
writer = csv.writer(f, delimiter="\t")
writer.writerows(data)
print("Tab-separated CSV file tsv_data.csv created.")
