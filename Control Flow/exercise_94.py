# Exercise 94: FizzBuzz for numbers 1 through 15.
for num in range(1, 16):
if num % 15 == 0:
print("FizzBuzz")
elif num % 3 == 0:
print("Fizz")
elif num % 5 == 0:
print("Buzz")
else:
print(num)
