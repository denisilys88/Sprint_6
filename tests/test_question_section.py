import pytest
from pages.scooter_delivery_page import ScooterDeliveryPage
from locators.question_section_locators import QuestionSectionLocators as LOC
from data import Data as DATA


class TestQuestionSection:

    LIST_1 = [LOC.FIRST_QUEST, LOC.FIRST_ANSWER, DATA.TEXT_1]
    LIST_2 = [LOC.SECOND_QUEST, LOC.SECOND_ANSWER, DATA.TEXT_2]
    LIST_3 = [LOC.THIRD_QUEST, LOC.THIRD_ANSWER, DATA.TEXT_3]
    LIST_4 = [LOC.FOURTH_QUEST, LOC.FOURTH_ANSWER, DATA.TEXT_4]
    LIST_5 = [LOC.FIFTH_QUEST, LOC.FIFTH_ANSWER, DATA.TEXT_5]
    LIST_6 = [LOC.SIXTH_QUEST, LOC.SIXTH_ANSWER, DATA.TEXT_6]
    LIST_7 = [LOC.SEVENTH_QUEST, LOC.SEVENTH_ANSWER, DATA.TEXT_7]

    @pytest.mark.parametrize('question,answer,text', [LIST_1, LIST_2, LIST_3, LIST_4, LIST_5, LIST_6, LIST_7])
    def test_question_section(self, driver, question, answer, text):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.scrolldown()
        delivery_page.click_cookie()
        element_text = delivery_page.click_on_question_section(question, answer)
        assert element_text == text

