import pytest
from pages.scooter_delivery_page import ScooterDeliveryPage


class TestTransferMainLogo:

    def test_click_logo_go_main(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.click_purchase()
        delivery_page.click_on_logo()
        assert delivery_page.wait_for_main_image_load

    def test_click_yandex_go_dzen(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.click_on_yandex()
        delivery_page.move_on_next_tab()
        assert delivery_page.wait_for_new_page_load

