Feature: Book Search
  As a library user
  I want to search for books by ISBN, title, or author
  So that I can find books I am interested in.

  Scenario: Search for a book by ISBN
    Given a library with books
    When I search for a book by ISBN "1234567890"
    Then I find the book with title "Sample Book Title" and author "Author Name"

  Scenario: Search for a book by title
    Given a library with books
    When I search for books by title "Sample Book Title"
    Then I find the book with ISBN "1234567890" and author "Author Name"

  Scenario: Search for books by author
    Given a library with books
    When I search for books by author "Author Name"
    Then I find the book with ISBN "1234567890" and title "Sample Book Title"
