from .base_page import BasePage
from .locators import MyPetsLocators
from .url_list import PetFriend
import os

class MyPetsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # url = os.getenv('LOGIN_URL') or 'https://petfriends1.herokuapp.com/login'
        driver.get(PetFriend.MY_PETS_URL)
        self.my_pets_btn = driver.find_element(*MyPetsLocators.MY_PETS_BTN)
        self.name_user = driver.find_element(*MyPetsLocators.MY_PETS_NAME).text
        self.exit_btn = driver.find_element(*MyPetsLocators.EXIT_BTN)

    def my_pets_click(self):
        self.my_pets_btn.click()




    def exit_btn_click(self):
        self.exit_btn.click()