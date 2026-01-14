from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators


class TestConstructor:
    """Тесты конструктора"""
    
    def test_constructor_sections(self, urls):
        """Проверка переходов по разделам конструктора"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        
        try:
            # Открываем главную страницу
            driver.get(urls["main"])
            
            # Ждем загрузки конструктора
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(MainPageLocators.MAIN_TITLE)
            )
            
            # Находим разделы конструктора
            buns_tab = driver.find_element(*MainPageLocators.BUNS_SECTION)
            sauces_tab = driver.find_element(*MainPageLocators.SAUCES_SECTION)
            fillings_tab = driver.find_element(*MainPageLocators.FILLINGS_SECTION)
            
            # Проверяем, что изначально активны "Булки"
            assert "tab_tab_type_current" in buns_tab.get_attribute("class") or \
                   "current" in buns_tab.get_attribute("class")
            
            # Кликаем на "Соусы"
            sauces_tab.click()
            
            # Проверяем, что теперь активны "Соусы"
            WebDriverWait(driver, 5).until(
                lambda d: "tab_tab_type_current" in sauces_tab.get_attribute("class") or 
                         "current" in sauces_tab.get_attribute("class")
            )
            
            # Кликаем на "Начинки"
            fillings_tab.click()
            
            # Проверяем, что теперь активны "Начинки"
            WebDriverWait(driver, 5).until(
                lambda d: "tab_tab_type_current" in fillings_tab.get_attribute("class") or 
                         "current" in fillings_tab.get_attribute("class")
            )
            
            # Возвращаемся к "Булки"
            buns_tab.click()
            
            # Проверяем, что снова активны "Булки"
            WebDriverWait(driver, 5).until(
                lambda d: "tab_tab_type_current" in buns_tab.get_attribute("class") or 
                         "current" in buns_tab.get_attribute("class")
            )
            
        finally:
            driver.quit()