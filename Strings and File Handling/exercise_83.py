# Exercise 83: Write a CSV file from a list of lists.
import csv

data = [
["ID", "Product", "Price"],
[1, "Laptop", 999.99],
[2, "Phone", 499.99]
]

with open("products.csv", "w", newline="") as f:
writer = csv.writer(f)
writer.writerows(data)
print("CSV file products.csv written.")
