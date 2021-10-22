from .base_page import BasePage
from .locators import AllPetsLocators
from .url_list import PetFriend
import os


class AllPetsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # url = os.getenv('LOGIN_URL') or 'https://petfriends1.herokuapp.com/login'
        driver.get(PetFriend.ALL_PETS_URL)
        self.my_pets_btn = driver.find_element(*AllPetsLocators.MY_PETS_BTN)
        self.exit_btn = driver.find_element(*AllPetsLocators.EXIT_BTN)

    def my_pets_click(self):
        self.my_pets_btn.click()

    def exit_click(self):
        self.exit_btn.click()
