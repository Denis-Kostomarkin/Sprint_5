"""
Фикстуры для тестов Stellar Burgers
"""
import pytest


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия браузера"""
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()