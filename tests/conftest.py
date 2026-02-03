"""
Фикстуры для тестов Stellar Burgers
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия браузера"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def login(driver):
    """Фикстура для логина пользователя"""
    from constants import UserData, Urls
    from locators.locators import LoginPageLocators, MainPageLocators
    from selenium.webdriver.support import expected_conditions as EC
    
    driver.get(Urls.LOGIN)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(UserData.EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(UserData.VALID_PASSWORD)
    driver.find_element(*LoginPageLocators.LOGIN_SUBMIT_BUTTON).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )