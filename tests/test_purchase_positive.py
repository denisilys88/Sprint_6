import allure
import pytest
from data import Data as DATA
from pages.scooter_delivery_page import ScooterDeliveryPage


class TestPurchasePositive:

    @allure.title('Проверка оформления заказа по первой кнопке Заказать')
    @allure.description(
        'Открываем страницу, на странице нажимаем кнопку заказать, заполняем поля Имя, Фамилия, Адрес, Станция метро, '
        'Телефон, нажимаем кнопку Далее, заполняем поля Когда привезти самокат, Срок аренды, Цвет самоката, '
        'Комментарий для курьера, нажимаем кнопку Заказать, нажимаем кнопку Да на pop-up окне с подтверждением,'
        'проверяем текст статуса заказа на следующем pop-up окне, он должен быть = Заказ оформлен')
    def test_positive_first_purchase_button(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.click_purchase()
        delivery_page.set_name(DATA.NAME)
        delivery_page.set_lastname(DATA.LASTNAME)
        delivery_page.set_address(DATA.ADDRESS_1)
        delivery_page.select_metro(DATA.METRO_1)
        delivery_page.set_phonenumber(DATA.PHONENUMBER_1)
        delivery_page.click_next()
        delivery_page.select_when(DATA.DATE_1)
        delivery_page.select_howlong(DATA.DAYS_1)
        delivery_page.set_checkbox_color(DATA.COLOUR_1)
        delivery_page.set_comment(DATA.COMMENT_1)
        delivery_page.click_next()
        delivery_page.confirm_purchase_popup()
        status = delivery_page.get_purchase_status()
        assert 'Заказ оформлен' in status, "После оформления заказа в popup должен быть тескт 'Заказ оформлен'"

    @allure.title('Проверка оформления заказа по второй кнопке Заказать')
    @allure.description(
        'Открываем страницу, скроллим страницу вниз до конца, нажимаем на кнопку принятия cookie, на странице '
        'нажимаем кнопку заказать, заполняем поля Имя, Фамилия, Адрес, Станция метро, Телефон,'
        'нажимаем кнопку Далее, заполняем поля Когда привезти самокат, Срок аренды, Цвет самоката, Комментарий для '
        'курьера, нажимаем кнопку Заказать, нажимаем кнопку Да на pop-up окне с подтверждением,'
        'проверяем текст статуса заказа на следующем pop-up окне, он должен быть = Заказ оформлен')
    def test_positive_second_purchase_button(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.scrolldown()
        delivery_page.click_cookie()
        delivery_page.click_second_purchase()
        delivery_page.set_name(DATA.NAME)
        delivery_page.set_lastname(DATA.LASTNAME)
        delivery_page.set_address(DATA.ADDRESS_2)
        delivery_page.select_metro(DATA.METRO_2)
        delivery_page.set_phonenumber(DATA.PHONENUMBER_2)
        delivery_page.click_next()
        delivery_page.select_when(DATA.DATE_2)
        delivery_page.select_howlong(DATA.DAYS_2)
        delivery_page.set_checkbox_color(DATA.COLOUR_2)
        delivery_page.set_comment('')
        delivery_page.click_next()
        delivery_page.confirm_purchase_popup()
        status = delivery_page.get_purchase_status()
        assert 'Заказ оформлен' in status, "После оформления заказа в popup должен быть тескт 'Заказ оформлен'"


