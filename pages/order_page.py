import allure

from pages.base_page import BasePage
from locators import Locators


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.window_text = None

    def get_cookie(self):
        self.click_to_element(Locators.GET_COOKIE_BUTTON)

    @allure.step('Клик по кнопке "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.click_to_element(Locators.ORDER_BUTTON)

    @allure.step('Клик по кнопке "Заказать" на главной странице')
    def click_order_button_on_page(self):
        self.click_to_element(Locators.ORDER_BUTTON_ON_PAGE)

    @allure.step('Ввод имени')
    def input_name(self, name):
        self.add_text_to_element(Locators.NAME_INPUT, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname):
        self.add_text_to_element(Locators.SURNAME_INPUT, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address):
        self.add_text_to_element(Locators.ADDRESS_INPUT, address)

    @allure.step('Выбор станции метро для первого теста')
    def choose_metro_station_1(self):
        self.click_to_element(Locators.METRO_STATION_INPUT)
        self.click_to_element(Locators.METRO_STATION_1)

    @allure.step('Выбор станции метро для второго теста')
    def choose_metro_station_2(self):
        self.click_to_element(Locators.METRO_STATION_INPUT)
        self.click_to_element(Locators.METRO_STATION_2)

    @allure.step('Ввод номера телефона')
    def input_phone(self, phone):
        self.add_text_to_element(Locators.PHONE_INPUT, phone)

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_to_element(Locators.NEXT_BUTTON)

    @allure.step('Ввод даты')
    def input_date(self, date):
        self.add_text_to_element(Locators.DATE_INPUT, date)

    @allure.step('Выбор срока аренды на 1 день')
    def choose_rental_period_1_day(self):
        self.click_to_element(Locators.RENTAL_PERIOD_INPUT)
        self.click_to_element(Locators.RENT_PERIOD_1_DAY)

    @allure.step('Выбор срока аренды на 5 дней')
    def choose_rental_period_5_days(self):
        self.click_to_element(Locators.RENTAL_PERIOD_INPUT)
        self.click_to_element(Locators.RENT_PERIOD_5_DAYS)

    @allure.step('Выбор серого цвета самоката')
    def choose_color_grey(self):
        self.click_to_element(Locators.CHECKBOX_COLOR_GREY)

    @allure.step('Выбор чёрного цвета самоката')
    def choose_color_black(self):
        self.click_to_element(Locators.CHECKBOX_COLOR_BLACK)


    @allure.step('Клик на кнопку "Да"')
    def click_yes_button(self):
        self.click_to_element(Locators.YES_BUTTON)

    @allure.step('Проверка оформления заказа ')
    def check_confirm_order(self):
        window_text = self.get_text_from_element(Locators.PLACE_ORDER_WINDOW)
        assert 'Заказ оформлен' in window_text, 'Не появилось всплывающее окно с сообщением об успешном создании заказа'

    def place_order_using_button_in_header(self, name, surname, address, phone, date):
        self.get_cookie()
        self.click_order_button_in_header()
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_metro_station_1()
        self.input_phone(phone)
        self.click_next_button()
        self.input_date(date)
        self.choose_rental_period_1_day()
        self.choose_color_black()
        self.click_order_button_on_page()
        self.click_yes_button()
        self.check_confirm_order()

    def place_order_using_button_on_page(self, name, surname, address, phone, date):
        self.get_cookie()
        self.click_order_button_on_page()
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_metro_station_2()
        self.input_phone(phone)
        self.click_next_button()
        self.input_date(date)
        self.choose_rental_period_5_days()
        self.choose_color_grey()
        self.click_order_button_on_page()
        self.click_yes_button()
        self.check_confirm_order()

