from pytest_bdd import scenarios, given, when, then
from src.LSM import Book, User, Library

# Define el path de las historias de usuario
scenarios('features')


# Shared contexts
@given('a library with books')
def library_with_books():
    library = Library()
    library.add_book('1234567890', 'Sample Book Title', 'Author Name')
    library.add_book('0987654321', 'Another Book Title', 'Another Author')
    return library


@given('a user "John Doe"')
def user_john_doe(library_with_books):
    library = library_with_books
    user = library.add_user('1', 'John Doe')
    return user


# Step Definitions for Book Search
@when('I search for a book by ISBN "1234567890"')
def search_book_by_isbn(library_with_books):
    library = library_with_books
    return library.find_book_by_isbn('1234567890')


@then('I find the book with title "Sample Book Title" and author "Author Name"')
def verify_book_found_by_isbn(search_book_by_isbn):
    book = search_book_by_isbn
    assert book.title == 'Sample Book Title'
    assert book.author == 'Author Name'


@when('I search for books by title "Sample Book Title"')
def search_books_by_title(library_with_books):
    library = library_with_books
    return library.find_books_by_title('Sample Book Title')


@then('I find the book with ISBN "1234567890" and author "Author Name"')
def verify_book_found_by_title(search_books_by_title):
    books = search_books_by_title
    assert len(books) == 1
    book = books[0]
    assert book.isbn == '1234567890'
    assert book.author == 'Author Name'


@when('I search for books by author "Author Name"')
def search_books_by_author(library_with_books):
    library = library_with_books
    return library.find_books_by_author('Author Name')


@then('I find the book with ISBN "1234567890" and title "Sample Book Title"')
def verify_book_found_by_author(search_books_by_author):
    books = search_books_by_author
    assert len(books) == 1
    book = books[0]
    assert book.isbn == '1234567890'
    assert book.title == 'Sample Book Title'


# Step Definitions for Book Reservation
@given('a library with an available book with ISBN "1234567890"')
def library_with_available_book(library_with_books):
    library = library_with_books
    book = library.find_book_by_isbn('1234567890')
    book.status = 'available'
    return book


@when('the user reserves the book')
def reserve_book(user_john_doe, library_with_available_book):
    user = user_john_doe
    book = library_with_available_book
    user.reserve_book(book)


@then('the book status becomes "reserved"')
def verify_book_reserved(library_with_available_book):
    book = library_with_available_book
    assert book.status == 'reserved'


@then('the user has the book with ISBN "1234567890" reserved')
def verify_user_reserved_book(user_john_doe):
    user = user_john_doe
    assert '1234567890' in user.books
    assert user.books['1234567890'] == 'reserved'


# Step Definitions for Book Borrowing
@when('the user borrows the book')
def borrow_book(user_john_doe, library_with_available_book):
    user = user_john_doe
    book = library_with_available_book
    user.borrow_book(book)


@then('the book status becomes "borrowed"')
def verify_book_borrowed(library_with_available_book):
    book = library_with_available_book
    assert book.status == 'borrowed'


@then('the user has the book with ISBN "1234567890" borrowed')
def verify_user_borrowed_book(user_john_doe):
    user = user_john_doe
    assert '1234567890' in user.books
    assert user.books['1234567890'] == 'borrowed'


# Step Definitions for Book Return
@given('a library with a borrowed book with ISBN "1234567890"')
def library_with_borrowed_book(library_with_books):
    library = library_with_books
    book = library.find_book_by_isbn('1234567890')
    book.status = 'borrowed'
    return book


@when('the user returns the book')
def return_book(user_john_doe, library_with_borrowed_book):
    user = user_john_doe
    book = library_with_borrowed_book
    user.return_book(book)


@then('the book status becomes "available"')
def verify_book_returned(library_with_borrowed_book):
    book = library_with_borrowed_book
    assert book.status == 'available'


@then('the user no longer has the book with ISBN "1234567890" borrowed')
def verify_user_returned_book(user_john_doe):
    user = user_john_doe
    assert '1234567890' not in user.books
