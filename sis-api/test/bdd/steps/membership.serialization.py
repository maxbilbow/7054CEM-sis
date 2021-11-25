from datetime import date

from behave import *

from core.model import to_dict
from core.model.membership import Membership
from core.model.membership_type import MembershipType
from core.utils.serialization import serialize

use_step_matcher("re")


@when("a serialized membership is requested")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.dict = serialize(context.membership).for_api()


@given("a membership is created with date (?P<date_string>.+)")
def step_impl(context, date_string: str):
    """
    :type context: behave.runner.Context
    :type date: str
    """
    date_obj = date.fromisoformat(date_string)
    context.membership = Membership(id=1, user_id=1,start_date=date_obj, end_date=date_obj, type=MembershipType.Smart)


@then("the dates are converted to ISO date format (?P<date_string>.+)")
def step_impl(context, date_string: str):
    """
    :type context: behave.runner.Context
    :type date: str
    """
    assert context.dict["start_date"] == date_string
