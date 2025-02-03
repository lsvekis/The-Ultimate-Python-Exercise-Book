# Exercise 79: Simulate a loop that would normally run at least once.
i = 0
while True:
print("Loop iteration", i)
i += 1
if i > 0:  # Condition checked after at least one iteration.
break
