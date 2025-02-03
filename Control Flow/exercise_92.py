# Exercise 92: Find and print prime numbers between 2 and 20.
for num in range(2, 21):
is_prime = True
for i in range(2, num):
if num % i == 0:
is_prime = False
break
if is_prime:
print(num, "is prime")
