import time
from pages.start_page import StartPage


def test_start_page(web_driver):
    page_start = StartPage(web_driver)
    time.sleep(2)
    page_start.start_click()
    print('\nПроверяем, что мы находимся на стартовой странице и переходим на страницу регистрации нового пользователя')
    assert page_start.get_relative_link() == '/new_user', 'Transition error'
    time.sleep(2)
