# Exercise 48: Return a formatted description of an object.
class Movie:
def __init__(self, title, director):
self.title = title
self.director = director

def description(self):
return f"'{self.title}' directed by {self.director}"

movie = Movie("Inception", "Christopher Nolan")
print("Movie description:", movie.description())
