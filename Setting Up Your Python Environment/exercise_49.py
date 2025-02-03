# Save as debug_breakpoint.py
def faulty_function():
x = 10
y = 0
breakpoint()  # This will trigger the debugger (Python 3.7+)
return x / y

if __name__ == "__main__":
try:
faulty_function()
except ZeroDivisionError:
print("Caught division by zero error.")
