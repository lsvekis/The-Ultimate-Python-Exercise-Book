# Save as write_lines.py:
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as f:
f.writelines(lines)
print("Lines written to output.txt.")
