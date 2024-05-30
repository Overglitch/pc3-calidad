class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.status = "available"  # status can be "available", "reserved", "borrowed"

    def borrow(self):
        if self.status == "available" or self.status == "reserved":
            self.status = "borrowed"
            return True
        return False

    def return_book(self):
        if self.status == "borrowed":
            self.status = "available"
            return True
        return False

    def reserve(self):
        if self.status == "available":
            self.status = "reserved"
            return True
        return False

    def cancel_reservation(self):
        if self.status == "reserved":
            self.status = "available"
            return True
        return False
