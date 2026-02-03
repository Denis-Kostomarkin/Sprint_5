"""
Вспомогательные функции для тестов
"""
import random


def generate_unique_email():
    """Генератор уникального email"""
    random_num = random.randint(10000, 99999)
    return f"testuser{random_num}@test.com"