from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from locators.main_and_logo_locators import MainAndLogoLocators as MAIN
from data import Data as DATA


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = DATA.BASE_URL
        self.page = MAIN.HTML

    def go_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Element wasnt found')

    def url_to_change(self, url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_changes(url))

    def move_on_next_tab(self):
        move = ActionChains(self.driver)
        return move.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)

    def scrolldown(self):
        self.find_element(self.page).send_keys(Keys.END)
