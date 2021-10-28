from .base_page import BasePage
from .locators import MyPetsLocators, AddMyPetsLocators
from .url_list import PetFriend
import os
from random import choice
from settings import list_pest

class MyPetsPage(BasePage):
    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)
        # url = os.getenv('LOGIN_URL') or 'https://petfriends1.herokuapp.com/login'
        driver.get(PetFriend.MY_PETS_URL)
        # Атрибуты поиска имени пользователя и кнопки выход
        self.my_pets_btn = driver.find_element(*MyPetsLocators.MY_PETS_BTN)
        self.name_user = driver.find_element(*MyPetsLocators.MY_PETS_NAME).text
        self.exit_btn = driver.find_element(*MyPetsLocators.EXIT_BTN)
        # Атрибуты поиска массива данных из таблицы моих питомцев
        self.images_my_pets = driver.find_elements(*MyPetsLocators.MY_PETS_IMAGES)
        self.names_my_pets = driver.find_elements(*MyPetsLocators.MY_PETS_NAMES)
        self.types_my_pets = driver.find_elements(*MyPetsLocators.MY_PETS_TYPES)
        self.ages_my_pets = driver.find_elements(*MyPetsLocators.MY_PETS_AGE)
        # Атрибуты поиска количества питомцев из статистики пользователя
        self.my_pets_count_stat = driver.find_element(*MyPetsLocators.MY_PETS_COUNT).text.split('\n')
        # Атрибуты добавления питомца
        self.list_pets = choice(list_pest)
        self.add_pet = driver.find_element(*AddMyPetsLocators.MY_PETS_BTN_ADD_PET)
        self.block_add_pet = driver.find_element(*AddMyPetsLocators.MY_PETS_BLOCK_ADD_PET)
        self.input_photo = driver.find_element(*AddMyPetsLocators.MY_PETS_INPUT_PHOTO)
        self.input_name = driver.find_element(*AddMyPetsLocators.MY_PETS_INPUT_NAME)
        self.input_type = driver.find_element(*AddMyPetsLocators.MY_PETS_INPUT_TYPE)
        self.input_age = driver.find_element(*AddMyPetsLocators.MY_PETS_INPUT_AGE)
        self.add = driver.find_element(*AddMyPetsLocators.MY_PETS_BTN_ADD)
        self.cancel = driver.find_element(*AddMyPetsLocators.MY_PETS_BTN_CANCEL)
        self.cross = driver.find_element(*AddMyPetsLocators.MY_PETS_BTN_CROSS)
        # Атрибуты удаления питомца
        self.del_my_pets = driver.find_elements(*MyPetsLocators.MY_PETS_DEL)


    def my_pets_click(self):
        self.my_pets_btn.click()

    def my_pets_count_stat_int(self):
        self.my_pets_count_stat_int = int((self.my_pets_count_stat[1].split(' '))[1])
        return self.my_pets_count_stat_int

    def add_pet_click(self):
        self.add_pet.click()

    def enter_photo(self, value):
        # self.input_photo.clear()
        self.input_photo.send_keys(os.getcwd() + value)

    def enter_name(self, value):
        self.input_name.clear()
        self.input_name.send_keys(value)

    def enter_type(self, value):
        self.input_type.clear()
        self.input_type.send_keys(value)

    def enter_age(self, value):
        self.input_age.clear()
        self.input_age.send_keys(value)

    def add_click(self):
        self.add.click()

    def cancel_click(self):
        self.cancel.click()

    def cross_click(self):
        self.cross.click()

    def del_pet_click(self):
        self.del_my_pets[-1].click()

    def refresh(self):
        self.driver.refresh()

    def exit_btn_click(self):
        self.exit_btn.click()

