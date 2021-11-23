# Created by maxbilbow at 23/11/2021
Feature: Serialization of dataclasses
  # Enter feature description here

  Scenario: Auto-Generated PK
    Given a dataclass instance with a auto-generated primary key "pk_auto"
    When the instance is serialized
    Then the property is omitted for sql insertion
    Then the property is included for sql update
    Then the property is included for json api responses

  Scenario: Non-Generated PK
    Given a dataclass instance with a non-generated primary key "pk"
    When the instance is serialized
    Then the property is included for sql insertion
    Then the property is included for sql update
    Then the property is included for json api responses

  Scenario: Non-SQL field
    Given a dataclass instance with a non-sql field "not_a_column"
    When the instance is serialized
    Then the property is omitted for sql insertion
    Then the property is omitted for sql update
    Then the property is included for json api responses

  Scenario: Cannot insert dataclasses
    Given a dataclass instance with property which is itself a dataclass: "a_dataclass"
    When the instance is serialized
    Then the property is omitted for sql insertion
    Then the property is omitted for sql update
    Then the property is included for json api responses

  Scenario: date serialization
    Given a dataclass instance with date property "a_date"
    When the instance is serialized
    Then the date was formatted as an ISO date string

  Scenario: datetime serialization
    Given a dataclass instance with date property "a_datetime"
    When the instance is serialized
    Then the datetime was formatted as an ISO datetime string

  Scenario: Enum serialization
     Given a dataclass instance with date property "an_enum"
    When the instance is serialized
    Then the enum is serialized as its name