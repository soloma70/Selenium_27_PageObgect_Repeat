import time
import pytest
from selenium import webdriver
from pages.start_page import StartPage, NewUserPage


@pytest.fixture(scope='module')
def web_driver(request):
    '''Фикстура загружает веб-драйвер Хром, меняет размер окна, устанавливает неявное ожидание,
    после выполнения основного кода закрывает браузер'''
    web_driver = webdriver.Chrome("C:\\1\\chromedriver.exe")
    web_driver.set_window_size(1280, 960)
    web_driver.implicitly_wait(3)
    yield web_driver
    web_driver.quit()


def test_start_page(web_driver):
    page_start = StartPage(web_driver)
    page_start.start_click()
    print('\nПроверяем, что мы находимся на стартовой странице')
    assert page_start.get_relative_link() == '/new_user', 'Transition error'
    time.sleep(2)


def test_new_user_page(web_driver):
    page_user = NewUserPage(web_driver)
    page_user.new_user_click()
    print('\nПроверяем, что мы находимся на странице регистрации нового пользователя')
    assert page_user.get_relative_link() == '/login', 'Transition error'
    time.sleep(2)
