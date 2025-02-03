# Exercise 23: Return both the minimum and maximum of two numbers.
def min_and_max(a, b):
return (a, b) if a < b else (b, a)

small, large = min_and_max(12, 7)
print("Smaller:", small, "Larger:", large)
