# Exercise 76: Accumulate numbers until a threshold is reached (simulated input).
numbers = [2, 4, 6, 8]  # Simulated inputs.
total = 0
i = 0
while i < len(numbers) and total < 15:
total += numbers[i]
i += 1
print("Accumulated total:", total)
