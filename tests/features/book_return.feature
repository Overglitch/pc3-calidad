Feature: Book Return
  As a library user
  I want to return borrowed books
  So that others can borrow them.

  Scenario: Return a borrowed book
    Given a library with a borrowed book with ISBN "1234567890"
    And a user "John Doe" who borrowed the book
    When the user returns the book
    Then the book status becomes "available"
    And the user no longer has the book with ISBN "1234567890" borrowed

  Scenario: Return a book that was not borrowed
    Given a library with an available book with ISBN "1234567890"
    And a user "John Doe"
    When the user attempts to return the book
    Then the return is unsuccessful
    And the book status remains "available"
