from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from constants import EMAIL, VALID_PASSWORD, MAIN_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL


class TestLogin:
    
    def test_login_from_main_page(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(MAIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
    
    def test_login_from_personal_account(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(MAIN_URL)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
    
    def test_login_from_registration_page(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(REGISTER_URL)
        
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
    
    def test_login_from_forgot_password_page(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(FORGOT_PASSWORD_URL)
        
        driver.find_element(*ForgotPasswordPageLocators.FORGOT_LOGIN_LINK).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
    
    def test_login_with_wrong_password(self, driver):
        """Вход с неправильным паролем"""
        driver.get(LOGIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        
        wrong_password = "wrong_password_123"
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(wrong_password)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        assert "login" in driver.current_url