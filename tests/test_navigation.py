from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from constants import EMAIL, VALID_PASSWORD, LOGIN_URL, MAIN_URL


class TestNavigation:
    
    def test_navigate_to_profile(self, driver):
        """Переход в личный кабинет"""
        driver.get(LOGIN_URL)
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        profile_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        assert profile_tab.is_displayed()
        assert "account/profile" in driver.current_url
    
    def test_navigate_from_profile_to_constructor_by_button(self, driver):
        """Переход из личного кабинета в конструктор по кнопке"""
        driver.get(LOGIN_URL)
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        assert driver.current_url == MAIN_URL
    
    def test_navigate_from_profile_to_constructor_by_logo(self, driver):
        """Переход из личного кабинета в конструктор по логотипу"""
        driver.get(LOGIN_URL)
        
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(VALID_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        
        driver.find_element(*MainPageLocators.LOGO).click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        assert driver.current_url == MAIN_URL