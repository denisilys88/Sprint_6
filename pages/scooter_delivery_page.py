from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.purchase_locators import PurchaseLocators as LOC
from locators.question_section_locators import QuestionSectionLocators as SEC
from locators.main_and_logo_locators import MainAndLogoLocators as MAIN
from selenium.webdriver.common.action_chains import ActionChains


class ScooterDeliveryPage:

    def __init__(self, driver):
        self.driver = driver

    def click_purchase(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LOC.FIRST_PURCHASE_BUTTON)).click()

    def set_name(self, name):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LOC.INPUT_NAME))
        return self.driver.find_element(*LOC.INPUT_NAME).send_keys(name)

    def set_lastname(self, lastname):
        return self.driver.find_element(*LOC.INPUT_LASTNAME).send_keys(lastname)

    def set_address(self, address):
        return self.driver.find_element(*LOC.INPUT_ADDRESS).send_keys(address)

    def select_metro(self, metro_station):
        self.driver.find_element(*LOC.INPUT_METRO).click()
        return self.driver.find_element(*LOC.INPUT_METRO).send_keys(metro_station, Keys.ARROW_DOWN, Keys.ENTER)

    def set_phonenumber(self, phonenumber):
        return self.driver.find_element(*LOC.INPUT_PHONENUMBER).send_keys(phonenumber)

    def click_next(self):
        return self.driver.find_element(*LOC.NEXT_PURCHASE_BUTTON).click()

    def select_when(self, date):
        return self.driver.find_element(*LOC.INPUT_WHEN).send_keys(date, Keys.ENTER)

    def select_howlong(self, howlong):
        if howlong == 1:
            element = LOC.INPUT_HOWLONG_OPTION_1
        else:
            element = LOC.INPUT_HOWLONG_OPTION_2
        self.driver.find_element(*LOC.INPUT_HOWLONG).click()
        return self.driver.find_element(*element).click()

    def set_checkbox_color(self, colour):
        if colour == 'black':
            element = LOC.INPUT_BLACK_CHECKBOX
        else:
            element = LOC.INPUT_GRAY_CHECKBOX
        return self.driver.find_element(*element).click()

    def set_comment(self, comment):
        return self.driver.find_element(*LOC.INPUT_COMMENT).send_keys(comment)

    def confirm_purchase_popup(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LOC.PURCHASE_POPUP))
        return self.driver.find_element(*LOC.YES_BUTTON).click()

    def get_purchase_status(self):
        return self.driver.find_element(*LOC.PURCHASE_STATUS).text

    def scrolldown(self):
        self.driver.find_element(*LOC.HTML).send_keys(Keys.END)

    def click_cookie(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LOC.COOKIE_BUTTON)).click()

    def click_second_purchase(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LOC.PURCHASE_SECOND_BUTTON))
        return self.driver.find_element(*LOC.PURCHASE_SECOND_BUTTON).click()

    def click_on_question_section(self, question, answer):
        self.driver.find_element(*question).click()
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer)).text

    def click_on_logo(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(MAIN.LOGO)).click()

    def click_on_yandex(self):
        return self.driver.find_element(*MAIN.YANDEX).click()

    def move_on_next_tab(self):
        move = ActionChains(self.driver)
        return move.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
