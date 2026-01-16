from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from constants import Urls


class TestLogout:
    
    def test_logout(self, driver, login):
        """Выход из аккаунта"""
        # login фикстура уже выполнила вход
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        
        # ПРОВЕРКА: перешли на страницу логина
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        ).is_displayed()