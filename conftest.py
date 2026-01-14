"""
Фикстуры для тестов Stellar Burgers
"""
import pytest
import random


@pytest.fixture
def test_data():
    """Фикстура с тестовыми данными для всех тестов"""
    return {
        "name": "Денис",
        "email": "DenisKostomarkin37000@gmail.com",
        "valid_password": "YandexPracticum22",
        "invalid_password": "№;%Pя1"  # 5 символов
    }


@pytest.fixture
def base_url():
    """Фикстура с базовым URL сайта"""
    return "https://stellarburgers.education-services.ru/"


@pytest.fixture
def urls(base_url):
    """Фикстура с URL всех страниц сайта"""
    return {
        "main": base_url,
        "login": f"{base_url}login",
        "register": f"{base_url}register",
        "forgot_password": f"{base_url}forgot-password",
        "profile": f"{base_url}account/profile"
    }


@pytest.fixture
def generate_unique_email():
    """Фикстура для генерации уникального email"""
    def _generate():
        random_num = random.randint(10000, 99999)
        return f"testuser{random_num}@test.com"
    return _generate