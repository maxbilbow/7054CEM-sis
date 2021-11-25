# Created by maxbilbow at 21/11/2021
Feature: # Enter feature name here
  # Enter feature description here
  Background:
    Given a clean database has been created
    And registered users exist in the database with profiles
    And a QuoteService instance

  Scenario: Cascading deletion of a User
    Given that a new quote was created
    When a request to delete the user is made
    Then the user is deleted
    And all the registered user's quotes are deleted
    And the registered user's profile is deleted

  Scenario: Active membership prevents user deletion
    Given the user has an active membership
    When a request to delete the user is made
    Then the user is not deleted
