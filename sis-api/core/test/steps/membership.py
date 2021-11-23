from datetime import date

from behave import given, when, then
from hamcrest import *
from isodate import duration

from core.model.membership import Membership
from core.model.membership_type import MembershipType, get_membership_type
from core.model.profile import Profile
from core.repository.membership import MembershipRepository
from core.service.membership_service import MembershipService


@given("a start date of {start_date}")
def step_impl(context, start_date: str):
    """
    :type context: behave.runner.Context
    :type start_date: str
    """
    y, m, d = start_date.split("-")
    context.start_date = date(int(y), int(m), int(d))


@given("a term time of {term:d} months")
def step_impl(context, term: int):
    """
    :type context: behave.runner.Context
    :type term: int
    """
    context.term = term


@when("a new membership is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ms = MembershipService(MembershipRepository())
    context.membership = ms.new_membership(user_id=-1, end_date=context.start_date)


@then("the renewal date will be {end_date}")
def step_impl(context, end_date: str):
    """
    :type context: behave.runner.Context
    :type end_date: str
    """
    y, m, d = end_date.split("-")
    expected = date(int(y), int(m), int(d))
    membership = context.membership
    assert_that(membership.end_date, equal_to(expected))


@given("a user profile with {points:d} points")
def step_impl(context, points: int):
    """
    :type context: behave.runner.Context
    :type points: int
    """
    context.points = points


@given("they {have_or_do_not_have} a valid membership")
def step_impl(context, have_or_do_not_have: str):
    """
    :type context: behave.runner.Context
    :type have_or_do_not_have: str
    """
    context.membership = Membership() if have_or_do_not_have == "have" else None


@when("their membership status is requested")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.membership_status = get_membership_type(context.points)


@then("their membership status will be {membership_type}")
def step_impl(context, membership_type: str):
    """
    :type context: behave.runner.Context
    :type membership_type: str
    """
    expected_type = MembershipType[membership_type]
    assert_that(context.membership_status, equal_to(expected_type))


@given("an end_date not after today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.end_date = date.today()


@when("a new membership is requested")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        MembershipService().new_membership(1, end_date=date.today())
    except Exception as e:
        context.error = e


@then("an error is thrown")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.error is not None


@given("the user has an active membership")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    MembershipService().new_membership(context.user_id, date.today() + duration.timedelta(days=1))
