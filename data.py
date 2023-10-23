from helpers import Helpers as HELP


class Data:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    DZEN_URL = 'https://dzen.ru/?yredirect=true'

    TEXT_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    TEXT_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    TEXT_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    TEXT_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    TEXT_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    TEXT_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    TEXT_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    TEXT_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    NAME = HELP.fake_data()[0]
    LASTNAME = HELP.fake_data()[1]

    ADDRESS_1 = 'ул. Космонавтов, 5'
    METRO_1 = 'ValueThree'
    PHONENUMBER_1 = 89991112244
    DATE_1 = '10.10.2023'
    DAYS_1 = 1
    COLOUR_1 = 'black'
    COMMENT_1 = 'no comments'

    ADDRESS_2 = 'ул. Садовая, 16'
    METRO_2 = 'ValueFour'
    PHONENUMBER_2 = 87771118756
    DATE_2 = '11.01.2024'
    DAYS_2 = 2
    COLOUR_2 = 'grey'
