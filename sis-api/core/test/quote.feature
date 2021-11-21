# Created by maxbilbow at 21/11/2021
Feature: Insurance Quote API
  # Behaviours for quote creation and tracking API

  Background:
    Given a clean database has been created
    And registered users exist in the database
    And a QuoteService instance

 Scenario Outline: New Quote with valid params
   Given a registered user
   Given requested insurance type "<insurance_type>"
   When a new quote is requested for a user
   Then the quote has the correct type attribute
   And the new quote was created for the user
   Examples:
     | insurance_type |
     | Motor |
     | Home |

 Scenario: Quote for non-existent user
   Given a user is not registered
   And requested insurance type "Motor"
   When a new quote is requested for a user
   Then quote cannot be created
   And a key constraint error is thrown

 Scenario: Update a quote
   Given that a new quote was created
   When new quote data is sent
   Then the quote is updated
   And the updated timestamp did increase

 Scenario: Delete a quote
   Given that a new quote was created
   When a request is sent to delete the quote
   Then the quote is deleted