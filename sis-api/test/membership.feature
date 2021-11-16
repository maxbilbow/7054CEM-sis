# Created by MaxBilbow at 03/11/2021
Feature: Membership model determined properties
  # Enter feature description here

  Scenario Outline: Create New Membership
    Given a start date of <start_date>
    And a term time of <term> months
    When a new membership is created
    Then the renewal date will be <end_date>
    Examples:
      | start_date | term | end_date |
      | 2021-11-1  | 12   | 2022-11-1    |
      | 2021-11-1  | 1    | 2021-12-1    |
      | 2020-02-29 | 12   | 2021-02-28   |
      | 2021-11-1  | 36   | 2024-11-1    |


  Scenario Outline: Membership Type Factory
    Given a user profile with <role> role
    And a user profile with <points> points
    When their membership status is requested
    Then their membership status will be <membership_type>
    Examples:
      | role    | points | membership_type |
      | Advisor | 0      | Gold   |
      | Member  | 0      | Smart  |
      | Member  | 0      | Smart  |
      | Member  | 1      | Smart  |
      | Member  | 2      | Silver |
      | Member  | 3      | Silver |
      | Member  | 4      | Silver |
      | Member  | 5      | Gold   |
