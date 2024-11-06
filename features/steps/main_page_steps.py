from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open reelly main page')
def open_reelly_main_page(context):
    context.app.main_page.open_main()

@when ('Input user name')
def input_username(context):
    context.app.main_page.input_username()


@when('Input user password')
def input_password(context):
    context.app.main_page.input_password()


@when ('Click continue button')
def click_continue(context):
    context.app.main_page.click_continue()

@when ('Get current window handle')
def get_current_window_handle(context):
    context.app.main_page.get_current_window()
