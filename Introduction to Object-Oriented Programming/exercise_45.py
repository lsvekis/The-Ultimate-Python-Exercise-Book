# Exercise 45: Create a class to store and manipulate a list of items.
class Inventory:
def __init__(self, items=None):
self.items = items if items is not None else []

def add_item(self, item):
self.items.append(item)

inv = Inventory(["pen", "notebook"])
inv.add_item("eraser")
print("Inventory:", inv.items)
