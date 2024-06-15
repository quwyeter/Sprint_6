import pytest

import data
from pages.order_page import OrderPage
import allure


class TestOrderPage:
    @allure.title('Тест заказа самоката по кнопке в хедере страницы')
    @pytest.mark.parametrize('name, surname, address, phone, date', data.TEST_DATA)
    def test_order_by_button_in_header(self, driver, name, surname, address, phone, date):
        page = OrderPage(driver)
        page.place_order_using_button_in_header(name, surname, address, phone, date)

    @allure.title('Тест заказа самоката по кнопке внизу страницы')
    @pytest.mark.parametrize('name, surname, address, phone, date', data.TEST_DATA)
    def test_order_by_button_on_page(self, driver, name, surname, address, phone, date):
        page = OrderPage(driver)
        page.place_order_using_button_on_page(name, surname, address, phone, date)
