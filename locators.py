"""
Локаторы для элементов сайта Stellar Burgers
URL: https://stellarburgers.education-services.ru/
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки навигации в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор" в шапке
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка "Лента Заказов" в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет" в шапке
    
    # Логотип
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип "stellar burgers"
    
    # Кнопка на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")  # Раздел "Булки" в конструкторе
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Раздел "Соусы" в конструкторе
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Раздел "Начинки" в конструкторе
    
    # Кнопка оформления заказа (видна только после входа)
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Кнопка "Оформить заказ"
    
    # Заголовок главной страницы
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    # Заголовок страницы
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок "Вход"
    
    # Поля формы
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода Пароля
    
    # Кнопки
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    
    # Ссылки
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")  # Ссылка "Зарегистрироваться"
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")  # Ссылка "Восстановить пароль"


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    # Заголовок страницы
    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок "Регистрация"
    
    # Поля формы
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода Имени
    REG_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    REG_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле ввода Пароля
    
    # Кнопки
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    
    # Ссылки
    LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка "Войти"
    
    # Ошибки валидации
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Сообщение об ошибке пароля


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""
    
    # Заголовок страницы
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")  # Заголовок "Восстановление пароля"
    
    # Поля формы
    FORGOT_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода Email
    
    # Кнопки
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"
    
    # Ссылки
    FORGOT_LOGIN_LINK = (By.LINK_TEXT, "Войти")  # Ссылка "Войти"


class ProfilePageLocators:
    """Локаторы страницы профиля (личного кабинета)"""
    
    # Заголовки и навигация
    PROFILE_TAB = (By.XPATH, "//a[text()='Профиль']")  # Вкладка "Профиль"
    
    # Кнопки
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход"