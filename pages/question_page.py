import allure

import data
from pages.base_page import BasePage
from locators import Locators


class QuestionPage(BasePage):
    question_and_answer = [(Locators.COST_QUE, data.ANSWER_1), (Locators.SCOOTER_COUNT_QUE, data.ANSWER_2),
                           (Locators.RENTAL_TIME_QUE, data.ANSWER_3), (Locators.ORDER_TODAY_QUE, data.ANSWER_4),
                           (Locators.EXTEND_ORDER_QUE, data.ANSWER_5), (Locators.CHARGER_QUE, data.ANSWER_6),
                           (Locators.CANCEL_ORDER_QUE, data.ANSWER_7), (Locators.MKAD_QUE, data.ANSWER_8)]

    @allure.step('Найти вопрос и открыть ответ')
    def open_answer(self, que):
        element = self.find_element_by_locator_with_wait(que)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        self.click_to_element(que)

    @allure.step('Найти открытый ответ')
    def find_opened_answer(self):
        self.ans = self.find_element_by_locator_with_wait(Locators.OPENED_ANSWER).text
        return self.ans
