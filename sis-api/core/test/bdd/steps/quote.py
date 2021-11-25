import dataclasses
import logging

from behave import *
from hamcrest import *

from core.model import to_dict
from core.model.quote import Quote
from core.service.profile_service import ProfileService
from core.service.quote_service import QuoteService

FOREIGN_KEY_CONSTRAINT_ERROR = 1452


@given('requested insurance type "{insurance_type}"')
def step_impl(context, insurance_type: str):
    """
    :type context: behave.runner.Context
    :type insurance_type: str
    """
    context.insurance_type = insurance_type


@when('a new quote is requested for a user')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    quote_service: QuoteService = context.quote_service
    context.quote = None
    user_id = context.user_id
    insurance_type = context.insurance_type
    try:
        context.quote = quote_service.new_quote(user_id=user_id, insurance_type=insurance_type)
    except Exception as e:
        logging.error(e)
        context.new_quote_error = e


@then("the quote has the correct type attribute")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.quote.type.name, equal_to(context.insurance_type))


@then("the new quote was saved to the database")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(QuoteService().get_quote(context.registered_user_id), equal_to(context.quote))


@then('the new quote was created for the user')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.quote.user_id, equal_to(context.registered_user_id))


@given("a user is not registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user_id = 0


@then("quote cannot be created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.quote, is_(None))
    assert_that(context.new_quote_error, not_none())


@step("a key constraint error is thrown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    assert_that(context.new_quote_error.errno, equal_to(FOREIGN_KEY_CONSTRAINT_ERROR))


def create_quote(context):
    quote_service: QuoteService = context.quote_service
    context.quote = None
    user_id = context.user_id
    insurance_type = context.insurance_type
    try:
        context.quote = quote_service.new_quote(user_id=user_id, insurance_type=insurance_type)
    except Exception as e:
        context.new_quote_error = e


@given("that a new quote was created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.user_id = context.registered_user_id
    context.insurance_type = "Motor"
    create_quote(context)


@when("new quote data is sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    quote: Quote = context.quote
    updated_quote = dataclasses.replace(quote, is_complete=True, created=0, updated=0)
    context.updated_quote = updated_quote
    quote_dict = to_dict(updated_quote)
    context.quote_service.update_quote(quote_id=quote.id, data=quote_dict)


@then("the quote is updated")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    qs: QuoteService = context.quote_service
    original_quote = context.quote
    retrieved_quote = qs.get_quote(context.quote.id)
    assert_that(original_quote.is_complete, equal_to(False))
    assert_that(retrieved_quote.is_complete, equal_to(True))
    assert_that(retrieved_quote.id, equal_to(original_quote.id))
    assert_that(retrieved_quote.created, equal_to(original_quote.created))


@step("the updated timestamp did increase")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    qs: QuoteService = context.quote_service
    original_quote = context.quote
    retrieved_quote = qs.get_quote(context.quote.id)
    assert_that(retrieved_quote.created, equal_to(original_quote.created))
    assert_that(retrieved_quote.updated, greater_than(original_quote.updated))


@when("a request is sent to delete the quote")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    qs: QuoteService = context.quote_service
    qs.delete_quote(context.quote.id)


@then("the quote is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    qs: QuoteService = context.quote_service
    assert_that(qs.get_quote(context.quote.id), is_(None))


@step("the created timestamp is unchanged")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    updated_quote = context.updated_quote
    original_quote = context.quote
    retrieved_quote = context.quote_service.get_quote(context.quote.id)
    assert_that(retrieved_quote.created, equal_to(original_quote.created))
    assert_that(retrieved_quote.created, not_(equal_to(updated_quote.created)))
