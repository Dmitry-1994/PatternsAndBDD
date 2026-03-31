Feature: Creating a note
  Scenario: Successful creation of a note with valid data
    Given I have random valid data to create a note.
    When I'm creating a note with random valid data.
    Then the response status should be "200"
    And the created note has the correct "title"
    And the created note has the correct "content"

  Scenario: Unsuccessfully creating a note with invalid data
    Given I have random invalid data to create a note.
    When I'm creating a note with a random invalid title.
    Then the response status should be "422"