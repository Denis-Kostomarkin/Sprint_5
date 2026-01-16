from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, ProfilePageLocators
from constants import Urls


class TestNavigation:
    
    def test_navigate_to_profile(self, driver, login):
        """Переход в личный кабинет"""
        # login фикстура уже выполнила вход
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        ).is_displayed()
        assert "account/profile" in driver.current_url
    
    def test_navigate_from_profile_to_constructor_by_button(self, driver, login):
        """Переход из личного кабинета в конструктор по кнопке"""
        # login фикстура уже выполнила вход
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
        assert driver.current_url == Urls.MAIN
    
    def test_navigate_from_profile_to_constructor_by_logo(self, driver, login):
        """Переход из личного кабинета в конструктор по логотипу"""
        # login фикстура уже выполнила вход
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB)
        )
        
        driver.find_element(*MainPageLocators.LOGO).click()
        
        # ПРОВЕРКА
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        ).is_displayed()
        assert driver.current_url == Urls.MAIN