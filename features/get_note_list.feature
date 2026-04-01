Feature: Getting a list of notes

  Scenario: Getting a list of notes when there are no notes
    Given There are no notes in the database
    When I get a list of notes
    Then the response status should be "200"
    And the list of notes should be empty

  Scenario: Getting a list of notes when there are notes
    Given I have two created notes notes note_1 and note_2
    When I get a list of notes
    Then the response status should be "200"
    And The list of notes consists only of note_1 and note_2