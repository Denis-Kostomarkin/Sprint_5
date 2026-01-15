from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from constants import EMAIL, VALID_PASSWORD, LOGIN_URL, PROFILE_URL


class TestLogout:
    
    def test_logout(self, driver):
        """Выход из аккаунта"""
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
        
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        
        login_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )
        assert login_title.is_displayed()