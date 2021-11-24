from dataclasses import dataclass, field
from typing import Optional

from behave import *
from hamcrest import *

from core.model.meta import DESERIALIZER
from core.test.bdd.a_dataclass import MyDataclass
from core.utils.deserialization import deserialize
from core.utils.serialization import serialize

DEFAULT_VALUE = "I am a value"


@given("a dataclass with a variety of data types")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.cls = MyDataclass


@given("a dataclass instance that has been serialized for json api consumption")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.original = context.cls()
    context.serialized = serialize(context.original).for_api()


@when("we deserialize it to the original dataclass")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.deserialized = deserialize(context.serialized, context.cls)


@then("the deserialized object is equal to the original dataclass")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.deserialized, equal_to(context.original))


@given('a serialized dataclass with {opt_or_required} property "{property_name}" that has {default_type}')
def step_impl(context, opt_or_required: str, property_name: str, default_type: str):
    """
    :type opt_or_required: str
    :type property_name: str
    :type default_type: str
    :type context: behave.runner.Context
    """
    context.property_name = property_name

    @dataclass
    class X:
        with_custom_factory: str = field(metadata={DESERIALIZER: lambda s: f"{s}_formatted"})
        required: str
        required_with_default: str = field(default=DEFAULT_VALUE)
        required_with_factory: str = field(default_factory=lambda: DEFAULT_VALUE)
        opt: Optional[str] = field(default=DEFAULT_VALUE)
        opt_with_factory: Optional[str] = field(default_factory=lambda: DEFAULT_VALUE)

    context.cls = X
    context.serialized = {
        "with_custom_factory": DEFAULT_VALUE
    }


@then("the property is set to None")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    x: object = context.deserialized
    value = getattr(x, context.property_name)
    assert_that(value, none())


@then("the property is set to the default value")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    x: object = context.deserialized
    value = getattr(x, context.property_name)
    assert_that(value, equal_to(DEFAULT_VALUE))


@then("the property is parsed with the custom deserializer")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    x: object = context.deserialized
    value = getattr(x, context.property_name)
    assert_that(value, equal_to(f"{DEFAULT_VALUE}_formatted"))