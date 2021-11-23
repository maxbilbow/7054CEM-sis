from behave import *
from hamcrest import *

from core.model import to_dict
from core.repository.user_profile import UserProfileRepository
from core.service.profile_service import ProfileService
from core.service.quote_service import QuoteService
from core.service.user_service import UserService
from swagger_server.models import PersonalDetails, Address

use_step_matcher("re")


@step("a user profile was created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ProfileService().insert_profile({
        "user_id": context.user_id,
        "personal_details": to_dict(PersonalDetails(full_name="", relationship_status="", employment_status="",
                                                    address={}))
    })


@when("a request to delete the user is made")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        UserService().delete_user(context.user_id)
    except Exception as e:
        context.delete_user_error = e


@then("the user is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = UserService().get_user(context.user_id)
    assert_that(user, is_(None))


@step("all the registered user's quotes are deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    qs: QuoteService = context.quote_service
    quotes = qs.find_for_user(context.user_id)
    assert_that(quotes, empty())


@step("the registered user's profile is deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    profile = UserProfileRepository.find_by_user_id(context.user_id)
    assert_that(profile, none())


@then("the user is not deleted")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    user = UserService().get_user(context.user_id)
    assert_that(user, not_none())
