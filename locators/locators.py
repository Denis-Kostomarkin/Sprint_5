"""
Локаторы для элементов сайта Stellar Burgers
URL: https://stellarburgers.nomoreparties.site/
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки навигации в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/')]//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account/profile')]//p[text()='Личный Кабинет']")
    
    # Логотип
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Кнопка на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__')]//span[text()='Начинки']/parent::div")
    
    # Активный раздел конструктора
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Заголовок главной страницы
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")


class LoginPageLocators:
    """Локаторы страницы входа"""
    
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    
    REGISTER_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    NAME_INPUT = (By.XPATH, "(//input[@type='text'])[1]")
    EMAIL_INPUT = (By.XPATH, "(//input[@type='text'])[2]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")


class ForgotPasswordPageLocators:
    """Локаторы страницы восстановления пароля"""
    
    FORGOT_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ProfilePageLocators:
    """Локаторы страницы профиля"""
    
    PROFILE_TAB = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@href, '/')]")