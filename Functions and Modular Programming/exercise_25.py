# Exercise 25: Return a list of squares for numbers in a given range.
def list_of_squares(n):
squares = []
for i in range(1, n + 1):
squares.append(i ** 2)
return squares

print("Squares up to 5:", list_of_squares(5))
