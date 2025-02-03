# Exercise 91: Write a CSV file from a list of tuples.
import csv

data = [
(1, "Red", "#FF0000"),
(2, "Green", "#00FF00"),
(3, "Blue", "#0000FF")
]

with open("colors.csv", "w", newline="") as f:
writer = csv.writer(f)
writer.writerow(["ID", "Color", "Hex"])
writer.writerows(data)
print("CSV file colors.csv created.")
