# Created by MaxBilbow at 03/11/2021
Feature: Membership model determined properties
  # Enter feature description here

  Scenario: Invalid Membership Term
    Given an end_date not after today
    When a new membership is requested
    Then an error is thrown


  Scenario Outline: Membership Type Factory
    Given a user profile with <points> points
    When their membership status is requested
    Then their membership status will be <membership_type>
    Examples:
      | points | membership_type |
      | 0      | Smart  |
      | 0      | Smart  |
      | 1      | Smart  |
      | 2      | Silver |
      | 3      | Silver |
      | 4      | Silver |
      | 5      | Gold   |


  Scenario Outline: Date Formatting
    Given a membership is created with date <date_string>
    When a serialized membership is requested
    Then the dates are converted to ISO date format <date_string>
    Examples:
      | date_string |
      | 2022-11-11  |