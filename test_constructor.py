from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators
from constants import MAIN_URL


class TestConstructor:
    
    def test_buns_section_active_by_default(self, driver):
        """Проверяем, что по умолчанию активна секция 'Булки'"""
        driver.get(MAIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_TITLE)
        )
        
        buns_tab = driver.find_element(*MainPageLocators.BUNS_SECTION)
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        
        assert buns_tab == active_tab
    
    def test_sauces_section_activation(self, driver):
        """Проверяем активацию секции 'Соусы' при клике"""
        driver.get(MAIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_TITLE)
        )
        
        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_SECTION)
        sauces_tab.click()
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        
        assert sauces_tab == active_tab
    
    def test_fillings_section_activation(self, driver):
        """Проверяем активацию секции 'Начинки' при клике"""
        driver.get(MAIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_TITLE)
        )
        
        fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_SECTION)
        fillings_tab.click()
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        
        assert fillings_tab == active_tab
    
    def test_return_to_buns_section(self, driver):
        """Проверяем возврат к секции 'Булки'"""
        driver.get(MAIN_URL)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.MAIN_TITLE)
        )
        
        sauces_tab = driver.find_element(*MainPageLocators.SAUCES_SECTION)
        sauces_tab.click()
        
        buns_tab = driver.find_element(*MainPageLocators.BUNS_SECTION)
        buns_tab.click()
        
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_SECTION)
        
        assert buns_tab == active_tab