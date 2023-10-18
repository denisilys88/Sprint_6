import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--width=800')
    firefox_options.add_argument('--height=800')
    driver = webdriver.Firefox(options=firefox_options)
    yield driver
    WebDriverWait(driver, 5)
    driver.quit()

