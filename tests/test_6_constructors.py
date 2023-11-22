import pytest

def test_constructor_bulki():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # проверить переход к разделу Булки
    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/")

    # клик на Начинки ибо по умолчанию выбраны Булки
    driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(3) > .text").click()

    # клик на Булки
    driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(1) > .text").click()
    # Проверка что раздел Булки на экране
    assert driver.find_element(By.CSS_SELECTOR, ".text_type_main-medium:nth-child(1)").text == 'Булки'

    driver.quit()

def test_constructor_sous():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    # проверить переход к разделу Соусы

    driver = webdriver.Chrome()

    # вход на сайт
    driver.get("https://stellarburgers.nomoreparties.site/")

    # выбрать раздел Соусы
    driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(2) > .text").click()
    # Проверка что раздел Соусы на экране
    assert driver.find_element(By.CSS_SELECTOR, ".text:nth-child(3)").text == 'Соусы'

    driver.quit()

def test_constructor_content():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    # проверить переход к разделу Начинки
    driver = webdriver.Chrome()

    # открыть сайт
    driver.get("https://stellarburgers.nomoreparties.site/")

    # клик на Начинки
    driver.find_element(By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(3) > .text").click()
    # Проверка что раздел Начинки на экране

    assert driver.find_element(By.CSS_SELECTOR, ".text:nth-child(5)").text == 'Начинки'

    driver.quit()