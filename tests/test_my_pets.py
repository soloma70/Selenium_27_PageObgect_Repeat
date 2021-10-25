import time
from pages.url_list import PetFriend
from pages.all_pets_page import AllPetsPage
from pages.my_pets_page import MyPetsPage
from settings import valid_name



def test_visit_my_pets(web_driver_with_cookies):
    page = MyPetsPage(web_driver_with_cookies)
    page.my_pets_click()
    assert page.get_relative_link() == '/my_pets', 'Login error'
    assert page.name_user == valid_name, 'Non valid name'


def test_show_my_pets(web_driver):
    """Тест проверяет загрузку страницы "Мои питомцы", наличие имени, возраста и породы; в статистике пользователя и в
    таблице одинаковае количество питомцев; хотя бы у половины питомцев есть фото; в таблице нет повторяющихся питомцев
    и повторяющихся имен питомцев"""
    # Переход на страницу "Мои питомцы"
    web_driver.find_element_by_xpath("//a[@href='/my_pets']").click()
    # Проверяем, что мы оказались на странице пользователя My Pets
    assert web_driver.find_element_by_tag_name('h2').text == valid_name
    # Получение массива данных из таблицы моих питомцев
    images_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr th img')
    names_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(1)')
    types_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(2)')
    ages_my_pets = web_driver.find_elements_by_css_selector('div#all_my_pets table tbody tr td:nth-of-type(3)')
    # Получение количества питомцев из статистики пользователя
    count_my_pets = web_driver.find_element_by_css_selector('html body div div div').text.split('\n')
    count_my_pets_count = int((count_my_pets[1].split(' '))[1])
    # Объявление списка переменных и присваивание им пустых значений
    count_my_pets_name = 0
    count_my_pets_img = 0
    names_my_pets_mas = []
    types_my_pets_mas = []
    ages_my_pets_mas = []
    list_my_pets = []
    unique_list_my_pets = []
    # Перебор массива имен
    for j in range(len(names_my_pets)):
        count_my_pets_name += 1
        # Проверка фото питомца и обновление счетчика фото
        if images_my_pets[j].get_attribute('src') != '':
            count_my_pets_img += 1
        # Добавляем в списки имя, породу и возраст
        names_my_pets_mas += names_my_pets[j].text.split(", ")
        types_my_pets_mas += types_my_pets[j].text.split(", ")
        ages_my_pets_mas += ages_my_pets[j].text.split(", ")
        # Добавляем в список имя, породу и возраст
        list_my_pets.append([names_my_pets[j].text, types_my_pets[j].text, ages_my_pets[j].text])
        # Проверяем условие вхождения в список, если не входит - добавляем
        if list_my_pets[j] not in unique_list_my_pets:
            unique_list_my_pets.append(list_my_pets[j])
        # Проверяем, что у питомца j есть имя, возраст и порода (т.е.не пустые)
        assert names_my_pets[j].text != ''
        assert types_my_pets[j].text != ''
        assert ages_my_pets[j].text != ''

    # Присутствуют все питомцы
    assert count_my_pets_count == count_my_pets_name\
        , 'ERROR: В статистике пользователя и в таблице разное количество питомцев'
    # Хотя бы у половины питомцев есть фото
    assert count_my_pets_count / 2 <= count_my_pets_img, 'ERROR: Фото есть менее, чем у половины питомцев'
    # У всех питомцев разные имена
    assert len(names_my_pets_mas) == len(set(names_my_pets_mas)), 'ERROR: Есть повторяющиеся имена'
    # В списке нет повторяющихся питомцев
    assert len(list_my_pets) == len(unique_list_my_pets), 'ERROR: Есть повторяющиеся питомцы'


def test_exit_visit_my_pets(web_driver_with_cookies):
    page = MyPetsPage(web_driver_with_cookies)
    page.exit_btn_click()
    assert web_driver_with_cookies.find_element_by_xpath(
        "//button[@class='btn btn-success']").text == 'Зарегистрироваться' \
        , 'ERROR: ошибка Log Out'
    time.sleep(3)