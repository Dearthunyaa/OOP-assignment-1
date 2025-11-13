books = []
members = []
borrowed_books = []

class Book:
    def __init__(self, book_id, title, author, all_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.all_copies = all_copies
        self.available_copies = all_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.all_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self): 
        """Return string"""
        return f"{self.title} by {self.author} ({self.available_copies}/{self.all_copies} available)"
