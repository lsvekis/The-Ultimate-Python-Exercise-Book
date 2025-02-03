# Exercise 86: Write data to a CSV file using csv.DictWriter.
import csv

data = [
{"Name": "Charlie", "Age": 28, "City": "Chicago"},
{"Name": "Dana", "Age": 32, "City": "Houston"}
]

with open("people.csv", "w", newline="") as f:
fieldnames = ["Name", "Age", "City"]
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(data)
print("CSV file people.csv created with DictWriter.")
