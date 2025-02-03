# Exercise 65: Print class attribute information using a class method.
class Device:
manufacturer = "TechCorp"

@classmethod
def info(cls):
print(f"Manufacturer: {cls.manufacturer}")

Device.info()
