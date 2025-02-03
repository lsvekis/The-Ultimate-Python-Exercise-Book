# Exercise 39: Create a Contact class with attributes for name and phone.
class Contact:
def __init__(self, name, phone):
self.name = name
self.phone = phone

def __str__(self):
return f"{self.name}: {self.phone}"

contact = Contact("Rachel", "123-4567")
print("Contact info:", contact)
