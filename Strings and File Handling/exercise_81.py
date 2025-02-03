# Exercise 81: Write a CSV file with header row.
import csv

with open("data.csv", "w", newline="") as csvfile:
writer = csv.writer(csvfile)
writer.writerow(["Name", "Age", "City"])
writer.writerow(["Alice", 30, "New York"])
writer.writerow(["Bob", 25, "Los Angeles"])
print("CSV file data.csv created.")
