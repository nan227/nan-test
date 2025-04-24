class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrowed_count = 0

class BookNotAvailableError(Exception):
    pass
