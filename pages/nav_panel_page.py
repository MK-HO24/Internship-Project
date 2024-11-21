from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class NavPanel(Page):

    CONNECT_TO_COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")
    EXPECTED_TEXT_FIELD = (By.XPATH, "//div[text()='Choose your plan']")
    BANNER = (By.XPATH, "//div[@class='lotion-your-h3--price size' and text()='Subscription & payments']")
    MAIN_MENU = (By.XPATH,"//div[@class = 'html-icon-bottom-bar w-embed']")
    USER_ICON = (By.XPATH,"//img[@class='menu-img-agent-listing']")
    SUB_AND_PMT = (By.XPATH, "//div[@class='main-menu-text' and text() = 'Subscription & payments']")


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


    def switch_to_main_menu(self):
        wait = WebDriverWait(self.driver, 10)
        self.click(*self.MAIN_MENU)
        sleep(10)



    def switch_to_user_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        self.wait_to_be_clickable(*self.USER_ICON)
        sleep(10)


    def click_sub_and_pmt(self):
        wait = WebDriverWait(self.driver, 10)
        target = self.driver.find_element(By.XPATH, "//div[@class='main-menu-text' and text()='Subscription & payments']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
        target.click()
        sleep(15)


    def verify_connect(self):
        wait = WebDriverWait(self.driver, 10)
        self.verify_text("Choose your plan",*self.EXPECTED_TEXT_FIELD)


    def verify_connect_mobile(self):
        wait = WebDriverWait(self.driver, 10)
        self.verify_text("Subscription & payments",*self.BANNER)