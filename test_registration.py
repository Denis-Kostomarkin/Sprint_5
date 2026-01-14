from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import RegistrationPageLocators, LoginPageLocators


class TestRegistration:
    """Тесты на регистрацию"""
    
    def test_registration_success(self, urls, test_data, generate_unique_email):
        """Успешная регистрация"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем страницу регистрации
            driver.get(urls["register"])
            
            # Ждем загрузки страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
            )
            
            # Заполняем форму
            driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(test_data["name"])
            driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(generate_unique_email())
            driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
            
            # Проверяем, что перешли на страницу входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
        finally:
            driver.quit()
    
    def test_registration_invalid_password(self, urls, test_data, generate_unique_email):
        """Регистрация с некорректным паролем (5 символов)"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем страницу регистрации
            driver.get(urls["register"])
            
            # Ждем загрузки страницы
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
            )
            
            # Заполняем форму с некорректным паролем
            driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(test_data["name"])
            driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(generate_unique_email())
            driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(test_data["invalid_password"])
            driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
            
            # Проверяем, что появилась ошибка
            error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
            )
            
            assert error.is_displayed()
            assert "Некорректный пароль" in error.text or "минимальная длина" in error.text.lower()
            
        finally:
            driver.quit()