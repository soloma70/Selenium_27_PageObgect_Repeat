from .base_page import BasePage
from .locators import AuthLocators
from .url_list import PetFriend
import os

class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # url = os.getenv('LOGIN_URL') or 'https://petfriends1.herokuapp.com/login'
        driver.get(PetFriend.LOGIN_URL)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_pass(self, value):
        self.passw.send_keys(value)

    def btn_click(self):
        self.btn.click()

    # Вспомашательные функции для добавления различных строк
    def generate_string(n):
        return "x" * n

    def russian_chars():
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def chinese_chars():
        return '的一是不了人我在有他这为之大来以个中上们'

    def special_chars():
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'