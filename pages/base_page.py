from urllib.parse import urlparse

class BasePage(object):
    # Конструктор класса - метод init, получающий объект веб-драйвера, адрес страницы и время ожидания элемента
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path