from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import RegistrationPageLocators, LoginPageLocators
from constants import NAME, VALID_PASSWORD, INVALID_PASSWORD, REGISTER_URL
from helpers import generate_unique_email


class TestRegistration:
    
    def test_registration_success(self, driver):
        """Успешная регистрация"""
        driver.get(REGISTER_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
        )
        
        unique_email = generate_unique_email()
        
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
        
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        assert login_title.is_displayed()
    
    def test_registration_invalid_password(self, driver):
        """Регистрация с некорректным паролем"""
        driver.get(REGISTER_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_TITLE)
        )
        
        unique_email = generate_unique_email()
        
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(NAME)
        driver.find_element(*RegistrationPageLocators.REG_EMAIL_INPUT).send_keys(unique_email)
        driver.find_element(*RegistrationPageLocators.REG_PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.REGISTER_SUBMIT_BUTTON).click()
        
        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text