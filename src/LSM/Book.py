class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.status = "available"

    def borrowed(self):
        if self.status == "available" or self.status == "reserved":
            self.status = "borrowed"
            return True
        return False

    def returned(self):
        if self.status == "borrowed":
            self.status = "available"
            return True
        return False

    def reserved(self):
        if self.status == "available":
            self.status = "reserved"
            return True
        return False

    def canceled(self):
        if self.status == "reserved":
            self.status = "available"
            return True
        return False
