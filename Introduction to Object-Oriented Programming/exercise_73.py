# Exercise 73: Use a method to print a class attribute.
class Manufacturer:
company = "GadgetCo"

def show_company(self):
print("Company:", Manufacturer.company)

m = Manufacturer()
m.show_company()
