# Save as parse_csv.py:
import csv
import sys

if len(sys.argv) < 2:
print("Usage: python parse_csv.py data.csv")
sys.exit(1)

csv_file = sys.argv[1]
with open(csv_file, newline='') as f:
reader = csv.reader(f)
for row in reader:
print(row)
