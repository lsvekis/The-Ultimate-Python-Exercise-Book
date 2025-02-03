# Exercise 43: Provide a method to return the object's data as a dictionary.
class Product:
def __init__(self, name, price):
self.name = name
self.price = price

def to_dict(self):
return {"name": self.name, "price": self.price}

prod = Product("Laptop", 1200)
print("Product as dict:", prod.to_dict())
