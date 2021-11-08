import datetime
from datetime import date
from behave import given, when, then
from core.model.membership import Membership
from core.model.roles import Role
from core.model.membership_status import MembershipStatusFactory, MembershipStatus
from isodate import duration, Duration
from hamcrest import *

@given("a membership with a start date of {start_date}")
def step_impl(context, start_date: str):
    """
    :type context: behave.runner.Context
    :type start_date: str
    """
    y, m, d = start_date.split("-")
    context.start_date = date(int(y), int(m), int(d))


@when("a term time of {term:d} months")
def step_impl(context, term: int):
    """
    :type context: behave.runner.Context
    :type term: int
    """
    context.term = term


@then("the renewal date will be {renewal_date}")
def step_impl(context, renewal_date: str):
    """
    :type context: behave.runner.Context
    :type renewal_date: str
    """
    y, m, d = renewal_date.split("-")
    expected = date(int(y), int(m), int(d))
    membership = Membership(start_date=context.start_date, term_months=context.term, name="")
    assert_that(membership.renewal_date, equal_to(expected))


@given("a user with {role} role")
def step_impl(context, role: str):
    """
    :type context: behave.runner.Context
    :type role: str
    """
    context.role = Role[role]


@given("they {have_or_do_not_have} a valid membership")
def step_impl(context, have_or_do_not_have: str):
    """
    :type context: behave.runner.Context
    :type have_or_do_not_have: str
    """
    context.membership = Membership(name="") if have_or_do_not_have == "have" else None


@given("they have accumulated {points:d} points")
def step_impl(context, points: int):
    """
    :type context: behave.runner.Context
    :type points: int
    """
    context.points = points


@when("their membership status is requested")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.membership_status = MembershipStatusFactory.get_membership_status(context.role, context.points,
                                                                              context.membership)


@then("their membership status will be {status}")
def step_impl(context, status: str):
    """
    :type context: behave.runner.Context
    :type status: str
    """
    expected_status = MembershipStatus[status]
    assert_that(context.membership_status, equal_to(expected_status))
