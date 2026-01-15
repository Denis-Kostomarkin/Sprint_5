"""
Локаторы для элементов сайта Stellar Burgers
URL: https://stellarburgers.education-services.ru/
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки навигации в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Логотип
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Кнопка на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел конструктора
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Заголовок главной страницы
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REG_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""
    
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    FORGOT_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    FORGOT_LOGIN_LINK = (By.LINK_TEXT, "Войти")


class ProfilePageLocators:
    """Локаторы страницы профиля"""
    
    PROFILE_TAB = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")