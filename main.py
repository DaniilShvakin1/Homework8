class Book:
    def __init__(self,  author: str, name: str):
        self.author = author
        self.name = name


    def get_change_status(self):
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True

    def get_information_book(self):
        return

class Library:
    def __init__(self,book = []):
        self.book = book
        self.books = []

    def add_book(self, book: str):
        self.books.append(book)
        print("Книга успешно добленна")

    def remove_book(self, book: list):
        if book in self.books:
            self.books.remove(book)
            print("вы удалили книгу")
        else:
            print("нет такой книги")


    def get_books_count(self):
        return len(self.books)

    def get_books_info(self):
        for book in self.books:
            print(book.get_book_info())

book1 = Book("Harry Potter ","Rowling")
book2 = Book("George Orwell", "1984")


library = Library("My Library")
library.add_book(book1)
library.add_book(book2)

library.remove_book("1984")


