from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_EMAIL = (By.ID, 'email')
    AUTH_PASS = (By.ID, 'pass')
    AUTH_BTN = (By.CLASS_NAME, 'btn-success')


class StartLocators:
    SUBMIT_BTN = (By.CLASS_NAME, 'btn.btn-success')


class NewUserLocators:
    NEW_USER_BTN = (By.CSS_SELECTOR, 'a[href="/login"]')


class AllPetsLocators:
    MY_PETS_BTN = (By.XPATH, "//a[@href='/my_pets']")
    ALL_PETS_IMAGES = (By.CLASS_NAME, 'card-img-top')
    ALL_PETS_NAMES = (By.CLASS_NAME, 'card-title')
    ALL_PETS_DESC = (By.CLASS_NAME, 'card-text')
    EXIT_BTN = (By.XPATH, "//button[@class='btn btn-outline-secondary']")

class MyPetsLocators:
    MY_PETS_BTN = (By.XPATH, "//a[@href='/my_pets']")
    MY_PETS_NAME = (By.TAG_NAME, "h2")
    EXIT_BTN = (By.XPATH, "//button[@class='btn btn-outline-secondary']")