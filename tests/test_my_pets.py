import time
from pages.my_pets_page import MyPetsPage
from settings import valid_name


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


def test_add_pet_positiv(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" проверяет окно добавления питомца
    и добавляет фото, имя, породу и возраст питомца """

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)
    # Добавление случайного питомца из списка (возможно повторение)
    list_pet = page.list_pets
    # Открітие окна добавленяи питомца и добавление его
    page.add_pet_click()
    page.enter_photo(list_pet['img'])
    page.enter_name(list_pet['name'])
    page.enter_type(list_pet['type'])
    page.enter_age(list_pet['age'])
    page.add_click()
    time.sleep(2)
    # Новая загрузка страницы "Мои питомцы"
    page_new = MyPetsPage(web_driver_with_cookies)
    # Проверяем, что последнее добавленые атрибут 'scr', имя, порода и возраст питомца соответствует заданному
    # - означает, что питомец добавлен.
    assert page_new.images_my_pets[-1].get_attribute('src') != '', 'ERROR: Ошибка добавления фото питомца'
    assert page_new.names_my_pets[-1].text == list_pet['name'], 'ERROR: Ошибка добавления имени питомца'
    assert page_new.types_my_pets[-1].text == list_pet['type'], 'ERROR: Ошибка добавления породы питомца'
    assert page_new.ages_my_pets[-1].text == list_pet['age'], 'ERROR: Ошибка добавления возраста питомца'
    print(f"\nПитомец {list_pet['name']}, {list_pet['type']}, {list_pet['age']} лет + фото успешно добавлен!")


def test_del_pet_positiv(web_driver_with_cookies):
    """Тест на странице "Мои питомцы" удаляет последнего добавленого питомца в списке и проверяет удаление """

    # Переход на страницу "Мои питомцы"
    page = MyPetsPage(web_driver_with_cookies)
    # Если питомцев нет - добавляем питомца
    count_stat_before = page.my_pets_count_stat_int()
    if count_stat_before == 0:
        list_pet = page.list_pets
        page.add_pet_click()
        print(f"\nНет питомцев. Добавляем питомца {list_pet['name']}")
        page.enter_photo(list_pet['img'])
        page.enter_name(list_pet['name'])
        page.enter_type(list_pet['type'])
        page.enter_age(list_pet['age'])
        page.add_click()
        count_stat_before += 1
    time.sleep(2)
    page_new = MyPetsPage(web_driver_with_cookies)
    # Получаем имя последнего питомца на странице преред удалением
    name_last_pet = page_new.names_my_pets[-1].text
    page_new.del_pet_click()
    # Новая загрузка страницы "Мои питомцы"
    time.sleep(2)
    page_new2 = MyPetsPage(web_driver_with_cookies)
    count_stat_after = page_new2.my_pets_count_stat_int()
    # Сравниваем количество питомцев до и после удаления.
    assert count_stat_before - 1 == count_stat_after, 'ERROR: Ошибка удаления имени питомца'
    print(f'\nПитомец {name_last_pet} успешно удален!')


def test_exit_visit_my_pets(web_driver_with_cookies):
    """Тест проверяет кнопку выхода со страницы "Мои питомцы" """

    page = MyPetsPage(web_driver_with_cookies)
    name_user = page.name_user
    page.exit_btn_click()
    # Проверка, что мы на стартовой странице
    assert web_driver_with_cookies.find_element_by_xpath(
        "//button[@class='btn btn-success']").text == 'Зарегистрироваться' \
        , 'ERROR: ошибка Log Out'
    print(f'\nУспешный выход из пользования {name_user}')
