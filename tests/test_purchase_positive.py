import pytest
from helpers import Helpers as HELP
from pages.scooter_delivery_page import ScooterDeliveryPage


class TestPurchasePositive:

    def test_positive_first_purchase_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.click_purchase()
        delivery_page.set_name(HELP.fake_data()[0])
        delivery_page.set_lastname(HELP.fake_data()[1])
        delivery_page.set_address('ул. Космонавтов, 5')
        delivery_page.select_metro('ValueThree')
        delivery_page.set_phonenumber(89991112244)
        delivery_page.click_next()
        delivery_page.select_when('10.10.2023')
        delivery_page.select_howlong(1)
        delivery_page.set_checkbox_color('black')
        delivery_page.set_comment('no comments')
        delivery_page.click_next()
        delivery_page.confirm_purchase_popup()
        status = delivery_page.get_purchase_status()
        assert 'Заказ оформлен' in status

    def test_positive_second_purchase_button(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.scrolldown()
        delivery_page.click_cookie()
        delivery_page.click_second_purchase()
        delivery_page.set_name(HELP.fake_data()[0])
        delivery_page.set_lastname(HELP.fake_data()[1])
        delivery_page.set_address('ул. Садовая, 16')
        delivery_page.select_metro('ValueFour')
        delivery_page.set_phonenumber(87771118756)
        delivery_page.click_next()
        delivery_page.select_when('11.01.2024')
        delivery_page.select_howlong(2)
        delivery_page.set_checkbox_color('grey')
        delivery_page.set_comment('')
        delivery_page.click_next()
        delivery_page.confirm_purchase_popup()
        status = delivery_page.get_purchase_status()
        assert 'Заказ оформлен' in status


