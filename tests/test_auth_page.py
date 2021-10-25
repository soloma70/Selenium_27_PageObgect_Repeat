import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from settings import valid_email, valid_password


@pytest.fixture(scope='module')
def web_driver(request):
     '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
     после выполнения основного кода закрывает браузер'''
     web_driver = webdriver.Chrome("C:\\1\\chromedriver.exe")
     web_driver.set_window_size(1280, 960)
     web_driver.implicitly_wait(3)
     yield web_driver
     web_driver.quit()

def test_auth_page_with_valid_data(web_driver):
    page = AuthPage(web_driver)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    print('\nПроверяем, что мы авторизовались и находимся на странице всех питомцев')
    assert page.get_relative_link() == '/all_pets', 'Login error'
