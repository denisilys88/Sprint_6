from selenium.webdriver.common.by import By


class QuestionSectionLocators:

    TEXT_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    TEXT_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    TEXT_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    TEXT_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    TEXT_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    TEXT_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    FIRST_QUEST = (By.ID, "accordion__heading-0")
    SECOND_QUEST = (By.ID, "accordion__heading-1")
    THIRD_QUEST = (By.ID, "accordion__heading-2")
    FOURTH_QUEST = (By.ID, "accordion__heading-3")
    FIFTH_QUEST = (By.ID, "accordion__heading-4")
    SIXTH_QUEST = (By.ID, "accordion__heading-5")
    SEVENTH_QUEST = (By.ID, "accordion__heading-6")
    EIGHT_QUEST = (By.ID, "accordion__heading-7")

    FIRST_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    SECOND_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    THIRD_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    FOURTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    FIFTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    SIXTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    SEVENTH_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    EIGHT_ANSWER = (By.XPATH, ".//div[@id='accordion__panel-7']/p")


