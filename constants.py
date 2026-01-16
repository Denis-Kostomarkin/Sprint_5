"""
Константы для тестов Stellar Burgers
"""


class UserData:
    """Данные пользователя"""
    NAME = "Денис"
    EMAIL = "DenisKostomarkin37000@gmail.com"
    VALID_PASSWORD = "YandexPracticum22"
    INVALID_PASSWORD = "12345"  # 5 символов - простой пароль для теста


class Urls:
    """URL сайта"""
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    MAIN = BASE_URL
    LOGIN = f"{BASE_URL}login"
    REGISTER = f"{BASE_URL}register"
    FORGOT_PASSWORD = f"{BASE_URL}forgot-password"
    PROFILE = f"{BASE_URL}account/profile"