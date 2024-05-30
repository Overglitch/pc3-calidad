from src.LSM.Book import Book
from src.LSM.User import User


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, isbn, title, author):
        new_book = Book(isbn, title, author)
        self.books.append(new_book)
        return new_book

    def add_user(self, user_id, name):
        new_user = User(user_id, name)
        self.users.append(new_user)
        return new_user

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_books_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
