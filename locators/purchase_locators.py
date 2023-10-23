from selenium.webdriver.common.by import By


class PurchaseLocators:

    FIRST_PURCHASE_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    NEXT_PURCHASE_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH, ".//button[text()='Да']")

    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    INPUT_LASTNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    INPUT_PHONENUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    INPUT_WHEN = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    INPUT_HOWLONG = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    INPUT_HOWLONG_OPTION_1 = (By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']")
    INPUT_HOWLONG_OPTION_2 = (By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']")

    INPUT_BLACK_CHECKBOX = (By.XPATH, ".//input[@id='black']")
    INPUT_GRAY_CHECKBOX = (By.XPATH, ".//input[@id='grey']")

    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    PURCHASE_POPUP = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']")

    PURCHASE_STATUS = (By.XPATH, ".//div[text()='Заказ оформлен']")

    PURCHASE_SECOND_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")





