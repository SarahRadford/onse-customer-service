Feature: As a recently married customer I want to change my surname in order to ensure my information is current.

  Scenario: Update customer surname
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer "12345" surname to "Nicole Smith"
    And I fetch customer "12345"
    Then I should see customer "Nicole Smith"
