Feature: Book Borrowing
  As a library user
  I want to borrow books that are available or reserved
  So that I can read them.

  Scenario: Borrow an available book
    Given a library with an available book with ISBN "1234567890"
    And a user "John Doe"
    When the user borrows the book
    Then the book status becomes "borrowed"
    And the user has the book with ISBN "1234567890" borrowed

  Scenario: Borrow a reserved book
    Given a library with a reserved book with ISBN "1234567890"
    And a user "John Doe"
    When the user borrows the book
    Then the book status becomes "borrowed"
    And the user has the book with ISBN "1234567890" borrowed

  Scenario: Borrow a borrowed book
    Given a library with a borrowed book with ISBN "1234567890"
    And a user "John Doe"
    When the user attempts to borrow the book
    Then the borrowing is unsuccessful
    And the book status remains "borrowed"
