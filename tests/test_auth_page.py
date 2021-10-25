import pytest
from pages.auth_page import AuthPage
from settings import valid_email, valid_password

@pytest.mark.parametrize("nv_email",
                        ['12356@g.com', AuthPage.generate_string(255), AuthPage.generate_string(1001)
                        , AuthPage.russian_chars(), AuthPage.russian_chars().upper(), AuthPage.chinese_chars()
                        , AuthPage.special_chars(), 123]
                        , ids= ['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
@pytest.mark.parametrize("nv_password",
                        ['123456', AuthPage.generate_string(255), AuthPage.generate_string(1001)
                        , AuthPage.russian_chars(), AuthPage.russian_chars().upper(), AuthPage.chinese_chars()
                        , AuthPage.special_chars(), 123]
                        , ids= ['any', '255 sym', '> 1000 sym', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
def test_auth_page_negativ(web_driver, nv_email, nv_password):
    page = AuthPage(web_driver)
    page.enter_email(nv_email)
    page.enter_pass(nv_password)
    page.btn_click()
    print('\nЗапрет на авторизацию. Проверено')
    assert page.get_relative_link() != '/all_pets', 'Login error'



def test_auth_page_with_valid_data(web_driver):
    page = AuthPage(web_driver)
    page.enter_email(valid_email)
    page.enter_pass(valid_password)
    page.btn_click()
    print('\nУспешная авторизация и переход на страницу всех питомцев')
    assert page.get_relative_link() == '/all_pets', 'Login error'
