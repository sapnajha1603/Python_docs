
'''Question 1: Counting Instances with Class Methods

Create a class Book with the following:

    A class attribute total_books initialized to 0.
    A class method add_book that increments total_books by 1 each time a new book is added.
    A class method get_total_books that prints the total number of books.

After defining the class:

    Call add_book three times to simulate adding three books.
    Then call get_total_books to print the current number of books.
'''

class Book:
    total_books = 0

    @classmethod
    def add_book(cls):
        cls.total_books += 1
        print(f"New book is added")

    @classmethod
    def get_total_books(cls):
        print(f"The total number of books are: {cls.total_books}")

Book.add_book()
Book.add_book()
Book.add_book()
Book.get_total_books()

'''
Question 2: Using Parameters in Class Methods

Create a class Library with the following:

    A class attribute library_name = "Default Library".
    A class method rename_library that accepts a new_name parameter and updates the library_name.
    A class method get_library_name that prints the current library_name.

After defining the class:

    Call get_library_name to display the default name.
    Call rename_library with a new name (e.g., "City Central Library").
    Call get_library_name again to display the updated name.'''