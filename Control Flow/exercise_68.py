# Exercise 68: Use a flag to control loop execution.
flag = True
i = 0
while flag:
print("i =", i)
i += 1
if i == 3:
flag = False
