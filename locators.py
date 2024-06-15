from selenium.webdriver.common.by import By


class Locators:
    YANDEX_lOGO = (By.XPATH, '//*[contains(@class, "Header_LogoYandex")]')  # Логотип Яндекс
    SCOOTER_LOGO = (By.XPATH, '//*[contains(@class, "Header_LogoScooter")]')  # Логотип Самокат

    ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')  # Кнопка заказать
    ORDER_BUTTON_ON_PAGE = (By.XPATH, '//*[contains(@class, "Button_Middle") and (text()="Заказать")]')

    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')  # Поле ввода имени
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # Поле ввода фамилии
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле воода адреса
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')  # Поле воода станции метро
    METRO_STATION_1 = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]/parent::button')
    METRO_STATION_2 = (By.XPATH, '//div[text()="Черкизовская"]/parent::button')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле воода номера телефона
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # Кнопка далее
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле ввода даты доставки
    DATE_IN_CALENDAR = (By.CLASS_NAME, 'react-datepicker__day react-datepicker__day--031')  # Выбранная дата в календаре
    RENTAL_PERIOD_INPUT = (By.CLASS_NAME, 'Dropdown-arrow')  # Поле срок аренды
    RENT_PERIOD_1_DAY = (By.XPATH, '//div[text()= "сутки"]/parent::div[@class = "Dropdown-menu"]')
    RENT_PERIOD_5_DAYS = (By.XPATH, '//div[text()="пятеро суток"]/parent::div[@class = "Dropdown-menu"]')
    CHECKBOX_COLOR_BLACK = (By.XPATH, '//label[@for="black"]')
    CHECKBOX_COLOR_GREY = (By.XPATH, '//label[@for="grey"]')
    COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    CONFIRM_PLACE_ORDER_WINDOW = (By.CLASS_NAME, 'Order_Modal__YZ-d3')  # Окно подтверждения заказа
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')  # Кнопка да
    PLACE_ORDER_WINDOW = (By.XPATH,  '//*[contains(@class, "Order_Modal")]')  # Окно заказ оформлен
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    COST_QUE = (By.XPATH, '//div[text()="Сколько это стоит? И как оплатить?"]')
    SCOOTER_COUNT_QUE = (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]')
    RENTAL_TIME_QUE = (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]')
    ORDER_TODAY_QUE = (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]')
    EXTEND_ORDER_QUE = (By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]')
    CHARGER_QUE = (By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]')
    CANCEL_ORDER_QUE = (By.XPATH, '//div[text()="Можно ли отменить заказ?"]')
    MKAD_QUE = (By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]')
    OPENED_ANSWER = (By.XPATH, '//div[@role="region" and not(@hidden)]/p')

    GET_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
