# Exercise 86: Use continue in nested loops.
for i in range(2):
for j in range(3):
if j == 1:
continue
print(f"i={i}, j={j}")
