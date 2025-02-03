# Exercise 44: Define a method that updates the price of a product.
class Product:
def __init__(self, name, price):
self.name = name
self.price = price

def update_price(self, new_price):
self.price = new_price

prod = Product("Smartphone", 800)
prod.update_price(750)
print("Updated price:", prod.price)
