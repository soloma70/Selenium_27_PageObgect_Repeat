from pages.start_page import StartPage, NewUserPage


def test_start_page(web_driver):
    page_start = StartPage(web_driver)
    page_start.start_click()

    assert page_start.get_relative_link() == '/new_user', 'Transition error'

def test_new_user_page(web_driver):
    page_user = NewUserPage(web_driver)
    page_user.new_user_click()

    assert page_user.get_relative_link() == '/login', 'Transition error'