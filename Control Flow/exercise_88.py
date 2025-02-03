# Exercise 88: Combine continue and break in a while loop.
i = 0
while i < 10:
i += 1
if i % 2 == 0:
continue
if i > 7:
break
print(i)
