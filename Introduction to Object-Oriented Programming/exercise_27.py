# Exercise 27: Instantiate several Book objects.
class Book:
def __init__(self, title, author):
self.title = title
self.author = author

books = [
Book("To Kill a Mockingbird", "Harper Lee"),
Book("Pride and Prejudice", "Jane Austen"),
Book("The Great Gatsby", "F. Scott Fitzgerald")
]

for book in books:
print(book.info())
