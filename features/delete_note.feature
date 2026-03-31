Feature: Deleting a note
  Scenario: Deleting a note with a valid id
    Given I have two created notes notes note_1 and note_2
    When I am deleting a note_2 by its id
    Then the response status should be "200"
    And the text in the body of the "Note deleted" response
    And the list of received notes consists of note_1

  Scenario: Deleting a note with an invalid id
    Given I have a random invalid note id.
    When I am deleting a note with an invalid id.
    Then the response status should be "404"
    And the text in the body of the "Note not found" response