from behave import *
from hamcrest import *

from test.bdd.a_dataclass import MyDataclass, DATE_STRING_TODAY, DATETIME_STRING_NOW, AnEnum, ADataclass, \
    A_DATACLASS_PK
from core.utils.serialization import serialize


@given('a dataclass instance with {condition} "{property_name}"')
def step_impl(context, condition, property_name):
    """
    :type condition: str
    :type property_name: str
    :type context: behave.runner.Context
    """
    context.property_name = property_name
    context.x_object = MyDataclass(fk_dataclass=ADataclass(id=A_DATACLASS_PK))
    context.fk_dataclass_id = A_DATACLASS_PK


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
    assert_that(context.property_name, not_(is_in(context.sql_insert)))


@then('the property is included for sql update')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name, is_in(context.sql_update))


@then('the property is included for json api responses')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name, is_in(context.json_api))


@then('the property is included for sql insertion')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name, is_in(context.sql_insert))


@then("the property is omitted for sql update")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.property_name, not_(is_in(context.sql_update)))


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
    assert_that(sql_value, equal_to(AnEnum.Name.name))
    assert_that(json_api_value, equal_to(AnEnum.Name.name))


@then('the property\'s primary key is included as "{fk_property_name}" for sql')
def step_impl(context, fk_property_name: str):
    """
    :type fk_property_name: str
    :type context: behave.runner.Context
    """
    sql_insert = context.sql_insert[fk_property_name]
    sql_update = context.sql_update[fk_property_name]

    assert_that(sql_insert, equal_to(context.fk_dataclass_id))
    assert_that(sql_update, equal_to(context.fk_dataclass_id))
