from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class NavPanel(Page):

    CONNECT_TO_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")
    EXPECTED_TEXT_FIELD = (By.XPATH, "//div[text()='Choose maximum amount of agents in yours company']")

    def click_connect(self):
        sleep(6)
        self.click(*self.CONNECT_TO_COMPANY_BTN)


    def get_current_window(self):
        self.get_current_window()


    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f"Switching to window {all_windows[1]}")
        self.driver.switch_to.window(all_windows[1])



    def verify_connect(self):
        self.verify_text("Choose maximum amount of agents in yours company",*self.EXPECTED_TEXT_FIELD)
