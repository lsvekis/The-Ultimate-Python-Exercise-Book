# Save as custom_exception.py:
class CustomError(Exception):
pass

def risky_operation():
raise CustomError("An error occurred in risky_operation")

if __name__ == "__main__":
try:
risky_operation()
except CustomError as e:
print("Caught a custom error:", e)
