Feature: Getting a note by id

  Scenario: Getting a note with a valid id
    Given I have one created notes notes note_1
    And I have a valid id
    When I get a note by valid id
    Then the response status should be "200"
    And The list of notes consists only of note_1

  Scenario: Getting a note with an invalid id
    Given I have a random invalid note id.
    When I get a note by invalid id
    Then the response status should be "404"
    And the text in the body of the "Note not found" response