import time
from pages.all_pets_page import AllPetsPage
from pages.my_pets_page import MyPetsPage


def test_visit_all_pets(web_driver_with_cookies):
    page = AllPetsPage(web_driver_with_cookies)
    print('\nПроверяем, что мы на странице всех питомцев...')
    assert page.get_relative_link() == '/all_pets', 'Ошибка логина'
    print('Ok')
    time.sleep(3)


def test_scroll_all_pets(web_driver_with_cookies):
    page = AllPetsPage(web_driver_with_cookies)
    print('\nПроверяем, что мы на странице всех питомцев...')
    assert page.get_relative_link() == '/all_pets', 'Ошибка логина'
    print('Ok')
    print('\nПроверяем скрол вниз и вверх...')
    web_driver_with_cookies.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    web_driver_with_cookies.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
    time.sleep(2)
    print('Ok')


def test_data_all_pets(web_driver_with_cookies):
    """Тест проверяет наличие фото у питомца, наличие имени, возраста и породы"""
    page = AllPetsPage(web_driver_with_cookies)
    print('Проверяем, что мы на странице всех питомцев...')
    assert page.get_relative_link() == '/all_pets', 'Ошибка логина'
    print('Ok')
    print('Проверяем, что есть фото, имя, порода и возраст у питомцев...')
    count_name = 0
    all_pets_without_photo = []
    count_photo = 0
    all_pets_without_type = []
    count_type = 0
    all_pets_without_age = []
    count_age = 0
    for i in range(len(page.names_all_pets)):
        # assert page.images_all_pets[i].get_attribute('src') != '', f'Нет фото у питомца {page.names_all_pets[i].text}'
        if page.images_all_pets[i].get_attribute('src') != '':
            count_photo += 1
        else:
            all_pets_without_photo.append(page.names_all_pets[i].text)
        # assert page.names_all_pets[i].text != '', 'Пустое имя питомца'
        if page.names_all_pets[i].text != '':
            count_name += 1
        assert page.desc_all_pets[i].text != '', 'Пустые порода и возраст у питомца'
        # assert ',' in page.desc_all_pets[i], 'Пустые порода и возраст у питомца'
        parts_all_pets = page.desc_all_pets[i].text.split(',')
        # assert len(parts_all_pets[0]) > 0, f'Не указана порода у питомца {page.names_all_pets[i].text}'
        if len(parts_all_pets[0]) > 0:
            count_type += 1
        else:
            all_pets_without_type.append(page.names_all_pets[i].text)
        # assert len(parts_all_pets[1]) > 0, f'Не указан возраст у питомца {page.names_all_pets[i].text}'
        if len(parts_all_pets[1]) > 0:
            count_age += 1
        else:
            all_pets_without_age.append(page.names_all_pets[i].text)

    print(
        f'Всего питомцев: {len(page.names_all_pets)}, из них с именем {count_name}, с фото: {count_photo}, с породой: {count_type}, с возрастом: {count_age}')
    print('Нет фото у питомцев: ')
    print(all_pets_without_photo)
    print('Нет породы у питомцев: ')
    print(all_pets_without_type)
    print('Нет возраста у питомцев: ')
    print(all_pets_without_age)


def test_exit_visit_all_pets(web_driver_with_cookies):
    page = MyPetsPage(web_driver_with_cookies)
    page.exit_btn_click()
    assert web_driver_with_cookies.find_element_by_xpath(
        "//button[@class='btn btn-success']").text == 'Зарегистрироваться' \
        , 'ERROR: ошибка Log Out'
    time.sleep(3)
