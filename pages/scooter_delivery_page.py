import allure
from selenium.webdriver import Keys
from locators.purchase_locators import PurchaseLocators as LOC
from locators.main_and_logo_locators import MainAndLogoLocators as MAIN
from pages.base_page import BasePage
from data import Data as DATA


class ScooterDeliveryPage(BasePage):

    @allure.step('Нажимаем кнопку Заказать')
    def click_purchase(self):
        return self.find_element(LOC.FIRST_PURCHASE_BUTTON).click()

    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        return self.find_element(LOC.INPUT_NAME).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_lastname(self, lastname):
        return self.find_element(LOC.INPUT_LASTNAME).send_keys(lastname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        return self.find_element(LOC.INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбираем станцию метро в поле Станция метро')
    def select_metro(self, metro_station):
        self.find_element(LOC.INPUT_METRO).click()
        return self.find_element(LOC.INPUT_METRO).send_keys(metro_station, Keys.ARROW_DOWN, Keys.ENTER)

    @allure.step('Заполняем поле Телефон')
    def set_phonenumber(self, phonenumber):
        return self.find_element(LOC.INPUT_PHONENUMBER).send_keys(phonenumber)

    @allure.step('Нажимаем кнопку Далее')
    def click_next(self):
        return self.find_element(LOC.NEXT_PURCHASE_BUTTON).click()

    @allure.step('Выбираем дату в поле Когда привезти самокат')
    def select_when(self, date):
        return self.find_element(LOC.INPUT_WHEN).send_keys(date, Keys.ENTER)

    @allure.step('Выбираем срок аренды в поле Срок аренды')
    def select_howlong(self, howlong):
        if howlong == 1:
            element = LOC.INPUT_HOWLONG_OPTION_1
        else:
            element = LOC.INPUT_HOWLONG_OPTION_2
        self.find_element(LOC.INPUT_HOWLONG).click()
        return self.find_element(element).click()

    @allure.step('Выбираем цвет в чекбоксе Цвет самоката')
    def set_checkbox_color(self, colour):
        if colour == 'black':
            element = LOC.INPUT_BLACK_CHECKBOX
        else:
            element = LOC.INPUT_GRAY_CHECKBOX
        return self.find_element(element).click()

    @allure.step('Заполняем поле Комментарий для курьера')
    def set_comment(self, comment):
        return self.find_element(LOC.INPUT_COMMENT).send_keys(comment)

    @allure.step('Нажимаем кнопку Да в pop-up окне с подтверждением заказа')
    def confirm_purchase_popup(self):
        self.find_element(LOC.PURCHASE_POPUP)
        return self.find_element(LOC.YES_BUTTON).click()

    @allure.step('Возвращаем тескт из pop-up окна после подтверждения заказа')
    def get_purchase_status(self):
        return self.find_element(LOC.PURCHASE_STATUS).text

    @allure.step('Нажимаем кнопку для подтверждения приема cookie во всплывающем окне')
    def click_cookie(self):
        self.find_element(LOC.COOKIE_BUTTON).click()

    @allure.step('Нажимаем на вторую кнопку Заказать')
    def click_second_purchase(self):
        return self.find_element(LOC.PURCHASE_SECOND_BUTTON).click()

    @allure.step('Нажимаем на вопрос в секции вопросов и возвращаем соответствующий ответ')
    def click_on_question_section(self, question, answer):
        self.find_element(question).click()
        return self.find_element(answer).text

    @allure.step('Нажимаем на лого Самокат')
    def click_on_logo(self):
        return self.find_element(MAIN.LOGO).click()

    @allure.step('Возвращаем локатор на объект самокат на главной странице')
    def wait_for_main_image_load(self):
        return self.find_element(MAIN.MAIN_IMAGE)

    @allure.step('Нажимаем на лого Яндекс')
    def click_on_yandex(self):
        return self.find_element(MAIN.YANDEX).click()

    @allure.step('Ожидаем изменный урл https://dzen.ru/?yredirect=true')
    def wait_for_new_page_load(self):
        return self.url_to_change(DATA.DZEN_URL)
