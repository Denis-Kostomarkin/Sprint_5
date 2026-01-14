from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


class TestNavigation:
    """Тесты навигации в личный кабинет"""
    
    def test_navigate_to_profile(self, urls, test_data):
        """Переход в личный кабинет"""
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
            
            # Кликаем на "Личный кабинет"
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            
            # Проверяем, что перешли в профиль
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(ProfilePageLocators.PROFILE_TAB)
            )
            
            assert "account/profile" in driver.current_url
            
        finally:
            driver.quit()
    
    def test_navigate_from_profile_to_constructor_by_button(self, urls, test_data):
        """Переход из личного кабинета в конструктор по кнопке"""
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
            
            # Кликаем на "Конструктор"
            driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
            
            # Проверяем, что вернулись на главную
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
            assert driver.current_url == urls["main"]
            
        finally:
            driver.quit()
    
    def test_navigate_from_profile_to_constructor_by_logo(self, urls, test_data):
        """Переход из личного кабинета в конструктор по логотипу"""
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
            
            # Кликаем на логотип "stellar burgers"
            driver.find_element(*MainPageLocators.LOGO).click()
            
            # Проверяем, что вернулись на главную
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
            assert driver.current_url == urls["main"]
            
        finally:
            driver.quit()