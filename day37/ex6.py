'''
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books, 
add a book and get the number of books using different methods. Show that your program doesnt persist
the books after the program is stopped!

'''
class Library:
    no_of_books = 0
    books = []

    def __init__(self):
        Library.no_of_books += 1


    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book collection is : {self.books}")
        self.Count_books()


    def Count_books(self):
        self.no_of_books = len(self.books)
        
        print(f"The number of books is: {self.no_of_books} and book list length is: {self.no_of_books}")

obj1 = Library()
obj1.add_book("Harry Potter")
obj2 = Library()
obj2.add_book("Twilight")

obj3 = Library()
obj3.add_book("Thirteen Reasons why")
obj4 = Library()
obj4.add_book("The life of Pie")
