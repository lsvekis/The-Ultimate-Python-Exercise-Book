# Exercise 84: Use continue to skip a loop iteration in a while loop.
i = 0
while i < 5:
i += 1
if i == 3:
continue
print("i =", i)
