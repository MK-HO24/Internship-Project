from pages.base_page import Page
from pages.main_page import MainPage
from pages.nav_panel_page import NavPanel


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.nav_panel_page = NavPanel(driver)