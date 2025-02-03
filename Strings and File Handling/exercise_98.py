# Exercise 98: Write and then read a CSV file containing Unicode characters.
import csv

data = [
["Name", "Country"],
["José", "España"],
["Miyuki", "日本"]
]

with open("unicode.csv", "w", newline="", encoding="utf-8") as f:
writer = csv.writer(f)
writer.writerows(data)

with open("unicode.csv", "r", newline="", encoding="utf-8") as f:
reader = csv.reader(f)
for row in reader:
print("Row:", row)
