from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import RegistrationPageLocators, LoginPageLocators
from constants import UserData, Urls
from helpers import generate_unique_email  


class TestRegistration:
    
    def test_registration_success(self, driver):
        """Успешная регистрация"""
        driver.get(Urls.REGISTER)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
        )
        
        unique_email = generate_unique_email()
        
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(UserData.NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА: перешли на страницу логина
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        ).is_displayed()
    
    def test_registration_invalid_password(self, driver):
        """Регистрация с некорректным паролем"""
        driver.get(Urls.REGISTER)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
        )
        
        unique_email = generate_unique_email()
        
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(UserData.NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(UserData.INVALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА: появилась ошибка
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert error.is_displayed()