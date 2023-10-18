from selenium.webdriver.common.by import By


class MainAndLogoLocators:

    LOGO = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    MAIN_IMAGE = (By.XPATH, ".//img[@alt='Scooter blueprint']")
