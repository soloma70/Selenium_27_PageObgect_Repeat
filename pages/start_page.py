from .base_page import BasePage
from pages.url_list import PetFriend
from pages.locators import StartLocators, NewUserLocators
import os


class StartPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = PetFriend.START_URL
        driver.get(url)
        self.start_btn = driver.find_element(*StartLocators.SUBMIT_BTN)

    def start_click(self):
        self.start_btn.click()
