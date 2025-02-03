# Exercise 26: Define a Book class with title and author.
class Book:
def __init__(self, title, author):
self.title = title
self.author = author

def info(self):
return f"'{self.title}' by {self.author}"

book1 = Book("1984", "George Orwell")
print("Book info:", book1.info())
