# Exercise 85: Append a new row to an existing CSV file.
import csv

with open("products.csv", "a", newline="") as f:
writer = csv.writer(f)
writer.writerow([3, "Tablet", 299.99])
print("New row appended to products.csv")
