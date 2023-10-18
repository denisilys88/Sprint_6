import pytest
from pages.scooter_delivery_page import ScooterDeliveryPage
from locators.question_section_locators import QuestionSectionLocators as LOC


class TestQuestionSection:

    LIST_1 = [LOC.FIRST_QUEST, LOC.FIRST_ANSWER, LOC.TEXT_1]
    LIST_2 = [LOC.SECOND_QUEST, LOC.SECOND_ANSWER, LOC.TEXT_2]
    LIST_3 = [LOC.THIRD_QUEST, LOC.THIRD_ANSWER, LOC.TEXT_3]
    LIST_4 = [LOC.FOURTH_QUEST, LOC.FOURTH_ANSWER, LOC.TEXT_4]
    LIST_5 = [LOC.FIFTH_QUEST, LOC.FIFTH_ANSWER, LOC.TEXT_5]
    LIST_6 = [LOC.SIXTH_QUEST, LOC.SIXTH_ANSWER, LOC.TEXT_6]
    LIST_7 = [LOC.SEVENTH_QUEST, LOC.SEVENTH_ANSWER, LOC.TEXT_7]

    @pytest.mark.parametrize('question,answer,text', [LIST_1, LIST_2, LIST_3, LIST_4, LIST_5, LIST_6, LIST_7])
    def test_question_section(self, driver, question, answer, text):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.scrolldown()
        delivery_page.click_cookie()
        element_text = delivery_page.click_on_question_section(question, answer)
        assert element_text == text

