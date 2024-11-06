from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when ('Click Connect the Company icon')
def click_connect(context):
    context.app.nav_panel_page.click_connect()

@when ('Switch to new tab')
def switch_to_new_tab(context):
    context.app.nav_panel_page.switch_to_new_window()


@then('Verify Connect the Company page is open in new tab')
def verify_connect(context):
    context.app.nav_panel_page.verify_connect()

