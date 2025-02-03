# In the interactive shell:
try:
1 / 0
except ZeroDivisionError as e:
print("Caught an error:", e)
