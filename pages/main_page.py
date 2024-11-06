from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class MainPage(Page):
    USERNAME_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    CONTINUE_BTN = (By.XPATH, "//a[@wized='loginButton']")

    def open_main(self):
        self.open("https://soft.reelly.io")

    def input_username(self):
        wait = WebDriverWait(self.driver, 5)
        self.input_text("bbkam99@gmail.com", *self.USERNAME_FIELD)

    def input_password(self):
        self.input_text("Purpose2024*", *self.PASSWORD_FIELD)


    def click_continue(self):
        self.click(*self.CONTINUE_BTN)

    def get_current_window(self):
        return self.driver.current_window_handle