import pytest
import allure
from pages.question_page import QuestionPage


class TestQuestionPage:
    allure.title('Тест выпадающего списка в разделе «Вопросы о важном».')
    allure.description('При клике на стрелочку, открывается соответствующий текст')

    @pytest.mark.parametrize('question, answer', QuestionPage.question_and_answer)
    def test_drop_down_list_on_the_question_page(self, driver, question, answer):
        page = QuestionPage(driver)
        page.open_answer(question)
        page.find_opened_answer()
        assert page.ans == answer
