# Save as factorial.py:
def factorial(n):
if n == 0:
return 1
return n * factorial(n - 1)

if __name__ == "__main__":
import sys
if len(sys.argv) != 2:
print("Usage: python factorial.py <number>")
else:
number = int(sys.argv[1])
print(f"Factorial of {number} is {factorial(number)}")
