# Exercise 80: Create a new dictionary containing items with values > 50.
scores = {"Alice": 90, "Bob": 45, "Charlie": 75}
high_scores = {k: v for k, v in scores.items() if v > 50}
print("High scores:", high_scores)
