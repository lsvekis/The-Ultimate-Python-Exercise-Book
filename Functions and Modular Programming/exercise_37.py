# Exercise 37: Define a generator function that yields even numbers up to n.
def even_numbers(n):
for i in range(2, n + 1, 2):
yield i

for num in even_numbers(10):
print(num, end=" ")
print()
