'''
[Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library
catalog system. Create a Python class Book to represent a single book with attributes: Title, 
Author, ISBN, Genre, Availability (whether the book is available for borrowing or not). Create
another Python class LibraryCatalog to manage the collection of books with following 
functionalities:
 - Add books by storing each book objects (Hint: Create an empty list in constructor 
 and store book objects)
 - get book details and get all books from the list of objects
'''
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG)


class Book:
    '''Class representing a book'''

    def __init__(self, title, author, isbn, genre, avaibility) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.avaibility = avaibility

    def get_info(self):
        '''Display information about book.'''
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('ISBN: ', self.isbn)
        print('Title: ', 'Yes' if self.avaibility else 'No')


class LibraryCatalog:
    '''Class representing a library catalog'''

    def __init__(self, books=[]) -> None:
        '''Initialize LibraryCatalog object'''
        self.books = books

    def add_book(self, book):
        '''Add new book to catalog.'''
        self.books.append(book)

    def list_book(self):
        '''List all books in catalog.'''
        print('Title\t\tAvailable')
        for i, book in enumerate(self.books):
            print(f'{i+1}. {book[i].title}', ' | ',
                  'Yes' if book[i].avaibility else 'No')

    def book_detail(self, book_idx):
        '''Get detail of single book from catalog.'''
        self.books[book_idx + 1].get_info()

    def borrow_return(self, book_idx):
        '''Either return or borrow book.'''
        if self.books[book_idx].avaibility:
            self.books[book_idx + 1].avaibility = False
            logging.info(f'Book {book_idx+1} borrowed')
        else:
            self.books[book_idx + 1].avaibility = True
            logging.info(f'Book {book_idx+1} returned')


def init_library():
    '''Function to initialize library catalog with few books'''
    book1 = Book('Harry Potter', 'J.K Rowling',
                 '9780590353427', 'Fiction', True)
    book2 = Book('The Lord of the Rings', 'J.R.R. Tolkien',
                 '9780007520825', 'Fantasy', False)
    book3 = Book('Pride and Prejudice', 'Jane Austen',
                 '9780140435225', 'Romance', True)
    book4 = Book('To Kill a Mockingbird', 'Harper Lee',
                 '9780446310727', 'Classic', True)

    library_catalog = LibraryCatalog([book1, book2, book3, book4])

    return library_catalog


library = init_library()


def menu(library):
    '''Function to display and operate library transactions.'''
    try:
        while True:
            print("\n", "*"*10)
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
                title, author, isbn, genre = input(
                    'Enter title,author,genre (use , to separate)').split(',')
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
