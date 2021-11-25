from behave import *

from core.repository import mysql
from core.service.profile_service import ProfileService
from core.service.quote_service import QuoteService
from core.service.user_service import UserService
from test import test_db

unique_id = 0


@given("a clean database has been created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_db.set_up()


@step("a QuoteService instance")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.quote_service = QuoteService()


@step("registered users exist in the database with profiles")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global unique_id
    context.registered_user_email = f"mock@email{unique_id}.mock"
    context.registered_user_password = "password"
    context.registered_user_id = UserService().register(
        context.registered_user_email,
        context.registered_user_password
    ).id
    context.user_id = context.registered_user_id
    unique_id += 1

    context.profile = ProfileService().insert_profile({"user_id": context.registered_user_id})


@step("insurance packages are defined")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    con = mysql.connect()
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO `insurance_package`(`type`, `name`, `details`, `base_annual_price`) "
                    "VALUES ('Motor','The Motor One','',5.00)")
        con.commit()
        context.package_id = cur.lastrowid
    finally:
        cur.close()
        con.close()
