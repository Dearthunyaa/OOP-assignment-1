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

class Library:
    """Main library class that manages books, members, and library operations."""

    def __init__(self):
        # Only collections of books and members
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, all_copies):
        """Add a book to the collection."""
        self.books.append(Book(book_id, title, author, all_copies))
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        """Add a member to the collection."""
        self.members.append(Member(member_id, name, email))
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        """Allow a member to borrow a book."""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return
        if not book:
            print("Error: Book not found!")
            return
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return

        # Both member and book handle their own states
        if member.borrow_book(book_id) and book.borrow():
            print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, book_id):
        """Allow a member to return a borrowed book."""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return

        if member.return_book(book_id) and book.return_book():
            print(f"{member.name} returned '{book.title}'")

    def display_available_books(self):
        """Show all available books."""
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, member_id):
        """Show all books borrowed by a specific member."""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")

