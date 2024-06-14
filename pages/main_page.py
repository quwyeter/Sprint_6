import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import data
from pages.base_page import BasePage
from locators import Locators


class MainPage(BasePage):

    @allure.step('Клик по логотипу "Яндекс"')
    def yandex_logo_click(self):
        self.click_to_element(Locators.YANDEX_lOGO)

    @allure.step('Клик по логотипу "Самокат"')
    def scooter_logo_click(self):
        self.click_to_element(locator=Locators.SCOOTER_LOGO)

    @allure.step('Клик по кнопке "Заказать"')
    def order_button_click(self):
        self.click_to_element(locator=Locators.ORDER_BUTTON)

    def wait_dzen_url(self):
        self.wait_url(data.DZEN_URL)

    def wait_main_page_url(self):
        self.wait_url(data.MAIN_PAGE_URL)

    def get_current_url(self):
        return self.current_url()
