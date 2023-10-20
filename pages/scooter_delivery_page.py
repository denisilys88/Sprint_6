from selenium.webdriver import Keys
from locators.purchase_locators import PurchaseLocators as LOC
from locators.main_and_logo_locators import MainAndLogoLocators as MAIN
from pages.base_page import BasePage
from data import Data as DATA


class ScooterDeliveryPage(BasePage):

    def click_purchase(self):
        return self.find_element(LOC.FIRST_PURCHASE_BUTTON).click()

    def set_name(self, name):
        return self.find_element(LOC.INPUT_NAME).send_keys(name)

    def set_lastname(self, lastname):
        return self.find_element(LOC.INPUT_LASTNAME).send_keys(lastname)

    def set_address(self, address):
        return self.find_element(LOC.INPUT_ADDRESS).send_keys(address)

    def select_metro(self, metro_station):
        self.find_element(LOC.INPUT_METRO).click()
        return self.find_element(LOC.INPUT_METRO).send_keys(metro_station, Keys.ARROW_DOWN, Keys.ENTER)

    def set_phonenumber(self, phonenumber):
        return self.find_element(LOC.INPUT_PHONENUMBER).send_keys(phonenumber)

    def click_next(self):
        return self.find_element(LOC.NEXT_PURCHASE_BUTTON).click()

    def select_when(self, date):
        return self.find_element(LOC.INPUT_WHEN).send_keys(date, Keys.ENTER)

    def select_howlong(self, howlong):
        if howlong == 1:
            element = LOC.INPUT_HOWLONG_OPTION_1
        else:
            element = LOC.INPUT_HOWLONG_OPTION_2
        self.find_element(LOC.INPUT_HOWLONG).click()
        return self.find_element(element).click()

    def set_checkbox_color(self, colour):
        if colour == 'black':
            element = LOC.INPUT_BLACK_CHECKBOX
        else:
            element = LOC.INPUT_GRAY_CHECKBOX
        return self.find_element(element).click()

    def set_comment(self, comment):
        return self.find_element(LOC.INPUT_COMMENT).send_keys(comment)

    def confirm_purchase_popup(self):
        self.find_element(LOC.PURCHASE_POPUP)
        return self.find_element(LOC.YES_BUTTON).click()

    def get_purchase_status(self):
        return self.find_element(LOC.PURCHASE_STATUS).text

    def click_cookie(self):
        self.find_element(LOC.COOKIE_BUTTON).click()

    def click_second_purchase(self):
        return self.find_element(LOC.PURCHASE_SECOND_BUTTON).click()

    def click_on_question_section(self, question, answer):
        self.find_element(question).click()
        return self.find_element(answer).text

    def click_on_logo(self):
        return self.find_element(MAIN.LOGO).click()

    def wait_for_main_image_load(self):
        return self.find_element(MAIN.MAIN_IMAGE)

    def click_on_yandex(self):
        return self.find_element(MAIN.YANDEX).click()

    def wait_for_new_page_load(self):
        return self.url_to_change(DATA.DZEN_URL)


