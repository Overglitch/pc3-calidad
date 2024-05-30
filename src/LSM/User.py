class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books = {}

    def borrow_book(self, book):
        if book.borrowed():
            self.books[book.isbn] = "borrowed"
            return True
        return False

    def return_book(self, book):
        if book.isbn in self.books and self.books[book.isbn] == "borrowed" and book.returned():
            del self.books[book.isbn]
            return True
        return False

    def reserve_book(self, book):
        if book.reserved():
            self.books[book.isbn] = "reserved"
            return True
        return False

    def cancel_reservation(self, book):
        if book.isbn in self.books and self.books[book.isbn] == "reserved" and book.canceled():
            del self.books[book.isbn]
            return True
        return False
