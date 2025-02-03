# Exercise 77: Simulate a loop that stops when a specific input is encountered.
inputs = ["start", "continue", "stop", "end"]
i = 0
while i < len(inputs):
if inputs[i] == "stop":
break
print("Input:", inputs[i])
i += 1
