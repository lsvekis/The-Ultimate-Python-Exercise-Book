# Exercise 66: Use a property at the class level (via descriptor).
class Temperature:
unit = "Celsius"  # Class attribute

@classmethod
def get_unit(cls):
return cls.unit

print("Temperature unit:", Temperature.get_unit())
