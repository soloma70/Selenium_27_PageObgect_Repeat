from .base_page import BasePage
from .locators import AllPetsLocators
from .url_list import PetFriend
from selenium.webdriver.common.by import By
import os


class AllPetsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # url = os.getenv('LOGIN_URL') or 'https://petfriends1.herokuapp.com/login'
        driver.get(PetFriend.ALL_PETS_URL)
        self.my_pets_btn = driver.find_element(*AllPetsLocators.MY_PETS_BTN)
        self.exit_btn = driver.find_element(*AllPetsLocators.EXIT_BTN)
        self.images_all_pets = driver.find_elements(*AllPetsLocators.ALL_PETS_IMAGES)
        self.names_all_pets = driver.find_elements(*AllPetsLocators.ALL_PETS_NAMES)
        self.desc_all_pets = driver.find_elements(*AllPetsLocators.ALL_PETS_DESC)

    def my_pets_click(self):
        self.my_pets_btn.click()


    def exit_btn_click(self):
        self.exit_btn.click()
