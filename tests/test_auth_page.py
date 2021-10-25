from pages.auth_page import AuthPage
from settings import valid_email, valid_password, non_valid_email, non_valid_password


def test_auth_page_negativ(web_driver):
    page = AuthPage(web_driver)
    page.enter_email(non_valid_email)
    page.enter_pass(non_valid_password)
    page.btn_click()
    print('\nПроверяем, что мы не авторизовались')
    assert page.get_relative_link() != '/all_pets', 'Login error'


def test_auth_page_with_valid_data(web_driver):
    page = AuthPage(web_driver)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    print('\nПроверяем, что мы авторизовались и находимся на странице всех питомцев')
    assert page.get_relative_link() == '/all_pets', 'Login error'
