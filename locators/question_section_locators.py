from selenium.webdriver.common.by import By


class QuestionSectionLocators:

    FIRST_QUEST = (By.ID, "accordion__heading-0")
    SECOND_QUEST = (By.ID, "accordion__heading-1")
    THIRD_QUEST = (By.ID, "accordion__heading-2")
    FOURTH_QUEST = (By.ID, "accordion__heading-3")
    FIFTH_QUEST = (By.ID, "accordion__heading-4")
    SIXTH_QUEST = (By.ID, "accordion__heading-5")
    SEVENTH_QUEST = (By.ID, "accordion__heading-6")
    EIGHT_QUEST = (By.ID, "accordion__heading-7")

    FIRST_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    SECOND_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    THIRD_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    FOURTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    FIFTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    SIXTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    SEVENTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    EIGHT_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-7']/p")


