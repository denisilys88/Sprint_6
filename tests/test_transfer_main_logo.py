import allure
import pytest
from pages.scooter_delivery_page import ScooterDeliveryPage


class TestTransferMainLogo:

    @allure.title('Проверка того, что нажатие на лого Самокат возвращает на главную страницу')
    @allure.description('Открываем страницу, нажимаем на кнопку Заказать, нажимаем на лого Самокат,'
                        'проверяем, что возвращаемся на главную страницу')
    def test_click_logo_go_main(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.click_purchase()
        delivery_page.click_on_logo()
        assert delivery_page.wait_for_main_image_load

    @allure.title('Проверка того, что нажатие на лого Яндекс редиректит на страницу dzen')
    @allure.description('Открываем страницу, нажимаем на лого Яндекс, переходим на новую открывшуюся вкладку,'
                        'проверяем, что урл новой вкладки соответствует https://dzen.ru/?yredirect=true')
    def test_click_yandex_go_dzen(self, driver):
        delivery_page = ScooterDeliveryPage(driver)
        delivery_page.go_page()
        delivery_page.click_on_yandex()
        delivery_page.move_on_next_tab()
        assert delivery_page.wait_for_new_page_load

