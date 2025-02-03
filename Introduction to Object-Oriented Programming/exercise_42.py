# Exercise 42: Automatically assign a unique ID to each object.
class Unique:
next_id = 1

def __init__(self):
self.id = Unique.next_id
Unique.next_id += 1

u1 = Unique()
u2 = Unique()
print("Unique IDs:", u1.id, u2.id)
