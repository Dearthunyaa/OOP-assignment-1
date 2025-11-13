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

class Member:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        self.borrowed_books.append(book_id)
        return True

    def return_book(self,book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        print("Error: This member hasn't borrowed this book!")
        return False

    def __str__(self):
        return f"{self.name} ({self.email})"

