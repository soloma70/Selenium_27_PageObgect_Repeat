import time
from selenium.webdriver.common.action_chains import ActionChains
from pages.url_list import PetFriend
from pages.all_pets_page import AllPetsPage

def test_visit_all_pets(web_driver_with_cookies):
    web_driver_with_cookies.get(PetFriend.ALL_PETS_URL)
    assert web_driver_with_cookies.title == 'PetFriends: My Pets'
    # time.sleep(3)

def test_scroll(web_driver_with_cookies):
    # web_driver_with_cookies.get(PetFriend.ALL_PETS_URL)
    # assert web_driver_with_cookies.title == 'PetFriends: My Pets'
    web_driver_with_cookies.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

def test_visit_my_pets(web_driver_with_cookies):
    page = AllPetsPage(web_driver_with_cookies)
    page.my_pets_btn_click()
    assert page.get_relative_link() == '/my_pets', 'Login error'
    web_driver_with_cookies.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)