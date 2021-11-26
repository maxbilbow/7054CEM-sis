# Created by maxbilbow at 23/11/2021
Feature: Deserialization of dicts into dataclasses
  Ensures the correct behaviour when converting a dictionary
  into an annotated dataclass

  Scenario: Correct json api deserialization
    Given a dataclass with a variety of data types
    Given a dataclass instance that has been serialized for json api consumption
    When we deserialize it to the original dataclass
    Then the deserialized object is equal to the original dataclass

  Scenario: Optional properties with default
    Given a serialized dataclass with an optional property "opt" that has a default value
    When we deserialize it to the original dataclass
    Then the property is set to None

  Scenario: Optional properties with default factory
    Given a serialized dataclass with an optional property "opt_with_factory" that has a default factory
    When we deserialize it to the original dataclass
    Then the property is set to None

  Scenario: Required properties with default
    Given a serialized dataclass with a required property "required_with_default" that has a default value
    When we deserialize it to the original dataclass
    Then the property is set to the default value

  Scenario: Optional properties with default factory
    Given a serialized dataclass with a required property "required_with_factory" that has a default factory
    When we deserialize it to the original dataclass
    Then the property is set to the default value

  Scenario: Optional properties without default
    Given a serialized dataclass with a required property "required" that has no default
    When we deserialize it to the original dataclass
    Then the property is set to None

  Scenario: Property with custom deserializer
    Given a serialized dataclass with a property "with_custom_factory" that has a custom deserializer
    When we deserialize it to the original dataclass
    Then the property is parsed with the custom deserializer
