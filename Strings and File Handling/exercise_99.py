# Exercise 99: Define a function to search for a record by name in a CSV file.
import csv

def search_record(filename, search_name):
with open(filename, "r", newline="") as f:
reader = csv.DictReader(f)
for row in reader:
if row["Name"] == search_name:
return row
return None

record = search_record("people.csv", "Alice")
print("Search result for 'Alice':", record)
