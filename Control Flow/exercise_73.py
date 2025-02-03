# Exercise 73: Accumulate numbers until a condition (simulated input).
inputs = ["5", "10", "15"]  # Simulated inputs.
total = 0
index = 0
while index < len(inputs):
total += int(inputs[index])
index += 1
print("Total sum from input:", total)
