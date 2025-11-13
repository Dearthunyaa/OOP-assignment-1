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

# Test Code for Procedural Library System
def test_library_system():
    """Comprehensive test of all library functions"""
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python Crash Course
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python Crash Course

    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)  # Alice's books
    library.display_member_books(102)  # Bob's books
    library.display_member_books(103)  # Carol's books (none)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    library.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)  # Bob tries to borrow unavailable book

    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)  # Alice's 3rd book
    library.display_member_books(101)
    library.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)  # Alice returns Python Crash Course
    library.return_book(102, 1)  # Bob returns Python Crash Course
    library.display_member_books(101)
    library.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)  # Bob tries to return book he didn't borrow

    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)  # Carol returns Pragmatic Programmer
    library.borrow_book(102, 3)  # Bob borrows it
    library.display_member_books(102)

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)  # Non-existent member
    library.borrow_book(101, 999)  # Non-existent book
    library.return_book(999, 1)  # Non-existent member
    library.display_member_books(999)  # Non-existent member

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    has_borrowed = False
    for member in library.members:
        for book_id in member.borrowed_books:
            book = library.find_book(book_id)
            print(f"  {member.name} has '{book.title}'")
            has_borrowed = True

    if not has_borrowed:
        print("  (No books are currently borrowed)")

    library.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

# Run the comprehensive test
if __name__ == "__main__":
    test_library_system()


