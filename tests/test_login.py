from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from constants import UserData, Urls
from helpers import generate_unique_email 


class TestLogin:
    
    def test_login_from_main_page(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(Urls.MAIN)
        
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_personal_account(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(Urls.MAIN)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_registration_page(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(Urls.REGISTER)
        
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_from_forgot_password_page(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD)
        
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
    
    def test_login_with_wrong_password(self, driver):
        """Вход с неправильным паролем"""
        driver.get(Urls.LOGIN)
        
        wrong_password = "wrong_password_123"
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(wrong_password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        # ПРОВЕРКА: остаемся на странице логина
        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        ).is_displayed()