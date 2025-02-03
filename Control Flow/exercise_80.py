# Exercise 80: Repeatedly divide a number until the remainder is zero.
num = 64
while num % 2 == 0 and num != 0:
print("Current num:", num)
num //= 2
print("Final num:", num)
