import dataclasses
from datetime import date, datetime
from enum import Enum

from behave import *
from hamcrest import *

from core.model.meta import GENERATED, PK, SQL_COLUMN
from core.utils.serialization import serialize

DATE_TODAY = date.today()
DATE_STRING_TODAY = DATE_TODAY.isoformat()

DATETIME_NOW = datetime.today()
DATETIME_STRING_NOW = DATETIME_NOW.isoformat()


class AnEnum(Enum):
    Name = "Value"


@dataclasses.dataclass
class ADataclass:
    p1: str = dataclasses.field(default="p1")


@dataclasses.dataclass
class X:
    pk: str = dataclasses.field(metadata={PK: True}, default="pk")
    pk_auto: int = dataclasses.field(metadata={PK: True, GENERATED: True}, default=42)
    not_a_column: str = dataclasses.field(metadata={SQL_COLUMN: False}, default="not_a_column")
    a_dataclass: ADataclass = dataclasses.field(default_factory=ADataclass)
    a_date: date = dataclasses.field(default=DATE_TODAY)
    a_datetime: date = dataclasses.field(default=DATETIME_NOW)
    an_enum: AnEnum = dataclasses.field(default=AnEnum.Name)


@given('a dataclass instance with {condition} "{property_name}"')
def step_impl(context, condition, property_name):
    """
    :type condition: str
    :type property_name: str
    :type context: behave.runner.Context
    """
    context.property_name = property_name
    context.x_object = X()


@when("the instance is serialized")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    s = serialize(context.x_object)
    context.sql_insert = s.for_sql_insert()
    context.sql_update = s.for_sql_update()
    context.json_api = s.for_api()


@then('the property is omitted for sql insertion')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name not in context.sql_insert)


@then('the property is included for sql update')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name in context.sql_update)


@then('the property is included for json api responses')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name in context.json_api)


@then('the property is included for sql insertion')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name in context.sql_insert)


@then("the property is omitted for sql update")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name not in context.sql_update)


@then("the date was formatted as an ISO date string")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sql_value = context.sql_insert[context.property_name]
    json_api_value = context.json_api[context.property_name]
    assert_that(sql_value, equal_to(DATE_STRING_TODAY))
    assert_that(json_api_value, equal_to(DATE_STRING_TODAY))


@then("the datetime was formatted as an ISO datetime string")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sql_value = context.sql_insert[context.property_name]
    json_api_value = context.json_api[context.property_name]
    assert_that(sql_value, equal_to(DATETIME_STRING_NOW))
    assert_that(json_api_value, equal_to(DATETIME_STRING_NOW))


@then("the enum is serialized as its name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    sql_value = context.sql_insert[context.property_name]
    json_api_value = context.json_api[context.property_name]
    assert_that(sql_value, equal_to(AnEnum.Name.Name))
    assert_that(json_api_value, equal_to(AnEnum.Name.Name))
