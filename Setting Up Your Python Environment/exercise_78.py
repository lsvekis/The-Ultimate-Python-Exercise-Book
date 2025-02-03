# Save as measure_time.py:
import time

start_time = time.time()

# Simulate a task
total = 0
for i in range(1000000):
total += i

end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")
