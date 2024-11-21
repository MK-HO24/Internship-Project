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


@when ('Click on main menu')
def switch_to_main_menu(context):
    context.app.nav_panel_page.switch_to_main_menu()


@when ('Click on user profile icon')
def switch_to_user_profile_icon(context):
    context.app.nav_panel_page.switch_to_user_profile_icon()

@when ('Click on subcription and payment')
def click_sub_and_pmt(context):
    context.app.nav_panel_page.click_sub_and_pmt()

@when ('Scroll to bottom')
def scroll_to_bottom(context):
    context.app.nav_panel_page.scroll_to_bottom_of_page()
    sleep(10)


@then('Verify Connect the Company page is open in new tab')
def verify_connect(context):
    context.app.nav_panel_page.verify_connect()

@then('Verify Connect the Company page is open')
def verify_contact_company(context):
    context.app.nav_panel_page.verify_connect_mobile()