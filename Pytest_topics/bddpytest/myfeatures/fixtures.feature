Feature: Fixtures and BDD Background on Python Set Datatype

    Background: Setting up data for test
        Given A datatype set
        And The set is not empty

    Scenario: Adding to a Set
    Given A set with 3 elements
    When Add 2 elements to the set
    Then The set should have 5 elements
