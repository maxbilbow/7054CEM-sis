# Created by MaxBilbow at 03/11/2021
Feature: Membership model determined properties
  # Enter feature description here

  Scenario Outline: Calculated renewal data
    Given a membership with a start date of <start_date>
    When a term time of <term> months
    Then the renewal date will be <renewal_date>
    Examples:
      | start_date | term | renewal_date |
      | 2021-11-1  | 12   | 2022-11-1    |
      | 2021-11-1  | 1    | 2021-12-1    |
      | 2020-02-29 | 12   | 2021-02-28   |
      | 2021-11-1  | 36   | 2024-11-1    |


  Scenario Outline: Membership Status Factory
    Given a user with <role> role
    And they <have_or_do_not_have> a valid membership
    And they have accumulated <points> points
    When their membership status is requested
    Then their membership status will be <status>
    Examples:
      | role    | have_or_do_not_have | points | status |
      | Advisor | do not have         | 0      | Gold   |
      | Member  | do not have         | 0      | Bronze |
      | Member  | do not have         | 10     | Bronze |
      | Member  | have                | 0      | Bronze |
      | Member  | have                | 1      | Bronze |
      | Member  | have                | 2      | Silver |
      | Member  | have                | 3      | Silver |
      | Member  | have                | 4      | Silver |
      | Member  | have                | 5      | Gold   |
