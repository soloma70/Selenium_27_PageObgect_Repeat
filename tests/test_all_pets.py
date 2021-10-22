import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.url_list import PetFriend
from pages.all_pets_page import AllPetsPage
from settings import valid_name


def test_visit_all_pets(web_driver_with_cookies):
    web_driver_with_cookies.get(PetFriend.ALL_PETS_URL)
    assert web_driver_with_cookies.title == 'PetFriends: My Pets'
    # time.sleep(3)


def test_scroll(web_driver_with_cookies):
    # web_driver_with_cookies.get(PetFriend.ALL_PETS_URL)
    # assert web_driver_with_cookies.title == 'PetFriends: My Pets'
    web_driver_with_cookies.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    web_driver_with_cookies.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
    time.sleep(2)


def test_visit_my_pets(web_driver_with_cookies):
    page = AllPetsPage(web_driver_with_cookies)
    page.my_pets_click()
    web_driver_with_cookies.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    web_driver_with_cookies.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
    time.sleep(2)
    assert page.get_relative_link() == '/my_pets', 'Login error'
    assert web_driver_with_cookies.find_element_by_tag_name('h2').text == valid_name, 'Non valid name'
