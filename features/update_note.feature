Feature: Update a note by id

  Scenario: Update a note by valid id
    Given I have two created notes notes note_1 and note_2
    And I have a valid id
    And I have random valid data
    When I am updating the note by valid id with valid data
    And I get a note by valid id
    Then the response status should be "200"
    And the note has the correct "title"
    And the note has the correct "content"

  Scenario: Update a note by invalid id
    Given I have random valid data
    And I have a random invalid note id.
    When I am updating the note by invalid id with valid data
    Then the response status should be "404"
    And the text in the body of the "Note not found" response