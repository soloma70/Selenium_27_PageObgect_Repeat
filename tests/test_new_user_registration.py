import time
from pages.new_user_page import NewUserPage


def test_new_user_page(web_driver):
    page_user = NewUserPage(web_driver)
    print('\nПроверяем, что мы находимся на странице регистрации нового пользователя')
    assert page_user.get_relative_link() == '/new_user', 'Transition error'
    time.sleep(2)
