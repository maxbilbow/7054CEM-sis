from datetime import date

from behave import given, when, then
from hamcrest import *

from core.model.membership import Membership
from core.model.membership_type import MembershipType, MembershipTypeFactory
from core.model.profile import Profile
from core.model.roles import Role
from repository.membership_repository import MembershipRepository
from service.membership_service import MembershipService


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
    points = context.points if "points" in context else 0
    role = context.role if "role" in context else Role.Member
    profile = Profile(user_id=0, points=points, role=role)
    ms = MembershipService(MembershipRepository())
    context.membership = ms.new_membership(profile=profile, start_date=context.start_date,
                                           term_months=context.term)


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


@given("a user profile with {role} role")
def step_impl(context, role: str):
    """
    :type context: behave.runner.Context
    :type role: str
    """
    context.role = Role[role]


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
    context.membership_status = MembershipTypeFactory.get_membership_type(context.role, context.points)


@then("their membership status will be {membership_type}")
def step_impl(context, membership_type: str):
    """
    :type context: behave.runner.Context
    :type membership_type: str
    """
    expected_type = MembershipType[membership_type]
    assert_that(context.membership_status, equal_to(expected_type))
