import pytest
from pages.scooter_delivery_page import ScooterDeliveryPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_and_logo_locators import MainAndLogoLocators as MAIN


class TestTransferMainLogo:

    def test_click_logo_go_main(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.click_purchase()
        delivery_page.click_on_logo()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MAIN.MAIN_IMAGE))

    def test_click_yandex_go_dzen(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.click_on_yandex()
        delivery_page.move_on_next_tab()
        assert WebDriverWait(driver, 5).until(EC.url_changes('https://dzen.ru/?yredirect=true'))

