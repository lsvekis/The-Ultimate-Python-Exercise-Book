# Exercise 96: Write a CSV file with quotes around all fields.
import csv

data = [
["Name", "Note"],
["Alice", "She said, \"Hello\""],
["Bob", "Good morning"]
]

with open("quoted.csv", "w", newline="") as f:
writer = csv.writer(f, quoting=csv.QUOTE_ALL)
writer.writerows(data)
print("CSV file with quoting created: quoted.csv")
