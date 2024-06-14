import allure

import data
from pages.main_page import MainPage


class TestMainPageLogo:
    allure.title('Тест клика на логотип самоката')
    allure.description('Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»')

    def test_scooter_logo_click_open_main_page(self, driver):
        page = MainPage(driver)
        main = data.MAIN_PAGE_URL
        page.order_button_click()
        page.scooter_logo_click()
        page.wait_main_page_url()
        assert page.get_current_url() == main

    allure.title('Тест клика на логотип яндекса')
    allure.description('Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')

    def test_yandex_logo_click_open_dzen_page(self, driver):
        page = MainPage(driver)
        dzen = data.DZEN_URL
        page.yandex_logo_click()
        page.switch_window()
        page.wait_dzen_url()
        assert page.get_current_url() == dzen
