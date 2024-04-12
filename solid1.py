'''
[Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library catalog system.
Create a Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability
(whether the book is available for borrowing or not). Create another Python class LibraryCatalog to manage the collection
of books with following functionalities:
 - Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects)
 - get book details and get all books from the list of objects
'''
import logging

logging.basicConfig('log.txt',level=logging.DEBUG)

class Book:
    def __init__(self, title, author, isbn, genre, avaibility) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avaibility = avaibility

    def get_info(self):
        print('Title: ',self.title)
        print('Author: ',self.author)
        print('ISBN: ',self.isbn)
        print('Title: ','Yes' if self.avaibility else 'No')

class LibraryCatalog:
    def __init__(self,books=[]) -> None:
        self.books = books
    
    def add_book(self,book):
        self.books.append(book)
    
    def list_book(self):
        print(f'Title\t\tAvailable')
        for i in range(len(self.books)):
            print(f'{i+1}. {self.books[i].title}',' | ', 'Yes' if self.books[i].avaibility else 'No')

    def book_detail(self,book_idx):
        self.books[book_idx + 1].get_info()

    def borrow_return(self,book_idx):
        if self.books[book_idx].avaibility:
            self.books[book_idx + 1].avaibility = False
            logging.info(f'Book {book_idx+1} borrowed')
        else:
            self.books[book_idx + 1].avaibility = True
            logging.info(f'Book {book_idx+1} returned')


def init_library():
    book1 = Book('Harry Potter', 'J.K Rowling', '9780590353427', 'Fiction', True)
    book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien', '9780007520825', 'Fantasy', False)
    book3 = Book('Pride and Prejudice', 'Jane Austen', '9780140435225', 'Romance', True)
    book4 = Book('To Kill a Mockingbird', 'Harper Lee', '9780446310727', 'Classic', True)

    library_catalog = LibraryCatalog([book1,book2,book3,book4])

    return library_catalog


# book5 = Book('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', '9780345391803', 'Science Fiction', False)
# book6 = Book('One Hundred Years of Solitude', 'Gabriel García Márquez', '9780307472838', 'Magical Realism', True)
# book7 = Book('The Great Gatsby', 'F. Scott Fitzgerald', '9780140241760', 'Fiction', False)

library = init_library()

def menu(library):
    try:
        while True:
            print("\n","*"*10)
            print('Enter your choice')
            print('1. List book')
            print('2. Add book')
            print('3. Get book detail')
            print('4. Borrow/return book')
            print('5. Exit')

            ch = input('YOur choice? (1,2,3,4): ')

            if ch == '1':
                library.list_book()
            
            elif ch == '2':
                title, author, isbn, genre = input('Enter title,author,genre (use , to separate)').split(',')
                book = Book(title, author, isbn, genre, True)
                library.add_book(book)
            
            elif ch == '3':
                book_idx = input('List book and enter book no.')
                library.book_detail(int(book_idx))
            
            elif ch == '4':
                book_idx = input('List book and enter book no.')
                library.borrow_return(int(book_idx))
            
            elif ch == '5':
                exit()
            else:
                print('Invalid input')
    except:
        logging.info(f'Library catalog crashed.')

menu(library)
