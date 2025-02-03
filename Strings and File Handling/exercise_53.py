# Exercise 53: Format a string with dynamic field widths.
width = 10
result = "{:^{w}}".format("center", w=width)
print("Dynamically centered:", result)
