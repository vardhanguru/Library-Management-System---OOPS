class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book has been added to the library")
    
    def view_available_books(self):
        # for book in self.books:
        #     if book.is_borrowed == False:
        #         print(f"{self.title} is available to borrow")

        available_books = [book for book in self.books if not book.is_borrowed]
        if available_books:
            for book in available_books:
                print(f"{book.title} is available to borrow")


    def borrow_book(self,book_title):
        for book in self.books:
            if book.title == book_title and not book.is_borrowed:
                if book.borrow():
                    print(f"borrowed")

                    return True
        return False
    
    def return_book(self,book_title):
        for book in self.books:
            if book.title == book_title and book.is_borrowed:
                if book.return_book():
                    print(f"book returned successfully")
                    return True
        print(f"book not borrowed")
        return False
    
class User:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self,library, book_title):
        if library.borrow_book(book_title):
            self.borrowed_books.append(book_title)
    
    def return_book(self,library, book_title):
        if library.return_book(book_title):
            self.borrowed_books.remove(book_title)

    def view_borrowed_books(self):
        print("borrowed books are")
        for book in self.borrowed_books:
            
            print(book)
        
    
def main():
    # Create library
    library = Library()

    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Add books to library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Create user
    user = User("Alice")

    # View available books in the library
    library.view_available_books()

    # User borrows a book
    user.borrow_book(library, "1984")
    
    # View available books after borrowing
    library.view_available_books()

    # View user's borrowed books
    user.view_borrowed_books()

    # User returns a book
    user.return_book(library, "1984")

    # View available books after returning
    library.view_available_books()

    # View user's borrowed books after returning
    user.view_borrowed_books()


if __name__ == "__main__":
    main()

