import allure

from locators import Locators
from pages.base_page import BasePage


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
