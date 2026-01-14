from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators


class TestLogin:
    """Тесты на вход в аккаунт"""
    
    def test_login_from_main_page(self, urls, test_data):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем главную страницу
            driver.get(urls["main"])
            
            # Кликаем на кнопку "Войти в аккаунт"
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
            )
            driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
            
            # Ждем загрузки страницы входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
            # Заполняем форму
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
            
            # Проверяем, что вошли успешно
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
        finally:
            driver.quit()
    
    def test_login_from_personal_account(self, urls, test_data):
        """Вход через кнопку 'Личный кабинет'"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем главную страницу
            driver.get(urls["main"])
            
            # Кликаем на "Личный кабинет"
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            
            # Ждем загрузки формы входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
            # Заполняем форму
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
            
            # Проверяем успешный вход
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
        finally:
            driver.quit()
    
    def test_login_from_registration_page(self, urls, test_data):
        """Вход через кнопку в форме регистрации"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем страницу регистрации
            driver.get(urls["register"])
            
            # Кликаем на ссылку "Войти"
            driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()
            
            # Ждем загрузки формы входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
            # Заполняем форму
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
            
            # Проверяем успешный вход
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
        finally:
            driver.quit()
    
    def test_login_from_forgot_password_page(self, urls, test_data):
        """Вход через кнопку в форме восстановления пароля"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем страницу восстановления пароля
            driver.get(urls["forgot_password"])
            
            # Кликаем на ссылку "Войти"
            driver.find_element(*ForgotPasswordPageLocators.FORGOT_LOGIN_LINK).click()
            
            # Ждем загрузки формы входа
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_TITLE)
            )
            
            # Заполняем форму
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(test_data["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_data["valid_password"])
            driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
            
            # Проверяем успешный вход
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            
        finally:
            driver.quit()