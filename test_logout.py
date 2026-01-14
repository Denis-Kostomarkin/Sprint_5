from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


class TestLogout:
    """Тесты выхода из аккаунта"""
    
    def test_logout(self, urls, test_data):
        """Выход из аккаунта"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем страницу входа
            driver.get(urls["login"])
            
            # Логинимся
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
            
            # Ждем успешного входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
            # Переходим в профиль
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(ProfilePageLocators.PROFILE_TAB)
            )
            
            # Кликаем на "Выход"
            driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
            
            # Проверяем, что перешли на страницу входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
            # Пытаемся перейти в профиль без авторизации
            driver.get(urls["profile"])
            
            # Должны перенаправить на страницу входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
        finally:
            driver.quit()