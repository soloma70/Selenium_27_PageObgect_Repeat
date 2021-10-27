import time, os
from pages.my_pets_page import MyPetsPage
from settings import *
from selenium.webdriver.common.by import By


def test_visit_my_pets(web_driver_with_cookies):
    """Тест проверяет загрузку страницы "Мои питомцы" """

    page = MyPetsPage(web_driver_with_cookies)
    # Проверка, что мы на странице и имя пользователя соответствует ожидаемому
    assert page.get_relative_link() == '/my_pets', 'Login error'
    assert page.name_user == valid_name, 'Non valid name'


def test_show_my_pets(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" проверяет у питомцев наличие имени, возраста и породы;
    в статистике пользователя и в таблице одинаковае количество питомцев;
    хотя бы у половины питомцев есть фото;
    в таблице нет повторяющихся питомцев и повторяющихся имен питомцев"""

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)

    # Объявление списка переменных и присваивание им пустых значений
    count_my_pets_name, count_my_pets_img = 0, 0
    list_names_my_pets, list_types_my_pets, list_ages_my_pets = [], [], []
    list_my_pets, unique_list_my_pets = [], []

    # Перебор массива имен
    print('\nПроверяем питомцев:')
    for j in range(len(page.names_my_pets)):
        count_my_pets_name += 1
        # Проверка фото питомца и обновление счетчика фото
        if page.images_my_pets[j].get_attribute('src') != '':
            count_my_pets_img += 1
        # Добавляем в списки имя, породу и возраст
        list_names_my_pets += page.names_my_pets[j].text.split(", ")
        list_types_my_pets += page.types_my_pets[j].text.split(", ")
        list_ages_my_pets += page.ages_my_pets[j].text.split(", ")
        # Добавляем в список имя, породу и возраст
        list_my_pets.append([page.names_my_pets[j].text, page.types_my_pets[j].text, page.ages_my_pets[j].text])
        # Проверяем условие вхождения в список, если не входит - добавляем
        if list_my_pets[j] not in unique_list_my_pets:
            unique_list_my_pets.append(list_my_pets[j])
        # Проверяем, что у питомца j есть имя, возраст и порода (т.е.не пустые)
        print(f'{page.names_my_pets[j].text}, {page.types_my_pets[j].text}, {page.ages_my_pets[j].text}... Ok')
        assert page.names_my_pets[j].text != ''
        assert page.types_my_pets[j].text != ''
        assert page.ages_my_pets[j].text != ''

    # Присутствуют все питомцы
    my_pets_count_stat = page.my_pets_count_stat_int()
    print(f'\nВ статистике питомцев: {my_pets_count_stat}')
    print(f'Актуально питомцев: {count_my_pets_name}')
    assert my_pets_count_stat == count_my_pets_name \
        , 'ERROR: В статистике пользователя и в таблице разное количество питомцев'
    # Хотя бы у половины питомцев есть фото
    print(f'Питомцев с фото: {count_my_pets_img}')
    assert my_pets_count_stat / 2 <= count_my_pets_img, 'ERROR: Фото есть менее, чем у половины питомцев'
    # У всех питомцев разные имена
    print('У всех питомцев разные имена')
    assert len(list_names_my_pets) == len(set(list_names_my_pets)), 'ERROR: Есть повторяющиеся имена'
    # В списке нет повторяющихся питомцев
    print('В списке нет повторяющихся питомцев')
    assert len(list_my_pets) == len(unique_list_my_pets), 'ERROR: Есть повторяющиеся питомцы'


def test_add_pet_and_cancel(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" проверяет окно добавления питомца
    и закрывает окно кнопкой "Отмена" """

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)
    page.add_pet_click()
    time.sleep(2)
    page.cancel_click()
    time.sleep(2)
    assert page.block_add_pet.is_displayed() == False, 'ERROR: Окно добавления питомца не закрыто'
    print('\nОкно добавления питомца успешно закрыто кнопкой "Отмена"')


def test_add_pet_and_cross(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" проверяет окно добавления питомца
    и закрывает окно крестиком """

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)
    page.add_pet_click()
    time.sleep(2)
    page.cross_click()
    time.sleep(2)
    assert page.block_add_pet.is_displayed() == False, 'ERROR: Окно добавления питомца не закрыто'
    print('\nОкно добавления питомца успешно закрыто "крестиком"')


def test_add_pet_and_add(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" проверяет окно добавления питомца
    и добавляет фото, имя, породу и возраст питомца """

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)
    page.add_pet_click()
    page.enter_photo(img_pet)
    page.enter_name(name_pet)
    page.enter_type(type_pet)
    page.enter_age(age_pet)
    page.add_click()
    print(f'Питомец {name_pet}, {type_pet}, {age_pet} + фото успешно добавлен!')
    time.sleep(2)


def test_exit_visit_my_pets(web_driver_with_cookies):
    """Тест проверяет кнопку выхода со страницы "Мои питомцы" """

    page = MyPetsPage(web_driver_with_cookies)
    page.exit_btn_click()
    # Проверка, что мы на стартовой странице
    assert web_driver_with_cookies.find_element_by_xpath(
        "//button[@class='btn btn-success']").text == 'Зарегистрироваться' \
        , 'ERROR: ошибка Log Out'
