# Exercise 100: Define a function to update a record in a CSV file.
import csv

def update_record(filename, search_name, new_data):
# Read all records
with open(filename, "r", newline="") as f:
reader = csv.DictReader(f)
records = list(reader)
fieldnames = reader.fieldnames
# Update the matching record
updated = False
for row in records:
if row["Name"] == search_name:
row.update(new_data)
updated = True
# Write back to the file
with open(filename, "w", newline="") as f:
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(records)
return updated

result = update_record("people.csv", "Bob", {"Age": 26, "City": "San Francisco"})
print("Record updated:", result)
