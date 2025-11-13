# Library Management System

## Project Overview

This project demonstrates a **Library Management System** built using Object-Oriented Programming (OOP) principles in Python. The system manages books, library members, and borrowing/returning operations with proper encapsulation, inheritance, and state management. This is a comprehensive educational project showcasing how OOP concepts can solve real-world problems effectively.

## Project Structure

```
library-management-oop/
├── README.md                          # Project documentation
├── oop_solution/                      # OOP implementation
│   ├── library_oop.py                # Main OOP library system
│   ├── test_oop.py                   # Test suite for OOP version
│   └── __pycache__/                  # Python cache files
└── procedural_version/               # Procedural implementation (reference)
    ├── library_procedural.py         # Procedural library system
    ├── test_procedural.py            # Test suite for procedural version
    └── __pycache__/                  # Python cache files
```

## Design Overview

#### 1. **Book Class**
Represents a book in the library with inventory management.

**Attributes:**
- `id` (int): Unique book identifier
- `title` (str): Book title
- `author` (str): Book author name
- `total_copies` (int): Total number of copies in the library
- `available_copies` (int): Number of copies currently available for borrowing

**Key Methods:**
- `borrow()`: Decrements available copies if any exist; returns True on success
- `return_book()`: Increments available copies if below total; returns True on success
- `__str__()`: Returns formatted string representation of the book with availability info

#### 2. **Member Class**
Represents a library member with borrowing privileges.

**Attributes:**
- `id` (int): Unique member identifier
- `name` (str): Member's full name
- `email` (str): Member's email address
- `borrowed_books` (list): List of book IDs currently borrowed by the member

**Key Methods:**
- `borrow_book(book_id)`: Adds a book to borrowed list if under the 3-book limit; returns True on success
- `return_book(book_id)`: Removes a book from borrowed list; returns True on success
- `__str__()`: Returns formatted string representation of the member

#### 3. **Library Class**
Main system controller that manages books, members, and all operations.

**Attributes:**
- `books` (list): Collection of all Book objects
- `members` (list): Collection of all Member objects

**Key Methods:**
- `add_book(book_id, title, author, total_copies)`: Adds a new book to the library
- `add_member(member_id, name, email)`: Registers a new member
- `find_book(book_id)`: Locates a book by ID; returns Book object or None
- `find_member(member_id)`: Locates a member by ID; returns Member object or None
- `borrow_book(member_id, book_id)`: Processes book borrowing with validation
- `return_book(member_id, book_id)`: Processes book return with validation
- `display_available_books()`: Lists all books with available copies
- `display_member_books(member_id)`: Lists books borrowed by a specific member

## Testing

The test suite (`test_oop.py`) provides comprehensive coverage of all library operations:

### Basic Operations
- **Adding Books**: Tests adding multiple books with different copy counts
- **Adding Members**: Tests registering multiple library members
- **Borrowing and Returning Books**: Tests successful borrowing and return transactions
- **Displaying Information**: Tests display methods for available books and member borrowings

### Edge Cases
- **Borrowing Unavailable Books**: Tests borrowing when no copies are available
- **Exceeding Borrowing Limit**: Tests the 3-book maximum borrowing limit per member
- **Returning Books Not Borrowed**: Tests error handling when members try to return books they didn't borrow
- **Non-existent Books/Members**: Tests error handling for invalid IDs

### Test Coverage Details
The test suite includes 14 comprehensive test scenarios:
1. Adding books to the library
2. Registering members
3. Displaying initial available books
4. Successful borrowing operations
5. Displaying member's borrowed books
6. Displaying books after borrowing
7. Borrowing the last available copy
8. Attempting to borrow unavailable books
9. Testing borrowing limit (maximum 3 books per member)
10. Returning borrowed books
11. Attempting invalid returns
12. Returning and re-borrowing scenarios
13. Error handling for non-existent members/books
14. Final library status report

## How to Run Your Test Code

### Prerequisites
- Python 3.7 or higher installed on your system

### Running the OOP Version Tests

#### Option 1: Run directly with Python
```bash
cd oop_solution
python test_oop.py
```

#### Option 2: Run the library module directly
```bash
cd oop_solution
python library_oop.py
```