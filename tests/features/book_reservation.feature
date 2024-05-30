Feature: Book Reservation
  As a library user
  I want to reserve available books
  So that I can borrow them later.

  Scenario: Reserve an available book
    Given a library with an available book with ISBN "1234567890"
    And a user "John Doe"
    When the user reserves the book
    Then the book status becomes "reserved"
    And the user has the book with ISBN "1234567890" reserved

  Scenario: Reserve an already reserved book
    Given a library with a reserved book with ISBN "1234567890"
    And a user "John Doe"
    When the user attempts to reserve the book
    Then the reservation is unsuccessful
    And the book status remains "reserved"
